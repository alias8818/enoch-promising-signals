# CPU N-Gram Cache Speculative Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-n-gram-cache-speculative-drafting-1c10ec21d00c`
Run ID: `cpu-n-gram-cache-speculative-drafting-1c10ec21d00c-20260603T212913746032+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/287d448b6e23

## What looked useful

Best natural-language configurations used order 3 and max draft 16, giving 1.87x-2.07x ideal target-call speedup and 46.5%-51.7% target-call reduction. Synthetic repetitive text reached 13.78x, while random ASCII stayed at 1.00x, indicating a real but distribution-dependent mechanism.

## Boundaries and scale limits

This run did not use a real LLM target, tokenizer, GPU verification kernel, KV cache, batching, or end-to-end serving path. Cache memory is a Python-object approximation, not a packed implementation measurement. The claim is limited to 20k-token prompts and 50k-token held-out byte traces.

## Claim scope

A bounded byte-token trace benchmark shows that an online CPU n-gram continuation cache can reduce modeled target verification calls by about half on three natural-language Project Gutenberg traces, with no meaningful gain on a random ASCII control and large gains on a repetitive control.

## Why it stopped

Proxy trace evidence supports the mechanism but is not full validation because it does not include real LLM logits, tokenizer effects, GPU/CPU overlap, or serving latency.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should integrate the same CPU n-gram drafter with a small real autoregressive model and measure end-to-end latency, acceptance, and quality against a no-draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model CPU N-Gram Speculative Drafting Latency Probe
- Success threshold: At least 20% end-to-end tokens/s improvement over no-draft on a repetitive-prompt suite, no regression on non-repetitive prompts beyond 5%, and greedy outputs identical to the target baseline when using deterministic verification.
- Stop condition: Stop if CPU lookup plus verification overhead eliminates modeled target-call savings or if acceptance on real tokenized prompts is below 10% across the repetitive suite.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-cache-speculative-drafting-1c10ec21d00c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
