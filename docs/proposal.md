# Project Proposal
## Climate-Feature Dashboard for Semiconductor Technology

## Purpose and research question

Semiconductor manufacturing uses substantial energy and water and can produce direct and indirect greenhouse-gas emissions. Public reports and government datasets describe parts of these impacts but differ in units, reporting periods, geography, and boundaries.

**Research question:** How can a source-aware dashboard communicate reported energy, water, and greenhouse-gas indicators relevant to semiconductor manufacturing while making differences in source scope and intentional data manipulation visible?

The project emphasizes traceability and careful interpretation. It does not calculate a complete semiconductor-industry footprint or rank manufacturers.

## Scope

The seven reviewed observations come from TSMC, Samsung Electronics' Device Solutions division, US EPA eGRID, and the EPA electronics-manufacturing sector profile. They cover total energy; recycled and consumed water; wafer-normalized water intensity; organizational GHG emissions; a regional electricity-generation emissions factor; and a broader electronics-manufacturing sector total.

These measures have different meanings and boundaries. Recycled water is not water consumption, a regional grid factor is not a company emissions total, and the EPA electronics sector includes non-semiconductor activities.

Research also discusses process gases, water scarcity, manufacturing yield, packaging, and life-cycle impacts, but the current observation set does not comprehensively measure them.

## Method

1. Preserve source documents and register each source.
2. Transcribe values with a page/table locator, original unit, year, geography, boundary, and limitations.
3. Validate required fields and supported metric-unit pairs.
4. Generate reviewed outputs, validation results, and a SHA-256 manifest.
5. Keep synthetic test data and intentionally altered records separate from reviewed observations.
6. Present source context and controlled manipulation in the browser dashboard.
7. Document findings, security controls, limitations, and incident-response steps.

A successful hash check verifies bytes against a reference; it does not authenticate a publisher or prove a measurement is true.

## Deliverables and acceptance criteria

The repository includes a local interactive dashboard, data and source documentation, five reviewed academic papers, seven source-checked observations, integrity checks, a controlled adversarial comparison, a final report, and a Power BI import-ready CSV model. A native Power BI report has not been created.

The project is successful when it preserves traceability and original units, shows reporting context and limitations, avoids unsupported aggregation or rankings, labels synthetic and manipulated data, runs documented validation checks, and explains what the dataset can and cannot establish.

## Limitations

Seven heterogeneous observations demonstrate provenance and manipulation checks but cannot support industry totals, trends, or company rankings. Values were checked against cited reports, but publishers' measurement systems were not independently audited. Five papers have full-text reviews; paper eligibility was owner-certified rather than independently verified for every journal.
