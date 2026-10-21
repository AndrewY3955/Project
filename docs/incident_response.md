# Incident-response plan

Use this plan when a trusted dataset, integrity reference, pipeline, or dashboard setting changes unexpectedly or when source credibility is in question. Do not use the intentionally manipulated training copy as evidence of a real incident.

For the classroom demonstration, use `data/processed/reviewed/trusted_data.csv` as the trusted baseline and `data/processed/reviewed/adversarial_data.csv` plus `adversarial_change_log.csv` as the intentionally altered branch. Their manifests are integrity references for their respective files, not proof that the source measurements are true or that a real incident occurred.

## 1. Preparation

- Keep the original user-provided sources, known-good trusted data, and a protected versioned backup.
- Protect the reference manifest separately from writers who can change the dataset; maintain key/signature custody separately if signatures are used.
- Record expected file locations, schemas, source provenance, transformations, reporting boundaries, dashboard versions, and responsible owners.
- Enable MFA, least privilege, change approvals, and platform audit logging where available.
- Know how to preserve a report copy and its model/filter settings before refresh or repair.

## 2. Detection and analysis

1. Record the report time, reporter, affected path/report, current file hashes, validation output, and observed behavior.
2. Stop refreshing or publishing the suspect data. Preserve a forensic copy and do not overwrite it with a regenerated output.
3. Compare files with the independently protected known-good version, not with a manifest stored under the same potentially compromised permissions.
4. Compare record IDs, row counts, metric coverage, values, sources, units, years, geography, lifecycle boundaries, assumptions, limitations, and uncertainty.
5. Review code, dependencies, report/model versions, refresh history, filters, chart scales, labels, and access/audit logs.
6. Determine affected metrics, time range, reports, and conclusions. Distinguish intentional test changes from unexplained events.

| Investigation question | Useful evidence | Limitation |
|---|---|---|
| What data changed? | Protected version history, known-good source copies, record-level diff, hashes | A matching hash without a protected reference is not proof of unchanged data |
| When did it change? | Trusted service audit timestamps, version-control event logs, backup snapshots | Local file timestamps may be changed or inaccurate |
| Which account or person changed it? | Identity-provider and repository/workspace audit logs, approved change records | A user/account event does not alone prove the human actor; shared or compromised credentials complicate attribution |
| Which systems and features were affected? | File/model diff, pipeline logs, refresh logs, report screenshots, feature/record comparison | Missing logs limit scope reconstruction |
| Were assumptions, sources, or visuals changed? | Prior report/model versions, source snapshots, filter/axis settings, review records | Screenshots alone may omit hidden filters or underlying model changes |
| Can trusted state be restored? | Protected backup, tagged release, signed artifact, clean validated source | A backup is not trustworthy if it shares the compromised write path |

## 3. Containment

- Stop publication and clearly mark affected outputs as under review.
- Restrict write access or disable compromised credentials/tokens through the relevant administrator.
- Preserve suspect files, manifests, logs, report versions, and screenshots in a separate evidence location with hashes and access control.
- Avoid editing the original evidence during containment.

## 4. Eradication

- Identify and remove unauthorized edits or the faulty transformation only after preserving evidence.
- Rotate/revoke compromised credentials and repair access-control gaps.
- Review pipeline, dependencies, data-source changes, and Power BI model settings.
- Restore required source citations, boundaries, units, and limitations; do not infer missing source facts.

## 5. Recovery

- Restore the last known-good source/data/report from a protected version or backup.
- Re-run validation and automated tests; review every reported warning and failure.
- Verify hashes/signatures against the independently protected reference.
- Refresh Power BI and verify values, metric coverage, source details, filters, axes, labels, units, and reporting boundaries.
- Have an independent reviewer approve the recovered output before publishing.

## 6. Lessons learned

- Record timeline, affected data and visuals, supported attribution, impact on conclusions, evidence preserved, controls that worked, and unresolved uncertainty.
- Add a targeted test, access control, approval, monitoring rule, backup, or dashboard review based on the root cause.
- Update the threat model, source plan, data dictionary, and response procedures.
- Notify stakeholders of corrected or withdrawn conclusions where needed.

## Evidence and attribution limits

Do not claim a person, account, or exact time caused a modification unless trustworthy audit evidence supports it. Local file metadata and Git history may show a change without proving who performed it or whether the account was compromised. A publisher's incomplete data may be misleading even if no file was tampered with.
