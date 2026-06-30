# Embedding-space greedy rollout for zero-VRAM drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `embedding-space-greedy-rollout-for-zero-vram-drafting-4fbc09e8b04e`
Run ID: `embedding-space-greedy-rollout-for-zero-vram-drafting-4fbc09e8b04e-20260601T044621176064+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e2ed0cb03f27

## What looked useful

Embedding geometry alone collapsed into local token cycles and achieved prefix_ge_2_rate=0.0 for both tested embedding rollout variants, worse than a trivial repeat-first-token control that reached prefix_ge_2_rate=0.015625.

## Boundaries and scale limits

Only distilgpt2, WikiText-2 validation, greedy continuations, 128 prompts, and simple input/output embedding cosine rollout heuristics were tested; larger models, non-greedy decoding, trained CPU-side predictors, n-gram caches, and hidden-state predictors remain untested.

## Claim scope

For distilgpt2 greedy decoding on 128 WikiText-2 validation prompts, pure embedding-nearest greedy rollouts seeded by the first true target token did not produce useful multi-token speculative drafts.

## Why it stopped

Proxy-limited but direct early falsification: the tested embedding-only rollout never accepted a second consecutive greedy token across 128 prompts, so it would add verification overhead without reducing target-model work.

## Recommended next action

Stop this pure embedding-nearest rollout path; only revisit zero-VRAM drafting with a different bounded mechanism such as a CPU-side n-gram or trained hidden-state transition predictor and require prefix_ge_2_rate above a repeat-token control.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/embedding-space-greedy-rollout-for-zero-vram-drafting-4fbc09e8b04e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
