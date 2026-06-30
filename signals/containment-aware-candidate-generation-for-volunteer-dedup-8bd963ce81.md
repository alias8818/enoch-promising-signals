# Containment-aware candidate generation for volunteer dedup

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `containment-aware-candidate-generation-for-volunteer-dedup-8bd963ce81`
Run ID: `containment-aware-candidate-generation-for-volunteer-dedup-8bd963ce81-20260522T073224464611+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Public-corpus volunteer minhash dedup validation: enoch://control-plane/projects/public-corpus-volunteer-minhash-dedup-validation-31cba8f7df/runs/public-corpus-volunteer-minhash-dedup-validation-31cba8f7df-20260522T044816585438+0000
- Parent run decision: Two-stage MinHash plus exact-containment volunteer dedup validation: enoch://control-plane/projects/two-stage-minhash-plus-exact-containment-volunteer-dedup-v-81c68575ba/runs/two-stage-minhash-plus-exact-containment-volunteer-dedup-v-81c68575ba-20260522T061525530247+0000

## What looked useful

Across 27 containment-stress scenarios, containment-aware recall averaged 0.763 versus 0.467 for rare-token/Jaccard, 0.389 for contact keys, and 0.361 for identity blocking. It exceeded the best real baseline in all 27 scenarios, with 11,916 mean candidate pairs and 0.583 precision. The unfiltered containment ablation had higher recall at 0.859 but emitted 719,190 mean pairs at 0.011 precision. A zero-containment control showed Jaccard slightly ahead on recall, narrowing the mechanism to containment-heavy data.

## Boundaries and scale limits

Evidence is synthetic only. No real labeled volunteer CRM/export data, no clerical labels, no production traffic, and no downstream resolver/reviewer workload were available. The hardest high-containment/high-missingness condition only reached 0.546 mean recall, so this does not support a broad deployment or paper claim.

## Claim scope

On a fixed-seed synthetic volunteer-dedup benchmark with 20,000 base entities per scenario and explicit subset/superset duplicate modes, containment-aware candidate generation improved duplicate-pair recall over contact-key, identity-blocking, and rare-token/Jaccard baselines while emitting far fewer candidates than an unfiltered containment ablation.

## Why it stopped

Synthetic bounded validation supports the containment-aware mechanism but is not publication-grade and does not close real-world volunteer dedup performance.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next concrete step is a bounded real-data validation on labeled volunteer records or a public entity-resolution dataset modified with documented containment injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data containment-aware volunteer dedup candidate validation
- Success threshold: Containment-aware generation achieves at least +0.10 absolute pair recall over the best real baseline at no more than 2x candidate pairs, or achieves the same recall with at least 50% fewer candidate pairs, on labeled non-synthetic data.
- Stop condition: Stop if containment-aware recall is not at least +0.03 absolute above the best baseline, if candidate volume exceeds 5x baseline at comparable recall, or if no labeled real/public dataset can be obtained within the bounded follow-up.

## Evidence references

- Artifact root: `<local-path>/projects/containment-aware-candidate-generation-for-volunteer-dedup-8bd963ce81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
