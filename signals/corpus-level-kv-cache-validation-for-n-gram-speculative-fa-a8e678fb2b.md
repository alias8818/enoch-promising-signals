# Corpus-level KV-cache validation for n-gram speculative fallback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `corpus-level-kv-cache-validation-for-n-gram-speculative-fa-a8e678fb2b`
Run ID: `corpus-level-kv-cache-validation-for-n-gram-speculative-fa-a8e678fb2b-20260610T023512037021+0000`

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

- Parent run decision: Medium KV-cache validation of n-gram fallback speculative decoding: enoch://control-plane/projects/medium-kv-cache-validation-of-n-gram-fallback-speculative-48993b0331/runs/medium-kv-cache-validation-of-n-gram-fallback-speculative-48993b0331-20260609T214957369993+0000
- Parent run decision: SpecDec with n-gram fallback for low-VRAM speculative decoding: enoch://control-plane/projects/specdec-with-n-gram-fallback-for-low-vram-speculative-decoding-401323b3d1c0/runs/specdec-with-n-gram-fallback-for-low-vram-speculative-decoding-401323b3d1c0-20260609T172035282114+0000

## What looked useful

Correct n-gram fallback matched greedy baseline on 224/224 prompts with max step logit difference 3.09e-4 and 264 natural partial rejections. Random drafts also remained exact but had far lower acceptance, while unsafe no-rewind matched only 117/224 prompts and forced unsafe partial rejection matched 1/224, showing stale rejected-token KV cache causes divergence.

## Boundaries and scale limits

One GPT-2-small-class model, one public corpus, greedy decoding only, prompt length 64, generation length 48, max draft length 8, single-process GPU inference, no batched serving throughput study, no sampling distribution validation, no larger decoder families, and no production-native cache API benchmark.

## Claim scope

On distilgpt2 with Wikitext-2 validation prompts, greedy n-gram speculative fallback preserved exact generated tokens and near-identical next-token logits versus a real autoregressive greedy baseline across 224 fixed-seed prompts when partial draft rejection cropped/rewound KV cache.

## Why it stopped

Medium fixed-seed evidence supports the cache-rewind mechanism but remains too narrow for a publication-grade corpus-level serving claim.

## Recommended next action

Do not write a paper from this run; run a bounded deepen follow-up that repeats the same direct correctness tests with native cache APIs plus batched throughput on at least one larger open decoder.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native-cache and batched-serving validation for n-gram speculative fallback
- Success threshold: Across at least 500 prompts, correct n-gram fallback has 100% token agreement, max next-logit drift below 1e-3, at least 5x the random-control acceptance rate, and at least 10% median latency or target-forward reduction in a batched setting.
- Stop condition: Stop if native cache rewind cannot preserve exactness, if n-gram acceptance is not meaningfully above random control, or if batched latency is not improved despite acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-level-kv-cache-validation-for-n-gram-speculative-fa-a8e678fb2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
