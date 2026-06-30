# Commit-reveal anti-sybil for volunteer gradients

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `commit-reveal-anti-sybil-for-volunteer-gradients-c95b709c7453`
Run ID: `commit-reveal-anti-sybil-for-volunteer-gradients-c95b709c7453-20260528T095504790403+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a77778913927

## What looked useful

Commit-reveal accepted 100% of precommitted sybil poison gradients. With 40 sybils out of 101 clients, mean aggregation flipped direction under both commit-reveal blind attack and no-commit adaptive attack; trimmed mean also flipped. Coordinate median stayed aligned, indicating protection came from robust aggregation rather than commit-reveal.

## Boundaries and scale limits

No real volunteer network, no full model training, no cryptographic network implementation, and no independent identity, stake, reputation, or rate-limit layer was modeled. The result supports only the protocol-level claim that commit-reveal alone does not reduce sybil weight or reject precommitted poison gradients.

## Claim scope

Synthetic 101-client, 64-dimensional volunteer-gradient aggregation simulation comparing precommitted blind sybil poisoning against adaptive no-commit poisoning under norm clipping, mean, coordinate-median, and trimmed-mean aggregation.

## Why it stopped

Early synthetic falsification of the standalone anti-sybil claim; this is not full training validation, but it directly tests the protocol distinction and shows valid precommitted poison is still accepted.

## Recommended next action

Stop treating commit-reveal as standalone anti-sybil; only revisit with an explicitly modeled identity-cost or robust-aggregation mechanism and a success threshold tied to effective sybil weight.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-reveal plus robust aggregation under bounded sybil weight
- Success threshold: Across at least three random seeds, the paired mechanism maintains positive validation-loss improvement and aggregate-gradient cosine above 0.5 when sybil weight is below the declared robust-aggregation threshold, while failing cleanly above that threshold.
- Stop condition: Stop if precommitted sybils still match adaptive poisoning below the declared threshold or if the only remaining improvement comes from the robust aggregator without any measurable commit-reveal contribution.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-anti-sybil-for-volunteer-gradients-c95b709c7453`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
