# Local browser dashboard

## Start the dashboard

After installing the profile shortcut, open a PowerShell console and enter `run` from any working directory. It calls the project launcher, regenerates the normalized reviewed dataset and separate controlled adversarial copy, starts the server, and opens the default browser. The shortcut is in this Windows user's PowerShell profile; close and reopen the terminal after installation, or load the profile into the current console with `. $PROFILE`. If the dashboard is already running on the selected port, `run` refreshes its input files and opens the existing local page instead of attempting to start a duplicate server.

```powershell
run
```

If the profile shortcut has not been installed, or you use a non-PowerShell console, run the project script from the repository root:

```powershell
.\run_dashboard.ps1
```

Stop the foreground server with `Ctrl+C`. Use another port and suppress automatic browser launch with `.\run_dashboard.ps1 -Port 8766 -NoBrowser`. If the local PowerShell policy blocks scripts, invoke it with `powershell -ExecutionPolicy Bypass -File .\run_dashboard.ps1`.

On macOS or Linux, run `sh ./run.sh` from the repository root. To add a `run` shell function to Bash/Zsh, use `sh ./install_run_command.sh`, open a new terminal, change into the clone, and type `run`.

Both launch paths require Python 3.10 or later. They create `.venv` if needed and install the runtime dependencies in `requirements.txt` only when pandas is missing. An existing `.venv` is reused; an unsupported Python version is reported rather than silently replacing the environment. Tests are a development-only dependency in `requirements-dev.txt`. First launch needs internet access to install pandas unless it is already installed or available from a local package cache. Minimal Debian/Ubuntu installations may need the operating-system `python3-venv` package before the launcher can create `.venv`.

The launch scripts were exercised on Windows PowerShell and Ubuntu/WSL. macOS and other Linux distributions use the POSIX `run.sh` path but have not each been independently tested. The project requires Python 3.10+ and a compatible pandas wheel; unsupported architectures, managed Python distributions, or locked-down devices may need manual dependency setup. Use a current Chrome, Edge, Firefox, or Safari browser on the same device as the server. The loopback-only server deliberately cannot be opened from a separate phone/tablet or other network device.

For a prepared environment, the equivalent Python command is:

```text
python -m climate_dashboard.launcher
```

Use `--port 8766` to select another port or `--no-browser` to suppress automatic browser launch. The server binds only to loopback. Startup errors are reported rather than silently switching ports.

The app reads the generated files in `data/processed/reviewed/` and does not modify the intake, raw synthetic dataset, trusted CSV, or adversarial CSV. If a required output is missing, the page reports that the data needs to be generated.

## Views and controls

- **Project summary:** communicates the research question, record coverage, dataset limitations, pipeline state, and threat-intelligence scope.
- **Environmental data:** dropdowns select source report, measure, year, organization, and value basis (standardized project units or the value/unit transcribed from the source). Each bar is one individual record; no rows or unlike units are aggregated. Bar lengths are relative only within that selected measure.
- **Measure guide:** switch between every metric and review standardized and original source values, unit meaning, geography, reporting boundary, and comparison cautions. This is a reference view, not a cross-metric chart or ranking.
- **Records & provenance:** search all reviewed records and inspect source URL/locator, original value and unit, conversion method, uncertainty note, scope, and limitation.
- **Reports & studies:** inspect a report or paper, including publisher, source URL, evidence, findings, review status, and limitations. A registered source with no reviewed observation is explicitly shown as having no data, not zero; paper summaries are not treated as measurements.
- **Threat intelligence:** browse ATT&CK scenario references and their project relevance, evidence, coverage, and attribution caveat. These are not a live feed or observed activity.
- **Security controls:** filter the control inventory by implemented, documented-manual, or recommended status.
- **Incident response:** select among six response stages and review objectives, actions, and exit criteria.
- **Integrity checks:** view pipeline validation, the trusted CSV's SHA-256 against its manifest, and each Power BI context-pack validation. A mismatch is explicitly surfaced above all views.
- **Adversarial comparison:** dropdowns select report, measure, year, and value basis. Each comparison card shows value, geography/year/facility, boundary, source label, and whether the value/record/source label changed. Event-log values use the selected unit basis when a numeric value was altered. A removed record is labeled as removed, not zero.

The five manipulation events currently cover the generator's energy-value change, source-label removal, and three omitted water rows. The adversarial file is intentionally altered for a classroom exercise and must not be used as source-backed evidence.

## Understanding units and comparisons

- **MWh:** megawatt-hours, a total energy quantity. The TSMC observation includes purchased electricity, natural gas, and diesel; it is not an electricity-only figure.
- **m³:** cubic metres of water (`1 m³ = 1,000 L`). Recycled water, tap-water consumption, withdrawal, and total consumption are different measures and should not be substituted for one another.
- **L per 12-inch equivalent wafer mask layer:** a production-normalized water-intensity measure, not an absolute volume. Compare only with the same normalization basis.
- **t CO₂e:** metric tonnes of carbon-dioxide equivalent. The Samsung value is division-level Scope 1+2; the EPA value is an electronics-sector total that includes non-semiconductor activity. They are not like-for-like observations.
- **lb CO₂e/MWh:** a grid-average generation emissions rate, not a company emissions total. Do not compare it directly to t CO₂e.

“Standardized project units” means the converted value used by the CSV/pipeline; “Original source units” preserves the number and unit as transcribed from the source. The basis selector changes labels and numbers consistently, including the numeric manipulation comparison; an altered value is scaled by the same conversion factor so both sides retain matching units. A common unit is not enough to establish comparability: confirm measure definition, year, geography, organizational coverage, reporting boundary, and method. Most measures have only one observation, so this dataset cannot provide peer comparisons or company rankings.

## Refresh and verify

After changing reviewed input data, rerun `.\run_dashboard.ps1` or the two generation commands above. Review `data/processed/reviewed/validation_report.json` and confirm the trusted hash check shows a match before interpreting the trusted view. The `.gitignore` excludes generated `data/processed/` artifacts; preserve the source intake and review evidence separately.

## Scope and security limitations

This is a local prototype, not an enterprise dashboard or a finished Power BI report. It uses a dependency-free Python HTTP server, fixed static routes, a read-only JSON endpoint, security response headers, and a loopback-only listener. It has no login, authorization, remote hosting, encrypted transport, protected audit service, or independent manifest trust anchor. Do not expose the server to a network or treat a matching hash as proof of source accuracy. The reviewed observations are reported aggregates with heterogeneous boundaries, not a representative industry sample.

The app is split into `run_dashboard.ps1` and `run.sh` (cross-platform environment bootstrap), `climate_dashboard/launcher.py` (one-process data preparation and server launch), `climate_dashboard/dashboard.py` (lightweight data loading and local server), `climate_dashboard/dashboard_ui/index.html` (view structure), `styles.css` (presentation), and `app.js` (filters and rendering), so copy, layout, or view behavior can be changed independently. Importing the dashboard service does not import pandas. The launch orchestrator delays pipeline imports until data preparation, then runs both transformations in one process, avoiding a second pandas initialization.
