# Position-aware residual selectors for KV outlier prediction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `position-aware-residual-selectors-for-kv-outlier-predictio-023629249e`
Run ID: `position-aware-residual-selectors-for-kv-outlier-predictio-023629249e-20260523T132735004937+0000`

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

- Parent run decision: Residual-KV: 2-bit cache with FP16 outlier channels: enoch://control-plane/projects/residual-kv-2-bit-cache-with-fp16-outlier-channels-9aa9954bacd3/runs/residual-kv-2-bit-cache-with-fp16-outlier-channels-9aa9954bacd3-20260523T111544425674+0000
- Parent run decision: Multi-layer real-model test of calibrated residual KV outlier selectors: enoch://control-plane/projects/multi-layer-real-model-test-of-calibrated-residual-kv-outl-52f5be2ae9/runs/multi-layer-real-model-test-of-calibrated-residual-kv-outl-52f5be2ae9-20260523T131838140283+0000

## What looked useful

Residual-only linear selectors achieved AUPRC 0.9191 and precision@10% 0.8480, far above norm and position-only baselines. Position-aware residual selectors reached AUPRC 0.9222 and precision@10% 0.8508, a consistent but very small delta of +0.0031 AUPRC and +0.0028 precision@10% over residual-only.

## Boundaries and scale limits

Tested only distilgpt2 layers 0, 3, and 5 on generated templated text, sequence length 128, three seeds, linear selectors, and direct KV magnitude labels. Not validated on natural corpora, larger models, long contexts, decoding-time cache behavior, head/channel-specific labels, or downstream serving quality/speed.

## Claim scope

On a medium fixed-seed distilgpt2 activation trace with locally generated prose, linear residual-stream selectors strongly predict top-10% per-token K/V projection RMS outliers; adding explicit position features gives only a tiny incremental gain over residual-only and shuffled-position controls.

## Why it stopped

Tier 2 direct target validation supports residual selectors but does not support a materially meaningful position-aware improvement; the observed explicit-position gain is too small for a paper claim.

## Recommended next action

Stop as no-paper useful signal unless a bounded deepen run tests real-corpus, layer/head-specific KV labels and requires at least a 2 percentage point precision@budget improvement over residual-only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer/head-specific position-aware KV outlier selectors on real text traces
- Success threshold: Across at least three seeds and multiple layers, residual-plus-position must beat residual-only and shuffled-position controls by >=2 absolute precision@budget points and >=0.02 AUPRC on direct K/V outlier labels.
- Stop condition: Stop if the mean position-aware gain over residual-only remains below 1 absolute precision@budget point or if shuffled-position controls match the gain.

## Evidence references

- Artifact root: `<local-path>/projects/position-aware-residual-selectors-for-kv-outlier-predictio-023629249e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
