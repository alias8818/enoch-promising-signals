# CPU Gradient Replay Verification for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-gradient-replay-verification-for-volunteer-training-117fd0700bc6`
Run ID: `cpu-gradient-replay-verification-for-volunteer-training-117fd0700bc6-20260531T180630776636+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1f7c49f7f4e2

## What looked useful

Full-gradient replay is mechanically viable as an audit check when the verifier has pre-update weights and deterministic batch identity, but it is not a cheap universal volunteer-training verifier because full replay has near-1x training overhead and compressed gradients require fragile tolerance choices.

## Boundaries and scale limits

Toy synthetic CPU-only model; no real dataset, no large model, no volunteer network, no adaptive adversary, no nondeterministic framework kernels, no privacy or cryptographic protocol, and no partial replay sampling.

## Claim scope

On a deterministic 8,906-parameter NumPy MLP with synthetic batches, CPU full-gradient replay exactly accepts honest gradients and rejects stale, random, 5%-noisy, and label-flipped submissions; replay costs about one extra backward pass per verified update.

## Why it stopped

Bounded CPU evidence supports the replay mechanism but does not validate the broader volunteer-training claim; this is a toy/proxy result with overhead and tolerance limitations.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement quantization-aware replay and adaptive near-threshold attacks on a real small dataset before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware CPU gradient replay on a real small dataset
- Success threshold: Quantization-aware replay accepts at least 99.5% of honest compressed gradients and rejects at least 99.5% of tested malicious submissions while keeping verifier cost at or below 1.25x one backward pass per checked update.
- Stop condition: Stop if compressed honest gradients and adaptive noisy submissions cannot be separated by a stable threshold across seeds/layers, or if deterministic replay cannot be made reproducible on the selected real dataset pipeline.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-gradient-replay-verification-for-volunteer-training-117fd0700bc6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
