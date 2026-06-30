# Sparse-Evict KV Cache for 128k Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-evict-kv-cache-for-128k-local-inference-c12ff9d6951a`
Run ID: `sparse-evict-kv-cache-for-128k-local-inference-c12ff9d6951a-20260607T174003715656+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/95be05aca633

## What looked useful

Across three 128k synthetic proxy seeds, sparse eviction retained 6.25% of tokens and achieved mean recall@1 0.5208 on recurring old-token queries, versus 0.0000 for sliding-window and 0.0208 for random old-token retention. Dense was 1.0000 and an oracle hot-needle ceiling was 0.8229.

## Boundaries and scale limits

The completed 128k proxy used 4 heads x 96 dim with 64 warmup and 128 test queries over three seeds. The originally targeted 8 heads x 128 dim shape terminated with exit 143 before metrics. No real transformer, perplexity, generation quality, multi-layer stack, or 7B-class inference engine was evaluated.

## Claim scope

In a synthetic 128k GPU-resident KV benchmark with recurring planted old-token references after warmup/prefill salience, a local-window plus sparse salience-retained cache recovered substantially more old-token recall than sliding-window or random retention at the same 6.25% retained-token ratio.

## Why it stopped

Closed as no-paper useful signal: evidence is synthetic/proxy-only and the full intended 8-head/128-dim benchmark shape did not complete, so it cannot support a publication-grade local 128k inference claim.

## Recommended next action

Run a bounded real-model follow-up using a small transformer or cached attention traces to test whether salience-retained sparse KV preserves retrieval-task accuracy or perplexity at similar retained ratios.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Sparse KV Retention at 128k Proxy Scale
- Success threshold: At 6.25% to 12.5% retained-token ratio, sparse eviction improves retrieval accuracy or perplexity degradation by at least 2x over random retention and materially over sliding-window, while remaining within 20% of the dense-control task metric on recurring-reference cases.
- Stop condition: Stop if sparse eviction is not materially better than random retention on real-model metrics, or if gains only appear in oracle/synthetic salience conditions that are unavailable during real inference.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-evict-kv-cache-for-128k-local-inference-c12ff9d6951a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
