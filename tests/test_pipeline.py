import pandas as pd

from climate_dashboard.pipeline import TRUSTED_FILE, run_pipeline, validate_dataframe
from climate_dashboard.schema import REQUIRED_COLUMNS


def test_pipeline_creates_trusted_dataset():
    report = run_pipeline()
    assert report["status"] == "PASS"
    assert TRUSTED_FILE.exists()
    df = pd.read_csv(TRUSTED_FILE)
    assert all(column in df.columns for column in REQUIRED_COLUMNS)
    assert len(df) > 0


def test_duplicate_record_ids_fail():
    df = pd.read_csv("data/raw/environmental_data.csv")
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
    report = validate_dataframe(df)
    assert report["status"] == "FAIL"
    assert any(e["type"] == "duplicate_record_id" for e in report["errors"])


def test_unit_mismatch_fails():
    df = pd.read_csv("data/raw/environmental_data.csv")
    df.loc[0, "unit"] = "banana"
    report = validate_dataframe(df)
    assert report["status"] == "FAIL"
    assert any(e["type"] == "unit_mismatch" for e in report["errors"])


def test_missing_columns_fail_validation():
    df = pd.DataFrame({"record_id": ["DEMO-001"]})

    report = validate_dataframe(df)

    assert report["status"] == "FAIL"
    assert any(error["type"] == "missing_columns" for error in report["errors"])

def test_empty_dataset_fails_validation():
    df = pd.read_csv("data/intake/observations_template.csv")

    report = validate_dataframe(df)

    assert report["status"] == "FAIL"
    assert any(error["type"] == "empty_dataset" for error in report["errors"])


def test_blank_required_text_fails_validation():
    df = pd.read_csv("data/raw/environmental_data.csv")
    df.loc[0, "company"] = "  "

    report = validate_dataframe(df)

    assert report["status"] == "FAIL"
    assert any(
        error["type"] == "missing_required_value" and error["column"] == "company"
        for error in report["errors"]
    )


def test_fractional_year_fails_validation():
    df = pd.read_csv("data/raw/environmental_data.csv")
    df["data_year"] = df["data_year"].astype(float)
    df.loc[0, "data_year"] = 2023.5

    report = validate_dataframe(df)

    assert report["status"] == "FAIL"
    assert any(error["type"] == "invalid_data_year" for error in report["errors"])
