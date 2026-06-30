# Loss-ranked curriculum vs uniform sampling for 124M GPT-2 pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `loss-ranked-curriculum-vs-uniform-sampling-for-124m-gpt-2-pretraining-a680e15d5e38`
Run ID: `loss-ranked-curriculum-vs-uniform-sampling-for-124m-gpt-2-pretraining-a680e15d5e38-20260621T035013493687+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/46f60061a86f

## What looked useful

Loss-ranked sampling mechanically oversampled higher-loss blocks (mean sampled rank percentile 0.6655 vs 0.5113 for uniform) but produced worse validation loss in 3/3 seeds. Mean loss_ranked - uniform validation loss was +0.1159 and mean relative perplexity was 1.1255.

## Boundaries and scale limits

This is not a full GPT-2 pretraining validation. It used WikiText-2, 128-token blocks, 768 ranked blocks, 192 validation blocks, and short post-warmup runs. It does not cover larger corpora, longer schedules, downstream tasks, alternative curriculum shapes, or full token budgets.

## Claim scope

Short-horizon 124M GPT-2-small-class WikiText-2 pretraining probe with shared warmup weights, 3 seeds, 48 optimizer steps per arm, batch size 4, sequence length 128: high-loss-biased sampling annealed toward uniform did not improve held-out validation loss over uniform sampling.

## Why it stopped

Bounded direct 124M GPT-2-small-class evidence showed loss-ranked sampling was worse than uniform on held-out validation loss across all three tested seeds, so the hypothesis is unsupported at this evidence tier.

## Recommended next action

Stop this run as a proxy/short-horizon early falsification of naive high-loss-ranked curriculum sampling; do not write a paper from these results.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/loss-ranked-curriculum-vs-uniform-sampling-for-124m-gpt-2-pretraining-a680e15d5e38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
