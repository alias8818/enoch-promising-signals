# HMAC-committed data shard lottery for volunteer pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hmac-committed-data-shard-lottery-for-volunteer-pretraining-7c5ff8adfee7`
Run ID: `hmac-committed-data-shard-lottery-for-volunteer-pretraining-7c5ff8adfee7-20260621T064831506515+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f1a51ae95934

## What looked useful

HMAC precommitment blocks a concrete post-seed shard grinding channel in the tested lottery model, and reveal verification detects manifest tampering. The mechanism is worth carrying into a bounded data-quality/Sybil follow-up, but is not paper-ready.

## Boundaries and scale limits

No real volunteer deployment, Sybil resistance, data quality scoring, or model-training outcomes were tested. Results are protocol-simulation evidence only and should not be generalized to full pretraining safety or utility.

## Claim scope

In a synthetic volunteer shard lottery with 900 honest fixed submissions, 100 adversarial accepted slots, and 100 selected shards, HMAC precommit/reveal kept adversarial selection near the 10-shard expected share while a no-commit adaptive baseline with 20x candidate grinding selected about 69 adversarial shards on average.

## Why it stopped

Stopped after bounded synthetic protocol evidence; this is useful mechanism support but not direct volunteer-system or model-training validation.

## Recommended next action

Run a bounded deepen follow-up that adds toy data-quality scores, admission/Sybil constraints, and a small training or sampling-quality proxy to test whether the lottery mechanism improves selected-corpus quality under realistic adversary budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: HMAC shard lottery with data-quality and Sybil admission constraints
- Success threshold: Across at least 3 adversary budgets, HMAC precommit plus admission constraints keeps adversarial selected-corpus quality degradation within 20% of the fixed-random baseline and at least 2x better than the adaptive no-commit baseline.
- Stop condition: Stop if HMAC precommitment does not improve selected-corpus quality over adaptive submission after admission constraints are modeled, or if benefits vanish under modest Sybil budget increases.

## Evidence references

- Artifact root: `<local-path>/projects/hmac-committed-data-shard-lottery-for-volunteer-pretraining-7c5ff8adfee7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
