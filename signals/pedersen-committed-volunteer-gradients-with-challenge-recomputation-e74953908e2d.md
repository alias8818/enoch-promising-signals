# Pedersen-committed volunteer gradients with challenge recomputation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pedersen-committed-volunteer-gradients-with-challenge-recomputation-e74953908e2d`
Run ID: `pedersen-committed-volunteer-gradients-with-challenge-recomputation-e74953908e2d-20260630T144854133653+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c910545da46

## What looked useful

Challenge recomputation exactly tracks challenge coverage: dense corruptions were always detected, 5% sparse corruptions reached 100% detection at k=128, 1% sparse corruptions reached 75% at k=128, and 0.1% sparse corruptions reached only 12.5% at k=128. Naive per-coordinate commitments cost about 37-41x a full toy gradient pass.

## Boundaries and scale limits

No production elliptic-curve/vector commitment implementation, no neural-network training loop, no distributed workers, no networked aggregation, and no adaptive challenge-manipulation model. Pure-Python modular commitments are timing proxies only.

## Claim scope

Toy logistic-regression gradients with 2048 coordinates and deterministic transcript-derived challenge recomputation. The evidence supports the protocol as a sampling audit for dense or moderately broad coordinate corruptions, not as a complete volunteer-gradient correctness guarantee.

## Why it stopped

Proxy experiment supports the sampling mechanism but early-falsifies the naive cheap-audit claim for sparse adversaries and per-coordinate Pedersen commitments; it is not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful evidence; deepen only with a bounded vector/Merkle commitment experiment that targets at least 95% detection for 1% coordinate corruptions while keeping verifier cost below a full gradient on a small MLP.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Vector-commitment challenge audit for sparse volunteer-gradient tampering
- Success threshold: At least 95% empirical detection for 1% coordinate corruptions with zero honest false rejects and median verifier cost below one full gradient recomputation.
- Stop condition: Stop if optimized commitments still make committer or verifier cost exceed full-gradient recomputation for k needed to reach 95% detection on 1% corruptions.

## Evidence references

- Artifact root: `<local-path>/projects/pedersen-committed-volunteer-gradients-with-challenge-recomputation-e74953908e2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
