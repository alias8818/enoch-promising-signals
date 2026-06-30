# Frozen 1-layer medusa head for local draft

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `frozen-1-layer-medusa-head-for-local-draft-140fb50ba046`
Run ID: `frozen-1-layer-medusa-head-for-local-draft-140fb50ba046-20260528T084043150177+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f42090396412

## What looked useful

Across three seeds, one-layer Medusa heads averaged 2.412 consecutive accepted local draft tokens versus 1.015 for linear controls, with 0.439 exact 4-token matches versus 0.019 for the linear control.

## Boundaries and scale limits

Synthetic data, tiny model, exact-match proxy metric only; no pretrained LLM, natural-language corpus, target-verifier speculative decoding, latency, or wall-clock throughput validation.

## Claim scope

On a controlled synthetic language with a tiny 2-layer transformer base LM, a frozen-base one-hidden-layer Medusa head trained for offsets 1..4 produces substantially longer exact-match local drafts than a linear frozen-hidden control.

## Why it stopped

No-paper useful signal: the toy mechanism is supported, but this run is synthetic/proxy evidence and does not validate real LLM speculative decoding.

## Recommended next action

Run a bounded GPT-2-small-class follow-up on a real text corpus with the base frozen, comparing one-layer Medusa, linear head, and autoregressive draft baselines using verifier acceptance and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen one-layer Medusa head on GPT-2-small natural text
- Success threshold: Mean verifier-accepted draft length improves by at least 0.25 tokens over the linear head and yields measurable decode latency reduction versus autoregressive local drafting on held-out natural text.
- Stop condition: Stop as negative if the one-layer head fails to beat the linear head by 0.25 accepted tokens or if latency overhead erases speculative decoding speedup.

## Evidence references

- Artifact root: `<local-path>/projects/frozen-1-layer-medusa-head-for-local-draft-140fb50ba046`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
