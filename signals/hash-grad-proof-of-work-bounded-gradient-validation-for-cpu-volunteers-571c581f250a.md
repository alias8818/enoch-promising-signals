# Hash-Grad: Proof-of-Work Bounded Gradient Validation for CPU Volunteers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `hash-grad-proof-of-work-bounded-gradient-validation-for-cpu-volunteers-571c581f250a`
Run ID: `hash-grad-proof-of-work-bounded-gradient-validation-for-cpu-volunteers-571c581f250a-20260524T053121032404+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27bbaca74165

## What looked useful

Hashing a gradient digest with proof-of-work proves CPU effort on chosen bytes, not correct gradient computation. In the benchmark, pow_norm matched norm exactly across all attacks: zero accuracy and malicious-accept-rate deltas relative to norm. Under sign_flip, pow_norm accepted 97.38% of malicious gradients and reached 9.59% mean test accuracy; audit-loss validation reached 91.41% but is a different mechanism based on held-out loss checking.

## Boundaries and scale limits

This is a small/medium proxy, not a full decentralized training deployment. It used synthetic IID logistic-regression data, no network or reward model, and did not test large neural models or adaptive economic attacks. PoW mining was benchmarked separately because certificate mining is independent of gradient correctness.

## Claim scope

On a local synthetic distributed logistic-regression benchmark with 24 workers, 25% malicious workers, 160 rounds, and 5 random seeds, proof-of-work over submitted gradient digests plus norm bounds provided no measurable validation benefit over norm bounds alone. Malicious bounded gradients could be certified and accepted, and sign-flip attackers drove mean test accuracy to 0.0959 under both norm and pow_norm validators.

## Why it stopped

Early falsification on a direct small/medium proxy: proof-of-work plus a norm bound does not validate gradient correctness and behaves identically to norm-only validation in the tested attacks.

## Recommended next action

Stop this Hash-Grad mechanism as a paper path; only revisit if the proof-of-work challenge is redesigned to bind to hidden validator information or verifiable-computation evidence rather than arbitrary submitted gradient bytes.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/hash-grad-proof-of-work-bounded-gradient-validation-for-cpu-volunteers-571c581f250a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
