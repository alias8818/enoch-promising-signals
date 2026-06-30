# KV-Cache Compression via Cross-Layer Attention Sinks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-compression-via-cross-layer-attention-sinks-5313eef5075b`
Run ID: `kv-cache-compression-via-cross-layer-attention-sinks-5313eef5075b-20260526T035032162235+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/db0fa7a5e0de

## What looked useful

At the same 30.5% causal-attention-entry budget, sink+recent had mean loss 4.403 and KL 0.435 vs full attention, while recent-only had mean loss 8.382 and KL 4.416. Sink+recent beat recent-only on 48/48 samples and retained 0.860 of full-attention mass vs 0.534 for recent-only.

## Boundaries and scale limits

This is a bounded proxy on one GPT-2-small-class model and short contexts. It does not implement physical KV-cache eviction during incremental decoding, does not measure serving latency or memory bandwidth, and does not validate modern long-context LLMs, larger models, multi-query/grouped-query attention, or post-compression fine-tuning.

## Claim scope

On GPT-2 small with 48 WikiText-2 test samples at sequence length 192, simulating KV-cache pruning via 4D attention masks, retaining 4 initial sink tokens plus a 28-token recent window preserved next-token behavior far better than a same-budget recent-only window and nearly matched an oracle high-attention-token diagnostic.

## Why it stopped

No-paper useful signal from a proxy attention-mask experiment; the local mechanism is supported, but full validation requires direct KV-cache decoding and broader model/context evidence.

## Recommended next action

Run a bounded direct incremental-decoding follow-up that implements actual KV-cache eviction and compares fixed sink+recent, measured cross-layer sink selection, stride+recent, and recent-only on longer prompts with quality plus latency/memory metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Incremental KV Eviction Test for Sink-Token Retention
- Success threshold: At matched KV budget, measured or fixed sink+recent should improve mean KL vs full-cache decoding by at least 25% over both recent-only and stride+recent while showing an actual KV-memory reduction and no decode-throughput regression larger than 10%.
- Stop condition: Stop if actual KV eviction removes the proxy advantage, if stride+recent matches sink selection within 5% KL across tested budgets, or if eviction overhead erases the memory/throughput benefit.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-via-cross-layer-attention-sinks-5313eef5075b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
