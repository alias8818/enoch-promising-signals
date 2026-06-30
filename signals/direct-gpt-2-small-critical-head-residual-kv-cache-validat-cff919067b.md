# Direct GPT-2-Small Critical-Head Residual KV Cache Validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-gpt-2-small-critical-head-residual-kv-cache-validat-cff919067b`
Run ID: `direct-gpt-2-small-critical-head-residual-kv-cache-validat-cff919067b-20260603T231421115689+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Residual KV-Cache: Critical-Head FP16 with Compressed Contextors: enoch://control-plane/projects/residual-kv-cache-critical-head-fp16-with-compressed-contextors-fe2b6fedf9f4/runs/residual-kv-cache-critical-head-fp16-with-compressed-contextors-fe2b6fedf9f4-20260603T192513821459+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/682b9ac9b3c0

## What looked useful

Single-head ablation found individually important early GPT-2-small heads, but the induced top-k retained-cache sets were worse than random controls on held-out rolling KV-cache evaluation. This suggests head importance is non-additive or the simple calibration objective is mismatched to retained-cache compression.

## Boundaries and scale limits

Pretrained GPT-2 small only; local text chunks only; zeroed full-shaped K/V cache rather than compact cache storage; no public benchmark, no true latency or memory-bandwidth measurement, no learned or greedy group-aware selector.

## Claim scope

In a Tier-1 direct GPT-2-small rolling decode test on a deterministic local text corpus, retaining heads selected by single-head KV-cache ablation did not preserve next-token loss better than same-budget random head retention at 8.3%, 16.7%, 25.0%, or 33.3% of attention heads.

## Why it stopped

The direct small GPT-2 test failed the predeclared success threshold: top calibrated retained heads were worse than random same-budget retention at every tested cache budget and remained far from full-cache loss.

## Recommended next action

Stop this run as a direct Tier-1 negative/useful signal; only pursue a bounded follow-up if testing group-aware head selection on the same direct KV-cache intervention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Group-aware GPT-2-small KV-cache head selection against random controls
- Success threshold: Group-aware selection must beat random mean by at least 0.10 NLL at two or more budgets, including one budget at or below 25% of heads, while reducing the full-cache NLL penalty relative to this run by at least 25%.
- Stop condition: Stop as negative if group-aware selection fails to beat random mean at two budgets or if the full-cache NLL penalty remains above 2.0 at all tested budgets.

## Evidence references

- Artifact root: `<local-path>/projects/direct-gpt-2-small-critical-head-residual-kv-cache-validat-cff919067b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
