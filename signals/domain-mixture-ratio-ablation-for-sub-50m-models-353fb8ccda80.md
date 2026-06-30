# Domain Mixture Ratio Ablation for Sub-50M Models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `domain-mixture-ratio-ablation-for-sub-50m-models-353fb8ccda80`
Run ID: `domain-mixture-ratio-ablation-for-sub-50m-models-353fb8ccda80-20260613T220530313875+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ee0ff0d24823

## What looked useful

Balanced mixture ranked first across three seeds with mean equal-weight validation NLL 3.8866 versus 4.1137-4.1182 for 70/15/15 heavy mixtures and 5.2553-5.5569 for single-domain-only mixtures.

## Boundaries and scale limits

Synthetic domains only; no natural corpus, tokenizer, transformer, near-50M-parameter, long-training, downstream-task, or GPU-scale evidence. This is not publication-grade validation.

## Claim scope

In a deterministic synthetic prose/code/math corpus with a 29,727-parameter NumPy context-average MLP next-token model, matching the training mixture to an equal-weight validation target produced the best held-out NLL across three seeds.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports the scoped mechanism, but it is proxy evidence and not a full validation of sub-50M transformer pretraining mixtures.

## Recommended next action

Run a bounded deepen follow-up using a parameter-matched tiny transformer on real prose/code/math corpus slices with the same mixture grid and equal-weight validation target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny-transformer domain mixture confirmation
- Success threshold: Balanced mixture mean equal-weight validation NLL beats every 70/15/15 heavy mixture by at least 0.05 NLL across three seeds without worse instability or failed runs.
- Stop condition: Stop if balanced is not best in at least two of three seeds, if the NLL gap is below 0.02, or if the real-corpus setup cannot run within the bounded local compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mixture-ratio-ablation-for-sub-50m-models-353fb8ccda80`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
