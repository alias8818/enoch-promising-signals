# Heavy-Hitter KV Eviction for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heavy-hitter-kv-eviction-for-cpu-long-context-b37bdac5d856`
Run ID: `heavy-hitter-kv-eviction-for-cpu-long-context-b37bdac5d856-20260527T143950865505+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5f787d423580

## What looked useful

Heavy-hitter retention preserved old salient anchors that recency always evicted and improved lower-tail cosine-to-full at budgets 512 and 1024, while bounded KV attention remained much faster than full attention. The mechanism is mixed because random retention beat heavy-hitter mean cosine at budget 256 and heavy-hitter had substantial selection overhead versus pure recency.

## Boundaries and scale limits

No real LLM, tokenizer, multi-layer/multi-head model, production KV implementation, perplexity, or downstream long-context benchmark was tested; context lengths and dimensions are proxy scale only.

## Claim scope

Synthetic CPU decode-attention benchmark with old-anchor long-context traces: heavy-hitter KV eviction was compared with recent-window and random bounded caches at 4096 tokens for quality and 8192 tokens for runtime.

## Why it stopped

Proxy evidence supports a mechanism but is not direct/full validation of heavy-hitter KV eviction for real CPU long-context LLM inference.

## Recommended next action

Stop this run as no-paper useful signal; next run should instrument a small real decoder model with the same policies and require quality retention plus end-to-end CPU speed/memory gains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU KV eviction validation on a small decoder
- Success threshold: At matched KV budget, heavy-hitter improves retrieval accuracy or perplexity degradation by at least 10% relative to recency-only while retaining at least 2x CPU tokens/s or memory advantage over full KV.
- Stop condition: Stop if heavy-hitter fails to beat recency on real-model quality at two budget points, or if policy overhead removes the practical CPU advantage versus full KV.

## Evidence references

- Artifact root: `<local-path>/projects/heavy-hitter-kv-eviction-for-cpu-long-context-b37bdac5d856`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
