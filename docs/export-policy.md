# Promising signals export policy

This repo is a parking lane for bounded useful research signals. It is intentionally separate from the public paper corpus.

## Invariants

1. A signal is not a paper.
2. A signal is not peer reviewed.
3. A signal is not publication-positive unless a separate future run independently becomes paper-positive.
4. Public evidence is not copied by this export; local artifact paths remain local-only references.
5. Missing required fields fail the export.

## Included statuses

| Status | Meaning |
|---|---|
| `useful_signal` | Local evidence looked useful enough to preserve or deepen. |
| `promising_if_scaled` | The mechanism may need larger or longer testing to evaluate properly. |
| `compute_scale_blocked` | The next meaningful test exceeds current local compute or wall-clock limits. |

## Exclusions

The exporter excludes rows with live paper rows, corpus imports, `write_needed=true`, paper-positive states, unsupported hard negatives, and rows missing required claim boundaries.

## Token Superposition seed notes

The seed batch queried the Token Superposition-related project set around `https://arxiv.org/abs/2605.06546`. Four rows were exportable. Unsupported follow-up rows from the same branch were intentionally excluded because this repository preserves promising signals, not every no-paper result.
