# Ground-truth trace corpus replay for exact anchor recovery under queue bounds

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ground-truth-trace-corpus-replay-for-exact-anchor-recovery-ea4f0c0405`
Run ID: `ground-truth-trace-corpus-replay-for-exact-anchor-recovery-ea4f0c0405-20260611T033228785347+0000`

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

- Parent run decision: Trace replay for exact anchor anchoring under bounded queues: enoch://control-plane/projects/trace-replay-for-exact-anchor-anchoring-under-bounded-queu-4ab869907d/runs/trace-replay-for-exact-anchor-anchoring-under-bounded-queu-4ab869907d-20260611T031057967189+0000
- Parent run decision: Bounded Work Queue with Exact Anchor Anchoring: enoch://control-plane/projects/bounded-work-queue-with-exact-anchor-anchoring-71bd01f19327/runs/bounded-work-queue-with-exact-anchor-anchoring-71bd01f19327-20260611T024921829887+0000

## What looked useful

Across five fixed seeds at jitter 32, arrival-order replay had 0.0 exact recall while bounded replay reached 1.0 mean/min exact recall at bounds 32, 48, and 64 with zero forced flushes. Jitter controls at 8, 16, and 64 showed the exact-recovery threshold moving with the disorder bound.

## Boundaries and scale limits

Validated on generated CPU-local traces up to 1,000,000 total events in the medium run plus three jitter-control sweeps; not validated on real production traces, multi-producer clock skew, missing/corrupt sequence metadata, dropped events, or storage/network replay effects.

## Claim scope

In a synthetic ground-truth trace corpus with bounded local arrival disorder and valid sequence metadata, queue-bounded replay recovers exact anchor IDs and spans when the queue bound is at least the true disorder bound; undersized queues fail with forced flushes.

## Why it stopped

The Tier 2 synthetic trace evidence supports the mechanism but is not real-corpus or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a real or production-style trace corpus that has independently known or injected anchor spans.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace anchor replay with injected ground-truth spans under measured queue bounds
- Success threshold: At least 99.9% exact anchor recall and 1.0 precision at the measured disorder-bound queue with zero forced flushes, plus at least a 20 percentage point exact-recall gap over the arrival-order baseline.
- Stop condition: Stop negative if the measured-bound queue has any forced flushes or exact recall below 99.9% on two fixed real/prod-style corpora after verifying the ground-truth anchors and parser.

## Evidence references

- Artifact root: `<local-path>/projects/ground-truth-trace-corpus-replay-for-exact-anchor-recovery-ea4f0c0405`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
