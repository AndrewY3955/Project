"""Create a clearly labeled adversarial copy and log each controlled manipulation."""

import argparse
from pathlib import Path

import pandas as pd

from climate_dashboard.integrity import write_manifest
from climate_dashboard.pipeline import OUT_DIR, TRUSTED_FILE, run_pipeline


def create_adversarial_copy(
    trusted_file: str | Path = TRUSTED_FILE,
    output_dir: str | Path = OUT_DIR,
) -> pd.DataFrame:
    trusted_file = Path(trusted_file)
    output_dir = Path(output_dir)
    adversarial_file = output_dir / "adversarial_data.csv"
    change_log_file = output_dir / "adversarial_change_log.csv"
    adversarial_manifest = output_dir / "adversarial_manifest.json"

    if not trusted_file.exists() and trusted_file == TRUSTED_FILE:
        run_pipeline()
    if not trusted_file.exists():
        raise FileNotFoundError(f"Trusted input dataset not found: {trusted_file}")

    output_dir.mkdir(parents=True, exist_ok=True)
    trusted = pd.read_csv(trusted_file)
    altered = trusted.copy()
    changes = []
    metrics = altered["metric"].astype("string")

    # Manipulation 1: inflate an energy-related measurement.
    target = altered.index[metrics.str.contains("energy|electricity", case=False, regex=True, na=False)]
    if len(target):
        idx = int(target[0])
        old = altered.at[idx, "value"]
        altered.at[idx, "value"] = float(old) * 1.5
        changes.append({
            "change_id": "ADV-001",
            "record_id": altered.at[idx, "record_id"],
            "manipulation": "Energy-related value altered",
            "field": "value",
            "original_value": old,
            "manipulated_value": altered.at[idx, "value"],
            "intended_effect": "Make reported energy use appear higher in the adversarial view",
            "detection_evidence": "Compare row with trusted version and check trusted file hash",
            "defensive_control": "Protected trusted copy, hash verification, and audit trail",
        })
    else:
        raise ValueError("Adversarial scenario requires at least one energy- or electricity-related record.")

    # Manipulation 2: remove source provenance from an emissions record.
    target = altered.index[metrics.str.contains("greenhouse|ghg|emission", case=False, regex=True, na=False)]
    if len(target):
        idx = int(target[0])
        old = altered.at[idx, "source_name"]
        altered.at[idx, "source_name"] = ""
        changes.append({
            "change_id": "ADV-002",
            "record_id": altered.at[idx, "record_id"],
            "manipulation": "Human-readable source label removed",
            "field": "source_name",
            "original_value": old,
            "manipulated_value": "",
            "intended_effect": "Make the report and publisher less visible while source_url and source_id remain",
            "detection_evidence": "Empty-source validation warning and trusted-version comparison",
            "defensive_control": "Review source metadata and compare against a protected trusted version",
        })
    else:
        raise ValueError("Adversarial scenario requires at least one greenhouse-gas or emissions record.")

    # Manipulation 3: remove water records to simulate feature omission.
    water_rows = altered.index[metrics.str.contains("water", case=False, na=False)]
    if len(water_rows):
        removed = altered.loc[water_rows]
        for _, row in removed.iterrows():
            changes.append({
                "change_id": "ADV-003",
                "record_id": row["record_id"],
                "manipulation": "Environmental feature omitted",
                "field": "entire row",
                "original_value": f'{row["metric"]}={row["value"]} {row["unit"]}',
                "manipulated_value": "row removed",
                "intended_effect": "Hide water-use information from the displayed dataset",
                "detection_evidence": "Compare record counts and record IDs with trusted data",
                "defensive_control": "Versioned datasets, row-count checks, and required-feature checks",
            })
        altered = altered.drop(index=water_rows)
    else:
        raise ValueError("Adversarial scenario requires at least one water-related record.")

    altered.to_csv(adversarial_file, index=False)
    pd.DataFrame(changes).to_csv(change_log_file, index=False)
    write_manifest(
        adversarial_file,
        adversarial_manifest,
        purpose="Intentionally manipulated dataset for classroom adversarial demonstration",
    )
    return pd.DataFrame(changes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a separate, logged adversarial dataset copy.")
    parser.add_argument(
        "--input",
        type=Path,
        default=TRUSTED_FILE,
        help=f"Trusted normalized CSV (default: {TRUSTED_FILE})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUT_DIR,
        help=f"Output directory (default: {OUT_DIR})",
    )
    args = parser.parse_args()
    change_log = create_adversarial_copy(args.input, args.output_dir)
    print(f"Created adversarial dataset: {args.output_dir / 'adversarial_data.csv'}")
    print(f"Created change log: {args.output_dir / 'adversarial_change_log.csv'}")
    print(f"Documented {len(change_log)} manipulation event(s).")
    print("This is a controlled simulation, not a real attack.")
