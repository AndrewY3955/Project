# Project proposal

## Project

**Climate-Feature Dashboard for Semiconductor Technology**

## Purpose

Semiconductor manufacturing supports digital infrastructure but depends on energy-intensive fabrication, substantial water use, and processes that can produce direct and indirect greenhouse-gas emissions. Public company disclosures and government datasets describe parts of these impacts, but differ in units, reporting periods, geographic coverage, and boundaries. A dashboard can make those differences visible while demonstrating how data or visual manipulation could change a reader's interpretation.

This project develops a traceable data workflow and dashboard prototype for reporting selected semiconductor-relevant energy, water, and greenhouse-gas indicators. It also demonstrates data-integrity checks and a separate, explicitly manipulated copy.

## Research question

**How can a provenance-aware dashboard communicate reported energy, water, and greenhouse-gas indicators relevant to semiconductor manufacturing while making differences in source scope and intentional data manipulation visible to users?**

The project evaluates the dashboard's ability to expose provenance, units, reporting periods, geographic scope, lifecycle/reporting boundaries, and limitations. It does not estimate a single semiconductor industry's total climate footprint or rank manufacturers.

## Scope and selected features

The source-backed intake dataset currently contains seven observations from TSMC, Samsung Electronics' Device Solutions division, EPA eGRID, and the EPA Electronics Manufacturing sector profile:

- Reported total energy consumption. The TSMC measure includes purchased electricity, natural gas, and diesel; it is not electricity-only.
- Water recycling, Taiwan-fab tap-water consumption, and water consumption per 12-inch wafer equivalent. These are distinct measures and cannot be substituted for one another.
- Device Solutions Scope 1 plus market-based Scope 2 greenhouse-gas emissions. The division is broader than semiconductor foundry operations.
- The CAMX regional grid output-emissions factor. It is not a company-specific electricity procurement factor.
- EPA-reported electronics-manufacturing sector emissions. This sector includes activities beyond semiconductor fabrication and represents 2017, not a company or fab.

Academic literature also motivates attention to fabrication capacity, water-stress geography, ultrapure-water treatment, and product-normalized indicators. Those topics are contextual unless a traceable source-backed observation is added.

## Climate relevance

Fab electricity and fuel use contribute to operational energy demand and, depending on energy sources and accounting methods, emissions. Process and refrigerant gases may also contribute direct emissions; the currently accepted dataset does not yet provide a comparable, semiconductor-only process-gas inventory. Water withdrawal, consumption, recycling, and treatment affect local water resources and energy use, but a volume alone is not a measure of climate impact or water scarcity. The dashboard must therefore display each measure with its source definition and boundary and avoid combining unlike indicators.

## Method and planned system

1. Preserve user-supplied PDFs and CSVs in the intake area.
2. Record sources and paper metadata in their respective intake registers.
3. Transcribe reported observations with a PDF page/table locator, original value and unit, any explicit conversion, and limitations.
4. Normalize a working copy through the Python pipeline. Required columns may arrive in any order; registered metric/unit pairs are validated and unknown metrics are rejected.
5. Generate a separate trusted output, validation report, and SHA-256 manifest. Keep the synthetic demonstration dataset and its output separate from reviewed observations.
6. Build a transparent dashboard with an accurate view and a separate controlled adversarial view. Review units, filters, labels, provenance, and missing records.
7. Compare the two versions and document detection, prevention, trust impact, and incident-response evidence.

The manifest detects byte changes only against a protected reference; it does not authenticate source claims. The current implementation is a local classroom prototype, not a deployed enterprise security service.

## Limitations and acceptance criteria

The seven observations are heterogeneous, mostly aggregate, and too few to support a representative industry trend or company ranking. Their values were checked against supplied reports, but the review does not independently assure the publishers' underlying measurement systems. Papers 1-5 have full-text reviews; Paper 2 was reviewed from rendered page images because its PDF has no embedded text. Paper 6 is supplemental dissertation background and is not counted among the five journal-paper records. Peer-review policies were not independently documented for every journal, so the final submission should retain that qualification.

The proposal is successful when the dashboard and report:

- preserve source traceability and original units;
- show periods, scopes, geography, boundaries, limitations, and status;
- prevent unlike metrics from being summed or ranked without comparable definitions;
- keep synthetic and adversarial values separate from reviewed observations;
- pass documented validation and integrity checks; and
- clearly state what the data do and do not support.
