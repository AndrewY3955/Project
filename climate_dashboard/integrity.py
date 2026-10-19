"""SHA-256 integrity helpers. A trusted manifest must be protected separately."""

import hashlib
import json
import sys
from pathlib import Path


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_manifest(file_path: str | Path, manifest_path: str | Path, purpose: str) -> dict:
    file_path = Path(file_path)
    payload = {
        "file": file_path.name,
        "sha256": sha256_file(file_path),
        "purpose": purpose,
        "warning": (
            "Integrity verification requires this manifest to be protected. "
            "If both the data file and manifest can be changed by the same attacker, "
            "the hash check alone is not sufficient."
        ),
    }
    Path(manifest_path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def verify_manifest(file_path: str | Path, manifest_path: str | Path) -> tuple[bool, str, str]:
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    expected = manifest["sha256"]
    actual = sha256_file(file_path)
    return actual == expected, expected, actual


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python -m climate_dashboard.integrity <data.csv> <manifest.json>")
        return 2
    ok, expected, actual = verify_manifest(sys.argv[1], sys.argv[2])
    print(f"Expected SHA-256: {expected}")
    print(f"Actual SHA-256:   {actual}")
    print("INTEGRITY OK" if ok else "INTEGRITY FAILURE: file differs from trusted reference")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
