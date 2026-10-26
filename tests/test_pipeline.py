from pathlib import Path

import pandas as pd

from climate_dashboard.pipeline import (
    TRUSTED_FILE,
    normalize_column_names,
    run_pipeline,
    validate_dataframe,
)
from climate_dashboard.schema import CANONICAL_COLUMNS, REQUIRED_COLUMNS


def test_pipeline_creates_trusted_dataset():
    report = run_pipeline()
    assert report["status"] == "PASS"
    assert TRUSTED_FILE.exists()
    df = pd.read_csv(TRUSTED_FILE)
    assert all(column in df.columns for column in REQUIRED_COLUMNS)
    assert len(df) > 0


def test_pipeline_accepts_shuffled_columns_and_exports_canonical_order(tmp_path):
    df = pd.read_csv("data/raw/environmental_data.csv")
    df["source_id"] = "SRC-001"
    df["source_locator"] = "Table 1"
    df["custom_note"] = "Keep this column"
    df = df[df.columns[::-1]]
    df.columns = [f" {column} " for column in df.columns]
    df = df.rename(columns={" record_id ": "\ufeff record_id "})

    input_file = tmp_path / "input.csv"
    output_dir = tmp_path / "processed"
    df.to_csv(input_file, index=False)

    report = run_pipeline(input_file=input_file, output_dir=output_dir)

    assert report["status"] == "PASS"
    output = pd.read_csv(output_dir / "trusted_data.csv")
    expected_columns = [column for column in CANONICAL_COLUMNS if column in output.columns]
    assert output.columns.tolist() == expected_columns + ["custom_note"]
    assert output["custom_note"].eq("Keep this column").all()


def test_pipeline_preserves_input_and_writes_isolated_outputs(tmp_path):
    from hashlib import sha256

    input_file = tmp_path / "intake.csv"
    output_dir = tmp_path / "reviewed"
    input_file.write_bytes(Path("data/intake/observations_template.csv").read_bytes())
    input_hash = sha256(input_file.read_bytes()).hexdigest()

    report = run_pipeline(input_file=input_file, output_dir=output_dir)

    assert report["status"] == "PASS"
    assert sha256(input_file.read_bytes()).hexdigest() == input_hash
    assert (output_dir / "trusted_data.csv").exists()
    assert (output_dir / "validation_report.json").exists()
    assert (output_dir / "trusted_manifest.json").exists()


def test_column_names_trim_whitespace_and_bom():
    df = pd.DataFrame([[1]], columns=["\ufeff record_id "])

    normalized = normalize_column_names(df)

    assert normalized.columns.tolist() == ["record_id"]


def test_duplicate_column_names_after_normalization_fail():
    df = pd.DataFrame([[1, 2]], columns=["record_id", " record_id "])

    try:
        normalize_column_names(df)
    except ValueError as error:
        assert "duplicate column names" in str(error)
    else:
        raise AssertionError("Expected duplicate normalized headers to fail")


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


def test_unsupported_metric_fails():
    df = pd.read_csv("data/raw/environmental_data.csv")
    df.loc[0, "metric"] = "Unregistered metric"

    report = validate_dataframe(df)

    assert report["status"] == "FAIL"
    assert any(error["type"] == "unsupported_metric" for error in report["errors"])


def test_missing_columns_fail_validation():
    df = pd.DataFrame({"record_id": ["DEMO-001"]})

    report = validate_dataframe(df)

    assert report["status"] == "FAIL"
    assert any(error["type"] == "missing_columns" for error in report["errors"])

def test_empty_dataset_fails_validation():
    df = pd.DataFrame(columns=REQUIRED_COLUMNS)

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
