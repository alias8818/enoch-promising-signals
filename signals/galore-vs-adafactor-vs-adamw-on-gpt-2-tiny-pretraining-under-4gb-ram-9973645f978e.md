# GaLore vs Adafactor vs AdamW on GPT-2-tiny pretraining under 4GB RAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-vs-adafactor-vs-adamw-on-gpt-2-tiny-pretraining-under-4gb-ram-9973645f978e`
Run ID: `galore-vs-adafactor-vs-adamw-on-gpt-2-tiny-pretraining-under-4gb-ram-9973645f978e-20260620T205332548346+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58ff8866ea9b

## What looked useful

Adafactor was the strongest bounded candidate: final loss 3.2040 with 17.9 KiB optimizer state. AdamW reached 3.3185 with 1054.1 KiB optimizer state. The GaLore proxy reached 4.5802 with 74.5 KiB optimizer state. All peak RSS values were about 354-360 MiB, below the 4 GiB target.

## Boundaries and scale limits

Not full GPT-2 pretraining; local byte corpus only; CPU-only; one seed; 40 steps; small 2-layer 64-wide model; GaLore is a local projected-gradient mechanism proxy rather than upstream package parity.

## Claim scope

Bounded CPU-only 40-step byte-level GPT-2-tiny-style causal Transformer comparison under a 4 GiB process RSS target. Adafactor achieved the best final loss and smallest optimizer state; the local GaLore-style projected AdamW proxy reduced optimizer state versus AdamW but converged worse.

## Why it stopped

Bounded CPU proxy produced useful early optimizer-memory evidence but not direct/full GPT-2 pretraining validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; deepen only with a standard small LM corpus, upstream-compatible GaLore, repeated seeds, and 1k-5k training steps under the same 4 GiB RSS telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-corpus 1k-step under-4GB optimizer comparison for AdamW, Adafactor, and upstream-compatible GaLore
- Success threshold: Adafactor or GaLore must finish within 5% of AdamW validation loss while reducing optimizer-state bytes by at least 5x and keeping peak RSS below 4 GiB.
- Stop condition: Stop if any memory-saving optimizer is more than 15% worse than AdamW validation loss after 1k steps or cannot stay below 4 GiB RSS with reproducible telemetry.

## Evidence references

- Artifact root: `<local-path>/projects/galore-vs-adafactor-vs-adamw-on-gpt-2-tiny-pretraining-under-4gb-ram-9973645f978e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
