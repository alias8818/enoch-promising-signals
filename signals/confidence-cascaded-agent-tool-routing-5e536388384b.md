# Confidence-Cascaded Agent Tool Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-cascaded-agent-tool-routing-5e536388384b`
Run ID: `confidence-cascaded-agent-tool-routing-5e536388384b-20260629T051814069778+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/95600b59db12

## What looked useful

Held-out sweep over 20 seeds and 20,000 test tasks per seed found 26.21% cost saving at 0.78 percentage-point accuracy loss for the calibrated condition, 9.00% cost saving at 0.89 percentage-point loss for mild shift, 0.59% saving with 99.35% fallback for anti-calibrated confidence, and a failed overconfident-shift condition with 9.47 percentage-point accuracy loss despite 36.53% apparent cost saving.

## Boundaries and scale limits

Synthetic single-turn routing only; no real agent traces, no live tool costs, no learned LLM router, no multi-turn downstream task success, and no production distribution shift.

## Claim scope

On a synthetic 8-tool routing benchmark with validation-selected thresholds, confidence cascades reduce cost while staying within 1 percentage point of expensive-router accuracy when cheap-router confidence separates easy/correct cases from hard/error-prone cases; they fail under overconfident distribution shift and become degenerate under anti-calibrated confidence.

## Why it stopped

No-paper useful signal: the local synthetic evidence supports a scoped mechanism and exposes a safety failure mode, but it is proxy evidence rather than direct validation on real agent tool-routing traces.

## Recommended next action

Run a bounded deepen follow-up on real or recorded agent tool-routing traces with validation-selected thresholds, requiring <=1 percentage point downstream success loss and at least 15% realized cost saving on held-out traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out confidence cascades on real agent tool-routing traces
- Success threshold: On held-out real traces, cascade success is within 1 percentage point of expensive-only routing and realized cost is at least 15% lower, with no shifted slice losing more than 2 percentage points unless flagged for fallback-only operation.
- Stop condition: Stop if held-out traces show less than 15% cost saving at <=1 percentage point success loss, or if confidence miscalibration forces fallback rates above 90% on most slices.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-cascaded-agent-tool-routing-5e536388384b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
