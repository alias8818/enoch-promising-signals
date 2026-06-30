# Real-trace anchor replay with injected ground-truth spans under measured queue bounds

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-trace-anchor-replay-with-injected-ground-truth-spans-37313e267d`
Run ID: `real-trace-anchor-replay-with-injected-ground-truth-spans-37313e267d-20260611T035330238501+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Trace replay for exact anchor anchoring under bounded queues: enoch://control-plane/projects/trace-replay-for-exact-anchor-anchoring-under-bounded-queu-4ab869907d/runs/trace-replay-for-exact-anchor-anchoring-under-bounded-queu-4ab869907d-20260611T031057967189+0000
- Parent run decision: Ground-truth trace corpus replay for exact anchor recovery under queue bounds: enoch://control-plane/projects/ground-truth-trace-corpus-replay-for-exact-anchor-recovery-ea4f0c0405/runs/ground-truth-trace-corpus-replay-for-exact-anchor-recovery-ea4f0c0405-20260611T033228785347+0000

## What looked useful

Measured queue bounds matter: open-span bounds 16+ achieved 1.000 recall/precision with zero misses, while bounds 8 and 4 dropped to 0.923 and 0.478 recall; no-anchor windows 32 and 128 dropped to 0.079 and 0.331 recall on spans up to 384 events.

## Boundaries and scale limits

Injected labels, local trace corpus, simulated anchor snapshots, no independent key custody, no crash/restart recovery, no concurrent writer workload, and no natural human-labeled span boundaries.

## Claim scope

On 43,926 real local Codex/Enoch JSONL events with deterministic injected ground-truth spans, compact anchor-state replay recovered all spans when the open-span queue bound was at least the measured maximum active span concurrency of 14; undersized queues and short no-anchor windows lost spans.

## Why it stopped

Mechanism supported in a bounded replay with injected ground truth, but publication readiness requires externalized anchoring/restart/concurrency evidence and non-injected span labels.

## Recommended next action

Stop as no-paper useful signal; a bounded follow-up should test the same queue-bound claim with online external anchors, restart recovery, and naturally labeled or independently generated spans.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online external-anchor span replay with restart recovery on real agent traces
- Success threshold: Across fixed seeds and at least 50,000 real events, externally anchored replay after forced restarts has precision and recall >= 0.999 at queue bound >= measured max active spans, while an undersized bound or no-anchor window fails on the same workload.
- Stop condition: Stop negative if restart recovery loses any anchor-consistent span at a sufficient queue bound, if external anchor persistence dominates replay cost, or if the no-anchor baseline matches performance at smaller memory.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-anchor-replay-with-injected-ground-truth-spans-37313e267d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
