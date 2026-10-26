# Data dictionary

| Field | Type | Meaning | Validation |
|---|---|---|---|
| `record_id` | Text | Stable identifier for a measurement record | Required and unique |
| `company` | Text | Company label or synthetic example label | Required |
| `facility` | Text | Facility label or synthetic example label | Required |
| `geography` | Text | Geographic scope associated with the measurement | Required |
| `metric` | Text | Environmental measurement type | Must be a supported metric for unit checks |
| `value` | Decimal | Numeric measurement | Numeric and non-negative |
| `unit` | Text | Measurement unit | Must match metric's expected unit |
| `data_year` | Integer | Year represented by the record | Must be numeric |
| `source_name` | Text | Dataset/report source label | Required for real data; blank generates warning |
| `source_url` | Text | URL or citation locator for the source | Document and validate before using real data |
| `source_type` | Text | Source type | Examples: synthetic example, company report, government dataset, peer-reviewed paper |
| `lifecycle_boundary` | Text | Boundary represented by the value | Must be documented before comparisons |
| `data_status` | Text | Record status: `reported`, `estimated`, `assumption`, `derived`, or `synthetic_demo` | Must match an allowed status in `climate_dashboard/schema.py` |
| `limitation` | Text | Known caveat for the measurement | Blank generates warning |
| `calculation_method` | Text | Method used for derived calculations | Document formula and input sources if derived |
| `last_validated` | Date-like text | Date of last source/data review | Update during validation |

## Supported metric/unit pairs

- Electricity consumption → `MWh`
- Electricity carbon intensity → `kgCO2e/kWh`
- Water consumption → `m3`
- Greenhouse-gas emissions → `tCO2e`
- Total energy consumption → `MWh`
- Water recycled from recovery systems → `m3`
- Tap water consumption → `m3`
- Water consumption per 12-inch equivalent wafer mask layer → `L per 12-inch equivalent wafer mask layer`
- Scope 1 and Scope 2 greenhouse-gas emissions → `t CO2e`
- Electricity-generation CO2-equivalent output emission rate → `lb CO2e/MWh`
- Reported greenhouse-gas emissions → `t CO2e`

These are the project's initial unit conventions, not a claim that all source datasets use these units. Convert source values only with a documented method and retain original source units where useful.

## Unit interpretation and safe comparisons

- `MWh` is a unit of energy (1 MWh = 1,000 kWh). Total energy may include multiple energy carriers; do not relabel it as electricity consumption.
- `m3` is a volume (1 m3 = 1,000 litres). Recycled water, tap-water consumption, withdrawal, and consumption are distinct indicators even when their units are all cubic metres.
- `L per 12-inch equivalent wafer mask layer` is a normalized intensity. Its denominator is part of the unit and must be preserved; it is not comparable to an absolute water volume.
- `t CO2e` is a mass of greenhouse-gas emissions expressed as carbon-dioxide equivalent. Organizational coverage and emissions scope still need to match before comparing totals.
- `lb CO2e/MWh` is an emissions rate per unit of electricity generated. It is not an emissions total and must not be directly compared with `t CO2e`.

The dashboard offers a dropdown between standardized project units and the source-transcribed original value/unit. The standardized value is useful for consistent storage; the original value supports checking the extraction against the source. Neither choice harmonizes differing metric definitions or reporting boundaries. For comparisons, align the metric, period, unit basis, geography, organizational coverage, lifecycle/reporting boundary, and calculation method. A shared unit alone does not make two records comparable.

Metrics in this list have different scopes and must not be compared or summed as though they were equivalent. In particular, total energy is not electricity alone; recycled water is not water withdrawal or consumption; product-normalized water intensity is not an absolute volume; grid-average output emissions are not a company's purchased-electricity emissions; and EPA electronics-sector totals include activities beyond semiconductor fabrication. A new metric must be added here and to `EXPECTED_UNITS` in `climate_dashboard/schema.py` before the pipeline will accept it.
