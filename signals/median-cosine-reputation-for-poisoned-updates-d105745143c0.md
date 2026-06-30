# Median-Cosine Reputation for Poisoned Updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `median-cosine-reputation-for-poisoned-updates-d105745143c0`
Run ID: `median-cosine-reputation-for-poisoned-updates-d105745143c0-20260602T131913494772+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2469cdae6780

## What looked useful

The median update is a useful reference direction for reputation when poisoned updates are directionally opposed to the honest majority. In the medium grid, median-cosine reputation achieved 0.863-0.887 mean accuracy under directed attacks where FedAvg fell to 0.140-0.507, and malicious aggregate weight was reduced to 0.00000034-0.1205 depending on attack and poison rate. Additive noise remained less separable, with malicious weight around 0.146-0.317 and only about +0.001 accuracy over FedAvg.

## Boundaries and scale limits

Synthetic data only; logistic regression only; 40 clients; 10 seeds; 35 rounds; simple non-adaptive attacks; no secure aggregation, client churn, sybil resistance, partial participation, image/text benchmark, or large model validation.

## Claim scope

In a synthetic non-IID federated logistic-regression simulator with persistent clients, median-cosine EMA reputation reduced malicious aggregate weight and improved clean test accuracy versus FedAvg under sign-flip and label-flip poisoned updates, with small gains over coordinate-wise median. It did not strongly separate additive-noise poisoned clients.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct or broad enough for a paper-ready positive result.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test is a bounded real-FL benchmark with adaptive attacks and partial client participation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Median-Cosine Reputation on Real Non-IID FL Benchmarks with Adaptive Poisoning
- Success threshold: Median-cosine reputation improves clean accuracy by at least 2 percentage points over coordinate median on at least two directed attack settings, keeps no-poison degradation below 1 percentage point versus FedAvg, and reduces malicious aggregate weight below the true malicious fraction by at least 50% for directed attacks.
- Stop condition: Stop if median-cosine reputation fails to beat coordinate median by at least 1 percentage point in directed attacks, degrades no-poison accuracy by more than 1 percentage point, or adaptive attacks keep malicious aggregate weight near the true malicious fraction while matching or beating coordinate median accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/median-cosine-reputation-for-poisoned-updates-d105745143c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
