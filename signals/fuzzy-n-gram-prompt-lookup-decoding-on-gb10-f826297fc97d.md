# Fuzzy N-Gram Prompt Lookup Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fuzzy-n-gram-prompt-lookup-decoding-on-gb10-f826297fc97d`
Run ID: `fuzzy-n-gram-prompt-lookup-decoding-on-gb10-f826297fc97d-20260608T225003420472+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/767958d5e25e

## What looked useful

At 12.5% key noise in the favorable recent-source scenario, fuzzy lookup improved first-token candidate accuracy from 0.344 to 0.772 and mean accepted span from 5.50 to 12.35 tokens. In controls, fuzzy false-candidate rates were high: 0.312 to 0.641 when the true source was older than distractors and 0.320 to 0.643 when no valid source existed.

## Boundaries and scale limits

216,000 synthetic trials with a naive CPU-side lookup implementation plus GB10 CUDA smoke telemetry; no model-integrated speculative decoding, no real corpus workload, no optimized GPU kernel, and no 7B+ serving benchmark.

## Claim scope

Synthetic copy-style prompt lookup trials show fuzzy n-gram matching can recover noisy repeated continuations when the correct source span is the most recent best near-match, but ungated fuzzy lookup has high false-candidate rates in older-source and absent-source controls.

## Why it stopped

Bounded synthetic evidence supports the mechanism but also shows high false-positive risk for ungated fuzzy lookup, so this is not a paper-ready positive result.

## Recommended next action

Stop this run as no-paper useful signal; next run should test a verifier-aware fuzzy lookup gate on real long-context copy/edit prompts and report accepted tokens per verifier step versus exact prompt lookup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-Gated Fuzzy Prompt Lookup on Real Long-Context Copy Tasks
- Success threshold: Confidence-gated fuzzy lookup improves accepted tokens per verifier step by at least 15% over exact prompt lookup while keeping wrong-candidate verifier steps under 10% on the evaluated workload.
- Stop condition: Stop if gated fuzzy lookup cannot reduce wrong-candidate verifier steps below 20% or if accepted tokens per verifier step is not better than exact lookup on two independent prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/fuzzy-n-gram-prompt-lookup-decoding-on-gb10-f826297fc97d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
