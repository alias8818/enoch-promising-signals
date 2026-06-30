# Contrastive margin selection with synthetic negatives

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `contrastive-margin-selection-with-synthetic-negatives-e468329e3be2`
Run ID: `contrastive-margin-selection-with-synthetic-negatives-e468329e3be2-20260520T155826142939+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b491ee72200a

## What looked useful

Across 96 runs, margin_band achieved the best mean centroid accuracy at all contamination rates: 0.9997 at 10%, 0.9993 at 25%, and 0.9976 at 40%, while hardest mining fell to 0.9941, 0.9875, and 0.9826 and selected false negatives at 0.3880, 0.6525, and 0.7902 respectively.

## Boundaries and scale limits

Evidence is synthetic-only, small-scale, near-ceiling, and CPU-only. It does not validate real language-model, retrieval, preference-model, or generated-negative pipelines.

## Claim scope

In a controlled NumPy metric-learning task with injected false negatives in synthetic negative pools, semi-hard margin-band selection preserved higher held-out nearest-centroid accuracy and Recall@1 than random, hardest, and loss-weighted candidate selection as contamination increased.

## Why it stopped

No-paper closure: the mechanism is supported only by a synthetic controlled study, which is useful but not direct publication-grade evidence.

## Recommended next action

Run a bounded real-data deepen test using a fixed embedding or retrieval dataset with generated synthetic negatives and hand/audit labels for false-negative contamination.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data audit of margin-band synthetic negative selection
- Success threshold: Margin-band must improve validation Recall@1 or task accuracy by at least 0.5 percentage points over the strongest non-margin selector while selecting fewer audited false negatives than hardest mining.
- Stop condition: Stop if margin-band does not beat the strongest non-margin selector on validation performance or if audited false-negative selection is not lower than hardest mining.

## Evidence references

- Artifact root: `<local-path>/projects/contrastive-margin-selection-with-synthetic-negatives-e468329e3be2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
