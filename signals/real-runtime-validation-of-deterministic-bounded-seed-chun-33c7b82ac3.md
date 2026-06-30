# Real-runtime validation of deterministic bounded seed-chunk stealing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-runtime-validation-of-deterministic-bounded-seed-chun-33c7b82ac3`
Run ID: `real-runtime-validation-of-deterministic-bounded-seed-chun-33c7b82ac3-20260602T115240541509+0000`

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

- Parent run decision: Bounded Work Stealing via Deterministic Seed Chunks: enoch://control-plane/projects/bounded-work-stealing-via-deterministic-seed-chunks-f62e24b83cb8/runs/bounded-work-stealing-via-deterministic-seed-chunks-f62e24b83cb8-20260601T061741524768+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7c1ce4c99f51

## What looked useful

Bounded seed stealing improved mean wall-clock time by 1.166x over static block assignment and was within 2.0% of an atomic dynamic baseline, but failed deterministic replay: assignment hashes differed across all five identical-seed calibrated repeats.

## Boundaries and scale limits

Synthetic CPU chunk work only; no GPU, distributed runtime, production task graph, NUMA stress, or model-training integration. The result directly tests deterministic replay and small-runtime scheduling behavior, not broad system scalability.

## Claim scope

Tier 1 CPU-only real-runtime scheduler harness with 8 threads, 4096 skewed deterministic chunks, fixed seed queues, and bounded steal budget 2.

## Why it stopped

Tier 1 direct runtime test produced an early falsification of the deterministic part of the hypothesis while preserving a useful performance signal.

## Recommended next action

Stop this run as a no-paper useful signal; test a deterministic arbitration variant that fixes steal ownership independent of thread arrival order.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic arbitration for bounded seed-chunk stealing
- Success threshold: 10/10 deterministic assignment hashes identical, >=1.10x static-block speedup, and <=1.15x dynamic-atomic wall-time ratio.
- Stop condition: Stop if deterministic arbitration either fails replay on the Tier 1 harness or loses the static-block speedup below 1.05x.

## Evidence references

- Artifact root: `<local-path>/projects/real-runtime-validation-of-deterministic-bounded-seed-chun-33c7b82ac3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
