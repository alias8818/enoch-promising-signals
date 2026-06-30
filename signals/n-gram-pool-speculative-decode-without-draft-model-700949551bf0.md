# N-gram pool speculative decode without draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-pool-speculative-decode-without-draft-model-700949551bf0`
Run ID: `n-gram-pool-speculative-decode-without-draft-model-700949551bf0-20260528T083003391720+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f42090396412

## What looked useful

The mechanism can work when repeated generated text lets the n-gram pool propose multi-token continuations, but exactness depends on cache repair and numerical precision. DynamicCache must be cropped before replay after partial rejection. fp32 was exact in the bounded run; fp16 was not robust.

## Boundaries and scale limits

Small fixed prompt set; GPT-2 small only; greedy argmax only; no sampling correction, batching, long-context serving engine, paged KV cache, or 1B-7B-class model validation. The fp16 serving-like run matched greedy output on only 18/24 prompts, so exact low-precision deployment is not established.

## Claim scope

Bounded local evidence: for GPT-2 small greedy decoding on 24 fixed prompts with 64 generated tokens each, an n-gram history-pool proposer plus target-model verification preserved exact fp32 greedy output and reduced average decode calls from 64.0 to 42.8, with 1.58x wall-clock speedup in this Hugging Face implementation.

## Why it stopped

Bounded fp32 evidence supports the mechanism, but fp16 exactness failure and small-scale prompt/model coverage prevent a paper-positive or broad deployment claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a precision-robust verifier study that targets 100% fp16 exactness before any larger-model scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Precision-robust n-gram pool verification for exact low-precision greedy decoding
- Success threshold: 100% token-level exact match against fp16 greedy baseline on the evaluated prompt corpus, with average decode-call ratio <= 0.75 and no wall-clock slowdown versus baseline.
- Stop condition: Stop if exactness remains below 99.9% after adding margin gating or selective fp32 verification, or if the method requires so many fallback/recompute calls that decode-call ratio is >= 0.9.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-pool-speculative-decode-without-draft-model-700949551bf0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
