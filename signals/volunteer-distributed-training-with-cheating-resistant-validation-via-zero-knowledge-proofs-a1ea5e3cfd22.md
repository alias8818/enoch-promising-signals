# Volunteer Distributed Training with Cheating-Resistant Validation via Zero-Knowledge Proofs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-distributed-training-with-cheating-resistant-validation-via-zero-knowledge-proofs-a1ea5e3cfd22`
Run ID: `volunteer-distributed-training-with-cheating-resistant-validation-via-zero-knowledge-proofs-a1ea5e3cfd22-20260620T110452872969+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/35b446046754

## What looked useful

For the tested arithmetic relation, 100% validation rejected all malformed updates, but 1-25% sampled audits accepted most malicious updates. Current proof-of-training literature reports about 15 minutes prover time per VGG-11 batch-16 iteration, suggesting per-update ZK validation is not practical as the default validation path for volunteer training today.

## Boundaries and scale limits

Local synthetic data, one small linear model, direct recomputation audit proxy only; no real SNARK/STARK implementation, no networked volunteer system, no large model, no private dataset commitment, and no adversarially adaptive workers.

## Claim scope

Toy softmax-classifier volunteer SGD updates show that exact per-update validation rejects malformed updates, while sampled recomputation leaves unaudited cheating accepted. External zkPoT evidence indicates real DNN proof generation remains far too costly for routine volunteer per-update proving.

## Why it stopped

Proxy evidence supports the integrity mechanism but falsifies the practical per-update ZK validation story for volunteer training at current proof-of-training costs; this is not a full validation of large-scale distributed training.

## Recommended next action

Stop this run as a proxy/useful-signal negative; next, implement one actual fixed-point logistic-regression proof for a single SGD step and compare prover time against recomputation and sampled-audit security.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Single-step fixed-point zk proof benchmark for volunteer SGD validation
- Success threshold: Produce and verify at least 100 valid single-step proofs with median verifier time under 100 ms and report prover/recompute overhead ratio; reject per-update deployment if prover overhead exceeds 100x direct recomputation for the toy step.
- Stop condition: Stop if the circuit cannot represent the fixed-point SGD update correctly, peak memory exceeds local capacity, or median prover overhead exceeds 1000x recomputation on the toy step.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-training-with-cheating-resistant-validation-via-zero-knowledge-proofs-a1ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
