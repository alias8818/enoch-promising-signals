# Mixed-Precision Gradient Scaling for 6GB VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixed-precision-gradient-scaling-for-6gb-vram-training-a6bd56453b0b`
Run ID: `mixed-precision-gradient-scaling-for-6gb-vram-training-a6bd56453b0b-20260605T193845316812+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a7f94acbc26

## What looked useful

Mixed precision provided the memory headroom needed to run the threshold shape under the 6GiB cap. Gradient scaling did not provide additional memory savings but reduced normal-loss fp16 zero gradients and rescued a tiny-loss fp16 underflow stress test from all-zero gradients.

## Boundaries and scale limits

Synthetic data only; 5 training steps; allocator-cap proxy rather than physical 6GB discrete VRAM; not exact GPT-2; no real-corpus convergence, multi-seed robustness, optimizer/offload comparison, or long-run stability evidence.

## Claim scope

On NVIDIA GB10 with a 6GiB PyTorch CUDA allocator cap, a 154M-parameter synthetic causal LM at batch 9 and sequence length 768 OOMed in fp32 but completed 5 finite AMP fp16/bf16 steps; GradScaler helped fp16 gradient underflow behavior but did not materially reduce peak memory.

## Why it stopped

Proxy/early bounded validation only: the experiment used synthetic data and an allocator cap, so it supports a mechanism distinction but not a full 6GB VRAM training claim.

## Recommended next action

Stop this worker run as no-paper useful signal; the next bounded action is a real-data GPT-2-small-class confirmation under an actual or stricter 6GB memory limit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data GPT-2-small-class AMP and GradScaler confirmation under a 6GB memory limit
- Success threshold: AMP fp16 or bf16 completes a threshold configuration where fp32 OOMs, with finite losses and no worse than 5% validation-loss degradation versus the best fitting baseline over the bounded run; GradScaler must reduce fp16 gradient underflow or skipped/unstable steps versus unscaled fp16.
- Stop condition: Stop if fp32 fits all tested real-data threshold shapes, AMP does not expand the feasible memory envelope, or GradScaler provides no measurable fp16 stability benefit across repeated runs.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-gradient-scaling-for-6gb-vram-training-a6bd56453b0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
