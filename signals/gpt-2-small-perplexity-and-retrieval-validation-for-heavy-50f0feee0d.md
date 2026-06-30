# GPT-2-small perplexity and retrieval validation for heavy-hitter KV eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-perplexity-and-retrieval-validation-for-heavy-50f0feee0d`
Run ID: `gpt-2-small-perplexity-and-retrieval-validation-for-heavy-50f0feee0d-20260524T175331440513+0000`

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
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0e85bfeb5280

## What looked useful

At budget 16, heavy-hitter text ppl was 120.38 versus full 120.21 and sliding 424.98; retrieval answer NLL was 3.246 versus full 0.237 and sliding 13.438. At budget 8, heavy-hitter text ppl was 159.29 versus sliding 2683.63; retrieval answer NLL was 9.543 versus sliding 15.610.

## Boundaries and scale limits

Four embedded prose snippets, four synthetic retrieval prompts, 85 text target tokens, 179 retrieval target tokens, five retrieval answer tokens, budgets 8 and 16 only; no public benchmark scale, optimized serving integration, larger model, or long-context robustness.

## Claim scope

Small direct GPT-2-small CPU validation showed cumulative-attention heavy-hitter KV eviction outperformed sliding-window eviction at equal KV-token budgets on sequential fallback-text perplexity and synthetic retrieval answer likelihood.

## Why it stopped

Tier 1 direct validation produced a useful mechanism signal but remains too small and partly synthetic for publication-grade evidence.

## Recommended next action

Run a bounded public-benchmark deepen follow-up on WikiText or LAMBADA-style retrieval with at least hundreds of target tokens and the same full/sliding/heavy-hitter controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public benchmark GPT-2-small perplexity and retrieval check for heavy-hitter KV eviction
- Success threshold: Heavy-hitter beats sliding by at least 25% relative NLL increase reduction versus full cache on corpus perplexity and retrieval answer NLL at two equal KV budgets, without a large regression on top-1 target rate.
- Stop condition: Stop if heavy-hitter fails to beat sliding on either corpus NLL or retrieval answer NLL at both tested budgets, or if public dataset/runtime constraints prevent a valid direct test within the allocated budget.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-perplexity-and-retrieval-validation-for-heavy-50f0feee0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
