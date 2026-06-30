# LLM-Augmented Tiny Pretraining Data

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `llm-augmented-tiny-pretraining-data-e4a46dc2c901`
Run ID: `llm-augmented-tiny-pretraining-data-e4a46dc2c901-20260522T075334297758+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5479b6846b10

## What looked useful

Extra synthetic diversity is not automatically beneficial in tiny pretraining regimes; in this proxy it diluted local surface statistics and increased held-out NLL. Future tests should include duplicate-token and simple-paraphrase controls plus token-budget matching before crediting LLM augmentation.

## Boundaries and scale limits

Synthetic micro-world data, no actual LLM generation, word trigram model rather than neural pretraining, no real tokenizer effects, no downstream benchmark transfer, and runs under 10 seconds per condition set.

## Claim scope

In a controlled synthetic tiny-corpus probe using a pure-Python word trigram language model, LLM-like diverse paraphrase augmentation worsened held-out paraphrase likelihood relative to real-only, duplicate-budget, and simple-augmentation controls.

## Why it stopped

Proxy early falsification: across 9-seed main and smoothing sensitivity runs, LLM-like augmentation consistently worsened held-out NLL versus real-only; this is not full-scale validation.

## Recommended next action

Stop this run as a proxy early falsification; the next direct test should use real tiny text slices, actual LLM-generated augmentations, token-matched budgets, and a small neural LM rather than extending this trigram probe.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural token-matched test of actual LLM augmentation for tiny pretraining
- Success threshold: Filtered LLM augmentation improves validation loss by at least 2% over real-only and duplicate-budget controls without degrading the downstream/factual diagnostic across seeds.
- Stop condition: Stop if unfiltered and filtered LLM augmentation both fail to beat duplicate-budget controls on validation loss, or if gains disappear under token matching.

## Evidence references

- Artifact root: `<local-path>/projects/llm-augmented-tiny-pretraining-data-e4a46dc2c901`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
