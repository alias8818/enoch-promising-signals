# Prompt-specific n-gram speculative decoding for local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-specific-n-gram-speculative-decoding-for-local-inference-ea5c1aeadf78`
Run ID: `prompt-specific-n-gram-speculative-decoding-for-local-inference-ea5c1aeadf78-20260527T223743949269+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0baf61e57fbd

## What looked useful

The method is useful as a cheap exact draft source when the expected continuation copies or follows repeated prompt-local templates; it is not a broad local-inference accelerator for arbitrary chat/reasoning prompts based on this evidence.

## Boundaries and scale limits

Tested 10 hand-built prompts, 64 generated tokens per prompt, batch size 1, greedy decoding, fp16 CUDA, small 135M and 0.6B models, and a simple full-context verifier rather than a production KV-cache serving engine.

## Claim scope

On two cached local causal LMs, prompt-specific n-gram drafting preserved exact greedy output and reduced target-model forward passes substantially for copy-repeat and template prompts, but only weakly for general prompts.

## Why it stopped

Bounded local evidence is mixed: strong gains in copy/template cases, weak gains in general cases, and insufficient workload breadth/serving realism for publication-grade claims.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a bounded production-style KV-cache benchmark on copy-heavy RAG or structured-output prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache prompt n-gram speculative decoding on copy-heavy RAG prompts
- Success threshold: At least 20% median end-to-end decode latency reduction and 100% exact greedy token match on copy-heavy prompts, with no claimed gain on the general-control set unless directly observed.
- Stop condition: Stop if median latency gain is below 10%, exact token equivalence fails, or acceptance is not concentrated in prompts with high prompt-output copy overlap.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-specific-n-gram-speculative-decoding-for-local-inference-ea5c1aeadf78`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
