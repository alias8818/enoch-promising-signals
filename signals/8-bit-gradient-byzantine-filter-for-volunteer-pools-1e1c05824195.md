# 8-bit Gradient Byzantine Filter for Volunteer Pools

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-gradient-byzantine-filter-for-volunteer-pools-1e1c05824195`
Run ID: `8-bit-gradient-byzantine-filter-for-volunteer-pools-1e1c05824195-20260529T034742064223+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f91fc069d69e

## What looked useful

8-bit gradient compression was not the limiting factor in the tested outlier filter: float-vs-int8 filter deltas were below 0.000013 mean cosine and 0.00013 L2 error. The limiting factor was the filter rule itself, which accepted nearly all adaptive-bias Byzantine updates at 20-40% Byzantine participation.

## Boundaries and scale limits

Synthetic gradients only; no real volunteer non-IID clients, no multi-round training, no secure aggregation protocol, no large-model gradients, and no fully adaptive adversary with server-feedback optimization.

## Claim scope

In one-round synthetic gradient aggregation with 64 workers, 512-dimensional gradients, and up to 40% Byzantine workers, per-worker signed int8 quantization caused negligible degradation for a median-centered cosine/norm outlier filter; the filter rejected obvious direction, norm, and sparse sign-flip attacks but not coordinated plausible-bias attacks.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports quantization compatibility for obvious outlier filtering, but the same evidence falsifies a broad Byzantine-filter claim under plausible adaptive bias.

## Recommended next action

Run a bounded multi-round federated training simulation with non-IID clients and adaptive-bias adversaries before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-round non-IID int8 Byzantine filtering under adaptive bias
- Success threshold: At 20-40% Byzantine clients, the int8-compatible filter reduces attack-induced validation loss degradation by at least 25% versus the best robust baseline while keeping clean-run validation within 1% relative of the no-attack baseline.
- Stop condition: Stop if adaptive biased updates are accepted at over 80% rate without validation improvement over trimmed mean, or if int8 quantization causes more than 1% relative clean-run validation degradation.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-gradient-byzantine-filter-for-volunteer-pools-1e1c05824195`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
