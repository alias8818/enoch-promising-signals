# Direct small-transformer CPU pretraining test of length-bucketed packing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-small-transformer-cpu-pretraining-test-of-length-bu-51f7c0a43c`
Run ID: `direct-small-transformer-cpu-pretraining-test-of-length-bu-51f7c0a43c-20260619T120950074176+0000`

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

- Parent run decision: Length-Bucketed Packing vs Random Shuffle for CPU Pretraining: enoch://control-plane/projects/length-bucketed-packing-vs-random-shuffle-for-cpu-pretraining-eeb6a8fde5e4/runs/length-bucketed-packing-vs-random-shuffle-for-cpu-pretraining-eeb6a8fde5e4-20260619T114936804698+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/86b6ef8f5ec2

## What looked useful

Across seeds 7, 11, and 13, bucketed packing met the predeclared threshold in all runs: mean packing-efficiency relative gain 2.3856x, minimum gain 2.3326x, mean useful tokens/sec relative gain 1.5115x, minimum gain 1.3160x, and mean tail loss difference bucketed-minus-random -0.0383.

## Boundaries and scale limits

Synthetic corpus only; 1024 documents per run; 80 optimizer steps per policy; tiny 48-dimensional single-layer Transformer; CPU-local throughput; not a real tokenizer, GPT-2-small-class model, GPU kernel study, or publication-scale pretraining validation.

## Claim scope

In a bounded CPU PyTorch tiny causal-Transformer pretraining test on a deterministic synthetic variable-length corpus, 8-token length-bucketed batch construction improved non-padding efficiency and useful token throughput versus random batching without worsening short-run tail loss.

## Why it stopped

Tier 1 direct small CPU test completed with useful mechanism support, but evidence is synthetic and too small for a paper-ready claim.

## Recommended next action

Run a bounded deepen follow-up on a real tokenized corpus slice with a GPT-2-small-class or parameter-matched small baseline, fixed token and wall-clock budgets, and at least three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus small-transformer confirmation of length-bucketed packing
- Success threshold: At least 20% higher useful tokens/sec or at least 20% lower padding waste for bucketed packing, with validation loss no worse than random batching by more than 0.05 in at least two of three seeds.
- Stop condition: Stop if bucketed packing fails to improve useful tokens/sec by 10% or worsens validation loss by more than 0.05 in two seeds under fixed-budget controls.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-transformer-cpu-pretraining-test-of-length-bu-51f7c0a43c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
