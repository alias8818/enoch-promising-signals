# Hierarchical Sliding Window Attention for 32K Context on GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-sliding-window-attention-for-32k-context-on-gpt-2-small-baf58a762461`
Run ID: `hierarchical-sliding-window-attention-for-32k-context-on-gpt-2-small-baf58a762461-20260608T235032297512+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6efc1435e55d

## What looked useful

Hierarchical sliding attention can reduce estimated fp16 score memory at 32768 tokens from 24.0 GiB to 0.464 GiB for 12 GPT-2-small heads, but mean summaries lose exact old-token retrieval: hierarchical value cosine was near zero or negative while dense attention achieved 1.0 on synthetic probes.

## Boundaries and scale limits

No trained GPT-2-small model was modified, fine-tuned, or evaluated on language modeling. Dense baseline was capped at 4096 tokens. The sparse implementation is a simple PyTorch block loop, not a custom optimized kernel. GPT-2-small positional embeddings remain 1024 by default.

## Claim scope

Attention-only benchmark for a GPT-2-small-shaped tensor layout on NVIDIA GB10: a simple hierarchical sliding pattern reaches 32768 tokens with much lower score-memory work, but naive mean block summaries fail synthetic exact long-range retrieval and diverge from dense attention by 4096 tokens.

## Why it stopped

Proxy attention-only evidence supports memory feasibility but early-falsifies the naive hierarchical-summary quality mechanism; this is not a full GPT-2-small 32K validation.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is to replace mean summaries with learned or selected landmark summaries and evaluate trained GPT-2-small-class perplexity plus long-range retrieval at 8K-32K.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Landmark Summaries for GPT-2-Small-Class 32K Attention
- Success threshold: At 16K or 32K, recover at least 90% synthetic retrieval accuracy for planted long-range keys and avoid more than 10% perplexity degradation versus the strongest feasible baseline while keeping score-memory work at least 10x below dense attention.
- Stop condition: Stop if trained landmark summaries still produce below 50% long-range retrieval accuracy or more than 20% perplexity degradation at 8K under matched compute.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-sliding-window-attention-for-32k-context-on-gpt-2-small-baf58a762461`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
