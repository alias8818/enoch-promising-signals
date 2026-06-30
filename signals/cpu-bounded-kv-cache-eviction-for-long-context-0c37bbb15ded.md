# CPU-bounded KV cache eviction for long context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-bounded-kv-cache-eviction-for-long-context-0c37bbb15ded`
Run ID: `cpu-bounded-kv-cache-eviction-for-long-context-0c37bbb15ded-20260609T053401148948+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ef43d9e2fcdf

## What looked useful

The stress run showed the clearest failure mode: with a 256-token cache and one CPU page fetch per step, lru_window reached 0.8056569085 macro mean served mass, while cpu_page_greedy reached 0.7000228402 and cpu_page_greedy_no_sink reached 0.7598155396. The page-aware rule wasted scarce cache on low-value page neighbors; CPU cost awareness alone was not enough.

## Boundaries and scale limits

No real LLM was run; attention traces are synthetic; no downstream accuracy, perplexity, GPU kernel, transfer-overlap, multi-layer/head, compression, or production serving measurements were collected.

## Claim scope

In a reproducible CPU-only trace/cost simulator with four synthetic long-context access patterns, uniform 16-token KV pages, fixed CPU page-fetch budgets, and GPU caches of 256 or 1024 tokens, a naive CPU page-benefit/byte greedy eviction rule did not outperform recent-window or attention-heavy-hitter baselines on served attention mass.

## Why it stopped

Proxy/trace-cost early falsification: the tested CPU page-greedy mechanism failed under the discriminating stress regime, but full validation would require real model traces and downstream quality measurements.

## Recommended next action

Stop this no-paper naive page-greedy line; the next bounded action is to replay real small-model attention traces and test a recency-aware CPU admission policy against the same baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay real attention traces for recency-aware CPU KV admission
- Success threshold: Recency-aware CPU admission improves macro mean served attention mass by at least 2 percentage points over lru_window at equal CPU bytes on real traces, with no worse downstream proxy quality.
- Stop condition: Stop if real-trace replay shows less than 1 percentage point served-mass improvement over lru_window or any downstream proxy quality regression at equal CPU bytes.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bounded-kv-cache-eviction-for-long-context-0c37bbb15ded`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
