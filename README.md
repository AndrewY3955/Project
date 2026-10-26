# Semiconductor Climate Data Dashboard

A local, source-aware dashboard that explores semiconductor-related environmental data and demonstrates how data manipulation can mislead users.

## Purpose

The project presents selected energy, water, and greenhouse-gas observations with their sources, units, years, geography, boundaries, and limitations. A separate, intentionally altered dataset demonstrates why data provenance and integrity checks matter.

This is a classroom proof of concept—not a complete industry footprint or company-ranking tool.

## Features

- Environmental observations with source and scope details.
- Metric guide and record-level provenance.
- Data validation and SHA-256 integrity checks.
- Controlled comparison showing a changed energy value, a blanked source label, and removed water records.
- Research, security-control, threat-reference, and incident-response views.
- A Power BI-ready CSV model for optional import.

## Run the dashboard

You need **Python 3.10 or newer**. From the repository root, run:

| Platform | Command |
| --- | --- |
| Windows PowerShell | `.\run.ps1` |
| Windows Command Prompt | `run.cmd` |
| macOS or Linux | `./run` |

The launcher prepares the data, starts the local server, and opens the dashboard. First launch may need internet access to install dependencies. Stop the server with **Ctrl+C**.

The dashboard is local-only and is intended for use in a browser on the same computer. See the [dashboard guide](docs/dashboard_local.md) for troubleshooting and optional shell shortcuts.

## Data and limitations

The reviewed dataset contains **seven source-checked observations** from company reports and US EPA sources. The observations use different years, geographies, reporting boundaries, and definitions; they cannot support an industry-wide estimate, trend, or company ranking.

Synthetic test data and manipulated records are separate from the reviewed observations and are not research findings. Validation and a matching local hash help check workflow consistency and file integrity against a reference; they do not prove that source claims are true or complete.

The project includes a **Power BI import-ready CSV model**, not a completed native `.pbix` or `.pbip` report. The browser dashboard is the primary interactive dashboard.

## Repository guide

- `climate_dashboard/` — dashboard and data-processing code
- `data/intake/` — source and observation registers
- `data/powerbi/` — generated Power BI CSV tables
- [Week 1 summary](docs/week1_deliverables.md)
- [Final report and references](docs/final_report.md)
- [Literature review](docs/literature_review.md)
- [Data-source plan](docs/data_source_plan.md)
- [Data dictionary](docs/data_dictionary.md)
- [Dashboard setup and views](docs/dashboard_local.md)
- [System architecture](docs/system_architecture.md)
- [Threat model](docs/threat_model.md) and [incident response](docs/incident_response.md)
- [Optional Power BI instructions](docs/power_bi_setup.md)

## Tests

Install development dependencies and run the tests:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest
```
