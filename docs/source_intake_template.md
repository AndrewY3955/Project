# Source and dataset intake template

Use this template when adding user-provided sources. Preserve original citations and files. Leave unknown fields blank and flag them for review; do not infer or fabricate them.

## Academic paper record

Create one record per paper:

| Field | Entry |
|---|---|
| Full citation | |
| DOI or stable publisher URL | |
| Peer-review/publication evidence | |
| Research objective | |
| Semiconductor technology or manufacturing feature | |
| Data and variables used | |
| Environmental/climate impact discussed | |
| Main findings | |
| Study limitations | |
| How it informs the research question/dashboard | |

## Dataset/source record

Create one record per source dataset or report:

| Field | Entry |
|---|---|
| Dataset/report name | |
| Source organization | |
| Original URL or supplied file name | |
| Publication/report year | |
| Data year or coverage period | |
| Semiconductor feature(s) represented | |
| Measurement unit(s) | |
| Geographic scope | |
| Lifecycle/reporting boundary | |
| Source reliability and reason | |
| Known limitations or uncertainty | |
| Validation method | |
| Access/permission notes | |

## Record-level data

Retain the source's original values and labels. For each normalized observation, record at minimum the fields in `data_dictionary.md`: record ID, entity/facility where available, geography, metric, value, unit, data year, source name/URL/type, lifecycle boundary, data status, limitation, calculation method, and validation date. Add original source units/values and conversion details when a transformation is necessary.

Allowed project data-status labels are `reported`, `estimated`, `assumption`, `derived`, and `synthetic_demo`. Mark a value `derived` only when its inputs, formula, units, and sources are documented. Mark intentional adversarial edits in the separate adversarial log, not as trusted source data.

## Review before ingestion

- Confirm the citation/URL resolves to the supplied source.
- Confirm the value, unit, year, location, scope, and boundary match the source.
- Record missing or conflicting metadata explicitly; do not silently fill it.
- Document conversion formulas and preserve original values.
- Identify any comparability limitations before placing observations in the same visual.
- Keep the provided original file unchanged and work from a controlled copy.
