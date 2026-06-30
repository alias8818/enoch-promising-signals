# Gradient Sparsification with Top-k Error Feedback for Low-Bandwidth Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-sparsification-with-top-k-error-feedback-for-low-bandwidth-volunteer-training-ec8995da3121`
Run ID: `gradient-sparsification-with-top-k-error-feedback-for-low-bandwidth-volunteer-training-ec8995da3121-20260620T111400402146+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/35b446046754

## What looked useful

Error feedback was the decisive control: mean final test accuracy was 0.7983 for dense, 0.7964 for 1% Top-k EF, and 0.7915 for 0.1% Top-k EF, while Top-k without EF dropped to 0.6660 and 0.4363 at the same densities. This supports testing EF-based sparsification further for low-bandwidth volunteer training, but only as a scoped proxy result.

## Boundaries and scale limits

Synthetic data, one GPU process, sequential simulated workers, no real volunteer network, no churn/straggler/adversarial-worker handling, no real sparse transport stack, and no GPT-2-small-class or larger model target. Communication time is modeled from bytes and bandwidth, not measured over a network.

## Claim scope

In a single-host GB10 PyTorch simulation of 4 synchronous workers training an 85,002-parameter MLP on synthetic teacher-labeled classification, local Top-k gradient sparsification with per-worker error feedback preserved dense-like final test accuracy at 1% and 0.1% update density while reducing modeled communication bytes by about 50x and 494x respectively.

## Why it stopped

Useful proxy evidence was obtained, but the result is not paper-ready because it lacks real-network volunteer training evidence and a direct language-model-scale target.

## Recommended next action

Run a bounded deepen follow-up on a compact real language-model training target with dense, Top-k without EF, and Top-k EF controls, including actual sparse serialization and multi-process or multi-host transport measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Top-k Error Feedback on a Compact Real Language-Model Target
- Success threshold: Top-k EF at 1% density reaches within 5% relative validation loss or perplexity of dense by the same optimizer-step budget while reducing serialized gradient bytes by at least 50x and outperforming Top-k without EF by at least 10% relative validation loss.
- Stop condition: Stop if Top-k EF fails to beat Top-k without EF by 10% relative validation loss after a calibrated short run, or if sparse serialization/transport overhead eliminates the modeled bandwidth advantage under the target low-bandwidth condition.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-sparsification-with-top-k-error-feedback-for-low-bandwidth-volunteer-training-ec8995da3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
