# Real-corpus small-transformer confirmation of length-bucketed packing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-small-transformer-confirmation-of-length-bucke-0338e23eac`
Run ID: `real-corpus-small-transformer-confirmation-of-length-bucke-0338e23eac-20260619T124201838433+0000`

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

- Parent run decision: Direct small-transformer CPU pretraining test of length-bucketed packing: enoch://control-plane/projects/direct-small-transformer-cpu-pretraining-test-of-length-bu-51f7c0a43c/runs/direct-small-transformer-cpu-pretraining-test-of-length-bu-51f7c0a43c-20260619T120950074176+0000
- Parent run decision: Length-Bucketed Packing vs Random Shuffle for CPU Pretraining: enoch://control-plane/projects/length-bucketed-packing-vs-random-shuffle-for-cpu-pretraining-eeb6a8fde5e4/runs/length-bucketed-packing-vs-random-shuffle-for-cpu-pretraining-eeb6a8fde5e4-20260619T114936804698+0000

## What looked useful

Length-bucketed packing reduced mean training pad fraction from 0.5181 for padding and 0.2583 for random packing to 0.0160, improved useful tokens/s by 67.9% versus padding and 4.47% versus random packing, and had slightly lower mean final eval loss than both controls across seeds 101, 202, and 303.

## Boundaries and scale limits

CPU-only run; 2 MB corpus; byte-level tokenizer; 141k-parameter model; 128-token context; 80-step training horizon; no GPT-2-small-class model, no subword tokenizer, no GPU kernel profiling, no long convergence test, and no large-corpus validation.

## Claim scope

On a 2 MB local real-text documentation corpus with a byte-level 141k-parameter causal Transformer, 128-token context, 3 fixed seeds, and 80 train steps per condition, length-aware first-fit packing sharply reduced padding and modestly improved useful-token throughput over padding and random-packing controls without validation-loss degradation.

## Why it stopped

Medium local confirmation supports the mechanism, but the evidence is too small, short, CPU-only, and tokenizer-limited for a publication-grade claim.

## Recommended next action

Stop this run as a no-paper useful signal; next run should reproduce the comparison with a real subword tokenizer and GPT-2-small-class or near-GPT-2-small model on a GPU host under equal-token and equal-wall-clock budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU GPT-2-small-class reproduction of length-aware packing
- Success threshold: Across at least 3 seeds, length-aware packing should improve useful-token throughput by at least 10% over random packing or reduce equal-wall-clock validation loss by at least 1% without any seed showing a material validation-loss regression.
- Stop condition: Stop as no-paper if length-aware packing is within 3% of random packing on useful-token throughput and equal-wall-clock validation loss, or if gains disappear once boundary masking and real tokenization are enforced.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-small-transformer-confirmation-of-length-bucke-0338e23eac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
