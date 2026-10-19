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
| `data_status` | Text | Reported/estimated/assumption/derived/synthetic label | Must be an allowed status |
| `limitation` | Text | Known caveat for the measurement | Blank generates warning |
| `calculation_method` | Text | Method used for derived calculations | Document formula and input sources if derived |
| `last_validated` | Date-like text | Date of last source/data review | Update during validation |

## Supported metric/unit pairs

- Electricity consumption → `MWh`
- Electricity carbon intensity → `kgCO2e/kWh`
- Water consumption → `m3`
- Greenhouse-gas emissions → `tCO2e`

These are the project's initial unit conventions, not a claim that all source datasets use these units. Convert source values only with a documented method and retain original source units where useful.
