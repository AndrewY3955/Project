# Semiconductor Climate Data Dashboard

A local dashboard and research project exploring environmental data, source integrity, and controlled data manipulation in the semiconductor sector.

## Project overview

The project examines how reported semiconductor-related energy, water, and greenhouse-gas indicators can be presented without implying that different sources are directly comparable. It also demonstrates how a changed value, obscured source label, or removed record can affect interpretation.

The project is a classroom proof of concept focused on transparent reporting and data integrity. Its seven source-checked observations are not representative of the semiconductor industry and do not support an industry-wide footprint estimate or company ranking.

## Week 1 deliverables

The Week 1 report summarizes the project purpose, research question, environmental features, literature foundation, data-source plan, and initial data dictionary.

- [Week 1 deliverables report](docs/week1_deliverables.md)
- [Final project report](docs/final_report.md)
- [Literature review](docs/literature_review.md)
- [Data-source plan](docs/data_source_plan.md)
- [Data dictionary](docs/data_dictionary.md)

## Run the dashboard

Clone the repository, open a terminal **in the project folder**, and run the command for your terminal:

| Terminal | Command |
|---|---|
| Windows PowerShell | \`.\run.ps1\` |
| Windows Command Prompt | \`run\` |
| macOS or Linux | \`./run\` |

The launcher prepares the dashboard data, starts the local server, and opens your browser. First launch requires **Python 3.10 or newer** and internet access (or a local package cache) to install dependencies. You do not need to install Power BI Desktop or create generated data files first.

To type bare \`run\` in PowerShell, Bash, or Zsh, install the optional shortcut once from the project folder:

\`\`\`powershell
.\install_run_command.ps1
\`\`\`

\`\`\`sh
sh ./install_run_command.sh
\`\`\`

Open a new terminal afterward, go to the project folder, and type \`run\`. In Command Prompt, \`run\` works directly from the project folder without installing the shortcut.

The dashboard is for local use on the same device; it does not accept connections from other devices on your network.

## Project contents

- Ten-screen browser dashboard with filters for reviewed environmental observations, sources, reports, research, security controls, integrity, and a controlled adversarial comparison.
- Seven source-checked observations covering selected company-reported energy and water measures, company-reported greenhouse-gas emissions, a regional electricity-generation factor, and a broader electronics-manufacturing sector total.
- Data validation and integrity documentation, including source provenance, metric-unit checks, and a SHA-256 reference.
- A separate synthetic test dataset. Synthetic and simulated values are labeled and are not research findings.
- A Power BI import-ready CSV model. This is not a completed native Power BI report.

Different metrics have different years, geographies, organizational boundaries, and definitions. The dashboard is designed to make those differences visible rather than combine unlike values.

## Tests

Install development dependencies and run the test suite:

\`\`\`powershell
python -m pip install -r requirements-dev.txt
python -m pytest
\`\`\`

## Documentation

- [Week 1 deliverables report](docs/week1_deliverables.md)
- [Final project report](docs/final_report.md)
- [Requirement traceability](docs/requirement_traceability.md)
- [Dashboard guide](docs/dashboard_local.md)
- [Demo runbook](docs/demo_runbook.md)
- [Optional Power BI setup](docs/power_bi_setup.md)
- [Data dictionary](docs/data_dictionary.md)
