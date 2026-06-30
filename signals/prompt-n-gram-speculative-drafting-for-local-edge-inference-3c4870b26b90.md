# Prompt n-gram speculative drafting for local edge inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-n-gram-speculative-drafting-for-local-edge-inference-3c4870b26b90`
Run ID: `prompt-n-gram-speculative-drafting-for-local-edge-inference-3c4870b26b90-20260525T012611453565+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e7f1bd0dbbd1

## What looked useful

Across 180 n-gram configurations per model, prompt lookup beat random prompt-token drafting: distilgpt2 averaged 2.46x oracle call speedup vs 1.08x random, and gpt2 averaged 1.61x vs 1.06x random. Gains concentrated in copy/structured prompts; wiki-like prompts were near baseline, especially for gpt2 at 1.02x mean.

## Boundaries and scale limits

Only 12 synthetic/local prompt cases, 48 generated tokens per case, GPT-2-class target models, and simulated verifier-call counts were tested. No production wall-clock speculative decoder, 7B+ target, quantized edge stack, or real traffic trace was validated.

## Claim scope

Prompt n-gram speculative drafting showed useful verifier-call reduction on small GPT-2-class local greedy continuations for copy-heavy QA, repeated JSON, and structured code prompts, but not for open wiki-like continuation.

## Why it stopped

Proxy/call-count evidence supports a narrow mechanism but does not validate end-to-end serving speedup or broad model-scale behavior.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a real wall-clock speculative decoder benchmark on copy-heavy RAG prompts using a quantized edge model and the same random/control comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock prompt lookup decoding on copy-heavy edge RAG prompts
- Success threshold: At least 15% end-to-end latency reduction or tokens/sec improvement over no drafting on copy-heavy prompts, with less than 5% regression on non-copy prompts and clear superiority over random prompt-span drafting.
- Stop condition: Stop if measured wall-clock speedup is under 5% on copy-heavy prompts or if verification overhead erases the call-count gains despite acceptance above the random control.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-n-gram-speculative-drafting-for-local-edge-inference-3c4870b26b90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
