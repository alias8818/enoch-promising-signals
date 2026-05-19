# Enoch Promising Signals

Public companion repository for bounded Enoch research results that looked useful but did **not** qualify for the public paper corpus.

These records are **not validated papers**, **not peer reviewed**, **not publication-positive Enoch corpus artifacts**, and **not the paper corpus**. They preserve local/toy/small-scale evidence, stop reasons, and next-test ideas so promising leads do not rot when the next useful test exceeds local compute or wall-clock limits.

## Current export

The current export contains 519 deterministic, contract-clean signals from the Enoch control plane.

Status counts:
- `compute_scale_blocked`: 67
- `useful_signal`: 452

Deterministic curation buckets:
- [Top external-researcher candidates](signals/buckets/top-external-researcher-candidates.md): 129
- [Compute-scale blocked](signals/buckets/compute-scale-blocked.md): 67
- [Follow-up recommended](signals/buckets/followup-recommended.md): 212
- [Weak/local-only preserved signals](signals/buckets/weak-local-only-preserved.md): 61
- [Likely stale/low-value archive](signals/buckets/likely-stale-low-value-archive.md): 50

Start with the generated [ranked index](signals/ranked-index.md). The generated title index is in [signals/index.md](signals/index.md). Machine-readable source of truth is [data/signals.jsonl](data/signals.jsonl), ranking metadata is in [data/ranking.json](data/ranking.json), and count/status accounting is in [data/manifest.json](data/manifest.json).

## What belongs here

A record belongs here only when deterministic control-plane fields mark it as one of:

- `useful_signal`
- `promising_if_scaled`
- `compute_scale_blocked`

A record does **not** belong here when it is paper-positive, already imported into the public corpus, missing required claim/evidence boundaries, or only supported by an LLM interpretation without a deterministic control-plane field.

## Ranking rule

Ranking is deterministic. Bucket labels and scores are derived only from exported fields: evidence strength, hypothesis status, source lineage, compute-scale status, follow-up metadata/depth, and local evidence artifact references. No LLM review or manual judgment is allowed to become ranking truth unless a validator can recompute it.

## Public-release rule

This repository is public, but every entry remains a preservation record rather than an endorsement. Promoting a signal into the paper corpus requires a separate future run that independently becomes paper-positive and passes the normal paper/corpus release gates.

## Regeneration

The exporter lives in the system repo:

```bash
python3 scripts/export_promising_signals.py --output-repo ../enoch-promising-signals --clean-only
```

Validate the generated repository with:

```bash
python3 scripts/validate.py
python3 scripts/validate_public_trust_surfaces.py
```
