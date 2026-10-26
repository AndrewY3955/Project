# Project Plan and Status

The project has progressed from planning to a working proof of concept. This document summarizes completed work and limitations; detailed methods are in the linked guides and final report.

## Completed

1. **Research and data:** Five academic papers reviewed and seven source-checked observations documented. This limited source set cannot support an industry-wide estimate or company ranking.
2. **Threat model and response:** Risks, controls, integrity limitations, and a six-stage incident-response process documented. MITRE ATT&CK references provide scenario context only; they are not evidence of a real attack.
3. **Browser dashboard:** Ten views cover the project summary, environmental data, metric guidance, provenance, reports/studies, threat references, controls, incident response, integrity, and adversarial comparison.
4. **Controlled manipulation:** Five logged events demonstrate a changed energy value, a blanked source label, and three removed water records. Simulated data remain separate from reviewed observations.
5. **Power BI export:** A repeatable exporter creates 13 CSV tables with observation, source, research, security, response, and validation context. A native Power BI report has not been created.
6. **Reporting and demo:** The final report and dashboard walkthrough are documented. The browser dashboard is the presentation format; there is no separate slide deck.

## Validation and limits

The project records successful checks for the test suite, Python compilation, data export, integrity validation, and fresh launch on Windows and Ubuntu/WSL. macOS and other CPU/platform combinations have not been individually verified. The local service binds to loopback and is not an enterprise-secured deployment.

## Handoff notes

- Keep the five-paper eligibility qualification: paper selection was owner-certified, not an independent audit of every journal's review policy.
- Keep the seven observations within the declared proof-of-concept scope; add records only when suitable sources and comparable definitions have been reviewed.
- Never present synthetic or manipulated data as research findings.
- Confirm the changed-file list and documentation links before publishing.

## Key references

- [Final report](final_report.md)
- [Dashboard guide](dashboard_local.md)
- [Demo runbook](demo_runbook.md)
- [Requirement traceability](requirement_traceability.md)
- [Data-source plan](data_source_plan.md)
- [Power BI setup](power_bi_setup.md)
