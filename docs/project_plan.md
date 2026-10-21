# Practical four-week plan

## Completed project phases

1. **Research and data planning:** The proposal, source plan, data dictionary, five paper reviews, and seven source-checked observations are available. Paper 6 is supplemental dissertation background. The selected observations remain heterogeneous and cannot support an industry-wide estimate or company ranking.
2. **Threat model and response:** Assets, scenario, risk assessment, defender controls, integrity limitations, and the six-stage incident-response plan are documented. MITRE ATT&CK references are mapped as scenario context only, not as evidence of a real attack.
3. **Dashboard and adversarial demonstration:** The local dashboard-as-presentation has ten selectable screens for summary, environmental data, units, provenance, reports/studies, threat references, controls, incident response, integrity, and adversarial comparison. Report, metric, year, organization, and unit-basis filters are wired; missing observations are not shown as zero. Five deterministic manipulation events are logged separately from trusted records.
4. **Power BI preparation:** A repeatable exporter creates 13 import-ready tables containing trusted/adversarial data, source and paper registers, metric guidance, threat references, controls, response steps, hash/validation status, and model-validation results. Power BI Desktop was unavailable, so no native `.pbix`/`.pbip` is claimed.
5. **Final report and dashboard presentation:** The 31-section report, dashboard-screen demo runbook, and six current-browser screenshots are present. The dashboard is the presentation format per user preference; there is no slide deck.

## Remaining handoff checks

- The project owner has certified the five selected papers as eligible. The seven-record source-backed dataset is complete for the declared proof-of-concept scope; do not expand it with unverified or incomparable data. Add records only if the assignment requires broader coverage and suitable sources are reviewed.
- Final tests passed: 27 tests on Python 3.11 and 3.14 with deprecation warnings treated as errors; Python compilation, `git diff --check`, Power BI export/integrity validation, and fresh Windows and Ubuntu/WSL first-launch validation also passed.
- macOS and non-x86 CPU/platform combinations were not individually tested. The local service remains loopback-only by design.
- The interactive browser dashboard fulfills the dashboard requirement. A native Power BI report is optional unless specifically required by the instructor; the CSV export is available as an alternate workflow.
