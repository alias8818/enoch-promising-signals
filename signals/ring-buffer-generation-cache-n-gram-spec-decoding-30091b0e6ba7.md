# Ring-Buffer Generation-Cache N-Gram Spec Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ring-buffer-generation-cache-n-gram-spec-decoding-30091b0e6ba7`
Run ID: `ring-buffer-generation-cache-n-gram-spec-decoding-30091b0e6ba7-20260628T092536182715+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e49079f54af2

## What looked useful

GPT-2 medium traces showed 59.3% mean verifier-call reduction for online ring cache versus 23.8% for static prompt cache; Qwen2.5-0.5B check showed 47.9% versus 14.1%. Gains were strongest when generated text entered repetition loops not present in the prompt, while explicitly repetitive prompts were already handled by static prompt n-grams.

## Boundaries and scale limits

Trace-simulated verifier-call reductions only; no integrated KV-cache speculative decoder, no measured end-to-end latency speedup, no sampling-quality study, no batched serving, and no broad non-repetitive benchmark coverage.

## Claim scope

On real greedy traces from cached GPT-2 and Qwen2.5-0.5B models, an online bounded ring-buffer n-gram cache over generated tokens substantially increases accepted n-gram speculative drafts versus a static prompt-only n-gram cache when repetition emerges during generation.

## Why it stopped

Closed as no-paper useful signal because evidence is trace-simulated and repetition-dominated rather than an integrated serving-speed validation.

## Recommended next action

Implement a KV-cache-aware speculative decoder and run a capped latency benchmark on GPT-2 and Qwen2.5-0.5B greedy plus low-temperature prompts; stop if real latency speedup is below 10% or acceptance collapses outside repetition-heavy traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache latency benchmark for ring-buffer n-gram speculation
- Success threshold: At least 10% median end-to-end latency speedup with identical greedy outputs on non-repetitive prompts, plus clear larger gains on repetition-heavy prompts.
- Stop condition: Stop if integrated overhead eliminates speedup, if correctness requires replaying accepted tokens often enough to erase call savings, or if non-repetitive prompt acceptance stays below 20%.

## Evidence references

- Artifact root: `<local-path>/projects/ring-buffer-generation-cache-n-gram-spec-decoding-30091b0e6ba7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
