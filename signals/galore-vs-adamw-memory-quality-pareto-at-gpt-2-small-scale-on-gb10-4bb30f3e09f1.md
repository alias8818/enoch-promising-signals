# GaLore vs AdamW: memory-quality Pareto at GPT-2-small scale on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `galore-vs-adamw-memory-quality-pareto-at-gpt-2-small-scale-on-gb10-4bb30f3e09f1`
Run ID: `galore-vs-adamw-memory-quality-pareto-at-gpt-2-small-scale-on-gb10-4bb30f3e09f1-20260630T105903212319+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/091de4528619

## What looked useful

GaLore reduced optimizer-state bytes by 57.2% and CUDA peak allocation by 19.3% versus AdamW, with mean validation loss 7.5043 vs 7.9095 after 100 steps, but throughput was only 30.5% of AdamW.

## Boundaries and scale limits

Short run only: 100 steps, two seeds, Wikitext-2 subset, no hyperparameter sweep, no long-run convergence, no wall-clock-normalized quality target, and no larger batch/sequence memory-pressure test.

## Claim scope

On a single GB10, for GPT-2-small architecture trained from scratch on Wikitext-2 for 100 steps at batch size 2 and sequence length 128 across two seeds, GaLoreAdamW rank 128 reduced optimizer-state tensor bytes and PyTorch CUDA peak allocation versus AdamW while preserving or improving short-run validation loss.

## Why it stopped

No-paper useful signal: the result is direct for a short GPT-2-small Wikitext-2 probe, but it is not a full validation of memory-quality Pareto behavior over long training or tuned baselines.

## Recommended next action

Stop this worker run; if continuing, run a bounded deepen study with matched-token and matched-wall-clock comparisons plus AdamW learning-rate and GaLore rank/scale sweeps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-token and matched-wall-clock GaLore vs AdamW sweep at GPT-2-small scale
- Success threshold: GaLore must reduce CUDA peak allocation by at least 15% and optimizer-state bytes by at least 40% while matching tuned AdamW validation loss within 0.1 nats at matched tokens, and its wall-clock quality penalty must be explicitly quantified.
- Stop condition: Stop if tuned AdamW matches or beats GaLore validation loss at the same memory-feasible batch/sequence setting and GaLore remains below 50% of AdamW throughput without enabling a larger feasible configuration.

## Evidence references

- Artifact root: `<local-path>/projects/galore-vs-adamw-memory-quality-pareto-at-gpt-2-small-scale-on-gb10-4bb30f3e09f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
