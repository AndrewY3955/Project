"""Load, validate, normalize, and export the trusted dataset."""

import json
import math
from pathlib import Path

import pandas as pd

from climate_dashboard.integrity import write_manifest
from climate_dashboard.schema import (
    ALLOWED_DATA_STATUSES,
    EXPECTED_UNITS,
    REQUIRED_TEXT_COLUMNS,
    REQUIRED_COLUMNS,
)

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "environmental_data.csv"
OUT_DIR = ROOT / "data" / "processed"
TRUSTED_FILE = OUT_DIR / "trusted_data.csv"
VALIDATION_FILE = OUT_DIR / "validation_report.json"
MANIFEST_FILE = OUT_DIR / "trusted_manifest.json"


def validate_dataframe(df: pd.DataFrame) -> dict:
    errors = []
    warnings = []

    missing_columns = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_columns:
        errors.append({"type": "missing_columns", "columns": missing_columns})
        return {
            "status": "FAIL",
            "row_count": int(len(df)),
            "error_count": len(errors),
            "warning_count": len(warnings),
            "errors": errors,
            "warnings": warnings,
        }

    if df.empty:
        errors.append({"type": "empty_dataset"})
        return {
            "status": "FAIL",
            "row_count": 0,
            "error_count": len(errors),
            "warning_count": len(warnings),
            "errors": errors,
            "warnings": warnings,
        }

    missing_record_ids = (
        df["record_id"].isna()
        | df["record_id"].astype("string").str.strip().eq("").fillna(False)
    )
    if missing_record_ids.any():
        errors.append({
            "type": "missing_record_id",
            "count": int(missing_record_ids.sum()),
        })
    if df["record_id"].duplicated().any():
        errors.append({
            "type": "duplicate_record_id",
            "values": df.loc[df["record_id"].duplicated(), "record_id"].astype(str).tolist(),
        })

    for column in sorted(REQUIRED_TEXT_COLUMNS):
        blank_values = df[column].isna() | df[column].astype("string").str.strip().eq("").fillna(False)
        if blank_values.any():
            errors.append({
                "type": "missing_required_value",
                "column": column,
                "rows": df.index[blank_values].tolist(),
            })

    numeric_values = pd.to_numeric(df["value"], errors="coerce")
    invalid_numeric = numeric_values.isna() | ~numeric_values.map(math.isfinite)
    if invalid_numeric.any():
        errors.append({"type": "invalid_numeric_value", "rows": df.index[invalid_numeric].tolist()})

    negative_values = numeric_values < 0
    if negative_values.any():
        errors.append({"type": "negative_value", "rows": df.index[negative_values].tolist()})

    numeric_years = pd.to_numeric(df["data_year"], errors="coerce")
    invalid_year = numeric_years.isna() | (numeric_years % 1 != 0)
    if invalid_year.any():
        errors.append({"type": "invalid_data_year", "rows": df.index[invalid_year].tolist()})

    for idx, row in df.iterrows():
        metric = row["metric"]
        unit = row["unit"]
        if metric in EXPECTED_UNITS and unit not in EXPECTED_UNITS[metric]:
            errors.append({
                "type": "unit_mismatch",
                "row": int(idx),
                "metric": metric,
                "unit": unit,
                "expected": sorted(EXPECTED_UNITS[metric]),
            })
        if row["data_status"] not in ALLOWED_DATA_STATUSES:
            errors.append({
                "type": "invalid_data_status",
                "row": int(idx),
                "data_status": row["data_status"],
            })
        if pd.isna(row["source_name"]) or not str(row["source_name"]).strip():
            warnings.append({"type": "empty_source_name", "row": int(idx)})
        if pd.isna(row["limitation"]) or not str(row["limitation"]).strip():
            warnings.append({"type": "missing_limitation", "row": int(idx)})

    if (df["data_status"] == "synthetic_demo").any():
        warnings.append({
            "type": "synthetic_data_present",
            "message": "Dataset contains synthetic demonstration values; do not treat as real measurements.",
        })

    return {
        "status": "PASS" if not errors else "FAIL",
        "row_count": int(len(df)),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "errors": errors,
        "warnings": warnings,
    }


def run_pipeline() -> dict:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Expected input dataset at {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if not missing_columns:
        for col in ["company", "facility", "geography", "metric", "unit", "source_name"]:
            df[col] = df[col].astype("string").str.strip()
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        df["data_year"] = pd.to_numeric(df["data_year"], errors="coerce")

    report = validate_dataframe(df)
    VALIDATION_FILE.write_text(json.dumps(report, indent=2), encoding="utf-8")

    if report["status"] != "PASS":
        raise ValueError(
            f"Dataset validation failed with {report['error_count']} error(s). "
            f"Review {VALIDATION_FILE}"
        )

    df["data_year"] = df["data_year"].astype("Int64")
    df.to_csv(TRUSTED_FILE, index=False)
    write_manifest(
        TRUSTED_FILE,
        MANIFEST_FILE,
        purpose="Trusted normalized dataset generated by the project pipeline",
    )
    return report


if __name__ == "__main__":
    result = run_pipeline()
    print(json.dumps(result, indent=2))
    print(f"\nTrusted dataset: {TRUSTED_FILE}")
    print(f"Validation report: {VALIDATION_FILE}")
    print(f"Integrity manifest: {MANIFEST_FILE}")
