# Self-Speculative Decoding via Early-Exit Draft from Same Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-draft-from-same-model-f0306613cb8a`
Run ID: `self-speculative-decoding-via-early-exit-draft-from-same-model-f0306613cb8a-20260528T195343374917+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8cf1563055e9

## What looked useful

Cheap exits were inaccurate, accurate exits were too late, and even a favorable speedup proxy stayed below 1.0. The raw hidden-state-logit variant is not a good first target for paper-scale validation without an added mechanism to improve early draft quality or reduce draft cost.

## Boundaries and scale limits

This was a bounded single-model, single-hardware probe. It measured early-exit agreement directly but used an idealized speedup proxy rather than a fully optimized KV-cache self-speculative decoder. It does not rule out trained exit heads, multi-token draft heads, layer skipping, or larger-model effects.

## Claim scope

On cached Qwen/Qwen3-0.6B over 192 greedy decoding steps from 12 prompts, raw same-model early-exit logits did not provide a favorable acceptance/cost tradeoff for speculative decoding; all tested exits had idealized speedup below 1.0.

## Why it stopped

Proxy/early falsification: direct early-exit agreement was insufficient for idealized speedup, so this run does not justify full-scale validation of the raw mechanism.

## Recommended next action

Stop this raw early-exit drafting line as a paper candidate; the next bounded test should train or calibrate lightweight intermediate exit heads and require measured wall-clock speedup from a real verifier implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Intermediate Heads for Same-Model Self-Speculative Decoding
- Success threshold: At least 1.15x measured tokens/s over cached greedy decoding with exact greedy-output equivalence and mean accepted draft tokens per verifier pass above 1.5 on held-out prompts.
- Stop condition: Stop if trained heads below 50% top-1 agreement before layer 16 or if the real verifier implementation remains below 1.05x speedup after bounded optimization.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-draft-from-same-model-f0306613cb8a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
