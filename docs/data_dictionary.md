# Data Dictionary

Each row represents one environmental observation for a defined organization/facility, geography, metric, and reporting year. Keep the source context with the value; a number without its unit, boundary, and source is not enough for safe comparison.

## Fields

| Field | Meaning | Validation/use |
|---|---|---|
| record_id | Stable record identifier | Required and unique |
| company, facility | Organization and facility labels | Required; label synthetic examples |
| geography | Geographic scope | Required |
| metric | Measurement type | Must be registered for unit validation |
| value | Numeric measurement | Numeric and non-negative |
| unit | Measurement unit | Must match the metric's expected unit |
| data_year | Year represented | Numeric year |
| source_name, source_url | Source identity and link/locator | Required for real data; verify against source |
| source_type | Company report, government dataset, paper, synthetic example, etc. | Use an accurate category |
| lifecycle_boundary | Organizational, operational, or lifecycle boundary | Document before comparison |
| data_status | Reported, estimated, assumption, derived, or synthetic | Must use an allowed status |
| limitation | Known caveat | Document or flag for review |
| calculation_method | Formula/source for derived values | Required when a value is derived |
| last_validated | Date of last source/data review | Update during validation |

## Supported metric and unit conventions

- Electricity consumption → MWh
- Total energy consumption → MWh
- Electricity carbon intensity → kgCO2e/kWh
- Water consumption, recycled water, and tap-water consumption → m3
- Water consumption per 12-inch equivalent wafer mask layer → L per 12-inch equivalent wafer mask layer
- Greenhouse-gas emissions and Scope 1 plus Scope 2 emissions → t CO2e or the exact registered variant
- Electricity-generation CO₂e output rate → lb CO₂e/MWh

These are project conventions, not a claim that source reports use identical units. New metrics must be registered in this dictionary and the pipeline's expected-unit rules before use. Retain original values and units when converting.

## Interpreting values safely

- **MWh:** Energy. Total energy may include electricity and fuels; do not label it electricity-only.
- **m³:** Water volume. Recycling, withdrawal, and consumption are different measures.
- **L per 12-inch equivalent wafer mask layer:** Production-normalized water intensity, not an absolute volume.
- **t CO₂e:** Emissions mass. Reporting scope and organizational coverage still matter.
- **lb CO₂e/MWh:** Emissions rate for electricity generation, not a company's emissions total.

The dashboard can show standardized project values or the original source-transcribed value/unit. A common unit alone does not make values comparable. Check the metric definition, year, geography, organization, boundary, and method before comparing or aggregating. Missing data must not be treated as zero.

## Data quality notes

The source-backed dataset contains seven heterogeneous observations and is not suitable for industry-wide estimates or company rankings. Source checking confirms transcription against cited reports; it is not an independent audit of the publisher's measurement process. SHA-256 checks detect byte changes against a reference but do not prove source authenticity or factual accuracy.
