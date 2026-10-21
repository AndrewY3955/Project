# Power BI import model

## What is included

The repository now prepares a Power BI-ready CSV model that combines the reviewed environmental observations with concise source, literature, threat-reference, security-control, incident-response, integrity, and manipulation summaries. It does not claim that a native `.pbix` or `.pbip` was created: Power BI Desktop is not installed in this environment. The CSV pack works with Power BI Desktop's **Get data → Text/CSV** flow.

Power BI Desktop is an optional alternate presentation format, not a prerequisite for this project: the assignment permits other dashboard technologies, and the interactive browser dashboard already fulfills the dashboard role. Use this guide only if you prefer Power BI or the instructor specifically requests a native `.pbix`/`.pbip` file.

The pack is generated with the reviewed observations, adversarial copy, change log, and manifests:

```powershell
python -m climate_dashboard.launcher --no-browser
```

This prepares the reviewed outputs, validates and hashes the trusted CSV, creates the controlled adversarial copy, and refreshes `data/powerbi/`. To export after regenerating the reviewed outputs separately, use:

```powershell
python -m climate_dashboard.powerbi_export
```

The exporter stops with an explicit error if the trusted validation fails, its digest does not match the manifest, record IDs are duplicated, manipulation IDs do not resolve, a source link is missing, or a metric has no comparison guidance. `table_validation.csv` lists the pack's cross-table checks. A passing digest verifies bytes against the local manifest only; keep the reference independently protected for security use.

## Tables to import

Import every CSV in `data/powerbi/` as a separate table:

| CSV | Suggested Power BI table name | Use |
|---|---|---|
| `trusted_observations.csv` | `TrustedObservations` | Source-backed, reviewed observations and traceability fields |
| `adversarial_observations.csv` | `AdversarialObservations` | Separate intentional simulation; never use as trusted evidence |
| `manipulation_events.csv` | `ManipulationEvents` | One event per changed/omitted record |
| `record_dimension.csv` | `RecordDimension` | Union of trusted IDs, presence flags, and manipulation summary |
| `source_register.csv` | `SourceRegister` | Publishers, report years, geography, boundaries, validation and limitations |
| `research_papers.csv` | `ResearchPapers` | Five reviewed journal-paper records and their summaries |
| `metric_guide.csv` | `MetricGuide` | Units, climate relevance, boundaries, and comparison cautions |
| `threat_intel_reference.csv` | `ThreatIntelReference` | Scenario-relevant MITRE ATT&CK reference mappings |
| `security_controls.csv` | `SecurityControls` | Implemented versus proposed controls and residual limitations |
| `incident_response.csv` | `IncidentResponse` | Six-stage response process |
| `project_summary.csv` | `ProjectSummary` | Executive summary, dataset scope, and threat-intelligence disclaimer |
| `integrity_summary.csv` | `IntegritySummary` | Current validation and trusted-hash evidence |
| `table_validation.csv` | `PackValidation` | Cross-table checks performed during export |

Set `TrustedObservations[value]`, `TrustedObservations[original_value]`, and `AdversarialObservations[value]` to decimal numbers. Set year and count columns to whole numbers. Keep `ManipulationEvents[original_value]` and `[manipulated_value]` as text: those fields intentionally mix numeric edits, removed labels, and the text `row removed`. Keep IDs, labels, descriptions, dates, statuses, URLs, flags, and units as text unless a column below is explicitly typed as numeric. Keep original and standardized value/unit columns together.

## Build the report in Power BI Desktop

The repository contains the prepared data model, not a native report file. To create the report, install/open Power BI Desktop, then follow this repeatable workflow:

