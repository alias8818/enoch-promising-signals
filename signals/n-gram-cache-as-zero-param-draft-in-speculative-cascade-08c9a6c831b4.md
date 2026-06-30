# N-Gram Cache as Zero-Param Draft in Speculative Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cache-as-zero-param-draft-in-speculative-cascade-08c9a6c831b4`
Run ID: `n-gram-cache-as-zero-param-draft-in-speculative-cascade-08c9a6c831b4-20260525T231621418079+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/74ed5f3bb060

## What looked useful

Prompt-local n-gram cache drafts are mostly ineffective for non-repeated Wikitext prose but show niche usefulness on repetitive local Python code prompts; even there, simple zero-parameter bigram successor baselines often match or beat accepted-prefix length.

## Boundaries and scale limits

No optimized serving implementation, no 7B+ verifier, no production KV-cache timing, no broad benchmark suite, and stochastic speculative acceptance is represented only by target probability proxies.

## Claim scope

Bounded local evaluation of prompt-local n-gram suffix-copy drafts verified by distilgpt2 on Wikitext prose and installed Python source prompts at 384 and 768 tokens.

## Why it stopped

Proxy/direct bounded verifier evidence is an early falsification of the general n-gram-cache draft claim, not a full production-scale validation.

## Recommended next action

Stop this broad claim as no-paper; if continuing, run a bounded code-only serving benchmark with cache-hit confidence gating against no-draft and bigram controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gated n-gram cache drafts for repetitive code decoding
- Success threshold: At least 15% tokens/sec improvement or verifier-forward reduction over both no-draft and bigram controls on code prompts, with no exactness or quality regression.
- Stop condition: Stop if gated n-gram fails to beat bigram and no-draft controls by 5% on a 100+ prompt code benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cache-as-zero-param-draft-in-speculative-cascade-08c9a6c831b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
