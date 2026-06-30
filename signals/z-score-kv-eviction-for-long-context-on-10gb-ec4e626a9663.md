# Z-score KV eviction for long context on 10GB

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `z-score-kv-eviction-for-long-context-on-10gb-ec4e626a9663`
Run ID: `z-score-kv-eviction-for-long-context-on-10gb-ec4e626a9663-20260601T021359002446+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4c0f43dccae5

## What looked useful

Medium synthetic run: age_zscore query recall 0.389 versus best non-z-score 0.109. No-anchor-signal control reduced the lift to +0.013 absolute recall, suggesting the main effect depends on observable anchor evidence. Noisy control still favored age_zscore at 0.247 versus best non-z-score 0.116.

## Boundaries and scale limits

No real transformer KV-cache implementation was tested; no LLM perplexity, retrieval benchmark accuracy, latency, memory bandwidth, or 10GB deployment quality was measured. Sequence lengths were up to 2048 tokens with budget 256 in CPU-only synthetic traces.

## Claim scope

In a bounded synthetic online KV-eviction trace benchmark with sparse noisy pre-query anchor evidence, age-binned z-score eviction preserved future retrieval anchors better than sliding-window, raw EMA attention, and cumulative-attention eviction at matched cache budgets.

## Why it stopped

Stopped after a bounded synthetic useful-signal result; this is a proxy mechanism test, not full validation of real long-context LLM behavior on 10GB hardware.

## Recommended next action

Implement age-binned z-score eviction in a small real transformer KV-cache path and compare against sliding and raw attention eviction on a long-context retrieval task with matched KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV-cache z-score eviction on a small long-context retrieval benchmark
- Success threshold: Age-zscore improves retrieval accuracy by at least 10 absolute percentage points over the best non-z-score eviction baseline at one or more constrained KV budgets while adding less than 10% decoding overhead.
- Stop condition: Stop if real-model age-zscore does not beat the best baseline by at least 5 absolute percentage points on a smoke plus one medium retrieval setting, or if policy bookkeeping overhead exceeds 20%.

## Evidence references

- Artifact root: `<local-path>/projects/z-score-kv-eviction-for-long-context-on-10gb-ec4e626a9663`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
