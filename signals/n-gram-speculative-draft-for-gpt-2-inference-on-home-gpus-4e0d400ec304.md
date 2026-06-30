# N-Gram Speculative Draft for GPT-2 Inference on Home GPUs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-for-gpt-2-inference-on-home-gpus-4e0d400ec304`
Run ID: `n-gram-speculative-draft-for-gpt-2-inference-on-home-gpus-4e0d400ec304-20260603T184345347360+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/810c7576d010

## What looked useful

N-gram speculative drafting reduced mean model calls from 64.00 to 36.36 for n=2,k=8 on 100 prompts, improved mean throughput from 220.4 to 441.9 tokens/s, and matched ordinary greedy GPT-2 output exactly for all tested prompts/settings.

## Boundaries and scale limits

Tested only GPT-2-small greedy decoding, single-sequence generation, 128-token prompts, 64-token continuations, WikiText-2 validation text, and one GB10 GPU. Did not test sampling, batching, KV-cache optimized serving, longer contexts, larger models, or production latency constraints.

## Claim scope

For single-sequence exact greedy GPT-2-small inference on a local NVIDIA GB10 using 128-token WikiText-2 validation prompts and 64 generated tokens, a history n-gram speculative drafter with target-model verification preserved baseline outputs exactly and improved mean throughput up to 2.00x on a 100-prompt confirmation run.

## Why it stopped

Bounded local evidence supports the mechanism but is not broad or robust enough for a paper; untested serving modes and larger/longer model settings could change the conclusion.

## Recommended next action

Stop this run as a no-paper useful signal; next run should deepen with a KV-cache-aware implementation and batched/sampling controls on GPT-2-small and GPT-2-medium.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache and batching controls for n-gram speculative GPT-2 decoding
- Success threshold: At least 1.3x median throughput improvement over KV-cache greedy decoding with exact output matches on all prompts and no more than 10% of prompts slower than baseline.
- Stop condition: Stop if KV-cache greedy removes the speedup below 1.1x median, exactness fails, or batching overhead makes more than 25% of prompts slower than baseline.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-gpt-2-inference-on-home-gpus-4e0d400ec304`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
