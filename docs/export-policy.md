# Promising signals export policy

This repo is a parking lane for bounded useful research signals. It is intentionally separate from the public paper corpus.

## Invariants

1. A signal is not a paper.
2. A signal is not peer reviewed.
3. A signal is not publication-positive unless a separate future run independently becomes paper-positive.
4. Public evidence is not copied by this export; local artifact paths remain local-only references.
5. Missing required fields fail selected-row exports and are skipped by the full `--clean-only` backfill.
6. `data/manifest.json` is the count/status contract for exported rows and skipped backfill buckets.

## Included statuses

| Status | Meaning |
|---|---|
| `useful_signal` | Local evidence looked useful enough to preserve or deepen. |
| `promising_if_scaled` | The mechanism may need larger or longer testing to evaluate properly. |
| `compute_scale_blocked` | The next meaningful test exceeds current local compute or wall-clock limits. |

## Exclusions

The exporter excludes rows with live paper rows, corpus imports, `write_needed=true`, paper-positive states, unsupported hard negatives, and rows missing required claim boundaries.

## Current full backfill

The current full backfill exported 245 rows that already satisfy the deterministic public record contract.

`data/manifest.json` records the selection summary:

- `export_cleanly_now`: exported rows.
- `missing_required_evidence_or_fields`: promising rows that remain parked until source/evidence fields are recovered.
- `excluded_paper_or_corpus`: rows that belong to the paper/corpus lane instead.
- `hard_negative_or_stale`: rows that are not promising-signal statuses.

Unsupported follow-up rows and missing-source rows are intentionally excluded because this repository preserves contract-clean promising signals, not every no-paper result.
