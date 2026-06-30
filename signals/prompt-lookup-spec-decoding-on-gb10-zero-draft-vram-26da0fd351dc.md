# Prompt-Lookup Spec Decoding on GB10 (Zero Draft VRAM)

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-lookup-spec-decoding-on-gb10-zero-draft-vram-26da0fd351dc`
Run ID: `prompt-lookup-spec-decoding-on-gb10-zero-draft-vram-26da0fd351dc-20260629T163001921692+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8432b9a0e5b0

## What looked useful

Prompt lookup can produce high acceptance and large target-forward reductions when the model copies repeated prompt spans, with zero draft-model VRAM; the benefit disappears on low-repeat prompts.

## Boundaries and scale limits

Evidence is limited to one small model, synthetic prompts, 64 generated tokens, greedy decoding, and a full-context verification proxy rather than a production KV-cache rollback serving implementation.

## Claim scope

On a GB10 worker using distilgpt2, exact greedy prompt-lookup speculative decoding with no draft model reduced target-model forward calls by 68.8% to 85.9% on a synthetic copy-heavy prompt while preserving exact greedy output; a low-repeat prompt showed no benefit.

## Why it stopped

Useful bounded signal only; this worker run used synthetic/proxy evidence and is not a full validation.

## Recommended next action

Run a direct KV-cache serving benchmark on real copy-heavy RAG or document-edit prompts before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache prompt-lookup decoding benchmark on real copy-heavy workloads
- Success threshold: At least 25% median end-to-end latency reduction on copy-heavy real prompts with exact greedy output match and less than 5% regression on low-repeat controls.
- Stop condition: Stop if KV-cache overhead or mismatch repair removes the latency gain, or if real workloads produce less than 10% accepted prompt-lookup draft tokens.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-spec-decoding-on-gb10-zero-draft-vram-26da0fd351dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
