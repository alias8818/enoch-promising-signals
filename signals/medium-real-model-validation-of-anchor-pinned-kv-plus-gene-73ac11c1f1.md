# Medium real-model validation of anchor-pinned KV plus generated summaries

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-real-model-validation-of-anchor-pinned-kv-plus-gene-73ac11c1f1`
Run ID: `medium-real-model-validation-of-anchor-pinned-kv-plus-gene-73ac11c1f1-20260630T000645401800+0000`

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

- Parent run decision: Real-Transformer KV Cache Test for Stable Anchor Pinning plus Tail Summaries: enoch://control-plane/projects/real-transformer-kv-cache-test-for-stable-anchor-pinning-p-85aa77ba5e/runs/real-transformer-kv-cache-test-for-stable-anchor-pinning-p-85aa77ba5e-20260629T234623619478+0000
- Parent run decision: Stable-Anchor KV Eviction: Pin Exact-Reference Tokens, Compress the Tail: enoch://control-plane/projects/stable-anchor-kv-eviction-pin-exact-reference-tokens-compress-the-tail-5319cf089497/runs/stable-anchor-kv-eviction-pin-exact-reference-tokens-compress-the-tail-5319cf089497-20260629T232609164757+0000

## What looked useful

The compressed anchor+summary artifact contained enough information for a deterministic parser to recover 8/8 answers, and it reduced prompt tokens by 87.8%, but the tested real model only answered 3/8 correctly under both generation and candidate-likelihood scoring.

## Boundaries and scale limits

No custom KV-cache pinning was implemented; anchors were represented as retained prompt text. The task was synthetic, medium-sized, and used a 1.5B model rather than 7B+ long-context serving or training-scale validation.

## Claim scope

On an eight-item synthetic two-hop retrieval task with Qwen2.5-1.5B-Instruct, generated summaries plus verbatim pinned anchors compressed the context from 2831 to 344 tokens and outperformed summary-only and anchor-only controls, but achieved only 3/8 accuracy.

## Why it stopped

Medium local validation produced a useful mechanism signal but low absolute real-model accuracy; this is not reliable enough for a paper-positive claim.

## Recommended next action

Stop this run as no-paper evidence; a bounded follow-up should implement actual KV pinning and test a stronger model on natural long-context QA with the same ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual KV-pinned anchor cache with stronger-model long-context QA
- Success threshold: Anchor+summary must reach at least 80% absolute accuracy, be within 5 percentage points of full context, beat both ablations by at least 20 percentage points, and reduce prefill/KV tokens by at least 70%.
- Stop condition: Stop if generated summaries plus pinned anchors remain below 60% absolute accuracy or fail to beat either ablation after prompt and summary-format sanity checks.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-model-validation-of-anchor-pinned-kv-plus-gene-73ac11c1f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
