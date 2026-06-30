# N-Gram Statistical Drafting with KV-Cache Window

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-statistical-drafting-with-kv-cache-window-1d66be146fbc`
Run ID: `n-gram-statistical-drafting-with-kv-cache-window-1d66be146fbc-20260629T171047581398+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/101a628c8c88

## What looked useful

Low-order local n-grams, especially order 2 with 4-token drafts, produced modest target-call reductions that increased with context window size and plateaued near 4k-8k tokens; higher-order n-grams had too little coverage to win.

## Boundaries and scale limits

Proxy only: no real LLM target logits, no model tokenizer, no GPU latency, no batching, no real KV-cache serving path, and the calibrated sweep timed out after 57 of 64 configurations.

## Claim scope

On an 8,000-token Tiny Shakespeare proxy with regex tokenization, a window-local n-gram drafter reduced deterministic target-continuation verification calls by up to 12.16% under speculative-decoding accounting.

## Why it stopped

No-paper useful signal: proxy supports the mechanism but does not provide direct model-serving evidence or publication-grade validation.

## Recommended next action

Run a bounded real-model deepen test with a GPT-2-small-class target, tokenizer-matched n-gram drafter, KV-cache decoding, and end-to-end latency versus no-drafter baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-Matched N-Gram Drafting Against a Real KV-Cached Small LM
- Success threshold: At least 5% end-to-end tokens/second improvement over no-drafter baseline with no output mismatch and documented drafter overhead.
- Stop condition: Stop if accepted drafts do not produce at least 2% target-call reduction or if drafter CPU overhead erases measured latency gains on the first corpus.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-statistical-drafting-with-kv-cache-window-1d66be146fbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
