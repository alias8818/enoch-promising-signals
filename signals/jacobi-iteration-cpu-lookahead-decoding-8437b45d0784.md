# Jacobi iteration CPU lookahead decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `jacobi-iteration-cpu-lookahead-decoding-8437b45d0784`
Run ID: `jacobi-iteration-cpu-lookahead-decoding-8437b45d0784-20260605T013704253438+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/08462091ff1f

## What looked useful

The CPU lookahead mechanism is draft-quality limited. Naive drafts accepted only about one token per Jacobi call and had 0.058x-0.290x median speedup, while half-oracle/oracle drafts reached up to 1.865x/3.390x median speedup with exact greedy matches.

## Boundaries and scale limits

Synthetic bigram and two-step causal models only; no transformer attention, KV cache, tokenizer, learned draft model, or production LLM serving path was tested.

## Claim scope

On self-contained NumPy causal CPU proxies, Jacobi lookahead exactly matches greedy decoding but is slower than greedy with naive constant or random drafts; it becomes faster only when the initial block is substantially correct.

## Why it stopped

Proxy early falsification of naive CPU Jacobi lookahead speedup: without a strong draft, the method falls back to one-token progress plus overhead; this is not full LLM validation.

## Recommended next action

Stop this run as a bounded proxy result; next, run the same exact-match and latency accounting on a tiny real causal transformer with a realistic draft source.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer CPU Jacobi Lookahead With Realistic Drafts
- Success threshold: Draft-assisted Jacobi achieves at least 1.2x median latency speedup over greedy at exact-match rate 1.0, while naive Jacobi remains at or below one accepted token per call.
- Stop condition: Stop if no realistic draft condition exceeds 1.0x median speedup with exact greedy matching, or if framework/runtime installation prevents a real transformer CPU benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/jacobi-iteration-cpu-lookahead-decoding-8437b45d0784`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
