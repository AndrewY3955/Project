# Assignment requirement traceability

This checklist maps `project_instructions.pdf` to the project artifacts required for a complete submission. “Existing foundation” means code or documentation exists but still needs review against the actual, source-backed project. It does not mean that the assignment requirement is complete.

| Assignment requirement | Intended artifact(s) | Current status / completion evidence |
|---|---|---|
| Project purpose, scope, research question, semiconductor features | `docs/proposal.md` | Pending. The repository describes the general assignment, but does not yet define a focused, evidence-backed question or selected feature scope. |
| At least five academic/peer-reviewed papers and full summaries | `docs/literature_review.md`, `docs/references.md`, `docs/source_intake_template.md` | Pending user-provided sources. Each paper must include citation, objective, studied feature, data/variables, impact, findings, limitations, and dashboard relevance. |
| Data-source plan and preliminary references | `docs/data_source_plan.md`, `docs/references.md`, `docs/source_intake_template.md` | Pending user-provided sources/data. Document source/organization, publication and data years, unit, feature, geography, lifecycle boundary, reliability, limitations, and validation method. |
| Verified, cleaned semiconductor-impact dataset and data dictionary | `data/raw/`, `data/processed/`, `docs/data_dictionary.md` | Partial foundation only. Current 24-row CSV is synthetic and broad; replace/supplement it with traceable source values and feature-specific metadata before drawing conclusions. |
| Data collection and validation methodology | `docs/data_source_plan.md`, `docs/data_dictionary.md`, `climate_dashboard/`, `tests/` | Partial foundation only. Existing checks cover a basic schema, values, units, status, and integrity; extend them to the selected sourced features and document limitations and uncertainty. |
| Threat model: assets, attackers, motivations, vectors, vulnerabilities, risks, indicators, consequences | `docs/threat_model.md` | Existing draft; review and complete against the implemented architecture and chosen attacker scenario. |
| Attacker-versus-defender scenario and defensive controls | `docs/threat_model.md` | Existing draft; pending assignment-specific scenario, attacker/defender profiles, and defensible controls. |
| Six-stage incident response and investigation evidence | `docs/incident_response.md` | Existing draft; review coverage of preparation, detection/analysis, containment, eradication, recovery, lessons learned, and limits of attribution. |
| System/data-flow or architecture diagram | `docs/system_architecture.md` | Draft diagram and trust boundaries now exist; verify and update them against the final sourced data workflow and Power BI report. |
| Secure dashboard prototype and accurate dashboard | Power BI project/report plus `docs/power_bi_setup.md` | Pending. Current document is a build guide, not a finished Power BI report. |
| Multiple environmental/technology-impact visualizations and transparency | Power BI report | Pending. Show applicable measures, source, data year, units, geography, lifecycle boundary, assumptions, limitations, and uncertainty/confidence. Avoid unsupported comparisons or unlike-unit aggregation. |
| Dashboard security and integrity features | Power BI report, pipeline outputs, `docs/threat_model.md` | Partial foundation only. Python hashing and validation exist; show and verify provenance, versioning, audit/change evidence, statuses, and integrity information in the report. |
| Separate controlled manipulated dashboard | Separate Power BI report/page and adversarial dataset | Partial foundation only. A script creates a manipulated data copy, but the dashboard view and complete documented comparison are not yet built. |
| Manipulation register and side-by-side evidence | `docs/manipulation_comparison.md`, dashboard screenshots | Pending. For every manipulation, document original and altered state, method, likely detectability, changed conclusion, trust impact, detection/prevention controls, and responder evidence. Include at least one non-numeric manipulation. |
| Complete written report and references | `report/` or `docs/final_report.md` | Pending. Follow the final-report section list in the PDF and link claims to sources and project evidence. |
| Presentation and live/recorded demonstration | `presentation/` and/or `evidence/demo.*` | Pending. Demonstrate the true and manipulated versions and cover research, sources, security, comparison, findings, and limitations. |
| Final project files and reproducible validation | Repository, tests, README, submission package | Partial foundation only. Python compilation, 9 automated tests, pipeline generation, adversarial generation, and trusted hash verification have passed; rerun after final data and dashboard changes. |

## Final acceptance criteria

1. Every deliverable in the assignment maps to a present, reviewable artifact; no “pending” requirement is presented as complete.
2. The final analysis uses traceable, verified source data. Synthetic and intentionally manipulated values are clearly labeled and used only for controlled demonstrations.
3. Each paper and data source is independently verified; citations, source metadata, assumptions, conversions, uncertainty, and reporting boundaries are documented.
4. The trusted dashboard can be refreshed from the documented pipeline and its views agree with the validated data.
5. The manipulated dashboard is separate, every intentional change is logged, and screenshots show the actual dashboards.
6. The comparison addresses climate conclusions, user trust, detection/prevention, and investigation evidence.
7. The final report and presentation cover the assignment requirements and accurately reflect implemented evidence.
8. Automated tests, data/integrity checks, dashboard refresh, and a clean handoff pass after final changes.
