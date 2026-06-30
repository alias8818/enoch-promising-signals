# FP8 activation compression for GPT-2-small training memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fp8-activation-compression-for-gpt-2-small-training-memory-2146e5415476`
Run ID: `fp8-activation-compression-for-gpt-2-small-training-memory-2146e5415476-20260602T165513824293+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3398ca971db3

## What looked useful

Hook-level FP8 packing achieved about 2.0x saved-tensor byte compression on the medium run, but CUDA peak allocated memory worsened from 2.028 GiB to 2.094 GiB (-3.22% saving) and throughput fell to 0.515x baseline; gradient cosine remained 0.996 with 8.7% relative gradient L2 drift.

## Boundaries and scale limits

Test used synthetic token IDs, batch 2, sequence 256, 3 measured optimizer steps per mode, and a PyTorch hook implementation rather than custom fused activation storage. It does not test real-corpus convergence, larger sequence/batch regimes, or custom kernel implementations.

## Claim scope

On a bf16 GPT-2-small-class synthetic training benchmark on NVIDIA GB10, a PyTorch saved_tensors_hooks FP8 activation-compression path reduced hook-accounted saved tensor bytes but did not reduce end-to-end CUDA peak allocation and substantially reduced throughput.

## Why it stopped

Direct local GPT-2-small-class proxy falsification for practical memory saving: FP8 saved-tensor hooks compressed recorded tensors but increased peak CUDA allocation and slowed training, so this is not a viable paper result as implemented.

## Recommended next action

Stop this implementation path as a no-paper useful signal; the next bounded test should replace generic saved_tensors_hooks with a selective activation-only packer/checkpointed block that avoids hook metadata and extra allocation overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Selective FP8 activation-only packing inside GPT-2 blocks
- Success threshold: At least 15% end-to-end CUDA peak allocated memory reduction on GPT-2-small-class batch/sequence settings with throughput >=75% of baseline and gradient cosine >=0.995.
- Stop condition: Stop if selective packing still fails to reduce CUDA peak allocation by 5% or if throughput remains below 60% of baseline after excluding non-activation tensors.

## Evidence references

- Artifact root: `<local-path>/projects/fp8-activation-compression-for-gpt-2-small-training-memory-2146e5415476`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
