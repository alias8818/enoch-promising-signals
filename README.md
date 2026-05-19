# Enoch Promising Signals

Public companion repository for bounded Enoch research results that looked useful but did **not** qualify for the public paper corpus.

These records are **not validated papers**, **not peer reviewed**, **not publication-positive Enoch corpus artifacts**, and **not the paper corpus**. They preserve local/toy/small-scale evidence, stop reasons, and next-test ideas so promising leads do not rot when the next useful test exceeds local compute or wall-clock limits.

## Current export

The current export contains 246 deterministic, contract-clean signals from the Enoch control plane:

- `useful_signal`: bounded local evidence worth preserving.
- `promising_if_scaled`: a lead that may deserve larger-compute validation.
- `compute_scale_blocked`: a lead where the next meaningful test exceeds current local compute/time limits.

The generated index is in [`signals/index.md`](signals/index.md). Machine-readable source of truth is [`data/signals.jsonl`](data/signals.jsonl), with count/status accounting in [`data/manifest.json`](data/manifest.json), validated against [`schemas/promising-signal.schema.json`](schemas/promising-signal.schema.json).

## What belongs here

A record belongs here only when deterministic control-plane fields mark it as one of:

- `useful_signal`
- `promising_if_scaled`
- `compute_scale_blocked`

A record does **not** belong here when it is paper-positive, already imported into the public corpus, missing required claim/evidence boundaries, or only supported by an LLM interpretation without a deterministic control-plane field.

## Public-release rule

This repository is public, but every entry remains a preservation record rather than an endorsement. Promoting a signal into the paper corpus requires a separate future run that independently becomes paper-positive and passes the normal paper/corpus release gates.

## Regeneration

The exporter lives in the system repo:

```bash
python3 scripts/export_promising_signals.py --output-repo ../enoch-promising-signals --clean-only
```

The exporter fails closed for selected rows with missing required fields. For full backfills, `--clean-only` exports only rows that satisfy the deterministic public record contract and records skipped bucket counts in `data/manifest.json`. Validate the generated repository with:

```bash
python3 scripts/validate.py
```
