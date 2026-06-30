# KV-Cache Row Reuse as Implicit Draft via Positional Offset Prediction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-row-reuse-as-implicit-draft-via-positional-offset-prediction-c34fee6043f6`
Run ID: `kv-cache-row-reuse-as-implicit-draft-via-positional-offset-prediction-c34fee6043f6-20260528T193631555810+0000`

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

Predicted-offset reuse underperformed trivial controls on NLL: predictor accuracy was 0.283 versus 0.336 for majority baseline, and predicted-offset substitution increased NLL by 0.0341 versus 0.0051 for fixed previous-row reuse. Final-layer fixed previous-row reuse preserved top-1 logits on 0.9398 of positions, suggesting local KV redundancy but not supporting the proposed offset-prediction mechanism.

## Boundaries and scale limits

Single small GPT-style model, final transformer block only, one public text corpus, no multi-layer cache editing, no actual speculative decoding acceptance benchmark, no large-model or serving-kernel validation.

## Claim scope

On distilgpt2 final-layer K/V row substitution over 6096 Tiny Shakespeare next-token positions, a lightweight hidden-state positional-offset predictor did not identify reusable prior K/V rows well enough to act as an implicit draft surrogate.

## Why it stopped

Proxy-bounded but direct final-layer test falsified the positional-offset predictor mechanism: the predictor failed to beat a majority baseline and produced worse NLL degradation than fixed previous-row reuse.

## Recommended next action

Stop this hypothesis as an early direct negative; a separate bounded follow-up should test fixed-neighbor K/V reuse as lossy cache compression rather than predictor-driven implicit drafting.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Fixed-Neighbor KV Row Reuse as Lossy Final-Layer Cache Compression
- Success threshold: Across models and corpora, fixed-neighbor reuse preserves top-1 agreement >= 0.93 with delta_nll <= 0.01 for final-layer edits, and remains meaningfully better than random/zero-row controls.
- Stop condition: Stop if fixed-neighbor reuse falls below 0.90 top-1 agreement or exceeds delta_nll 0.02 on either model/corpus, or if multi-layer edits erase the final-layer signal.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-row-reuse-as-implicit-draft-via-positional-offset-prediction-c34fee6043f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
