# Deterministic CPU Gradient Replay for Volunteer Cheating Detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deterministic-cpu-gradient-replay-for-volunteer-cheating-detection-ecdb4ca35fd1`
Run ID: `deterministic-cpu-gradient-replay-for-volunteer-cheating-detection-ecdb4ca35fd1-20260609T015212941126+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4890047f9ba5

## What looked useful

Deterministic replay gave 0/2000 honest false positives and 2000/2000 detections for random, scaled, sign-flipped, zero, stale-batch, and claimed-label-flip gradients at relative L2 threshold 1e-10. It failed by design on semantic poisoning already present in the committed inputs, with 0/2000 detections.

## Boundaries and scale limits

Tested only on a single CPU worker with synthetic data, softmax regression, one process, one BLAS thread, and 2,000 main trials. Not tested on multi-host volunteers, heterogeneous CPU libraries, deep networks, private data, cryptographic assignment commitments, GPU training, adaptive attackers, or production audit sampling.

## Claim scope

In a local NumPy softmax-regression proxy where the verifier has the exact committed model state, data, labels, batch indices, and deterministic CPU gradient code, replay detects gradient submissions that differ from the committed computation.

## Why it stopped

Useful proxy result but not a full validation: replay verifies consistency with committed computation, not semantic honesty of committed volunteer inputs.

## Recommended next action

Stop this run as bounded no-paper evidence; next concrete action is a multi-host committed-transcript replay audit with heterogeneous CPU implementations and adaptive attackers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-host committed-transcript replay audit for volunteer gradient verification
- Success threshold: At least 99% detection of non-committed fabricated/stale/scaled gradients at under 1% honest false positives, plus explicit measured failure on committed semantic poisoning.
- Stop condition: Stop if cross-platform honest replay error overlaps materially with stale or scaled attack errors, or if verifier recomputation cost makes the audit impractical for the target workload.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-cpu-gradient-replay-for-volunteer-cheating-detection-ecdb4ca35fd1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
