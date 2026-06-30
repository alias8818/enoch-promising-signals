# Residual-Compensated 1-bit Gradients for Home Distributed Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-compensated-1-bit-gradients-for-home-distributed-training-f1824475b741`
Run ID: `residual-compensated-1-bit-gradients-for-home-distributed-training-f1824475b741-20260522T150955082830+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bd4403e6afb2

## What looked useful

Residual compensation appears to fix the practical convergence failure of naive 1-bit gradients in this bounded local proxy, including IID and non-IID worker shard controls, but the result is not paper-ready without direct distributed and larger-model evidence.

## Boundaries and scale limits

No real home network, multi-machine process group, WAN latency/bandwidth shaping, packet loss, straggler behavior, larger model, optimizer-state compression, or language-model workload was tested. This is mechanism evidence only, not direct validation of home distributed training.

## Claim scope

In a local PyTorch synchronous data-parallel proxy on a generated two-moons classification task, per-worker residual/error-feedback compensation made scaled-sign 1-bit gradient averaging converge within 0.18 percentage points of dense averaging while preserving about 31.9x simulated payload reduction; naive 1-bit lost 7.2 to 9.4 percentage points in calibrated controls.

## Why it stopped

Closed as no-paper useful-signal evidence because the current tests support the residual-compensation mechanism only in a local proxy, not in direct home distributed training.

## Recommended next action

Run a bounded real torch.distributed follow-up with 2 to 4 local processes, bandwidth/latency shaping, and a real small vision or language workload; require residual 1-bit to remain within 1 percentage point or comparable validation loss of dense while reporting wall-clock throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bandwidth-shaped local DDP validation of residual 1-bit gradients
- Success threshold: Residual 1-bit finishes within 1 percentage point accuracy or equivalent validation-loss tolerance of dense in both IID and non-IID conditions, beats naive 1-bit by at least 3 percentage points where naive degrades, and shows a net communication-volume reduction of at least 16x after metadata overhead.
- Stop condition: Stop if residual 1-bit misses dense by more than 2 percentage points or comparable validation-loss tolerance in two independent seeds, or if compression/decompression overhead removes the wall-clock benefit under shaped bandwidth.

## Evidence references

- Artifact root: `<local-path>/projects/residual-compensated-1-bit-gradients-for-home-distributed-training-f1824475b741`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
