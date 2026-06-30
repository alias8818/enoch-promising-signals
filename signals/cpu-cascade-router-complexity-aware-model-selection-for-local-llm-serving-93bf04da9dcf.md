# CPU Cascade Router: Complexity-Aware Model Selection for Local LLM Serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-cascade-router-complexity-aware-model-selection-for-local-llm-serving-93bf04da9dcf`
Run ID: `cpu-cascade-router-complexity-aware-model-selection-for-local-llm-serving-93bf04da9dcf-20260610T154201826850+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3cf9fae43f79

## What looked useful

Across 20 seeds, the complexity router improved reward over always-small by 11.0% in-distribution, 65.5% on harder prompts, and 21.8% when length was misleading; it also reduced regret versus an attainable expected-utility oracle relative to length-only routing.

## Boundaries and scale limits

No real LLM inference was run. The result does not cover real prompt corpora, quantized local models, batching, queueing, KV-cache effects, CPU memory bandwidth contention, or human/model-graded quality.

## Claim scope

Synthetic CPU-serving trace evidence: prompt-complexity features improved expected utility for routing between a fast weaker model and a slower stronger model, outperforming length-only baselines across in-distribution, harder-shift, and misleading-length scenarios.

## Why it stopped

Proxy evidence supports the mechanism but is not full validation or paper-ready direct serving evidence.

## Recommended next action

Run a bounded direct validation on real local CPU LLM pairs by collecting per-prompt latency and quality traces, then compare complexity routing against length-only and static baselines using the same utility.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured CPU LLM cascade trace validation
- Success threshold: Complexity router improves mean utility by at least 5% over the best non-oracle baseline and closes at least 40% of oracle regret on a held-out measured trace without increasing p95 latency beyond the selected utility tradeoff.
- Stop condition: Stop as negative if the complexity router fails to beat the best length-only/static baseline by 2% mean utility on two independently measured prompt sets or if measured model quality differences are too small to create a meaningful cascade decision.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascade-router-complexity-aware-model-selection-for-local-llm-serving-93bf04da9dcf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
