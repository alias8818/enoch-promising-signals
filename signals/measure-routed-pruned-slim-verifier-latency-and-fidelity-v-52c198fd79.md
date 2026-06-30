# Measure routed/pruned slim-verifier latency and fidelity versus early-exit proxy

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `measure-routed-pruned-slim-verifier-latency-and-fidelity-v-52c198fd79`
Run ID: `measure-routed-pruned-slim-verifier-latency-and-fidelity-v-52c198fd79-20260629T070939199055+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: VIA-SD slim-verifier tier for speculative decoding: enoch://control-plane/projects/viasd-slim-verifier-speculative-decoding-20260628/runs/viasd-slim-verifier-speculative-decoding-20260628-20260629T065258208026+0000
- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-206 frontier research issue: linear-ALI-206
- VIA-SD slim-verifier tier for speculative decoding: https://zju-xyc.github.io/VIA-SD-Project-Page/
- VIA-SD slim-verifier tier for speculative decoding: https://arxiv.org/abs/2606.12243v1

## What looked useful

Routed/pruned accuracy averaged 0.8518 versus 0.6879 for early-exit threshold 0.90, and router route accuracy averaged 0.9781. However routed/pruned median latency was about 2.3x to 2.5x slower than early-exit threshold 0.90 for batches 8 through 512, indicating that dynamic routing overhead can dominate small pruned-verifier compute.

## Boundaries and scale limits

Synthetic 96-feature classification task, 4 routes, small MLPs, 24k train/6k test per seed, 3 calibrated seeds, naive dynamic routing with boolean masking/scatter, no real LLM verifier, no fused kernels, no production serving concurrency.

## Claim scope

On a local synthetic route-structured verifier task with small MLP students on NVIDIA GB10, routed/pruned verification improves teacher-label accuracy versus an early-exit proxy but a naive dynamic PyTorch routed implementation is slower than early-exit inference across practical batch sizes.

## Why it stopped

No-paper useful signal: the synthetic local benchmark supports the fidelity mechanism but early-falsifies the naive latency claim; it is not full validation on real verifier workloads.

## Recommended next action

Run a bounded deepen follow-up with static/fused grouped routing or a transformer-block proxy where skipped compute is large enough to test whether routing overhead can be amortized.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure fused/static routed verifier latency on a heavier transformer-block proxy
- Success threshold: Routed/pruned verifier achieves at least 95% of dense-reference fidelity and is at least 15% faster than the best early-exit threshold with matched fidelity at batch sizes 32 and 128.
- Stop condition: Stop if fused/static routing remains slower than early-exit at matched fidelity for two independent seeds or if the fidelity advantage disappears under parameter-matched transformer-block controls.

## Evidence references

- Artifact root: `<local-path>/projects/measure-routed-pruned-slim-verifier-latency-and-fidelity-v-52c198fd79`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
