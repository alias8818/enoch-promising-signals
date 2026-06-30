# Heavy-hitter KV eviction for GPT-2-small CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `heavy-hitter-kv-eviction-for-gpt-2-small-cpu-03a33bf74a4a`
Run ID: `heavy-hitter-kv-eviction-for-gpt-2-small-cpu-03a33bf74a4a-20260524T173407491267+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0e85bfeb5280

## What looked useful

On real GPT-2-small past_key_values eviction, heavy-hitter reduced mean KL versus full cache to 17.8% of sliding at budget 8 and 10.3% of sliding at budget 16; top-1 agreement improved from 6.8% to 50.5% at budget 8 and from 12.0% to 69.3% at budget 16.

## Boundaries and scale limits

No corpus perplexity, downstream task accuracy, optimized serving runtime, long-context benchmark, larger model, or production memory-pressure validation was run. The prompt set is small and hand-written, so this is mechanism evidence only.

## Claim scope

Bounded GPT-2-small CPU probe: cumulative-attention heavy-hitter KV eviction with a recent-token reserve preserved full-cache next-token logits better than sliding-window eviction at equal tiny cache budgets of 8 and 16 retained positions across 8 short prompts and 24 teacher-forced decode steps per prompt.

## Why it stopped

Closed as a no-paper useful signal: the mechanism is supported locally, but evidence is too small and proxy-like for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up measuring GPT-2-small corpus perplexity and long-context retrieval accuracy with full-cache, sliding-window, and heavy-hitter controls before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small perplexity and retrieval validation for heavy-hitter KV eviction
- Success threshold: At matched KV budgets, heavy-hitter should reduce perplexity degradation versus sliding by at least 30% and improve retrieval accuracy without more than 10% end-to-end CPU latency regression.
- Stop condition: Stop if heavy-hitter fails to beat sliding on both perplexity degradation and retrieval accuracy at two or more practical budgets, or if cache-maintenance overhead erases the CPU memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/heavy-hitter-kv-eviction-for-gpt-2-small-cpu-03a33bf74a4a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
