# Deterministic Replay Verification for CPU Federated Gradient Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-replay-verification-for-cpu-federated-gradient-validation-4e601681087a`
Run ID: `deterministic-replay-verification-for-cpu-federated-gradient-validation-4e601681087a-20260620T123552224540+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/06998cec680a

## What looked useful

Deterministic replay is mechanically viable for CPU federated-gradient validation when reduction order and dtype are part of the replay contract; exact aggregate hashing is brittle without those controls because float32 order drift changed every control aggregate hash.

## Boundaries and scale limits

Single-process local simulation only; 64 clients, 10 rounds, 256 samples/client, 128 features; no networked FL runtime, secure aggregation, DP noise, production dataset, non-IID benchmark, or multi-host persistence.

## Claim scope

In a CPU-only synthetic federated linear-regression simulator, deterministic replay metadata with fixed client seeds, per-client gradient hashes, dtype, and reduction order exactly accepted 50 clean replay trials and rejected 50 injected client-gradient perturbations; unfixed float32 reduction order produced aggregate hash drift in 50 of 50 control trials.

## Why it stopped

No-paper useful signal: synthetic local evidence supports the replay mechanism but is not direct or broad enough for publication-grade federated-gradient validation.

## Recommended next action

Run one bounded deepen follow-up inside a real federated-learning framework with non-IID client partitions, fixed replay metadata, and adversarial gradient perturbation cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework-level deterministic replay for non-IID federated gradient validation
- Success threshold: Clean accept rate >= 0.99, tamper detection rate >= 0.99 for predefined perturbations, and documented replay metadata sufficient to reproduce aggregate hashes across separate processes.
- Stop condition: Stop if clean replay false rejections exceed 1% after fixing seeds/order/dtype, or if tampered gradients cannot be detected without raw client gradients in the selected framework mode.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-verification-for-cpu-federated-gradient-validation-4e601681087a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
