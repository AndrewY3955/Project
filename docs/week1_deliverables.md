# Week 1 Deliverables Report
## Climate-Feature Dashboard for Semiconductor Technology

**Project:** Semiconductor Climate Data Dashboard  
**Prepared by:** Andrew Yates  
**Purpose:** Summarize the proposal, background research, environmental features, and data-source planning deliverables for Week 1.

## 1. Project Purpose

The project explores how a dashboard can present environmental information related to semiconductor manufacturing while making data sources, units, reporting boundaries, and limitations clear. It also demonstrates how changing a value, hiding source information, or removing records can mislead users.

The project focuses on transparency and data integrity. It is not intended to calculate a complete semiconductor-industry footprint or rank companies.

## 2. Research Question

How can a source-aware dashboard communicate semiconductor-related energy, water, and greenhouse-gas information while making differences in data scope and intentional data manipulation visible?

## 3. Environmental Features

The project considers these main measures:

- **Energy use:** Reported energy consumption, which may include electricity and fuels.
- **Water:** Water consumption, recycled water, and water-use intensity.
- **Greenhouse-gas emissions:** Reported emissions with their scope and organizational boundary.
- **Electricity carbon intensity:** Regional electricity-generation emissions factors.
- **Data coverage and provenance:** Source, reporting year, geography, units, and known limitations.

Other important topics—such as process-gas emissions, water scarcity, manufacturing yield, packaging, and full product life-cycle impacts—are discussed in the research but are not comprehensively represented in the current observation dataset.

## 4. Research and Data Sources

The project reviewed five academic papers addressing semiconductor life-cycle impacts, water and energy use, foundry environmental performance, and the geographic relationship between water use and scarcity. The papers support the decision to preserve units, boundaries, denominators, and limitations rather than treating every published number as directly comparable.

The registered data sources include:

- TSMC's 2024 Sustainability Report
- Intel's corporate responsibility reporting as a candidate source
- Samsung Electronics' Sustainability Report
- US EPA eGRID electricity-emissions data
- US EPA Greenhouse Gas Reporting Program electronics-manufacturing data

Company reports and government datasets provide different kinds of evidence. Each observation therefore needs its own source locator, reporting year, unit, geographic coverage, and boundary. A source can be registered without necessarily having an extracted observation.

## 5. Data Dictionary and Validation

The project data dictionary defines fields such as record ID, company, facility, geography, metric, value, unit, data year, source name, source URL, source type, lifecycle boundary, data status, limitation, calculation method, and validation date.

The data workflow checks required fields and metric-unit combinations and records provenance and integrity information. Original source values and units are retained for review where applicable. Missing data are not automatically treated as zero, and values are not combined when their definitions or boundaries differ.

## 6. Current Project Status

The project has progressed beyond the initial planning stage. The repository contains a local browser dashboard, documentation, a source-reviewed dataset with seven observations, integrity checks, and a controlled adversarial comparison. A separate synthetic dataset is used for testing and is not presented as research evidence. The project also includes a Power BI import-ready CSV model; it should not be described as a completed native Power BI report.

The seven observations form a bounded proof of concept. They are not a representative sample of the semiconductor industry and do not support an industry-wide estimate or direct company ranking.

## 7. Conclusion

The Week 1 deliverables establish the project's purpose, research question, environmental indicators, literature foundation, source-selection approach, and data dictionary. The main design principle is that environmental values should be presented with enough context to understand where they came from and what they actually measure. Clear provenance, validation, and limitations help prevent both accidental misinterpretation and deliberate data manipulation.

## Further Documentation

- [Final project report](final_report.md)
- [Literature review](literature_review.md)
- [Data-source plan](data_source_plan.md)
- [Data dictionary](data_dictionary.md)
- [Dashboard guide](dashboard_local.md)
- [Power BI setup](power_bi_setup.md)