1. **Refresh the export pack.** From the repository root, run `python -m climate_dashboard.powerbi_export`. Confirm it completes successfully and every row in `data/powerbi/table_validation.csv` has `validation_status` = `PASS`. If the files are missing, first regenerate the reviewed pipeline, separate adversarial copy, and context pack using the launcher. Do not load a failed or stale export.
2. **Import the CSVs.** In Power BI Desktop choose **Home → Get data → Text/CSV**. Select each of the 13 CSVs in `data/powerbi/` and choose **Transform Data** (not a combined-folder import). In Power Query, name the queries exactly as the table names above, promote the first row to headers if needed, and retain each CSV as its own table.
3. **Set types before loading.** In Power Query, set each `TrustedObservations[value]` / `[original_value]` and `AdversarialObservations[value]` / `[original_value]` to decimal number; set both tables' `data_year`, `RecordDimension[data_year]`, and source-register year fields to whole number. Set count fields in `ProjectSummary` and `IntegritySummary` to whole number. Keep `ManipulationEvents[original_value]` and `[manipulated_value]` as text because events include numeric edits, a blanked label, and descriptive text such as `row removed`. Keep IDs, flags, validation fields, and `PackValidation[actual]` / `[expected]` as text. Check that numeric columns contain no conversion errors or silently introduced nulls. Choose **Close & Apply**.
4. **Create the relationships.** In **Model view**, add the one-to-many, single-direction relationships in the model section below. Confirm each dimension key is unique and each fact-side key can repeat. Do not create relationships among the standalone context tables or enable bidirectional filtering.
5. **Add measures, not implicit sums.** Create the safe measures below (right-click a table → **New measure**). For the environmental page, display a value only when filters reduce the context to one observation. Do not use Power BI's automatic `Sum of value` or average across different entities, units, years, or boundaries.
6. **Build the pages.** Add the six pages described below. Apply slicers only to the environmental fields relevant to that page, keep the source and boundary visible, and put the scope/disclaimer text in a visible text box. Use a table/matrix when multiple unmatched observations are selected instead of presenting a misleading aggregate.
7. **Validate and save.** Compare loaded row counts to the export CSVs and `IntegritySummary`; confirm the five adversarial events and three removed water records are represented. Test every slicer, check blank/no-data states, and make sure simulation labels remain visible. Save as `.pbix` (single-file report) or `.pbip` (project-folder format) in a submission/output directory, then reopen the saved file and refresh once to confirm it is reproducible.

Keep the authored report outside `data/powerbi/`, which is regenerated by the exporter. The repository ignore rules intentionally keep `.pbix`, `.pbip`, `.pbit`, and their project source files eligible for version control; only local Power BI caches and transient recovery files are excluded. Use version control or a protected backup for the native report and source data.

## Model relationships

Create one-to-many, single-direction relationships:

```text
RecordDimension[record_id] 1 ── * TrustedObservations[record_id]
RecordDimension[record_id] 1 ── * AdversarialObservations[record_id]
RecordDimension[record_id] 1 ── * ManipulationEvents[record_id]
MetricGuide[metric]         1 ── * TrustedObservations[metric]
MetricGuide[metric]         1 ── * AdversarialObservations[metric]
SourceRegister[source_id]   1 ── * TrustedObservations[source_id]
SourceRegister[source_id]   1 ── * AdversarialObservations[source_id]
```

Keep the paper, threat, control, incident-response, project-summary, integrity, and pack-validation tables available as standalone context pages. Do not connect the latter to observation rows using accidental many-to-many relationships.

## Suggested report pages

### 1. Executive summary

- Cards from `ProjectSummary`: trusted observations, sources, papers, and logged manipulation events. Use `Trusted Record Count` and appropriate distinct counts for live fact counts; the summary CSV counts are an export-time snapshot.
- A clear scope statement: seven heterogeneous reported observations; not a representative industry sample and not suitable for company ranking.
- A small table from `MetricGuide` explaining why metric values cannot be combined into a single total.

### 2. Environmental observations

- Slicers: metric, data year, company, geography, and data status.
- Table: company, facility, metric, value, unit, year, source, source locator, geography, lifecycle/reporting boundary, status, and limitation.
- Use a measure-specific visual only after filtering to one metric and a compatible unit/boundary. Most metrics have one record, so do not present them as trends or peer comparisons.
- Show `original_value` and `original_unit` in a tooltip or detail table when a value was converted.

