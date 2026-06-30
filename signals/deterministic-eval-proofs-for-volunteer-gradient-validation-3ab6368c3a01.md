# Deterministic eval proofs for volunteer gradient validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `deterministic-eval-proofs-for-volunteer-gradient-validation-3ab6368c3a01`
Run ID: `deterministic-eval-proofs-for-volunteer-gradient-validation-3ab6368c3a01-20260527T160503806802+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05d9de47723a

## What looked useful

Across 1,000 trials per mode, honest workers were accepted and buggy/nondeterministic eval implementations were rejected, but four malicious workers with poisoned training gradients and valid public eval proofs were accepted 100% of the time.

## Boundaries and scale limits

Synthetic logistic-regression simulation only; no real distributed volunteer network, large model, or cryptographic binding variant was tested. The failure is protocol-level for the unbound design, not a benchmark of all possible proof systems.

## Claim scope

For an unbound protocol where volunteers submit a private training gradient plus deterministic public eval-gradient hashes, public eval proofs validate implementation determinism on challenge batches but do not validate the submitted training gradient.

## Why it stopped

Proxy/early falsification of the unbound validation protocol: valid public eval proofs can be attached to arbitrary poisoned training gradients, so the mechanism does not validate the volunteered gradient.

## Recommended next action

Stop using unbound deterministic eval proofs as a volunteer gradient validator; next test should add an explicit binding mechanism and adversarially measure bad-gradient rejection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded binding mechanisms for deterministic volunteer gradient checks
- Success threshold: Bad-gradient accept rate below 1% for large corruptions, honest false-reject rate below 1%, and verifier recomputation below 10% on at least a small real model or public dataset task.
- Stop condition: Stop if the binding variant either requires full gradient recomputation for reliable detection or still accepts more than 5% of large poisoned gradients under adaptive attacks.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-eval-proofs-for-volunteer-gradient-validation-3ab6368c3a01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
