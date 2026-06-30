# Context-Aware N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `context-aware-n-gram-speculative-decoding-cfd239152dc8`
Run ID: `context-aware-n-gram-speculative-decoding-cfd239152dc8-20260526T020851382698+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d456810f23e

## What looked useful

Context routing improved accepted draft length by 36.25% on ambiguous context-switching streams and 46.88% on unambiguous switching streams, nearly matching oracle context labels; it gave no gain on random control or unlabeled natural prompt text, and naive recent-window adaptation was worse than global.

## Boundaries and scale limits

No neural target model, no GPU serving path, no latency/token measurement, no KV-cache measurement, synthetic context markers dominate the positive result, and natural text was limited to local prompt files where context routing had no benefit.

## Claim scope

In a deterministic CPU proxy with held-out token streams, marker-routed context-aware 3-gram drafting increased mean exact accepted draft tokens versus a global 3-gram baseline on controlled context-switching synthetic streams.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a proxy simulation, not full model-serving validation.

## Recommended next action

Run a bounded direct serving follow-up with a small real target LM to measure verifier calls/token and latency/token for global n-gram versus marker/context-routed n-gram drafting on natural corpora with inferred contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM serving test for context-routed n-gram speculative decoding
- Success threshold: Context-routed drafting must improve accepted tokens per verifier call by at least 15% and end-to-end latency per token by at least 5% over global n-gram on natural text, with no quality regression in exact target-model outputs under deterministic decoding.
- Stop condition: Stop if context routing improves accepted-token proxy metrics but fails to improve end-to-end latency, or if routing overhead exceeds the saved verifier work.

## Evidence references

- Artifact root: `<local-path>/projects/context-aware-n-gram-speculative-decoding-cfd239152dc8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
