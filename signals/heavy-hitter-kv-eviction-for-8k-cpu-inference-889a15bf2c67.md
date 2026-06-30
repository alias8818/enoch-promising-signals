# Heavy-hitter KV eviction for 8k CPU inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `heavy-hitter-kv-eviction-for-8k-cpu-inference-889a15bf2c67`
Run ID: `heavy-hitter-kv-eviction-for-8k-cpu-inference-889a15bf2c67-20260604T165320947878+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/21130c243385

## What looked useful

At 512/1024/2048 tokens per head, heavy-hitter retained 0.641/0.735/0.850 exact attention mass versus recency at 0.182/0.337/0.561 and reduced mean relative L2 error by 26.5%/36.3%/44.8%. CPU microbenchmarks showed 512/1024/2048 KV attention was 13.7x/12.9x/8.5x faster than 8192 KV attention for the tested dimensions.

## Boundaries and scale limits

Evidence is attention-level and synthetic. It does not validate real language-model perplexity, generation quality, multi-layer error accumulation, tokenizer/prompt effects, or production CPU serving overhead.

## Claim scope

On a synthetic 8k-token CPU attention trace with recurring long-recall anchors, cumulative heavy-hitter KV eviction plus a protected recent window retained more exact attention mass and reduced mean exact-output relative L2 error versus equal-budget recency and random-old baselines; fixed-length CPU attention microbenchmarks showed shorter KV lengths can materially reduce one-token attention time.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic 8k attention probe, but this is not full validation of model quality or production inference speed.

## Recommended next action

Run a bounded real-model follow-up on a small long-context transformer or GPT-2-class model with layerwise heavy-hitter KV eviction, measuring perplexity or next-token KL plus end-to-end CPU decode latency against full KV and sliding-window baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of heavy-hitter KV eviction at 8k context
- Success threshold: At one or more KV budgets no larger than 25% of full 8k KV, heavy-hitter must beat sliding-window latency-adjusted quality, keep mean next-token KL or perplexity delta within a predeclared small bound, and avoid severe worst-case degradation on long-recall examples.
- Stop condition: Stop if heavy-hitter does not improve quality over sliding-window at matched budget, if end-to-end CPU latency is not materially better after accounting for heavy-hitter maintenance, or if worst-case quality failures persist at practical budgets.

## Evidence references

- Artifact root: `<local-path>/projects/heavy-hitter-kv-eviction-for-8k-cpu-inference-889a15bf2c67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
