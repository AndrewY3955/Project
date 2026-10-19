import pandas as pd

from climate_dashboard.adversarial import create_adversarial_copy, ADVERSARIAL_FILE, CHANGE_LOG_FILE
from climate_dashboard.integrity import verify_manifest
from climate_dashboard.pipeline import run_pipeline, TRUSTED_FILE, MANIFEST_FILE, OUT_DIR


def test_trusted_manifest_verifies():
    run_pipeline()
    ok, expected, actual = verify_manifest(TRUSTED_FILE, MANIFEST_FILE)
    assert ok
    assert expected == actual


def test_tampering_is_detected(tmp_path):
    run_pipeline()
    tampered = tmp_path / "tampered.csv"
    df = pd.read_csv(TRUSTED_FILE)
    df.loc[0, "value"] = float(df.loc[0, "value"]) + 1
    df.to_csv(tampered, index=False)
    ok, expected, actual = verify_manifest(tampered, MANIFEST_FILE)
    assert not ok
    assert expected != actual


def test_adversarial_copy_is_separate_and_documented():
    run_pipeline()
    changes = create_adversarial_copy()
    assert ADVERSARIAL_FILE.exists()
    assert CHANGE_LOG_FILE.exists()
    assert len(changes) >= 2
    trusted = pd.read_csv(TRUSTED_FILE)
    adversarial = pd.read_csv(ADVERSARIAL_FILE)
    assert len(adversarial) < len(trusted)
