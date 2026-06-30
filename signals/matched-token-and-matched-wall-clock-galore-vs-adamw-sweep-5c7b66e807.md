# Matched-token and matched-wall-clock GaLore vs AdamW sweep at GPT-2-small scale

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `matched-token-and-matched-wall-clock-galore-vs-adamw-sweep-5c7b66e807`
Run ID: `matched-token-and-matched-wall-clock-galore-vs-adamw-sweep-5c7b66e807-20260630T130202008745+0000`

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

- Parent run decision: GaLore vs AdamW: memory-quality Pareto at GPT-2-small scale on GB10: enoch://control-plane/projects/galore-vs-adamw-memory-quality-pareto-at-gpt-2-small-scale-on-gb10-4bb30f3e09f1/runs/galore-vs-adamw-memory-quality-pareto-at-gpt-2-small-scale-on-gb10-4bb30f3e09f1-20260630T105903212319+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/091de4528619

## What looked useful

GaLore-style projection provided a large optimizer-state memory reduction and short-run regularization signal, but the local implementation's SVD overhead prevented a matched-wall-clock throughput advantage.

## Boundaries and scale limits

Synthetic data, one seed, 80 steps, 8192 vocabulary instead of full GPT-2 vocabulary, local non-fused SVD GaLore implementation, no real-corpus pretraining or downstream evaluation.

## Claim scope

On a 91.4M-parameter GPT-2-small-trunk model trained for 80 steps on deterministic structured synthetic tokens, a local GaLore-style projected AdamW optimizer reduced estimated optimizer-state bytes to 1.3-5.0% of AdamW and slightly improved held-out synthetic validation loss at matched token count, but achieved only about 25% of AdamW token throughput for matched-token runs and only 7-10 steps within AdamW's 80-step wall-clock budget.

## Why it stopped

Closed as no-paper useful signal: the local synthetic GPT-2-small-class sweep is informative but not direct publication-grade evidence for GaLore vs AdamW at real GPT-2-small pretraining scale.

## Recommended next action

Run a bounded real-corpus follow-up using an optimized or official GaLore implementation on WikiText/OpenWebText shards with AdamW LR tuning, at least 3 seeds, and both matched-token and matched-wall-clock reporting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus optimized GaLore vs AdamW GPT-2-small-class confirmation
- Success threshold: GaLore reaches validation loss no worse than 0.05 above tuned AdamW at matched tokens while using at most 10% optimizer-state memory, and reaches equal or better validation loss per wall-clock hour after projection overhead is included.
- Stop condition: Stop if optimized GaLore remains below 50% of AdamW token throughput and does not improve validation loss per wall-clock hour after the first calibrated medium run.

## Evidence references

- Artifact root: `<local-path>/projects/matched-token-and-matched-wall-clock-galore-vs-adamw-sweep-5c7b66e807`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
