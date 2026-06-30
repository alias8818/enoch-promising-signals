# PagedAdamW8bit real-training memory and convergence check

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pagedadamw8bit-real-training-memory-and-convergence-check-965b7cab81`
Run ID: `pagedadamw8bit-real-training-memory-and-convergence-check-965b7cab81-20260619T144901701313+0000`

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

- Parent run decision: bitsandbytes-8bit-AdamW-paged-state: enoch://control-plane/projects/bitsandbytes-8bit-adamw-paged-state-fb5d4d8a98ec/runs/bitsandbytes-8bit-adamw-paged-state-fb5d4d8a98ec-20260619T143043838444+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f8d67d49d54

## What looked useful

PagedAdamW8bit worked in real CUDA training and preserved early convergence versus AdamW. It cut optimizer-state bytes by about 74.5% in both direct runs; in the 151.3M-parameter state-heavy run it reduced CUDA peak allocated by 43.7%, CUDA reserved by 45.6%, and MemAvailable drop by 38.6%, with validation loss only 0.0019 nats worse.

## Boundaries and scale limits

Short small-model runs only: 25.4M parameters for 250 steps and 151.3M parameters for 100 steps, character-level data, one seed, no mixed precision, no checkpoint reload test, no Hugging Face Trainer/FSDP integration, no multi-GPU or long-horizon validation.

## Claim scope

In two bounded single-seed CUDA character-language-model training runs on Tiny Shakespeare, PagedAdamW8bit reduced apparent optimizer-state memory by about 75% and reduced CUDA/UMA memory in the larger state-heavy run while matching AdamW early validation loss within 0.1%.

## Why it stopped

Tier 1 controlled direct test completed with useful mechanism support, but evidence remains too small, short, and single-seed for publication readiness.

## Recommended next action

Run a bounded medium confirmation on a tokenized GPT-2-small-class model across at least 3 seeds, including checkpoint reload and mixed-precision/activation-checkpointing settings, before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class multi-seed PagedAdamW8bit memory and convergence confirmation
- Success threshold: PagedAdamW8bit shows at least 20% lower end-to-end CUDA/UMA memory on median across seeds while final validation loss remains within 5% relative or 0.05 nats absolute of AdamW and checkpoint resume succeeds.
- Stop condition: Stop as unsupported if PagedAdamW8bit fails to run/reload, loses the memory advantage below 10% median, or shows repeatable validation loss degradation above 5% relative and 0.05 nats absolute versus AdamW.

## Evidence references

- Artifact root: `<local-path>/projects/pagedadamw8bit-real-training-memory-and-convergence-check-965b7cab81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
