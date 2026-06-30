# Gradient-Norm Outlier Defense for Volunteer CPU Training Without Server Trust

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-outlier-defense-for-volunteer-cpu-training-without-server-trust-950bc14626cf`
Run ID: `gradient-norm-outlier-defense-for-volunteer-cpu-training-without-server-trust-950bc14626cf-20260620T173552226454+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/871b7fc1a29f

## What looked useful

Gradient norms are useful only when trustworthy: oracle true-norm trimming restored mean accuracy to 0.990708 while reported-norm trimming removed zero malicious updates and matched no-defense failure at 0.009333 mean accuracy. Coordinate median reached 0.990667 without relying on reported norms.

## Boundaries and scale limits

Not tested on real volunteer CPU infrastructure, secure aggregation, neural-network-scale models, non-IID production data, asynchronous rounds, cryptographic norm proofs, or long-duration training.

## Claim scope

Synthetic federated logistic-regression proxy with 40 clients, 25% malicious label-flip scaled-gradient attackers, and adversarially self-reported norms. True-norm trimming works when individual norms are trustworthy; self-reported norm trimming fails under no-server-trust assumptions.

## Why it stopped

Proxy/mechanism evidence falsifies the no-server-trust version where malicious volunteers can self-report norms; this is not a full-scale validation of all verifiable-norm defenses.

## Recommended next action

Stop this naive self-reported norm-defense path; run a bounded follow-up that tests cheap verifiable norm commitments/proofs against coordinate median on a small non-IID federated benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifiable Gradient-Norm Proofs Versus Robust Aggregation On Small Non-IID Federated Training
- Success threshold: Verifiable norm trimming must achieve within 1 percentage point of the best robust aggregation baseline while removing at least 90% of malicious updates and adding less than 20% client CPU overhead in the bounded benchmark.
- Stop condition: Stop if proof/commitment overhead exceeds 20% in the toy implementation or if verifiable norm trimming fails to beat coordinate median on attack robustness.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-outlier-defense-for-volunteer-cpu-training-without-server-trust-950bc14626cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