### 3. Data provenance and integrity

- Source register and observation locator table.
- `IntegritySummary` cards for validation status, record count, warning count, and `trusted_manifest_match`.
- Show the SHA-256 in a text card with a note that Power BI displays the value but does not authenticate it. Verification is performed by the project pipeline against its reference manifest.

### 4. Trusted versus simulated

- Side-by-side trusted and adversarial values filtered to the same metric and unit.
- Use `RecordDimension` presence flags to show removed rows explicitly; missing is not zero.
- Add the `ManipulationEvents` table with the event, original/manipulated state, intended effect, detection evidence, and defensive control.
- Label the adversarial series **Controlled simulation — not source-backed evidence**.

### 5. Threat intelligence and controls

- `ThreatIntelReference` maps the project scenario to MITRE ATT&CK Enterprise techniques T1078, T1565.001, and T1565.002.
- Include technique ID, relevance, source link, and coverage status.
- Keep the disclaimer visible: this is a taxonomy-based scenario mapping, not a live threat feed, indicator-of-compromise list, observed attack, or actor attribution.
- Show `SecurityControls` with implementation status distinguished from recommendations.

### 6. Response and literature

- Timeline or six-stage list from `IncidentResponse`.
- Paper table with citation, feature studied, finding, limitation, and dashboard relevance; paper 6 is supplemental dissertation background and is not part of the five-paper register.

Keep these report-page conventions:

- Name pages in plain language (for example, **Executive summary**, **Environmental observations**, **Provenance & integrity**, **Trusted vs simulation**, **Threats & controls**, and **Response & literature**).
- Use descriptive visual titles, axis titles, units, source citations, and visible captions. Avoid 3-D effects, truncated axes, and red/green-only status encoding.
- Do not create a single sustainability score or cross-metric total from this dataset. If more than one observation remains in scope, use a detail table or an explicit blank result rather than summing.
- Show `data_status`, source, year, geography, reporting boundary, and limitation next to any observation visual; preserve original values and units in tooltips or a detail table.
- Keep the simulation visually distinct and label it **Controlled classroom simulation — not source-backed evidence** on every page that uses adversarial data.
- For dynamic missing-record review, use `RecordDimension` as the row field and show trusted/adversarial presence flags plus record-level measures. Do not count a missing row as a measured value of zero.

## Safe measures

Use a selected value rather than summing heterogeneous observations:

```DAX
Selected Trusted Value =
    SELECTEDVALUE(TrustedObservations[value])

Selected Adversarial Value =
    SELECTEDVALUE(AdversarialObservations[value])

Trusted Record Count =
    DISTINCTCOUNT(TrustedObservations[record_id])

Adversarial Record Count =
    DISTINCTCOUNT(AdversarialObservations[record_id])

Missing From Adversarial =
    CALCULATE(
        COUNTROWS(RecordDimension),
        RecordDimension[trusted_present] = "true",
        RecordDimension[adversarial_present] = "false"
    )
```

The `SELECTEDVALUE` measures intentionally return blank when the current selection contains multiple values. Do not replace that behavior with a sum or average across unlike boundaries or units. A trend is not supported unless compatible observations for multiple years are added and validated.

## Presentation and refresh workflow

1. Run `python -m climate_dashboard.launcher --no-browser` (or the cross-platform `run` command) to regenerate and validate the source-backed artifacts and export the Power BI tables.
2. Check the terminal result and `data/powerbi/table_validation.csv`; stop if validation is not `PASS`.
3. Refresh the Power BI model and verify row counts against `integrity_summary.csv`.
4. Inspect the source, year, geography, unit, status, boundary, missing-row flags, filters, and visual scales.
5. Clearly label the adversarial data as an intentional classroom simulation.
6. Save the authored report as `.pbix` or `.pbip` in Power BI Desktop if available, then capture screenshots of the actual pages for submission.

The included local browser dashboard is implemented and independently testable. The Power BI CSV model is import-ready, but Power BI Desktop was not available in the project environment, so no native report has yet been authored or visually validated.
