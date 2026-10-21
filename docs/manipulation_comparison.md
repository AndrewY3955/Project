# Controlled manipulation comparison

## Evidence boundary

This is a reproducible, local classroom simulation, not a real attack or evidence of an actual incident. The trusted source-backed file is generated from the reviewed intake at `data/processed/reviewed/trusted_data.csv`. The separate manipulated copy and event log are generated at `data/processed/reviewed/adversarial_data.csv` and `data/processed/reviewed/adversarial_change_log.csv`. Do not use the adversarial file for trusted analysis.

The generator changes a copy only. It does not edit the intake CSV or trusted output. The adversarial manifest hashes the manipulated artifact itself; detection requires comparing it with the separately protected trusted reference and reviewing the change log.

## Recorded changes

| Change | Trusted state | Manipulated state | Possible user interpretation | Detectability and controls |
|---|---|---|---|---|
| `ADV-001` - numeric alteration | `OBS001` reports 27,456,000 MWh total energy (27,456 GWh) | Value increased by 50% to 41,184,000 MWh | A chart may imply a larger energy burden or a false trend. The measure is total energy, not electricity-only. | Compare the record with the trusted CSV; the protected-reference hash fails if the altered file is checked against the trusted manifest. Prevent with restricted write access, review, and an independently protected baseline. |
| `ADV-002` - source label removal | `OBS005` displays "Samsung Electronics Sustainability Report 2026" | `source_name` is blank; `source_url` and `source_id` remain | Users lose the immediate human-readable report identity, although the remaining URL and source ID still provide a route to provenance. | The current validator emits an `empty_source_name` warning; record-level diff also detects the edit. Treat warnings as a review signal; preserve source metadata and require reviewer approval. |
| `ADV-003` - water-feature omission | Seven records include three water observations: recycled water, Taiwan-fab tap-water consumption, and normalized wafer-layer intensity | All three water rows are removed; four records remain | The view can hide water-related resource information and overemphasize energy/emissions. Missing rows must not be interpreted as zero. | Compare record IDs, row counts, and expected feature coverage with the trusted version; review the change log and manifest. Prevent with versioned inputs, required-feature checks, and separation of adversarial/trusted paths. |

The exact before/after values and record IDs are generated in `adversarial_change_log.csv`; the table above summarizes the current deterministic manipulation rules. Regenerate the artifacts after changing the trusted dataset and update this analysis from the new log.

## Comparison findings

The numeric edit changes an energy total but does not establish a real-world increase; it is a deliberately altered single record. The missing water rows remove all water coverage from this seven-record demonstration. The source-label edit weakens human-readable provenance but does not fully unlink the observation because its source ID and URL remain. Together, these demonstrate data-value, completeness, and presentation risks. They do not demonstrate manipulation of a real Power BI report, hidden filters, or changed visual scales.

The dataset is heterogeneous and does not support ranking TSMC, Samsung, eGRID, or the EPA sector total. The meaningful lesson is that integrity checks and visible provenance help reviewers detect tampering but cannot make unlike boundaries comparable or prove that publisher-reported values are scientifically correct.

## Captured dashboard evidence

The current local browser prototype was recaptured after the multi-screen dashboard refactor and saved under `evidence/`:

- `trusted-overview.png` - reviewed energy observation, unit, source, and limitation.
- `measure-guide.png` - measure definitions and comparison cautions.
- `provenance.png` - record-level source and conversion information.
- `integrity.png` - validation and manifest status.
- `adversarial-energy-source-units.png` - trusted 27,456 GWh versus simulated 41,184 GWh.
- `adversarial-water-omission.png` - removed water rows shown as removed, not zero.

These are screenshots of the local browser dashboard, not a native Power BI report. Power BI Desktop was unavailable; no `.pbix`/`.pbip` or Power BI screenshot is claimed. The import-ready CSV model and report design are documented in [`power_bi_setup.md`](power_bi_setup.md).
