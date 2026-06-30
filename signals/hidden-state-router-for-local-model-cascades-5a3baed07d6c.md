# Hidden-State Router for Local Model Cascades

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `hidden-state-router-for-local-model-cascades-5a3baed07d6c`
Run ID: `hidden-state-router-for-local-model-cascades-5a3baed07d6c-20260523T034404613932+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/db6ac62421a6

## What looked useful

Across a five-seed learnable-mixture smoke sweep where the larger model was consistently better than the small model, the hidden-state router trailed confidence routing by mean 0.0236 AUROC and by 0.0115 absolute cascade accuracy at 45% escalation. In medium runs, the larger expert was not reliably better, making naive local cascades fragile.

## Boundaries and scale limits

Synthetic classification only; not a GPT-2-small-class or LLM benchmark; no production serving latency, energy, KV-cache, calibration, or human-quality evaluation; medium runs showed the nominal larger expert could overfit and become worse than the small model.

## Claim scope

Controlled local proxy experiments with compact PyTorch sequence classifiers found no hidden-state router advantage over confidence routing for deciding when to escalate from a small model to a larger local model.

## Why it stopped

Proxy experiments did not support the claimed hidden-state routing advantage, and medium runs exposed a prerequisite failure: the larger local expert was not reliably better than the small model under finite-data training.

## Recommended next action

Stop this run as proxy early falsification; only revisit with a direct local LLM trace study that first verifies the expert model is consistently stronger and then compares hidden-state routing against confidence/calibration baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local LLM hidden-state router trace test
- Success threshold: Hidden-state routing improves over the best confidence/calibration baseline by at least 0.03 AUROC and at least 1.0 absolute accuracy point at a matched escalation budget on held-out real LLM traces.
- Stop condition: Stop if the expert model is not at least 3 absolute accuracy points better than the small model, or if hidden-state routing fails to beat confidence/calibration baselines on two held-out splits.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-router-for-local-model-cascades-5a3baed07d6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
