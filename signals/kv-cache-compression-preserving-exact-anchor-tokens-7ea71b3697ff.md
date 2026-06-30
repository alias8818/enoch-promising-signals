# KV-cache compression preserving exact anchor tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-preserving-exact-anchor-tokens-7ea71b3697ff`
Run ID: `kv-cache-compression-preserving-exact-anchor-tokens-7ea71b3697ff-20260613T162901783630+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e4c4acd0bf0

## What looked useful

Exact anchor preservation is a conditional compression strategy: it produced 4.0% mean error reduction in the corrected moderate anchor-biased sweep and 74.8% in a high-anchor-mass sensitivity sweep, while random queries were neutral and non-anchor-biased queries were worse by 6.9% to 21.6%.

## Boundaries and scale limits

Tested only synthetic KV caches with seq_len=1024, dim=64, 512 queries, 5 seeds, anchor fractions 1-5%, slot budgets 64-256, and centroid compression. No real transformer, real prompt distribution, learned/dynamic anchor selection, multilayer/head effects, task quality, or serving latency was validated.

## Claim scope

In synthetic single-layer attention with a fixed compressed KV slot budget, preserving exact anchor-token KV entries reduces attention-output approximation error when future queries place substantial attention mass on those anchors, but hurts when important tokens are non-anchors.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports the mechanism under anchor-heavy attention and identifies a failure mode under non-anchor-heavy attention, but it is not full validation.

## Recommended next action

Run a bounded real-transformer validation on long-context retrieval/summarization prompts with static anchor policies and compare task accuracy, perplexity, KV memory, and decode latency against uniform/grouped KV compression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer validation of exact-anchor KV compression
- Success threshold: At matched KV slot budget, exact-anchor compression improves quality over uniform centroid compression on anchor-heavy prompts by at least 5% relative error/accuracy loss reduction, does not degrade non-anchor-heavy controls by more than 2%, and adds less than 10% decode latency overhead.
- Stop condition: Stop if selected anchors do not receive meaningfully elevated attention mass in real prompts or if exact-anchor compression fails to outperform uniform centroid compression at matched memory in two independent prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-preserving-exact-anchor-tokens-7ea71b3697ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
