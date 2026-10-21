# Climate-Feature Dashboard for Semiconductor Technology

This project is a Python data-preparation and integrity-checking foundation for the class assignment. The full assignment requirements are in [`docs/project_instructions.pdf`](docs/project_instructions.pdf). Their relationship to the current project and completion criteria is tracked in [`docs/requirement_traceability.md`](docs/requirement_traceability.md).

> **Data status:** `data/raw/environmental_data.csv` remains a synthetic test fixture, not research evidence. The dashboard launcher processes the separate intake dataset, which contains seven observations checked against the PDFs in `data/intake/incoming/`. These company, grid, and sector indicators form a deliberately bounded proof of concept, not a representative semiconductor-industry dataset. Do not present synthetic sample values as research findings or treat reported aggregates as facility measurements.

## Current implementation status

Implemented:

- A modular Python package for schema checks, data validation, trusted-data export, SHA-256 manifests, and a controlled adversarial copy.
- A source-backed dashboard data path that validates the seven reviewed intake observations into separate reviewed outputs; the synthetic raw fixture remains available for pipeline tests.
- A clearly labeled 24-row synthetic dataset for exercising the pipeline.
- A dependency-free local dashboard-as-presentation with ten navigable screens for project summary, environmental data, units, provenance, reports and papers, threat references, controls, incident response, integrity, and adversarial comparison. Report, measure, year, organization, and unit-basis filters keep source-backed, missing, and simulated data distinct.
- Validation and integrity tests, plus data dictionary, threat model, incident-response, and Power BI setup documentation.
- A repeatable Power BI CSV model that summarizes environmental observations, provenance, research papers, ATT&CK reference mappings, implemented versus proposed controls, incident response, integrity, and adversarial changes.

Remaining external or conditional work:

- Broader source data are not required for the declared bounded scope; add observations only if the assignment requires broader coverage and sources can be reviewed for comparable definitions and boundaries. The project owner has certified the five selected papers as eligible for the assignment.
- The native Power BI `.pbix`/`.pbip` format is not required for the current submission: the assignment allows a dashboard prototype using other tools, and this repository already has the interactive browser dashboard. The CSV export remains available if a Power BI model is useful, but do not treat the lack of a native file as a project blocker.
- The latest full test suite passes 27 tests on Python 3.11 and 3.14. Clean first-launch checks on Windows and Ubuntu/WSL also succeeded. macOS and other CPU/platform combinations are not certified.

Power BI Desktop is optional. The browser dashboard is the project's selected presentation and reads the reviewed data directly through the launch pipeline. The 13-table CSV model and [Power BI build guide](docs/power_bi_setup.md) are an alternative, not a prerequisite; a native `.pbix`/`.pbip` file has not been authored.

The 31-section written report is [`docs/final_report.md`](docs/final_report.md); its requirement mapping is in [`docs/requirement_traceability.md`](docs/requirement_traceability.md). The live dashboard is the chosen presentation format; use [`docs/demo_runbook.md`](docs/demo_runbook.md) for the walkthrough and [`evidence/README.md`](evidence/README.md) for its current screenshots. Research framing and evidence are in [`docs/proposal.md`](docs/proposal.md), [`docs/data_source_plan.md`](docs/data_source_plan.md), and [`docs/literature_review.md`](docs/literature_review.md). The Power BI tables are generated under `data/powerbi/`; follow [`docs/power_bi_setup.md`](docs/power_bi_setup.md) for import, relationships, report pages, and safe measures. For the intake workflow, use [`docs/collecting_sources_and_data.md`](docs/collecting_sources_and_data.md) and the CSV templates in `data/intake/`. Security and architecture documentation is in [`docs/threat_model.md`](docs/threat_model.md), [`docs/incident_response.md`](docs/incident_response.md), and [`docs/system_architecture.md`](docs/system_architecture.md).

## Project layout

```text
climate_dashboard/       Python package
data/
  intake/
    incoming/            Original PDFs/CSVs awaiting review and classification
    *_template.csv       Source, paper, and observation intake templates
  raw/                   Input dataset
  processed/             Generated datasets, reports, and manifests
docs/                    Assignment and project documentation
tests/                   Automated tests
```

Python modules, test files, and Markdown documents use lowercase `snake_case` names.

## Requirements and setup

- Python 3.10+
- Windows PowerShell 5.1 or PowerShell 7, or a POSIX shell on macOS/Linux
- A current Chrome, Edge, Firefox, or Safari browser
- Internet access on first launch when the runtime dependencies are not already installed
- Power BI Desktop is optional if a `.pbix`/`.pbip` deliverable is specifically required

The launchers and responsive UI were exercised on Windows and Ubuntu/WSL. Other operating systems, CPU architectures, managed Python distributions, and browser versions are not individually certified; they need a working Python 3.10+ installation and compatible pandas wheel. On minimal Debian/Ubuntu installs, the `python3-venv` OS package may also be needed before the first Linux launch.

### Quick start from a fresh clone

No manual virtual-environment setup, test installation, Power BI Desktop, or generated `data/processed/` files are needed to launch the dashboard. From the cloned repository root, run the platform launcher:

```powershell
# Windows PowerShell
.\run.ps1
```

```sh
# macOS or Linux
./run
```

