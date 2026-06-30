# Memory-aware micro-batch scheduler under VRAM cap

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-aware-micro-batch-scheduler-under-vram-cap-dbb1bcd0ee11`
Run ID: `memory-aware-micro-batch-scheduler-under-vram-cap-dbb1bcd0ee11-20260614T013018971263+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a89d19a40a

## What looked useful

Memory-aware packing reduced mean micro-batches from 460.7 to 72.3/71.2 and improved proxy tokens/s by 1.71x on the main grid; under tighter stress caps it avoided all over-cap batches while a naive fixed-width baseline averaged 117.9 over-cap batches, and improved proxy tokens/s by 4.30x/4.39x versus the safe worst-case fixed baseline.

## Boundaries and scale limits

Proxy-only CPU simulation; no real model training, no measured CUDA allocator behavior, no real VRAM/UMA pressure, no convergence or quality measurement, and no large-model or multi-GPU validation.

## Claim scope

On deterministic synthetic sequence-length traces with an explicit per-sample memory estimator, greedy ordered and first-fit-decreasing memory-aware micro-batch schedulers stayed under configured memory caps and improved proxy tokens/s versus a conservative worst-case fixed-width baseline.

## Why it stopped

Closed as no-paper useful signal because the result supports the scheduling mechanism only in a synthetic/proxy simulator, not through direct GPU training evidence.

## Recommended next action

Run a bounded real PyTorch transformer training follow-up with measured peak memory, OOM rate, tokens/s, and loss parity for fixed, greedy ordered, and first-fit-decreasing memory-aware schedulers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured PyTorch micro-batch scheduling under real memory pressure
- Success threshold: Memory-aware scheduler has zero OOMs, at least 20% measured tokens/s improvement versus safe fixed-width, and no more than 2% worse loss after the fixed training budget.
- Stop condition: Stop if memory-aware scheduling cannot maintain identical sample coverage per optimizer step, causes repeated OOMs under the cap, or fails to improve measured tokens/s by 10% in the tight-cap condition.

## Evidence references

- Artifact root: `<local-path>/projects/memory-aware-micro-batch-scheduler-under-vram-cap-dbb1bcd0ee11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
