# Threat model and data-integrity plan

## Scope and security objectives

The prototype handles user-supplied semiconductor/environmental source records, normalized CSV outputs, integrity manifests, Power BI report settings, and a deliberately manipulated demonstration. The primary security objective is to preserve provenance and detect unauthorized or misleading changes before data inform climate-related conclusions.

The current project is a local classroom prototype. It does not yet implement cloud identity, MFA, enterprise role-based access control, encryption/key management, or centralized audit logging. Those are controls to apply on the hosting platform, not claims about the current code.

## Assets

- Original source files, citations, source URLs, and publication metadata
- Raw and normalized trusted datasets, including units, boundaries, and limitations
- Data dictionary, transformation assumptions, validation rules, and tests
- Integrity manifests or signatures and known-good backups
- Python source code and dependencies
- Power BI model, visuals, filters, labels, and refresh configuration
- Adversarial copy, manipulation register, screenshots, and investigation evidence
- Final report and presentation claims based on the preceding evidence

## Threat actors and motivations

| Actor | Motivation | Relevant capability |
|---|---|---|
| Malicious insider or contributor | Promote a preferred conclusion, conceal an error, or bypass review | Write access to CSVs, scripts, report settings, or shared storage |
| External attacker with a compromised account | Alter evidence, disrupt the project, or misuse access | Stolen credentials or an exposed account/session |
| Vendor or source publisher | Present favorable or incomplete performance information | Control over published scope, assumptions, or reported records |
| Unintentional contributor error | Accidental misstatement or misleading comparison | Incorrect units, conversions, filters, formulas, or edits |

## Attacker-versus-defender scenario

A contributor account with write access to the shared project folder is compromised. The actor changes an electricity value, removes water records and source attribution, then changes a Power BI filter or axis so an unfavorable result is less visible. A simple re-hash performed after the edit would not help if the attacker can replace both the CSV and manifest.

Defenders preserve a known-good version in a separately protected repository/backup, use least privilege and MFA for shared services, review approved changes, validate record IDs/units/provenance/feature coverage, compare output with the protected reference, inspect report filters and model changes, and keep the manipulated training copy on a separate path. During response, they quarantine the changed copy and use platform audit logs and version history to investigate; they do not claim attribution without evidence.

## Attack vectors, weaknesses, and consequences

| Attack vector / weakness | Example manipulation | Potential consequence |
|---|---|---|
| Writable raw CSV or spreadsheet | Change a value, unit, year, location, or source | Invalid or incomparable climate result |
| Incomplete or selectively reported vendor data | Omit process gases, facilities, water stress, or lifecycle stages | Understated environmental impact despite an untampered file |
| Shared credentials or excessive write access | Replace files, pipeline code, or report | Unauthorized changes and loss of trustworthy baseline |
| Dataset and manifest stored under the same writer permissions | Replace both after changing data | Hash check appears valid against an attacker-chosen reference |
| Missing validation or test coverage | Duplicate IDs, non-finite values, absent features, or invalid units pass through | Silent data corruption or misleading comparisons |
| Power BI model/filter/visual edits | Cherry-pick years, change axis scale/labels, hide a metric | Misleading result without changing source measurements |
| Unsupported conversion or changed lifecycle boundary | Compare inconsistent units or system boundaries | False company/technology ranking |
| Loss of source report or lack of audit service | Evidence cannot establish who changed what or when | Delayed response; unsupported attribution |

## Defensive controls

### Data and software controls

- Preserve source originals; keep raw input, trusted normalized output, and adversarial copies separate.
- Validate identifiers, required metadata, numeric values, allowed statuses, units, years, and selected-feature completeness. Reject failures visibly.
- Record source, data/publication year, geography, lifecycle boundary, assumptions, limitations, uncertainty, and every conversion.
- Run automated tests and review code/report changes before accepting outputs.
- Generate a cryptographic digest and compare it with a known-good reference protected separately from the data. Use a digital signature or HMAC with separately controlled keys if writers can replace the manifest.
- Keep versioned, access-controlled backups; enable platform audit logs and change alerts where available.

### Access and operational controls

- Use MFA, least-privilege roles, separate read/write permissions, and remove access when no longer needed.
- Encrypt files in transit and at rest using the hosting platform's controls; protect signing keys/secrets independently.
- Require a second-person review for trusted-data, code, and report changes where practical.
- Review Power BI source lineage, refresh status, filters, axes, labels, units, and lifecycle boundaries before release.
- Label synthetic/adversarial examples prominently and prevent them from being mixed with trusted analysis.

### Control status

The Python validation, separate adversarial generator, SHA-256 manifest, and tests are implemented as local prototype controls. MFA, organizational access controls, encryption configuration, external key custody, central audit logs, protected remote backups, and Power BI workspace controls require configuration of the selected host/workspace and have not been established by this local source tree alone.

## Indicators of compromise

- Trusted hash does not match a separately protected known-good reference
- Unexpected row-count or record-ID changes; required metrics/features missing
- Blank/changed source, unit, year, geography, boundary, status, or limitation
- Unexpected value, pipeline, dependency, manifest, report-model, filter, or axis change
- Validation warnings/errors or unexplained changes in refresh results
- A trusted dataset and its manifest both changed without an approved record

## Severity and response triggers

Quarantine the affected output when an unexplained data/hash/report change could change conclusions. Escalate if trusted references or credentials may also be compromised. An intact hash does not clear a source that is incomplete, biased, or scientifically inaccurate; provenance review is separate from file-integrity review.

## Limitations

A hash detects byte changes only relative to a trusted, independently protected reference. It does not prove source truthfulness, completeness, scientific validity, or who made a change. Attribution and precise timing require trustworthy identity/audit evidence from the relevant platform; local metadata and Git history alone may be insufficient.
