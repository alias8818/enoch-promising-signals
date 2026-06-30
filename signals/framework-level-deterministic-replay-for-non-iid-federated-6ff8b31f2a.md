# Framework-level deterministic replay for non-IID federated gradient validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `framework-level-deterministic-replay-for-non-iid-federated-6ff8b31f2a`
Run ID: `framework-level-deterministic-replay-for-non-iid-federated-6ff8b31f2a-20260620T131632459404+0000`

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

- Parent run decision: Deterministic Replay Verification for CPU Federated Gradient Validation: enoch://control-plane/projects/deterministic-replay-verification-for-cpu-federated-gradient-validation-4e601681087a/runs/deterministic-replay-verification-for-cpu-federated-gradient-validation-4e601681087a-20260620T123552224540+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/06998cec680a

## What looked useful

Canonical framework-level replay exactly reproduced non-IID per-client gradients and aggregate updates with zero replay failures and 0.0 max absolute canonical replay difference. Arrival-order aggregation drifted by 8.940696716308594e-08 in float32, and a 1e-3 client tensor tamper was detected by gradient hash mismatch.

## Boundaries and scale limits

Synthetic data only; one process and one host; no real federated framework, secure aggregation, privacy layer, partial participation, dropout, multi-node networking, GPU nondeterminism, large models, or adversarial clients.

## Claim scope

Small direct NumPy logistic-regression federated replay test with 8 strongly label-skewed clients, canonical client ordering, per-client gradient hashes, exact same-seed replay, an arrival-order nondeterminism control, and a gradient-visible tamper control.

## Why it stopped

No-paper useful signal: Tier 1 direct mechanism test passed, but evidence is too small and synthetic for publication readiness.

## Recommended next action

Run a bounded deepen follow-up in a real federated-learning framework with partial participation and client dropout; require exact canonical replay while showing arrival-order or runtime nondeterminism fails the same threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework-integrated deterministic replay under partial participation and dropout
- Success threshold: Zero per-client gradient replay failures, 0.0 canonical aggregate replay max absolute difference across reruns, tamper/dropout metadata controls detected, and at least one nondeterministic runtime-order control showing nonzero drift or explicit replay failure.
- Stop condition: Stop as negative if any framework-integrated rerun cannot reproduce canonical aggregate updates exactly after replay descriptors include client order, model hash, data hash, gradient hash, and dropout metadata.

## Evidence references

- Artifact root: `<local-path>/projects/framework-level-deterministic-replay-for-non-iid-federated-6ff8b31f2a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
