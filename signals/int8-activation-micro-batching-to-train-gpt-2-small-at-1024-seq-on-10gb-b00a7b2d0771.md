# Int8 activation micro-batching to train GPT-2-small at 1024 seq on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-activation-micro-batching-to-train-gpt-2-small-at-1024-seq-on-10gb-b00a7b2d0771`
Run ID: `int8-activation-micro-batching-to-train-gpt-2-small-at-1024-seq-on-10gb-b00a7b2d0771-20260605T023014193145+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/33ebd991a77f

## What looked useful

Saved activation bytes fell to about 40% of original and one-step gradient cosine was 0.9994, but actual peak CUDA memory increased: two-step micro-batch 1 accumulation 4 used 2.192 GiB allocated/2.225 GiB reserved for baseline versus 2.309 GiB allocated/4.418 GiB reserved for int8. At micro-batch 8, baseline was 9.797 GiB allocated/10.820 GiB reserved while int8 was 9.958 GiB allocated/13.635 GiB reserved.

## Boundaries and scale limits

Synthetic tokens only; short one- and two-step runs; no real-data convergence; no fused/custom-autograd int8 kernel; memory judged by PyTorch CUDA allocation/reservation telemetry on a 124 GiB GB10 rather than an actual 10 GiB GPU.

## Claim scope

On a GB10 with PyTorch 2.12/CUDA 13, a naive PyTorch saved_tensors_hooks implementation of per-tensor int8 saved activations for GPT-2-small-shape BF16 training at sequence length 1024 compresses saved tensor payloads and preserves one-step gradient direction, but does not reduce peak CUDA allocated or reserved memory versus the BF16 baseline.

## Why it stopped

Proxy/local early falsification of the naive int8 saved-activation micro-batching path, not a full validation of all possible int8 activation training designs.

## Recommended next action

Stop this run as a bounded negative result; only pursue a follow-up if implementing fused/selective activation quantization that avoids packing temporaries and is measured against the same peak allocated/reserved memory thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused selective int8 activation packing for GPT-2-small memory peak reduction
- Success threshold: Int8 path must reduce both peak allocated and peak reserved CUDA memory by at least 15% versus BF16 baseline at the same micro-batch, keep gradient relative L2 error under 5%, and complete 100 real-data steps without NaN/Inf loss.
- Stop condition: Stop if packing temporaries or allocator behavior still make peak allocated or reserved memory equal to or higher than baseline, or if gradient relative L2 error exceeds 5%.

## Evidence references

- Artifact root: `<local-path>/projects/int8-activation-micro-batching-to-train-gpt-2-small-at-1024-seq-on-10gb-b00a7b2d0771`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
