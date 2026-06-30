# Muon-orthogonalized optimizer for GPT-2-small on single gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `muon-orthogonalized-optimizer-for-gpt-2-small-on-single-gb10-d465d6158ee6`
Run ID: `muon-orthogonalized-optimizer-for-gpt-2-small-on-single-gb10-d465d6158ee6-20260620T012631661523+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/279864772475

## What looked useful

Muon lr 0.005-0.02 produced final validation loss about 7.17 after 100 steps versus AdamW 7.35, with about 9.66k-9.68k tokens/s versus AdamW 11.13k tokens/s. A second 60-step seed also favored Muon on validation loss, 7.33 versus 7.54, with similar throughput penalty.

## Boundaries and scale limits

Only 100 optimizer steps at batch size 16 and sequence length 128 were run for the main comparison, plus one 60-step confirmation seed. The model was randomly initialized and trained on WikiText-2, not a full GPT-2 corpus/token budget. AdamW and Muon were not exhaustively tuned.

## Claim scope

On a single GB10, a short GPT-2-small architecture WikiText-2 probe found that Muon on hidden 2D matrices plus AdamW fallback reached lower validation loss per optimizer step than AdamW alone, while incurring measurable Newton-Schulz throughput overhead.

## Why it stopped

No-paper closure: the result is a bounded early local signal, not a full GPT-2-small validation or publication-grade optimizer comparison.

## Recommended next action

Run a 1k-2k step deepen experiment on the same GB10 with tuned AdamW and Muon schedules, fixed eval slices, and equal wall-clock checkpoints before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer equal-wall-clock GPT-2-small Muon vs tuned AdamW probe on GB10
- Success threshold: Muon must beat the best tuned AdamW validation loss by at least 0.05 nats at equal wall-clock and equal or lower instability across seeds while keeping throughput penalty below 25%.
- Stop condition: Stop if tuned AdamW matches or beats Muon at equal wall-clock after 1k steps, if Muon diverges under the tested schedules, or if projected runtime exceeds the local GB10 budget without improving the evidence tier.

## Evidence references

- Artifact root: `<local-path>/projects/muon-orthogonalized-optimizer-for-gpt-2-small-on-single-gb10-d465d6158ee6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
