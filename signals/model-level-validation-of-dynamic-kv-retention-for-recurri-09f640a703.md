# Model-level validation of dynamic KV retention for recurring-anchor long-context prompts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `model-level-validation-of-dynamic-kv-retention-for-recurri-09f640a703`
Run ID: `model-level-validation-of-dynamic-kv-retention-for-recurri-09f640a703-20260522T070132998447+0000`

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

- Parent run decision: Dynamic KV-Cache Pruning for Long-Context Serving: enoch://control-plane/projects/dynamic-kv-cache-pruning-for-long-context-serving-174d8a19a4d4/runs/dynamic-kv-cache-pruning-for-long-context-serving-174d8a19a4d4-20260522T013834496230+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/097ee83fc7b8

## What looked useful

Dynamic anchor retention matched full-cache accuracy at 100% on the two-fact condition with 54 retained tokens while sliding-window accuracy was 4.7%. On four facts, dynamic-anchor accuracy was 54.7% versus 3.9% sliding and 51.2% full. On eight facts, dynamic-anchor accuracy was 20.3% versus 3.1% sliding and 22.7% full. The mechanism signal is positive, but harder conditions are limited by model competence.

## Boundaries and scale limits

Synthetic token task only; tiny decoder trained from scratch; maximum evaluated prefix length 320 tokens; two/four/eight facts only; anchor spans were detected by known token IDs; no pretrained LLM, natural-language benchmark, learned retention controller, or production serving runtime.

## Claim scope

In a tiny trained causal decoder on synthetic 320-token recurring-anchor associative-recall prompts, preserving anchor-local KV spans plus a recent suffix can recover full-cache behavior under a tight cache budget in an easy two-fact condition and remains much better than sliding-window retention in harder four/eight-fact conditions.

## Why it stopped

Tier 1 direct model/KV test completed; evidence supports a narrow mechanism signal but not publication readiness or broad validation.

## Recommended next action

Run a bounded deepen test that first trains or sizes the model until full-cache accuracy is at least 85% on 4-8 fact anchored prompts, then retest dynamic-anchor versus sliding at matched cache budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Competent-model dynamic KV retention on 4-8 recurring-anchor facts
- Success threshold: For both 4-fact and 8-fact conditions: full-cache accuracy >= 0.85, dynamic-anchor accuracy >= full-cache accuracy - 0.10, and dynamic-anchor accuracy - sliding-window accuracy >= 0.25.
- Stop condition: Stop if full-cache accuracy cannot reach 0.85 within a bounded local run, or if dynamic-anchor falls more than 10 points below full cache after full-cache competence is established.

## Evidence references

- Artifact root: `<local-path>/projects/model-level-validation-of-dynamic-kv-retention-for-recurri-09f640a703`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
