# Climate-Feature Dashboard for Semiconductor Technology

This project is a Python data-preparation and integrity-checking foundation for the class assignment. The full assignment requirements are in [`docs/project_instructions.pdf`](docs/project_instructions.pdf). Their relationship to the current project and completion criteria is tracked in [`docs/requirement_traceability.md`](docs/requirement_traceability.md).

> **Data status:** The included CSV is synthetic demonstration data, not verified measurements from real companies or facilities. The current dataset covers broad environmental metrics only; it does not yet represent semiconductor process-node, packaging, process-gas, supply-chain, or other technology-specific features. Do not present the sample values as research findings.

## Current implementation status

Implemented:

- A modular Python package for schema checks, data validation, trusted-data export, SHA-256 manifests, and a controlled adversarial copy.
- A clearly labeled 24-row synthetic dataset for exercising the pipeline.
- Validation and integrity tests, plus data dictionary, threat model, incident-response, and Power BI setup documentation.

Still required by the assignment:

- Five selected academic papers with summaries and citations.
- A source plan and verified, traceable semiconductor-impact data.
- A secure dashboard prototype and a separate manipulated dashboard, with screenshots and a complete comparison analysis.
- The final written report, presentation, and live or recorded demonstration.

The supplied Power BI guidance is a build guide; this repository does not contain a finished `.pbix` or `.pbip` report.

The assignment requirement mapping is in [`docs/requirement_traceability.md`](docs/requirement_traceability.md). For a step-by-step intake workflow, use [`docs/collecting_sources_and_data.md`](docs/collecting_sources_and_data.md) and the CSV templates in `data/intake/`. Security and architecture documentation is in [`docs/threat_model.md`](docs/threat_model.md), [`docs/incident_response.md`](docs/incident_response.md), and [`docs/system_architecture.md`](docs/system_architecture.md).

## Project layout

```text
climate_dashboard/       Python package
data/
  raw/                   Input dataset
  processed/             Generated datasets, reports, and manifests
docs/                    Assignment and project documentation
tests/                   Automated tests
```

Python modules, test files, and Markdown documents use lowercase `snake_case` names.

## Requirements and setup

- Python 3.10+
- Dependencies from `requirements.txt`
- Power BI Desktop on Windows to build and view the report

From the project root in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If activation is blocked, run the virtual environment's interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the data pipeline

```powershell
python -m climate_dashboard.pipeline
```

This validates `data/raw/environmental_data.csv` and creates:

- `data/processed/trusted_data.csv`
- `data/processed/validation_report.json`
- `data/processed/trusted_manifest.json`

The manifest records a SHA-256 hash. It must be protected separately from the data; changing both the CSV and its manifest defeats this basic comparison. A matching hash establishes file consistency against that reference, not scientific accuracy or trustworthy sourcing.

## Generate the controlled adversarial example

After running the trusted pipeline:

```powershell
python -m climate_dashboard.adversarial
```

This creates a manipulated copy, a change log, and a manifest under `data/processed/`. The script does not overwrite the raw or trusted dataset.

## Verify integrity

```powershell
python -m climate_dashboard.integrity data/processed/trusted_data.csv data/processed/trusted_manifest.json
```

To demonstrate detection, edit a copy of the trusted CSV and verify that copy against the original manifest; verification should fail.

## Run tests

```powershell
python -m pytest
```

## Build the Power BI report

Follow [`docs/power_bi_setup.md`](docs/power_bi_setup.md) to import the generated data and assemble the proposed report pages. Use the generated data only as a labeled demonstration until it is replaced with source-verified data.

## Data fields

Each row represents one metric measurement. Do not aggregate unlike units. Keep the source definition, reporting boundary, year, and limitations visible when comparing values.

The CSV columns are `record_id`, `company`, `facility`, `geography`, `metric`, `value`, `unit`, `data_year`, `source_name`, `source_url`, `source_type`, `lifecycle_boundary`, `data_status`, `limitation`, `calculation_method`, and `last_validated`. See [`docs/data_dictionary.md`](docs/data_dictionary.md) for definitions and current validation rules.

## Academic and project integrity

- Replace synthetic values with traceable, verified sources before drawing conclusions.
- Preserve full academic citations and summaries for the five required research papers.
- Keep trusted inputs and their known-good manifests in protected version control or backups.
- Label adversarial outputs as intentional simulations.
- Do not claim that hashes prove source accuracy or that this code is a completed dashboard.
