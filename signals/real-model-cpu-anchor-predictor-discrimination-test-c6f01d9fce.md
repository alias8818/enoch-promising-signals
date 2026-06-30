# Real-model CPU anchor predictor discrimination test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-cpu-anchor-predictor-discrimination-test-c6f01d9fce`
Run ID: `real-model-cpu-anchor-predictor-discrimination-test-c6f01d9fce-20260523T031754718229+0000`

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

- Parent run decision: Anchor-Guided CPU Speculative Decoding: enoch://control-plane/projects/anchor-guided-cpu-speculative-decoding-0ed3d0541802/runs/anchor-guided-cpu-speculative-decoding-0ed3d0541802-20260523T023105487758+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b356e38b90fa

## What looked useful

Corrected calibrated seed 7 reached accuracy 0.800 and ROC-AUC 0.8447 against a threshold of accuracy >= 0.78 and ROC-AUC >= 0.85; across six seeds mean ROC-AUC was 0.8570 but only 3/6 runs met the full threshold. Shuffled-label mean ROC-AUC was 0.4764 and unigram bag-of-words mean ROC-AUC was 0.5000.

## Boundaries and scale limits

Single small pretrained model, synthetic templates, 240 lexical pairs per calibrated seed, final-token hidden-state probe only, no natural task, no causal intervention, no larger-model validation, and no ordered n-gram/template-aware baseline.

## Claim scope

In a CPU-only controlled synthetic-text test with frozen distilgpt2 hidden states, a linear probe can sometimes discriminate whether a predeclared anchor word is in the first ordered slot, with unigram and shuffled-label controls near chance; however the effect is seed-sensitive and did not robustly satisfy the predeclared threshold.

## Why it stopped

The corrected direct Tier 1 test found a useful but seed-sensitive signal; the primary seed narrowly missed the AUC threshold and only half of robustness seeds passed, so this is not paper-positive support.

## Recommended next action

Stop this run as no-paper mixed evidence; if continuing, run a preregistered multi-seed deepen test with stronger baselines and at least one larger real model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Preregistered multi-model anchor position probe with ordered baselines
- Success threshold: Median hidden-state ROC-AUC >= 0.88, accuracy >= 0.80, at least 8/10 seeds passing ROC-AUC >= 0.85 and accuracy >= 0.78, and hidden-state ROC-AUC at least 0.05 above the strongest lexical/template baseline.
- Stop condition: Stop if median ROC-AUC is below 0.82, if fewer than 6/10 seeds pass the original threshold, or if ordered lexical/template baselines match the hidden-state probe within 0.02 ROC-AUC.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-cpu-anchor-predictor-discrimination-test-c6f01d9fce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
