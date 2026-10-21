# Semiconductor Climate Data Dashboard

A local dashboard and research project exploring environmental data, source integrity, and controlled data manipulation in the semiconductor sector.

## Run the dashboard

Clone the repository, open a terminal **in the project folder**, and run the command for your terminal:

| Terminal | Command |
|---|---|
| Windows PowerShell | `.\run.ps1` |
| Windows Command Prompt | `run` |
| macOS or Linux | `./run` |

The launcher prepares the dashboard data, starts the local server, and opens your browser. First launch requires **Python 3.10 or newer** and internet access (or a local package cache) to install dependencies. You do not need to install Power BI Desktop or create generated data files first.

To type bare `run` in PowerShell, Bash, or Zsh, install the optional shortcut once from the project folder:

```powershell
.\install_run_command.ps1
```

```sh
sh ./install_run_command.sh
```

Open a new terminal afterward, go to the project folder, and type `run`. In Command Prompt, `run` works directly from the project folder without installing the shortcut.

The dashboard is for local use on the same device; it does not accept connections from other devices on your network.

## Project contents

- Ten-screen browser dashboard with filters for reviewed environmental observations, sources, reports, research, security controls, integrity, and a controlled adversarial comparison.
- Seven source-checked observations for a bounded proof of concept; they are not representative of the semiconductor industry.
- A separate synthetic test dataset. Synthetic and simulated values are labeled and are not research findings.

## Tests

Install development dependencies and run the test suite:

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest
```

## Documentation

- [Final project report](docs/final_report.md)
- [Requirement traceability](docs/requirement_traceability.md)
- [Dashboard guide](docs/dashboard_local.md)
- [Demo runbook](docs/demo_runbook.md)
- [Optional Power BI setup](docs/power_bi_setup.md)
- [Data dictionary](docs/data_dictionary.md)
