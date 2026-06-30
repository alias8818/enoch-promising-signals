# Adaptive Draft-Length Speculative Decoding Under Queue Saturation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-draft-length-speculative-decoding-under-queue-saturation-6ee345ed9ee2`
Run ID: `adaptive-draft-length-speculative-decoding-under-queue-saturation-6ee345ed9ee2-20260620T044502278801+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1d9a11bb32e

## What looked useful

Queue saturation alone is an insufficient control signal for adaptive draft length. It helps reduce harm from high fixed draft lengths when acceptance is low, but it can shut off beneficial speculation too early under medium acceptance; acceptance/SLO/cost signals are likely required.

## Boundaries and scale limits

Synthetic CPU-only simulator; no real LLM weights, GPU kernels, KV-cache allocator, serving engine integration, production traces, or measured draft/target acceptance distributions. Results should be treated as a bounded mechanism probe, not full serving validation.

## Claim scope

In a dependency-free synthetic continuous-batching simulator, a queue-pressure draft-length controller protects against pathological fixed-high speculation under low-acceptance overload but does not beat tuned fixed-k or no-spec baselines across tested saturation regimes.

## Why it stopped

Proxy evidence is mixed: queue-only adaptation avoids fixed-high overload pathologies but fails to dominate tuned fixed and no-spec baselines, so it is not a paper-ready positive result.

## Recommended next action

Stop this run as no-paper useful signal; a bounded next test should add an online acceptance-aware controller and compare it against static k=2 and no-spec baselines in the same simulator or a small serving-engine replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-aware draft-length control under queue saturation
- Success threshold: Acceptance-aware control must match or improve the best static/no-spec baseline within 5% p95 TPOT and p95 E2E in every tested overload scenario, and improve at least one low-acceptance fixed-high failure case by 2x p95 E2E versus static_k8.
- Stop condition: Stop if the acceptance-aware controller still loses by more than 5% p95 TPOT or p95 E2E to static_k2/no-spec in medium- or low-acceptance overload.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-draft-length-speculative-decoding-under-queue-saturation-6ee345ed9ee2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
