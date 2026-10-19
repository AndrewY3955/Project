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

EXPECTED_UNITS = {
    "Electricity consumption": {"MWh"},
    "Electricity carbon intensity": {"kgCO2e/kWh"},
    "Water consumption": {"m3"},
    "Greenhouse-gas emissions": {"tCO2e"},
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
