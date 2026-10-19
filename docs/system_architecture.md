# Dashboard system and data-flow architecture

This is the planned local prototype architecture. A control shown below is a design requirement, not evidence that an enterprise identity, encryption, signing, or audit service has been deployed.

```mermaid
flowchart LR
    U["User-provided sources and dataset"] --> R["data/raw<br/>read-only source copy"]
    R --> P["Python validation and normalization pipeline"]
    P --> V{"Validation result"}
    V -->|Fail| E["Validation report<br/>review and correct source data"]
    V -->|Pass| T["Trusted normalized dataset"]
    P --> M["SHA-256 manifest"]
    T --> PB["Power BI trusted report"]
    M --> PB
    T --> A["Controlled adversarial-copy generator"]
    A --> X["Separate manipulated dataset"]
    A --> L["Manipulation log and adversarial manifest"]
    X --> PX["Power BI adversarial view/report"]
    L --> PX
    PB --> C["Side-by-side analysis and screenshots"]
    PX --> C
    V -. "validation checks" .-> Q["Automated tests"]
    P -. "hash comparison against protected reference" .-> Q
```

## Trust boundaries and controls

1. **Source to raw input:** Preserve supplied originals and citations. Do not silently correct source data. Record transformations separately, verify source metadata, and control write access.
2. **Raw input to pipeline:** Treat input as untrusted. Check required fields, identifiers, numeric values, years, units, provenance, allowed statuses, and required feature coverage. Fail visibly and preserve a validation report.
3. **Pipeline to trusted output:** Keep generated output separate from raw data. Record a version and SHA-256. Protect the known-good manifest independently; a writable adjacent hash file alone does not authenticate data.
4. **Trusted data to Power BI:** Restrict report/model edits, preserve source lineage, and independently review filters, axes, labels, units, reporting boundaries, and refresh results.
5. **Trusted to adversarial branch:** Copy trusted output before modification. Never write manipulated records back to raw or trusted files. Log every controlled change and label all adversarial outputs.
6. **Report to evidence/submission:** Capture screenshots from actual report versions and retain the report, datasets, validation output, and change log needed to reproduce each comparison.

## Design requirements

- Use least privilege and MFA for any shared account or cloud repository; encrypt data in transit and at rest where the storage platform supports it.
- Use version control, protected backups, and review/approval for trusted data or report changes.
- If an actor can alter both a dataset and its manifest, use a separately controlled digital signature/HMAC key or trusted artifact store; a plain SHA-256 file beside the dataset is not sufficient.
- Record who/when changed files only when backed by platform audit logs. Local file timestamps and Git history alone do not reliably prove person-level attribution.
- Clearly distinguish implemented demo controls from proposed organizational controls in the report.
