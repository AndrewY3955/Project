# Data-Source Plan

## Purpose and scope

The dataset demonstrates how to preserve provenance and interpret selected semiconductor-related environmental measures. It is a small proof of concept, not a representative sample or a consistent company comparison.

The seven reviewed observations cover energy, water recycling and consumption, wafer-normalized water intensity, organizational GHG emissions, a regional electricity-generation factor, and a broader electronics-manufacturing sector total. The five reviewed papers provide research context; study-specific figures are not mixed into the observation table.

Process-gas inventories, water-scarcity scores, packaging impacts, facility-level comparisons, and comparable historical company series remain outside the measured dataset because a sufficiently reviewed and consistently scoped record set is not available. No values are invented to fill gaps.

## Registered sources

| Source | Intended use | Coverage and key limitation |
|---|---|---|
| TSMC, *2024 Sustainability Report* | Total energy, recycled water, Taiwan-fab tap-water consumption, water per wafer equivalent | 2024; measures have different company/subsidiary or Taiwan-fab boundaries. Total energy includes purchased electricity, natural gas, and diesel. Values checked against report pp. 120 and 129. |
| Intel, *2025–26 Corporate Responsibility Report* | Candidate for future observations | Source identity checked; no observation extracted. Review each value, unit, year, boundary, and locator before use. |
| Samsung Electronics, *Sustainability Report 2026* | Device Solutions Scope 1 plus market-based Scope 2 emissions | 2024; division-level, not a semiconductor-foundry-only total. Value checked against p. 72; original unit and documented conversion are retained. |
| US EPA, *eGRID Summary Tables 2023* | CAMX regional electricity-generation CO₂e rate | 2023 regional generation factor, not a company-specific purchased-electricity factor. Rounded value checked against p. 2. |
| US EPA, *2011–2017 GHGRP Industrial Profile: Electronics Manufacturing Sector* | Reported electronics-manufacturing emissions | 2017 US reporting facilities, including non-semiconductor activities; not a semiconductor-only or company total. Value checked against p. 3. |

The source register is in [sources_template.csv](../data/intake/sources_template.csv); record-level references and caveats are in [observations_template.csv](../data/intake/observations_template.csv).

## Current observations

| Record | Value used in project | Year | Main caveat |
|---|---:|---:|---|
| OBS001 | 27,456,000 MWh total energy | 2024 | Includes electricity, natural gas, and diesel |
| OBS002 | 284,600,000 m³ recycled water | 2024 | Recycling is not withdrawal or consumption |
| OBS003 | 94,600,000 m³ Taiwan-fab tap-water consumption | 2024 | Taiwan fabs only |
| OBS004 | 161.0 L per 12-inch equivalent wafer mask layer | 2024 | Normalized intensity; denominator must be preserved |
| OBS005 | 14,546,000 t CO₂e | 2024 | Samsung Device Solutions Scope 1 plus market-based Scope 2 |
| OBS006 | 430.0 lb CO₂e/MWh | 2023 | Rounded CAMX regional generation factor |
| OBS007 | 6,100,000 t CO₂e | 2017 | EPA electronics sector, not semiconductor-only |

Original values and units remain recorded with observations. A documented unit conversion does not mean the underlying measurement was independently audited. Missing observations are not treated as zero.

## Collection and validation

1. Preserve original source files and record publisher, title, year, geography, unit, boundary, and limitations.
2. Transcribe the value and a page/table/field locator. Retain original value/unit and document any conversion.
3. Link every observation to its source ID and URL. Use “Not stated” when the source omits a detail; do not guess.
4. Check unique record IDs, required fields, numeric values, years, allowed statuses, metric-unit pairs, source links, and CSV structure.
5. Review the validation report. A PASS means implemented checks passed; it does not prove a source or claim is true.
6. Keep synthetic fixtures and intentionally manipulated records separate from source-reviewed observations.

## Comparison rules

A shared unit does not make measures comparable. Check metric definition, year, geography, organizational coverage, reporting boundary, and method. Do not combine total energy with electricity-only values, recycled water with consumption, water intensity with absolute volume, grid emission rates with company totals, or the EPA electronics-sector total with semiconductor-only emissions.
