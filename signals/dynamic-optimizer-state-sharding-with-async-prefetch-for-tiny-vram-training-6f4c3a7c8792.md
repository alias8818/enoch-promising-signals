# Dynamic Optimizer State Sharding with Async Prefetch for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-optimizer-state-sharding-with-async-prefetch-for-tiny-vram-training-6f4c3a7c8792`
Run ID: `dynamic-optimizer-state-sharding-with-async-prefetch-for-tiny-vram-training-6f4c3a7c8792-20260527T143553266767+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/14b3509bc498

## What looked useful

The mechanism is memory-effective but bandwidth-limited: 54 MB transformer-block Adam-state shards take about 0.96 ms to prefetch and 0.96 ms to write back, comparable to the measured 0.94 ms transformer-block forward/backward time, so memory-fitting configurations still show 59.9-81.3% exposed stall rather than the <=10% target.

## Boundaries and scale limits

No end-to-end training loop, no large-model run, no multi-node validation, and no hard allocator-enforced device-memory cap beyond simulated optimizer-state residency. Results are bounded to local GB10 measurements and deterministic scheduling simulation.

## Claim scope

On GB10 with measured pinned CPU-CUDA copy bandwidth and GPT-2-small-class bf16 MLP/transformer-block proxies, dynamic Adam-state sharding can reduce peak optimizer-state residency by 75-83% under 216 MB peak-state configurations, but async prefetch/writeback does not keep exposed stall below 10% of compute for 256-512 MB optimizer-state caps.

## Why it stopped

Proxy/simulator early falsification: dynamic sharding alone reduces peak optimizer-state memory but misses the practical async-prefetch stall threshold by a large margin under the tested tiny-VRAM caps.

## Recommended next action

Stop this line as a no-paper useful signal; the bounded next test should combine sharding with optimizer-state byte reduction rather than relying on prefetch scheduling alone.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Compressed Optimizer-State Sharding with Async Prefetch
- Success threshold: Under a 256 MB optimizer-state cap, achieve at least 4x lower transferred state bytes than fp32 Adam-state sharding and <=10% step-time overhead versus the standard optimizer baseline on the same proxy model.
- Stop condition: Stop if compression/decompression plus transfer still exceeds 20% exposed stall on the transformer-block proxy or if convergence diverges from the baseline in a short controlled training run.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-optimizer-state-sharding-with-async-prefetch-for-tiny-vram-training-6f4c3a7c8792`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
