# Confidence-Router Cascade for VRAM Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-router-cascade-for-vram-reduction-ee2ba6c3c184`
Run ID: `confidence-router-cascade-for-vram-reduction-ee2ba6c3c184-20260518T234223242898+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a1d9380147a

## What looked useful

Confidence routing can avoid most fallback calls on easy examples in a small controlled task, but simple validation calibration did not guarantee held-out accuracy preservation across seeds.

## Boundaries and scale limits

Toy 8x8 digit classification only; not an LLM, not transformer KV-cache memory, not production batching, and not a direct large-model VRAM/offload measurement. Large fallback parameter memory was only 68.35 MB, and latency measurements were noisy.

## Claim scope

On sklearn digits with a tiny MLP front model and larger MLP fallback, validation-calibrated max-softmax confidence routing reduced mean routed fallback calls to 9.39% while matching mean large-model test accuracy across five seeds, but seed-level noninferiority was not reliable.

## Why it stopped

Finalized as no-paper useful signal because the local proxy produced mixed seed-level accuracy preservation and only parameter-residency memory evidence, not full VRAM validation.

## Recommended next action

Run a bounded deepen follow-up on a larger direct task with a predeclared per-seed noninferiority margin and actual GPU residency/offload telemetry; do not write a paper from this toy proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-seed noninferiority test for confidence-router cascades on a larger direct task
- Success threshold: At least 50% fewer large-model invocations, no seed worse than -0.5 percentage points versus always-large accuracy, and measured GPU residency reduction under the stated offload policy.
- Stop condition: Stop as negative if any seed misses the -0.5 percentage point noninferiority margin or if actual GPU residency does not decrease under the offload policy.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-router-cascade-for-vram-reduction-ee2ba6c3c184`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
