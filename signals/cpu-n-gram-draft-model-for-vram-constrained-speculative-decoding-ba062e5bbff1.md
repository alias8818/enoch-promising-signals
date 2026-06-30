# CPU N-Gram Draft Model for VRAM-Constrained Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-model-for-vram-constrained-speculative-decoding-ba062e5bbff1`
Run ID: `cpu-n-gram-draft-model-for-vram-constrained-speculative-decoding-ba062e5bbff1-20260604T095926608470+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3e23ef2ea36a

## What looked useful

CPU n-gram drafting is cheap enough to test further, but in 512-context GPT-2 runs roughly 64-69% of iterations rejected the first token, K=4 full-draft acceptance stayed below 1%, and order 1 beat higher-order tables on mean accepted length.

## Boundaries and scale limits

Small corpus, GPT-2-small-class verifier, greedy-token agreement metric, and full-prefix latency proxy rather than a production KV-cache speculative decoder or large VRAM-constrained serving workload.

## Claim scope

On tinyshakespeare with a GPT-2 verifier, a CPU n-gram draft table has negligible proposal latency and nonzero greedy-token agreement, but accepted runs are short and higher-order n-grams do not outperform unigram proposals.

## Why it stopped

Proxy evidence is mixed: CPU overhead is negligible, but acceptance is weak and the measured speedup is not an end-to-end speculative decoding validation.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should implement true KV-cache speculative decoding and require at least 1.15x end-to-end tokens/sec with unchanged target VRAM pressure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-Cache End-to-End Test for CPU N-Gram Speculative Decoding
- Success threshold: At least 1.15x median tokens/sec over no-draft baseline with first-token match above 35% and no increase in target model VRAM allocation.
- Stop condition: Stop if end-to-end speedup is below 1.05x or if unigram remains equal or better than higher-order tables across both domains.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-model-for-vram-constrained-speculative-decoding-ba062e5bbff1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
