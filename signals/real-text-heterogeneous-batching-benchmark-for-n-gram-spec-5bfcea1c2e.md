# Real-text heterogeneous batching benchmark for n-gram speculative GPT-2 decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-heterogeneous-batching-benchmark-for-n-gram-spec-5bfcea1c2e`
Run ID: `real-text-heterogeneous-batching-benchmark-for-n-gram-spec-5bfcea1c2e-20260604T005540987885+0000`

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

- Parent run decision: KV-cache and batching controls for n-gram speculative GPT-2 decoding: enoch://control-plane/projects/kv-cache-and-batching-controls-for-n-gram-speculative-gpt-6bebb401ea/runs/kv-cache-and-batching-controls-for-n-gram-speculative-gpt-6bebb401ea-20260603T223303950374+0000
- Parent run decision: N-Gram Speculative Draft for GPT-2 Inference on Home GPUs: enoch://control-plane/projects/n-gram-speculative-draft-for-gpt-2-inference-on-home-gpus-4e0d400ec304/runs/n-gram-speculative-draft-for-gpt-2-inference-on-home-gpus-4e0d400ec304-20260603T184345347360+0000

## What looked useful

Real text supplied accepted n-gram drafts at about 0.60-0.75 acceptance and reduced verifier iterations from 384 to about 241-265 per seed, but full-context heterogeneous verification expanded model token slots from 7.6k for greedy KV decoding to about 238k-262k plus about 24k padding slots, leaving all accepted-draft variants around 5x slower than greedy.

## Boundaries and scale limits

Tested one small model, one real-text dataset, fixed equal-length 96-token prompts, one batch size, and a Python/Transformers full-context verifier. Did not test cache-aware speculative verification, paged-attention serving kernels, larger models, live request queues, or longer production workloads.

## Claim scope

On GPT-2-small with Wikitext-2 validation prompts, batch size 8, 48 prompts per seed, 64 greedy tokens per prompt, and three fixed seeds, prompt/history n-gram speculative decoding produced exact greedy outputs and meaningful draft acceptance, but the tested heterogeneous full-context verifier was about 5x slower than a real KV-cache greedy baseline.

## Why it stopped

Direct medium validation with fixed seeds, real text, ablations, a no-hit control, and a real KV-cache greedy baseline found that accepted n-gram drafts do not overcome full-context heterogeneous verification overhead.

## Recommended next action

Stop this implementation as no-paper evidence; the only bounded deepen worth running is a cache-aware verifier on the same fixed prompt set with exact-output checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware n-gram speculative verifier for real-text GPT-2 batching
- Success threshold: At least 1.10x mean tokens/s versus greedy KV baseline across all three fixed seeds, with no seed below 1.00x and exact greedy output matches.
- Stop condition: Stop if a correct cache-aware implementation remains below greedy KV throughput on two fixed seeds or if exact-output matching cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-heterogeneous-batching-benchmark-for-n-gram-spec-5bfcea1c2e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
