# HMAC shard lottery with data-quality and Sybil admission constraints

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hmac-shard-lottery-with-data-quality-and-sybil-admission-c-ee950a282f`
Run ID: `hmac-shard-lottery-with-data-quality-and-sybil-admission-c-ee950a282f-20260621T071412849189+0000`

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

- Parent run decision: HMAC-committed data shard lottery for volunteer pretraining: enoch://control-plane/projects/hmac-committed-data-shard-lottery-for-volunteer-pretraining-7c5ff8adfee7/runs/hmac-committed-data-shard-lottery-for-volunteer-pretraining-7c5ff8adfee7-20260621T064831506515+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f1a51ae95934

## What looked useful

Naive HMAC admission filled 74.54% of slots with Sybil identities and had p95 max shard Sybil share of 1.0. Quality-only admission reduced mean Sybil share to 9.32%. Quality plus entity cap reduced mean Sybil share to 5.10% and target-attacker share to 0.48%, with mean load CV 0.2601.

## Boundaries and scale limits

Synthetic admission scores and synthetic identities only; no real identity proofing, production data-quality calibration, adaptive attacker economics, collusion model, or large deployment trace was tested.

## Claim scope

In a deterministic 64-trial controlled simulation with 16 shards, 200 honest single-identity entities, 20 Sybil entities with 20 identities each, one 200-identity target attacker, a 0.60 quality threshold, global capacity 240, and per-entity cap 1, HMAC shard assignment plus pre-lottery quality and entity-cap admission reduced Sybil amplification while preserving approximate shard-load balance.

## Why it stopped

Tier 1 controlled direct simulation supports the mechanism but is not publication-grade validation because admission quality and identity uniqueness were simulated.

## Recommended next action

Run a bounded deepen follow-up on a realistic or high-fidelity admission trace with calibrated quality scores and adaptive high-quality Sybil attempts; stop short of paper writing until that direct evidence exists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-calibrated HMAC shard lottery under adaptive Sybil admission
- Success threshold: Across at least 256 deterministic trials or trace windows, quality-plus-entity-cap admission must keep mean Sybil slot share below 0.10, p95 max-shard Sybil share below 0.35, target-attacker share below quality-only by at least 50%, and load CV below 0.30.
- Stop condition: Stop if adaptive high-quality Sybils exceed 0.20 mean slot share or if load CV exceeds 0.35 after applying the constraints, because that would falsify the bounded mechanism claim for trace-calibrated admission.

## Evidence references

- Artifact root: `<local-path>/projects/hmac-shard-lottery-with-data-quality-and-sybil-admission-c-ee950a282f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
