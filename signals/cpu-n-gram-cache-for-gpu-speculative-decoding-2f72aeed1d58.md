# CPU N-Gram Cache for GPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-cache-for-gpu-speculative-decoding-2f72aeed1d58`
Run ID: `cpu-n-gram-cache-for-gpu-speculative-decoding-2f72aeed1d58-20260604T055113685497+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae31537fae7b

## What looked useful

CPU n-gram lookups were fast enough in Python, roughly 2.3M to 6.4M positions/s, and positive controls showed the mechanism can work on repeated contexts. Natural text acceptance was small: best Tiny Shakespeare configuration was n=2, draft=2, hit_rate=0.6276, nonzero_accept_rate=0.0745, mean_accepted_tokens=0.0902, proxy speedup=1.0902x. Shuffled text dropped to 1.0162x and IID random to 1.0000x.

## Boundaries and scale limits

No real GPU target model, no end-to-end speculative decoding loop, no CPU/GPU synchronization cost, no batching effects, no production prompt distribution, and only a small public text corpus plus synthetic controls. The result is a mechanism/proxy signal, not a serving validation.

## Claim scope

A single-process CPU exact n-gram continuation cache was evaluated as a proxy draft generator on 220k-token Tiny Shakespeare, shuffled text, IID random, periodic, and Markov-reuse token streams. The cache is computationally cheap and can produce large accepted drafts on repetition-heavy streams, but chronological natural text only reached 1.090x proxy verifier-call speedup with 0.090 mean accepted tokens.

## Why it stopped

Proxy-only useful signal is not paper-ready: natural-text acceptance is small before real GPU serving overheads, although repetition-heavy controls support the mechanism.

## Recommended next action

Run one bounded deepen test by integrating this cache into a small GPU LLM speculative decoding loop and require at least 5% end-to-end tokens/s improvement over no-draft on fixed realistic prompts; otherwise stop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-LLM speculative decoding with CPU n-gram drafts
- Success threshold: At least 5% end-to-end tokens/s improvement over no-draft baseline with mean accepted tokens >= 0.15 and no regression on low-repetition controls beyond 2%.
- Stop condition: Stop if mean accepted tokens remains below 0.15 on realistic prompts or if CPU/GPU orchestration overhead erases the proxy speedup.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-cache-for-gpu-speculative-decoding-2f72aeed1d58`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
