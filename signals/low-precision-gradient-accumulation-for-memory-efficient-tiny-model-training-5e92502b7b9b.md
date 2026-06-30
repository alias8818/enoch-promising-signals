# Low-precision gradient accumulation for memory-efficient tiny model training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `low-precision-gradient-accumulation-for-memory-efficient-tiny-model-training-5e92502b7b9b`
Run ID: `low-precision-gradient-accumulation-for-memory-efficient-tiny-model-training-5e92502b7b9b-20260607T174002419198+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa1218c962cc

## What looked useful

Low-precision accumulation appears viable in the bounded tiny-model proxy: fp16 best validation accuracy was 0.6076 vs fp32 0.6108 with 0.5x accumulator memory, and int8 was 0.6120 with 0.25x accumulator memory. Reconstruction diagnostics at 8 microbatches showed fp16 relative L2 error 0.000373 and int8 0.01636 against exact fp32 accumulation.

## Boundaries and scale limits

Synthetic MLP only; no real language model, attention stack, optimizer-state interaction, GPU kernel, memory allocator attribution, or long-run convergence validation was tested.

## Claim scope

On a self-contained NumPy synthetic teacher/student classification task with a 569k-parameter two-layer MLP, fp16 and per-tensor symmetric int8 gradient accumulation buffers reduced accumulator storage by 2x and 4x respectively while matching fp32 best validation accuracy across three seeds.

## Why it stopped

The run produced bounded synthetic evidence supporting the mechanism, but not direct paper-grade evidence for real tiny model training.

## Recommended next action

Stop this run as no-paper useful signal; next concrete test is a bounded real tiny-LM training comparison with memory attribution and validation perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-LM validation of low-precision gradient accumulation
- Success threshold: fp16 and int8 accumulator variants achieve validation perplexity within 1% of fp32 while showing measured accumulator memory reductions of at least 1.9x and 3.5x respectively.
- Stop condition: Stop if either low-precision variant exceeds 3% validation perplexity degradation in two independent seeds at tuned stable learning rates, or if memory attribution shows accumulator savings are negligible relative to total peak memory for the target tiny-LM regime.

## Evidence references

- Artifact root: `<local-path>/projects/low-precision-gradient-accumulation-for-memory-efficient-tiny-model-training-5e92502b7b9b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
