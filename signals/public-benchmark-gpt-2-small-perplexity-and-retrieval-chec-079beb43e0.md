# Public benchmark GPT-2-small perplexity and retrieval check for heavy-hitter KV eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `public-benchmark-gpt-2-small-perplexity-and-retrieval-chec-079beb43e0`
Run ID: `public-benchmark-gpt-2-small-perplexity-and-retrieval-chec-079beb43e0-20260524T180855818474+0000`

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

- Parent run decision: Heavy-hitter KV eviction for GPT-2-small CPU: enoch://control-plane/projects/heavy-hitter-kv-eviction-for-gpt-2-small-cpu-03a33bf74a4a/runs/heavy-hitter-kv-eviction-for-gpt-2-small-cpu-03a33bf74a4a-20260524T173407491267+0000
- Parent run decision: GPT-2-small perplexity and retrieval validation for heavy-hitter KV eviction: enoch://control-plane/projects/gpt-2-small-perplexity-and-retrieval-validation-for-heavy-50f0feee0d/runs/gpt-2-small-perplexity-and-retrieval-validation-for-heavy-50f0feee0d-20260524T175331440513+0000

## What looked useful

Heavy-hitter eviction reached WikiText perplexity 27.51 versus full-cache 23.76, while sliding and random controls degraded to 1285.58 and 91.99. Retrieval accuracy was full 0.50, heavy-hitter 0.375, sliding 0.125, random 0.0; heavy-hitter nearly matched full-cache mean answer log probability.

## Boundaries and scale limits

Single model (GPT-2-small), one 512-token WikiText-2 validation slice, one cache budget, one heavy-hitter recent-token reserve, eight synthetic retrieval seeds, CPU-only execution; no larger-model, longer-context, throughput, or multi-corpus validation.

## Claim scope

On GPT-2-small token-by-token inference with a 128-token retained KV cache, cumulative attention heavy-hitter eviction preserved WikiText-2 perplexity and synthetic key-value retrieval behavior much better than sliding-window and seeded-random eviction controls in the tested 512-token/8-seed public benchmark.

## Why it stopped

Tier-2 bounded evidence supports the mechanism but is too narrow for publication readiness.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with a budget/recent-token sweep over longer public GPT-2-small text and at least 32 retrieval seeds before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small heavy-hitter KV eviction budget and retrieval robustness sweep
- Success threshold: At budget 128, heavy-hitter mean NLL delta is at least 50% lower than both sliding and random controls, and retrieval accuracy is no worse than 10 percentage points below full cache while exceeding both eviction controls.
- Stop condition: Stop if heavy-hitter loses to random or sliding on either perplexity delta or retrieval accuracy in two independent slices/seeds groups, or if runtime exceeds the local bounded CPU budget without producing checkpointed metrics.

## Evidence references

- Artifact root: `<local-path>/projects/public-benchmark-gpt-2-small-perplexity-and-retrieval-chec-079beb43e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
