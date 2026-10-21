# Project pickup

## Current direction

The dashboard is the presentation: a dedicated multi-screen browser app navigated with one screen dropdown. The duplicate tab menu and slide deck were removed at the user's request. Keep source-reported, synthetic, and intentionally manipulated data clearly separated and labeled.

## Current state

- The 31-section report is in `docs/final_report.md`; the live walkthrough is in `docs/demo_runbook.md`.
- The local dashboard has ten screens: project summary, environmental data, measure guide, records and provenance, reports and studies, threat intelligence, controls, incident response, integrity checks, and adversarial comparison.
- Report, measure, year, organization, and value-basis filters are wired. Registered reports without reviewed observations show an explicit no-data state, not zero.
- The Power BI context pack has 13 validated CSV tables. Power BI Desktop is optional: the assignment permits other dashboard tools, and the browser dashboard is the selected presentation. No native `.pbix`/`.pbip` is needed unless the instructor explicitly requires that format.
- The report/context screens distinguish the five reviewed journal papers from the supplemental dissertation. Paper 2 was reviewed from page images because its PDF has no extractable text.
- Six evidence screenshots were recaptured from the current local dashboard at a 1600 × 1100 desktop viewport. They document the local prototype, not Power BI Desktop.
- The simulated branch remains separate from the trusted seven-record branch. The energy alteration and water-row removals are clearly labeled as classroom simulation.
- The seven source-checked records are the complete dataset for the declared bounded proof-of-concept scope; they are not representative. The separate `data/raw/` input remains a synthetic fixture used for pipeline tests. No unsupported gaps are filled with estimates.
- The demo runbook and README now describe the dashboard rather than a slideshow.

## Completion status

The assignment's dashboard deliverable is fulfilled by the interactive browser prototype; a separate Power BI report would use the same records and filters without adding a required project capability. The Power BI CSV pack remains available as an alternate import path. The local prototype has disclosed deployment limits: it is loopback-only and does not provide enterprise authentication, independent manifest protection, or publisher authentication.

## Verification to date

- Browser interaction exercised all ten screens at desktop, tablet, and narrow mobile widths; the single dropdown navigated every view, the API returned valid data, and no JavaScript errors or horizontal overflow were observed.
- Browser checks confirmed the empty-observation Intel report is not represented as zero, paper summaries are not treated as measurement records, and the TSMC energy and water examples show the expected simulated changes.
- The complete project test suite passes: 27 tests on Python 3.11 and 3.14 with deprecation warnings treated as errors.
- Python compilation and `git diff --check` passed. Git reported only LF/CRLF conversion warnings.
- The Power BI exporter regenerated 13 tables; all 10 validation checks passed and the trusted SHA-256 matched the manifest.
- Fresh clean copies on Windows and Ubuntu/WSL installed runtime dependencies only and served the dashboard API with HTTP 200. macOS and other CPU/platform combinations are not individually certified.

## Remaining checks

1. Complete the final security and repository review, then verify the staged file list before GitHub submission.
2. Keep the qualification that paper eligibility is owner-certified, not an independent audit of each journal's peer-review process.
3. Incoming research/report PDFs are intentionally excluded from GitHub to avoid redistributing copyrighted source documents. `gh` is not authenticated in this environment.

## Key locations

- `climate_dashboard/dashboard_ui/` — dashboard markup, styles, and interactions
- `data/powerbi/` — generated import-ready tables
- `docs/requirement_traceability.md` — assignment-to-evidence status
- `evidence/` — current local-dashboard screenshots
- `tests/` — pipeline, export, dashboard, and deliverable checks
