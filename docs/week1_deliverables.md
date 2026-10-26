# Week 1 Deliverables Report
## Climate-Feature Dashboard for Semiconductor Technology

**Prepared by:** Andrew Yates

## 1. Purpose and research question

The project explores how a dashboard can present semiconductor-related energy, water, and greenhouse-gas (GHG) information without implying that unlike sources are directly comparable. It also demonstrates how changed values, hidden source details, or removed records can mislead users.

**Research question:** How can a source-aware dashboard communicate semiconductor environmental indicators while making differences in source scope and intentional data manipulation visible?

The goal is transparent reporting and data integrity—not a complete industry footprint or company ranking.

## 2. Environmental features

- **Energy use:** Reported energy totals, which may include electricity and fuels.
- **Water:** Consumption, recycling, and production-normalized water intensity.
- **GHG emissions:** Reported emissions with their organizational and emissions-scope boundaries.
- **Electricity carbon intensity:** Regional electricity-generation emissions factors.
- **Provenance:** Source, year, geography, unit, boundary, and known limitations.

Process-gas emissions, water scarcity, manufacturing yield, packaging, and full product life-cycle impacts are discussed in the research but are not comprehensively represented in the current observations.

## 3. Research and data sources

Five academic papers were reviewed on semiconductor life-cycle impacts, foundry environmental performance, energy and water use, and water scarcity.

Registered sources include TSMC's 2024 Sustainability Report, Samsung Electronics' Sustainability Report 2026, US EPA eGRID data, and US EPA electronics-manufacturing emissions data. Intel corporate responsibility reporting is registered as a candidate source, but no observation has been extracted from it.

Every observation records its source locator, reporting year, unit, geography, boundary, and limitations. Registering a source does not mean data have been extracted from it.

## 4. Data dictionary and validation

Each record includes an identifier, organization/facility, geography, metric, value, unit, year, source, boundary, status, limitation, calculation method, and validation date.

The workflow checks required fields and metric-unit combinations, retains original source values and units where available, and records provenance and SHA-256 integrity information. Missing data are not treated as zero, and unlike measures are not combined.

## 5. Current implementation and limitations

The repository contains a local browser dashboard, seven source-checked observations, integrity checks, a controlled adversarial comparison, and a Power BI import-ready CSV model. Synthetic test data and manipulated records are kept separate from research observations. A native Power BI report has not been created.

The seven observations are a bounded proof of concept. They do not represent the entire semiconductor industry and cannot support an industry-wide estimate, trend, or company ranking.

## 6. Conclusion

The Week 1 deliverables establish the research question, environmental indicators, literature foundation, source-selection approach, and data dictionary. The central design principle is to show each environmental value with enough context to understand what it measures and where it came from.

## Further documentation

- [Final report](final_report.md)
- [Literature review](literature_review.md)
- [Data-source plan](data_source_plan.md)
- [Data dictionary](data_dictionary.md)
- [Dashboard guide](dashboard_local.md)
- [Power BI setup](power_bi_setup.md)
