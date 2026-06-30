# Gradient Accumulation Bucket Batching for CPU-Constrained Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-accumulation-bucket-batching-for-cpu-constrained-training-2639791b6654`
Run ID: `gradient-accumulation-bucket-batching-for-cpu-constrained-training-2639791b6654-20260611T153930021055+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/cad2ec9c2531

## What looked useful

Bucketed accumulation consistently reduced padding overhead and wall time across smoke, medium, and bucket-size sweep runs, with negligible loss differences in the toy task.

## Boundaries and scale limits

The experiment used a small synthetic token classifier, not GPT-2-small or a production transformer; it did not use a real corpus, multi-epoch convergence, framework dataloaders, attention kernels, or validation perplexity.

## Claim scope

In a bounded CPU-only NumPy proxy with variable-length synthetic sequences, length-bucketed gradient-accumulation microbatches reduced padded dense token work by about 56-59% and improved true-token throughput versus random accumulation at the same effective batch size and optimizer-step cadence.

## Why it stopped

No-paper closure: local evidence is a useful bounded CPU proxy signal, but not direct/full training evidence.

## Recommended next action

Run a bounded PyTorch transformer or GPT-2-small-class CPU experiment on a real tokenized corpus with matched optimizer steps, validation perplexity, dataloader overhead, and wall-clock throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch Transformer Validation of Bucketed Gradient Accumulation
- Success threshold: At least 25% higher true-token throughput or at least 20% lower wall-clock time at matched validation perplexity within 1% relative degradation.
- Stop condition: Stop if bucketed accumulation improves padded-token accounting but fails to improve end-to-end wall time by at least 10%, or if validation perplexity degrades by more than 1% at matched optimizer steps.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-accumulation-bucket-batching-for-cpu-constrained-training-2639791b6654`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
