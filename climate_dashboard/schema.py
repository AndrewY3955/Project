"""Schema and validation rules for the project dataset."""

REQUIRED_COLUMNS = [
    "record_id",
    "company",
    "facility",
    "geography",
    "metric",
    "value",
    "unit",
    "data_year",
    "source_name",
    "source_url",
    "source_type",
    "lifecycle_boundary",
    "data_status",
    "limitation",
    "calculation_method",
    "last_validated",
]

OPTIONAL_TRACEABILITY_COLUMNS = [
    "source_id",
    "source_locator",
    "original_value",
    "original_unit",
    "conversion_method",
    "uncertainty",
]

CANONICAL_COLUMNS = REQUIRED_COLUMNS + OPTIONAL_TRACEABILITY_COLUMNS

EXPECTED_UNITS = {
    "Electricity consumption": {"MWh"},
    "Electricity carbon intensity": {"kgCO2e/kWh"},
    "Water consumption": {"m3"},
    "Greenhouse-gas emissions": {"tCO2e"},
    "Total energy consumption": {"MWh"},
    "Water recycled from recovery systems": {"m3"},
    "Tap water consumption": {"m3"},
    "Water consumption per 12-inch equivalent wafer mask layer": {
        "L per 12-inch equivalent wafer mask layer"
    },
    "Scope 1 and Scope 2 greenhouse-gas emissions": {"t CO2e"},
    "Electricity-generation CO2-equivalent output emission rate": {"lb CO2e/MWh"},
    "Reported greenhouse-gas emissions": {"t CO2e"},
}

REQUIRED_TEXT_COLUMNS = {
    "company",
    "facility",
    "geography",
    "metric",
    "unit",
    "source_type",
    "lifecycle_boundary",
    "data_status",
}

ALLOWED_DATA_STATUSES = {
    "synthetic_demo",
    "reported",
    "estimated",
    "assumption",
    "derived",
}
