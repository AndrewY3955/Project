"""Create a clearly labeled adversarial copy and log each controlled manipulation."""

import pandas as pd

from climate_dashboard.integrity import write_manifest
from climate_dashboard.pipeline import OUT_DIR, TRUSTED_FILE, run_pipeline

ADVERSARIAL_FILE = OUT_DIR / "adversarial_data.csv"
CHANGE_LOG_FILE = OUT_DIR / "adversarial_change_log.csv"
ADVERSARIAL_MANIFEST = OUT_DIR / "adversarial_manifest.json"


def create_adversarial_copy() -> pd.DataFrame:
    if not TRUSTED_FILE.exists():
        run_pipeline()

    trusted = pd.read_csv(TRUSTED_FILE)
    altered = trusted.copy()
    changes = []

    # Manipulation 1: inflate one synthetic electricity measurement.
    target = altered.index[altered["metric"] == "Electricity consumption"]
    if len(target):
        idx = int(target[0])
        old = altered.at[idx, "value"]
        altered.at[idx, "value"] = float(old) * 1.5
        changes.append({
            "change_id": "ADV-001",
            "record_id": altered.at[idx, "record_id"],
            "manipulation": "Numerical value altered",
            "field": "value",
            "original_value": old,
            "manipulated_value": altered.at[idx, "value"],
            "intended_effect": "Make electricity consumption appear higher in the adversarial view",
            "detection_evidence": "Compare row with trusted version and check trusted file hash",
            "defensive_control": "Protected trusted copy, hash verification, and audit trail",
        })

    # Manipulation 2: remove a source name from a greenhouse-gas record.
    target = altered.index[altered["metric"] == "Greenhouse-gas emissions"]
    if len(target):
        idx = int(target[0])
        old = altered.at[idx, "source_name"]
        altered.at[idx, "source_name"] = ""
        changes.append({
            "change_id": "ADV-002",
            "record_id": altered.at[idx, "record_id"],
            "manipulation": "Source provenance removed",
            "field": "source_name",
            "original_value": old,
            "manipulated_value": "",
            "intended_effect": "Make the value harder to trace to its origin",
            "detection_evidence": "Empty-source validation warning and trusted-version comparison",
            "defensive_control": "Required provenance fields and change approval",
        })

    # Manipulation 3: remove water records to simulate feature omission.
    water_rows = altered.index[altered["metric"] == "Water consumption"]
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

    altered.to_csv(ADVERSARIAL_FILE, index=False)
    pd.DataFrame(changes).to_csv(CHANGE_LOG_FILE, index=False)
    write_manifest(
        ADVERSARIAL_FILE,
        ADVERSARIAL_MANIFEST,
        purpose="Intentionally manipulated dataset for classroom adversarial demonstration",
    )
    return pd.DataFrame(changes)


if __name__ == "__main__":
    change_log = create_adversarial_copy()
    print(f"Created adversarial dataset: {ADVERSARIAL_FILE}")
    print(f"Created change log: {CHANGE_LOG_FILE}")
    print(f"Documented {len(change_log)} manipulation event(s).")
    print("This is a controlled simulation, not a real attack.")
