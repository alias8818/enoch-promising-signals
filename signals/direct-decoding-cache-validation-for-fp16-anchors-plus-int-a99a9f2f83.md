# Direct decoding-cache validation for FP16 anchors plus INT3 residual spans

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-decoding-cache-validation-for-fp16-anchors-plus-int-a99a9f2f83`
Run ID: `direct-decoding-cache-validation-for-fp16-anchors-plus-int-a99a9f2f83-20260604T053044190336+0000`

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

- Parent run decision: Context-Adaptive Precision: Exact Anchors FP16, Spans INT3: enoch://control-plane/projects/context-adaptive-precision-exact-anchors-fp16-spans-int3-0bb9b6665c91/runs/context-adaptive-precision-exact-anchors-fp16-spans-int3-0bb9b6665c91-20260604T033753643712+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/79f886d5213e

## What looked useful

INT3 residual spans are a real mechanism improvement over anchor-only cache interpolation, but the tested compression/fidelity tradeoff is weak: span 2 passes the small direct threshold at only 1.53x compression, while span 4 reaches mean KL 0.01513 at 2.12x compression but only 0.9167 top-1 match.

## Boundaries and scale limits

Single model family, 12 prompts, one-step next-token decode only, no packed INT3 kernel, no latency measurement, no multi-token persistence, no long-context or larger-model validation.

## Claim scope

On GPT-2 small with 12 short prompts, FP16 anchors plus per-head interval-scaled INT3 residuals improve direct next-token KV-cache reconstruction over anchor-only interpolation. The Tier 1 fidelity threshold is met at span 2 with about 1.53x cache compression, but not reliably at span 4 or larger.

## Why it stopped

Tier 1 direct validation produced a useful no-paper signal: mechanism support exists, but paper-grade or broadly useful compression was not demonstrated.

## Recommended next action

Run one bounded deepen test using span 4 with per-channel or layer-adaptive residual scaling, at least 100 prompts, and 16-token greedy continuation persistence; stop if top-1 match remains below 0.95 or mean KL exceeds 0.02.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Span-4 direct decode persistence for FP16 anchors plus channel-adaptive INT3 residuals
- Success threshold: Span-4 INT3 residual cache reaches mean KL <= 0.02, top-1 match >= 0.95, top-5 Jaccard >= 0.90, and 16-token greedy continuation exact-match rate >= 0.80 while maintaining at least 1.9x cache compression.
- Stop condition: Stop as no-paper if span-4 top-1 match is below 0.95, mean KL exceeds 0.02, or continuation exact-match rate is below 0.80 under the stated controls.

## Evidence references

- Artifact root: `<local-path>/projects/direct-decoding-cache-validation-for-fp16-anchors-plus-int-a99a9f2f83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
