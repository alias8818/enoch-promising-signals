# Trace-calibrated HMAC shard lottery under adaptive Sybil admission

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-calibrated-hmac-shard-lottery-under-adaptive-sybil-a-802940629e`
Run ID: `trace-calibrated-hmac-shard-lottery-under-adaptive-sybil-a-802940629e-20260621T073342216752+0000`

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

- Parent run decision: HMAC-committed data shard lottery for volunteer pretraining: enoch://control-plane/projects/hmac-committed-data-shard-lottery-for-volunteer-pretraining-7c5ff8adfee7/runs/hmac-committed-data-shard-lottery-for-volunteer-pretraining-7c5ff8adfee7-20260621T064831506515+0000
- Parent run decision: HMAC shard lottery with data-quality and Sybil admission constraints: enoch://control-plane/projects/hmac-shard-lottery-with-data-quality-and-sybil-admission-c-ee950a282f/runs/hmac-shard-lottery-with-data-quality-and-sybil-admission-c-ee950a282f-20260621T071412849189+0000

## What looked useful

Trace-calibrated HMAC had zero target-overload and attack-success windows across 960 windows, versus 100% for open public-hash grinding and 0.3125% for keyed global lottery. It avoided the 20.6% mean honest rejection of equal caps, but did not dominate keyed global lottery on mean target adversary share.

## Boundaries and scale limits

Synthetic trace only; honest demand is reserved before Sybil headroom admission; no production trace, credential-cost model, mixed-arrival replay, multi-operator deployment, or datacenter-scale validation.

## Claim scope

In a deterministic synthetic trace-shaped admission model with 64 shards, 5 fixed seeds, 192 windows per seed, and Sybil submissions at 75% of honest load, trace-calibrated HMAC admission headroom prevented target overload and kept target adversary share below 0.33 while avoiding honest rejection.

## Why it stopped

Tier 2 local validation produced a useful bounded signal but mixed mechanism superiority; this is not paper-positive evidence.

## Recommended next action

Run a bounded deepen follow-up using mixed honest/Sybil arrival replay and credential-cost sensitivity to test whether the zero-overload result survives without reserving honest trace demand first.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mixed-arrival credential-cost replay for trace-calibrated HMAC shard lottery
- Success threshold: Across at least 5 fixed seeds and 960 total windows, trace-calibrated HMAC has target overload below 1%, honest rejection below 2%, and p95 target adversary share below 0.25 while outperforming keyed global lottery on target overload.
- Stop condition: Stop as negative if honest rejection exceeds 5% or target overload exceeds keyed global lottery by more than 1 percentage point in the mixed-arrival setting.

## Evidence references

- Artifact root: `<local-path>/projects/trace-calibrated-hmac-shard-lottery-under-adaptive-sybil-a-802940629e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
