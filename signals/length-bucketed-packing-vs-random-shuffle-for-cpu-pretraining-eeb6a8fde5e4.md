# Length-Bucketed Packing vs Random Shuffle for CPU Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `length-bucketed-packing-vs-random-shuffle-for-cpu-pretraining-eeb6a8fde5e4`
Run ID: `length-bucketed-packing-vs-random-shuffle-for-cpu-pretraining-eeb6a8fde5e4-20260619T114936804698+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/86b6ef8f5ec2

## What looked useful

Across three seeds, packed scheduling raised slot utilization from 0.3767 to 0.8019 on average and improved attention-proxy valid-token throughput by 2.15x mean, while the final validation-loss delta was only 0.000083 packed minus random.

## Boundaries and scale limits

Synthetic corpus, NumPy attention-shaped proxy, simple bigram learner, one CPU process, one BLAS thread, no full transformer, no real corpus, and no long pretraining run.

## Claim scope

On synthetic variable-length token documents, bounded-window length bucketing plus greedy packing improved CPU attention-shaped valid-token throughput versus random shuffled padded batches without a meaningful bigram validation-loss regression.

## Why it stopped

Stopped as no-paper useful signal because this is synthetic/proxy evidence, not direct full pretraining validation.

## Recommended next action

Run a bounded direct small-transformer CPU pretraining follow-up on a real tokenized corpus with fixed consumed-token budgets, framework-level throughput, perplexity curves, and packing-mask correctness checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-transformer CPU pretraining test of length-bucketed packing
- Success threshold: At least 1.3x wall-clock valid-token throughput improvement with validation perplexity no worse than 1% relative at the matched consumed-token checkpoint.
- Stop condition: Stop if throughput gain is below 1.1x, if validation perplexity worsens by more than 3% at matched consumed tokens, or if packing-mask overhead eliminates the proxy efficiency gain.

## Evidence references

- Artifact root: `<local-path>/projects/length-bucketed-packing-vs-random-shuffle-for-cpu-pretraining-eeb6a8fde5e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
