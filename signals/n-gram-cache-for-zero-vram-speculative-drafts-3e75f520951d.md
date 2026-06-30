# N-gram cache for zero-VRAM speculative drafts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cache-for-zero-vram-speculative-drafts-3e75f520951d`
Run ID: `n-gram-cache-for-zero-vram-speculative-drafts-3e75f520951d-20260613T080441571222+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f2ba7072f820

## What looked useful

The mechanism can save verifier calls with zero draft-model VRAM, but low acceptance means wall-clock speedup requires multi-token verification overhead below roughly 2% to 3% per drafted token or a much more local cache.

## Boundaries and scale limits

Trace-level simulator only; no production tokenizer, no transformer verifier, no GPU wall-clock latency, no sampling/logit effects, and no serving integration. Corpora were small public-domain books/plays with 17,934 to 49,998 evaluated tokens.

## Claim scope

A CPU-resident n-gram continuation cache reduced oracle simulated verifier calls by 7.8% to 12.9% on three held-out public-domain text traces using word/punctuation tokens, but accepted only 2.1% to 3.1% of drafted tokens.

## Why it stopped

No-paper useful signal: proxy trace evidence supports modest verifier-call reduction but not real model/runtime speedup.

## Recommended next action

Run a bounded direct LLM follow-up with a production BPE tokenizer and small local causal-LM verifier; stop if measured greedy-equivalent wall-clock speedup is below 5%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM latency test for zero-VRAM n-gram speculative drafts
- Success threshold: At least 5% wall-clock decode speedup over greedy on 3 or more held-out prompts with identical greedy outputs and no draft-model VRAM allocation.
- Stop condition: Stop as negative if acceptance remains below 5% or wall-clock speedup is below 5% after 3 representative prompt families.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cache-for-zero-vram-speculative-drafts-3e75f520951d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
