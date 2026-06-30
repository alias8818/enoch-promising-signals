# Real-corpus CPU training test of shuffled length buckets

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-cpu-training-test-of-shuffled-length-buckets-69a1461942`
Run ID: `real-corpus-cpu-training-test-of-shuffled-length-buckets-69a1461942-20260602T163933727517+0000`

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

- Parent run decision: Length Stratification Cuts Padding Waste in CPU Pretraining: enoch://control-plane/projects/length-stratification-cuts-padding-waste-in-cpu-pretraining-f8a7a51138a4/runs/length-stratification-cuts-padding-waste-in-cpu-pretraining-f8a7a51138a4-20260601T053711338734+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aa233e0bb664

## What looked useful

Across 3 seeds, bucketed batching reduced pad fraction from 0.4118 to 0.0843, improved real tokens/s from 13960.5 to 20572.9 (+47.4%), and changed validation loss by only +0.26% relative.

## Boundaries and scale limits

Tiny Shakespeare corpus, byte-level tokenization, small GRU model, 3 seeds, one full pass over 2048 variable-length windows per seed and strategy; not validated on GPT-2-small-class Transformers, larger corpora, long training, distributed training, or production dataloaders.

## Claim scope

In a Tier 1 CPU-only direct test on a real public text corpus, shuffled length-bucket batching for a small byte-level GRU language model reduced padding and improved real-token training throughput versus ordinary random batching over the same examples, without material short-run validation-loss degradation.

## Why it stopped

Tier 1 direct evidence supports the mechanism, but this remains a small real-corpus CPU test and is not sufficient for paper readiness.

## Recommended next action

Run a bounded medium confirmation on WikiText-2 or OpenWebText shards with a small Transformer or GPT-2-small-class model, matched token/update budgets, and the same random-vs-bucketed scheduler controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Transformer confirmation of shuffled length buckets on a larger real corpus
- Success threshold: Bucketed batching reduces padding fraction by at least 20% relative, improves real tokens/s by at least 10%, and keeps final validation loss no worse than 2% relative to random batching.
- Stop condition: Stop if the larger Transformer run shows less than 10% throughput improvement, validation loss worsens by more than 2%, or the effect cannot be reproduced across matched seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-cpu-training-test-of-shuffled-length-buckets-69a1461942`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
