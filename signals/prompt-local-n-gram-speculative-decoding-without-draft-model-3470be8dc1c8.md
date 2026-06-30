# Prompt-Local N-gram Speculative Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-local-n-gram-speculative-decoding-without-draft-model-3470be8dc1c8`
Run ID: `prompt-local-n-gram-speculative-decoding-without-draft-model-3470be8dc1c8-20260529T164121072698+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/35d2c96c8efa

## What looked useful

Prompt-local n-gram drafts accepted 128-133 of 288 generated tokens on copy-biased prompts and 169-182 of 576 tokens on WikiText, with 0 exact-output mismatches and 28-45% fewer target calls. History-local WikiText accepted 320 of 576 tokens and cut calls by 54%.

## Boundaries and scale limits

Simple full-context PyTorch verifier only; no KV-cache-aware serving engine, no sampling-mode verification, no 7B-class or instruction-tuned model, and only small local prompt suites.

## Claim scope

On distilgpt2 greedy decoding with small copy-biased and WikiText prompt sets, exact prompt-local n-gram speculation preserved output and reduced target forward calls; history-local n-grams improved the natural-prompt signal.

## Why it stopped

Bounded small-model evidence supports the mechanism but the speed claim is proxy-only and not sufficient for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate KV-cache-aware verification in an inference engine and evaluate a current small instruction-tuned model on copy-heavy and ordinary prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware prompt-local n-gram speculative decoding on an instruction-tuned model
- Success threshold: At least 15% median latency reduction on copy-heavy prompts with 0 exact greedy mismatches, and no more than 5% median latency regression on ordinary prompts.
- Stop condition: Stop if KV-aware integration cannot exceed 5% median latency reduction on copy-heavy prompts or causes more than 5% median regression on ordinary prompts.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-local-n-gram-speculative-decoding-without-draft-model-3470be8dc1c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
