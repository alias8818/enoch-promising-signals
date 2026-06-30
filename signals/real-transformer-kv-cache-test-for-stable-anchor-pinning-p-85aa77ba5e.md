# Real-Transformer KV Cache Test for Stable Anchor Pinning plus Tail Summaries

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-transformer-kv-cache-test-for-stable-anchor-pinning-p-85aa77ba5e`
Run ID: `real-transformer-kv-cache-test-for-stable-anchor-pinning-p-85aa77ba5e-20260629T234623619478+0000`

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

- Parent run decision: Stable-Anchor KV Eviction: Pin Exact-Reference Tokens, Compress the Tail: enoch://control-plane/projects/stable-anchor-kv-eviction-pin-exact-reference-tokens-compress-the-tail-5319cf089497/runs/stable-anchor-kv-eviction-pin-exact-reference-tokens-compress-the-tail-5319cf089497-20260629T232609164757+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/889938e71ba1

## What looked useful

Anchor+tail KV reduced mean KL from full context versus tail-only KV by 4.50 to 4.79 nats across 64/96/128 retained-token budgets, with target-token logprob gains of 8.75 to 11.25. Full-cache replay control stayed near exact with mean KL 0.000165 and full top-k overlap.

## Boundaries and scale limits

One small pretrained decoder model, synthetic prompts, one-step next-token metrics, fp16 inference, no learned or generated hidden-state summaries, no multi-token generation quality, no production serving throughput, and no modern Llama/RoPE-class model validation.

## Claim scope

On 12 synthetic but natural prompts using distilgpt2 fp16 inference, retaining stable early anchor KVs plus recent tail KVs under 64, 96, and 128 token KV budgets preserved full-context next-token distributions substantially better than same-budget tail-only KV retention. A compact text anchor+summary+tail prompt also improved over tail-only text, but this is a text-level proxy rather than hidden-state summary KV evidence.

## Why it stopped

No-paper useful signal: the local direct KV experiment supports stable anchor pinning under small synthetic conditions, but the summary portion is proxied at text level and the evidence is not broad or direct enough for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on GPT-2-small-class or small Llama/RoPE-class models with natural long-context prompts, generated summaries, multi-token continuation metrics, and latency/memory measurements before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-model validation of anchor-pinned KV plus generated summaries
- Success threshold: Anchor+tail or anchor+summary+tail must reduce KL or improve target retrieval by at least 25% versus tail-only at equal memory on two model families, while keeping latency overhead below 15% versus tail-only compressed inference.
- Stop condition: Stop if anchor-pinned variants fail to beat tail-only on natural prompts in either model family, or if generated summaries erase the distributional advantage after equal-budget controls.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-kv-cache-test-for-stable-anchor-pinning-p-85aa77ba5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
