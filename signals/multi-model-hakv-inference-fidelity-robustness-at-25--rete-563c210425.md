# Multi-model HAKV inference fidelity robustness at 25% retention

Status: `useful_signal`
Project ID: `multi-model-hakv-inference-fidelity-robustness-at-25--rete-563c210425`
Run ID: `multi-model-hakv-inference-fidelity-robustness-at-25--rete-563c210425-20260515T224552943405+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Multi-model HAKV inference fidelity robustness at 25% retention: internal_generated:multi-model-hakv-inference-fidelity-robustness-at-25--rete-563c210425

## What looked useful

Corrected multi-model inference-fidelity evaluation produced 192 rows. HAKV achieved only 0.156 mean generated-token match, 0.244 teacher-forced top-1 agreement, and KL 3.697 versus full cache; attention-only and sink/recent controls were stronger on most direct fidelity metrics.

## Boundaries and scale limits

No 7B+ models, no long-context benchmark suites, no downstream QA/task accuracy, and no per-layer/per-head adaptive HAKV implementation were tested.

## Claim scope

On three small pretrained causal LMs with 128-token prefill, 40-token greedy decode, and fixed local prose prompts, the tested layer-shared holistic HAKV selector at 25% KV retention does not preserve full-cache inference fidelity robustly and does not consistently outperform attention-only or sink/recent controls.

## Why it stopped

Tier-2 local evidence directly tested full-cache inference fidelity at 25% retention and found HAKV weak and not robust across models; this is a no-paper useful negative, not a full-scale validation.

## Recommended next action

Stop the 25% layer-shared HAKV robustness claim; only pursue a bounded follow-up if testing a materially different per-layer/per-head or adaptive-retention selector against the same controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-layer attention-only versus adaptive HAKV retention at 25-50%
- Success threshold: At 25% retention, the adaptive selector must improve mean teacher-forced top-1 agreement by at least 0.10 over attention-only and sink+recent controls and must not reduce generated-token match; at 50%, it must reach at least 0.60 mean teacher-forced top-1 agreement across all three models.
- Stop condition: Stop if the adaptive selector fails to beat both attention-only and sink+recent on paired mean teacher-forced top-1 agreement at 25%, or if 50% retention still remains below 0.60 mean teacher-forced top-1 agreement.

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-hakv-inference-fidelity-robustness-at-25--rete-563c210425`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