The launcher creates a project-local `.venv`, installs the runtime dependencies from `requirements.txt` if needed, prepares the reviewed dashboard data and Power BI CSV pack, and starts the browser dashboard. Python 3.10+ and internet access (or a local package cache containing compatible dependencies) are required on first launch. The root `run` script is executable on macOS/Linux; on Windows PowerShell, use `.\run.ps1`, and in Command Prompt use `run` or `run.cmd`. Shells intentionally do not run commands from the current directory by bare name in every configuration, so a universal bare `run` command requires an optional per-user profile shortcut.

### Optional development/test environment

From the project root in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

If activation is blocked, run the virtual environment's interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

For running the dashboard without tests, install only `requirements.txt`.

The server intentionally listens on `127.0.0.1`, so use the browser on the same device that runs the launcher. Other devices can clone the repository and run their own local instance; this prototype is not configured for phone/tablet access over a network.

## Run the data pipeline

```powershell
python -m climate_dashboard.pipeline
```

This validates `data/raw/environmental_data.csv` and creates:

- `data/processed/trusted_data.csv`
- `data/processed/validation_report.json`
- `data/processed/trusted_manifest.json`

The manifest records a SHA-256 hash. It must be protected separately from the data; changing both the CSV and its manifest defeats this basic comparison. A matching hash establishes file consistency against that reference, not scientific accuracy or trustworthy sourcing.

To process the reviewed intake without replacing the synthetic sample or its default outputs, run:

```powershell
python -m climate_dashboard.pipeline --input data/intake/observations_template.csv --output-dir data/processed/reviewed
```

This creates a separate normalized file, validation report, and manifest in `data/processed/reviewed/`.

## Generate the controlled adversarial example

After running the trusted pipeline:

```powershell
python -m climate_dashboard.adversarial
```

This creates a manipulated copy, a change log, and a manifest under `data/processed/`. The script does not overwrite the raw or trusted dataset.

## Run the local browser dashboard

From the repository root, use the platform launcher directly:

```powershell
# Windows PowerShell
.\run.ps1
```

```sh
# macOS or Linux
./run
```

The launcher regenerates the reviewed trusted dataset, creates a separate adversarial copy, then starts the app and opens the browser. Stop it with `Ctrl+C`. On Windows, use `.\run.ps1 -Port 8766 -NoBrowser` to choose another port or keep the browser closed. If the PowerShell policy blocks scripts, use `powershell -ExecutionPolicy Bypass -File .\run.ps1`.

For a bare `run` command from inside the repository, install the optional per-user shell shortcut using `.\install_run_command.ps1` on Windows PowerShell or `sh ./install_run_command.sh` on macOS/Linux. Open a new terminal or reload the profile afterward.

Both launchers require Python 3.10 or newer. Windows selects the newest supported interpreter registered with the Python Launcher; macOS/Linux uses `python3` (or `python`) and checks its version. They create a project-local `.venv` when needed, install the runtime `requirements.txt` only when pandas is missing, then perform the complete data-preparation and dashboard run. The lightweight dashboard module avoids importing pandas until preparation starts; the trusted pipeline and adversarial generator run in one Python process so pandas is loaded once. The app remains local to `127.0.0.1`.

Manual launch, if preferred:

```powershell
.\.venv\Scripts\python.exe -m climate_dashboard.launcher
```

The server binds only to `127.0.0.1`. Ten menu-separated views cover project summary, filtered environmental observations, measure guidance, searchable provenance, reports and research, threat references, security controls, incident response, validation/hash checks, and controlled adversarial comparison. Dropdowns select reports, measures, years, organizations, and unit basis. Values are not aggregated across unlike measures; removed records are labeled as missing rather than zero. A hash mismatch or failed validation is shown as a warning. Hash agreement does not prove source accuracy, and the manifest still needs independent protection.

See [`docs/dashboard_local.md`](docs/dashboard_local.md) for view details, data refresh steps, and security limitations. The ignored `data/processed/reviewed/` directory keeps this source-backed demonstration separate from the synthetic default dataset.

## Verify integrity

```powershell
python -m climate_dashboard.integrity data/processed/trusted_data.csv data/processed/trusted_manifest.json
```

To demonstrate detection, edit a copy of the trusted CSV and verify that copy against the original manifest; verification should fail.

## Run tests

```powershell
python -m pytest
```

Install `requirements-dev.txt` first in a clean development environment; it includes the runtime dependencies and pytest.

## Build the Power BI report

The local browser dashboard is the current working prototype. Follow [`docs/power_bi_setup.md`](docs/power_bi_setup.md) only if the assignment specifically requires a Power BI `.pbix`/`.pbip` deliverable; Power BI Desktop must be installed separately. The repository does not contain a finished Power BI report.

## Data fields

Each row represents one metric measurement. Do not aggregate unlike units. Keep the source definition, reporting boundary, year, and limitations visible when comparing values.

The observation CSV must include the fields `record_id`, `company`, `facility`, `geography`, `metric`, `value`, `unit`, `data_year`, `source_name`, `source_url`, `source_type`, `lifecycle_boundary`, `data_status`, `limitation`, `calculation_method`, and `last_validated`; their column order does not matter. The pipeline trims surrounding header whitespace and a UTF-8 BOM, then exports known fields in the documented order and preserves extra columns. See [`docs/data_dictionary.md`](docs/data_dictionary.md) for definitions and current validation rules.

## Academic and project integrity

- Keep source-backed observations distinct from synthetic demonstration values.
- Preserve full academic citations and summaries for the five required research papers.
- Keep trusted inputs and their known-good manifests in protected version control or backups.
- Label adversarial outputs as intentional simulations.
- Do not claim that hashes prove source accuracy or that the browser prototype is an enterprise-secured or native Power BI service.
