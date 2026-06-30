# Segment-Routed Attention for Local Long-Context Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `segment-routed-attention-for-local-long-context-serving-181976552290`
Run ID: `segment-routed-attention-for-local-long-context-serving-181976552290-20260525T065111412064+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4fd1de6819f7

## What looked useful

At 32,768 tokens with 256-token segments and top-8 routed segments, routing read 6.25% of tokens, achieved 0.896 dense top-32 token recall versus 0.037 for a same-budget sliding window, and ran 5.75x faster than dense attention. Under sharper retrieval-style attention at the same length and budget, output cosine to dense attention rose to 0.971 with 5.76x speedup. Diffuse attention remains a weakness: at attention scale 8.0, 32k/top-8 covered only 0.179 dense attention mass and output cosine was 0.694.

## Boundaries and scale limits

Not tested on real LLM KV traces, multi-head/layer distributions, paged KV-cache serving engines, trained-model perplexity, downstream task quality, adversarial contexts, or contexts beyond 32,768 tokens.

## Claim scope

Synthetic clustered long-context KV-cache benchmark on NVIDIA GB10: fixed-size segment routing can recover dense attention's top retrieval tokens with substantially fewer token reads and lower decode-attention latency, especially when attention is retrieval-sparse.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only and mixed: segment routing works for retrieval-sparse attention but is not validated for real LLM serving quality.

## Recommended next action

Run a bounded real-trace replay using an open long-context model's KV/query tensors before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV-Trace Replay for Segment-Routed Attention
- Success threshold: At 32k context, top-32 dense-token recall >= 0.90, output cosine >= 0.95, decode-attention speedup >= 3x versus dense, and clear improvement over same-budget sliding-window attention.
- Stop condition: Stop if real traces show routed output cosine below 0.90 or top-32 recall below 0.85 at token budgets that still provide at least 3x speedup.

## Evidence references

- Artifact root: `<local-path>/projects/segment-routed-attention-for-local-long-context-serving-181976552290`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
