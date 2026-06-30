# Host-RAM N-gram Cache for Zero-VRAM Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `host-ram-n-gram-cache-for-zero-vram-speculative-decoding-c9c92ea9e9a6`
Run ID: `host-ram-n-gram-cache-for-zero-vram-speculative-decoding-c9c92ea9e9a6-20260604T125051968580+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4b3dd5e2c185

## What looked useful

Across five-window evaluations, repeated synthetic corpora accepted 4.48 to 4.64 draft tokens per evaluated token with sub-microsecond p95 lookup latency, while natural prose accepted only 0.09 to 0.22 tokens per evaluated token and the low-repeat control accepted zero.

## Boundaries and scale limits

No neural verifier, no GPU decoder integration, no tokenizer/model-specific acceptance, no batching or KV-cache interaction, and no end-to-end wall-clock generation speedup were measured. Python memory layout is not a production cache estimate.

## Claim scope

Bounded exact-token proxy over sampled public-domain prose and synthetic controls: a dynamic host-RAM n-gram cache can produce useful draft tokens for repetition-heavy contexts, but shows weak general natural-prose acceptance.

## Why it stopped

This run produced a proxy/mechanism useful signal but not direct publication-grade evidence for zero-VRAM speculative decoding.

## Recommended next action

Run a bounded real-decoder follow-up that integrates host-RAM n-gram prompt lookup with a small model verifier and measures end-to-end tokens/s on repeated-context prompts and natural prose controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-decoder host-RAM n-gram speculative lookup on repeated-context prompts
- Success threshold: At least 10% end-to-end tokens/s improvement on repeated-context prompts, accepted draft tokens per verifier call above 1.0, and natural-prose slowdown no worse than 3%.
- Stop condition: Stop if repeated-context speedup is below 5% or natural-prose slowdown exceeds 5% after a correct real-decoder implementation and smoke validation.

## Evidence references

- Artifact root: `<local-path>/projects/host-ram-n-gram-cache-for-zero-vram-speculative-decoding-c9c92ea9e9a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
