# Adafactor Factored Second Moments vs AdamW on CPU Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adafactor-factored-second-moments-vs-adamw-on-cpu-pretraining-aeb892926838`
Run ID: `adafactor-factored-second-moments-vs-adamw-on-cpu-pretraining-aeb892926838-20260620T092941754538+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c2a7e9f9b68f

## What looked useful

Factored second moments preserved early validation loss on synthetic recurrence and Tiny Shakespeare byte-level proxy runs while roughly halving optimizer-state memory; throughput was similar on synthetic data but slower for Adafactor in the real-text NumPy run.

## Boundaries and scale limits

Not transformer-scale, not GPT-2-small-class, not long-horizon pretraining, not optimized framework kernels, and not a publication-grade corpus/tokenizer setup.

## Claim scope

On two bounded CPU next-token proxies using a small NumPy MLP language model, tuned factored Adafactor matched tuned AdamW validation loss within 0.001 while using about 49% less optimizer state.

## Why it stopped

Proxy-scale evidence supports the memory/loss mechanism but is not direct full validation of CPU transformer pretraining.

## Recommended next action

Stop this run as no-paper useful signal; next run should use a bounded mini-transformer real-corpus benchmark with matched AdamW/Adafactor tuning, RSS telemetry, and longer training horizon.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mini-transformer CPU Adafactor vs AdamW real-corpus confirmation
- Success threshold: Adafactor final validation loss within 1% of best tuned AdamW with at least 40% lower optimizer-state memory and no more than 20% throughput regression.
- Stop condition: Stop if Adafactor is more than 3% worse in validation loss after matched tuning or if throughput regression exceeds 50% without a memory-pressure benefit.

## Evidence references

- Artifact root: `<local-path>/projects/adafactor-factored-second-moments-vs-adamw-on-cpu-pretraining-aeb892926838`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
