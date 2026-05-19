# Multi-model held-out exact-anchor ledger replay on real agent traces

Status: `useful_signal`
Project ID: `multi-model-held-out-exact-anchor-ledger-replay-on-real-ag-d3dd4b6cc9`
Run ID: `multi-model-held-out-exact-anchor-ledger-replay-on-real-ag-d3dd4b6cc9-20260516T002359480306+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Multi-model held-out exact-anchor ledger replay on real agent traces: internal_generated:multi-model-held-out-exact-anchor-ledger-replay-on-real-ag-d3dd4b6cc9

## What looked useful

Exact anchors are useful sparse replay handles for held-out real trace facts: deterministic replay reached 100% accuracy, Qwen2.5 models improved from 27.5-28.3% under compressed/hash-only controls to 85.0% under exact anchors, and exact anchors were statistically indistinguishable from full event-window replay rather than better.

## Boundaries and scale limits

The test used multiple-choice command probes, prompt-text anchor reveals, one fixed seed, 60 selected anchors, and three cached small local instruction models; one model had severe format noncompliance, and the method was not integrated into a production replay API or tested on frontier models.

## Claim scope

On 60 fixed-seed held-out command anchors sampled from real local Codex agent JSONL traces, exact-anchor replay restored command-answer accuracy versus compressed/no-anchor and hash-only controls for deterministic replay and compliant Qwen2.5 local instruction models, matching but not exceeding a full-event-window baseline.

## Why it stopped

Tier 2 direct real-trace validation produced a useful mechanism signal, but multi-model robustness and citation behavior were insufficient for a paper-positive decision, and exact anchors did not outperform the full-event-window baseline.

## Recommended next action

Run a structured-tool replay follow-up where models answer through a JSON/tool schema from exact-anchor retrieval over a larger multi-seed real-trace split, and require exact anchors to match full-window accuracy while preserving citation validity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured-tool exact-anchor replay on multi-seed real Codex trace splits
- Success threshold: Exact-anchor replay must be within 2 percentage points of full-event-window answer accuracy, at least 40 percentage points above hash-only and compressed controls, and at least 95% valid-citation/parse compliance across at least four compliant models.
- Stop condition: Stop if exact anchors fail to match full-window accuracy on any two fixed seeds, if citation validity remains below 95%, or if gains over hash-only/compressed controls fall below 20 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-held-out-exact-anchor-ledger-replay-on-real-ag-d3dd4b6cc9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
