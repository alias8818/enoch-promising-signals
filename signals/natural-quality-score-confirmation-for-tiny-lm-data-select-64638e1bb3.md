# Natural quality-score confirmation for tiny LM data selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-quality-score-confirmation-for-tiny-lm-data-select-64638e1bb3`
Run ID: `natural-quality-score-confirmation-for-tiny-lm-data-select-64638e1bb3-20260610T224301666308+0000`

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

- Parent run decision: Quality-Weighted Data Selection Beats Random Sampling for Tiny Pretraining: enoch://control-plane/projects/quality-weighted-data-selection-beats-random-sampling-for-tiny-pretraining-e5551f92e73c/runs/quality-weighted-data-selection-beats-random-sampling-for-tiny-pretraining-e5551f92e73c-20260610T222129984697+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/469411b4e18c

## What looked useful

High-score selection beat low-score selection consistently by 0.2735 mean validation loss, showing the score captures destructive low-quality text. High-score selection beat random by only 0.0186 mean loss and lost one of three seeds, so the stronger quality-over-random claim is not confirmed.

## Boundaries and scale limits

Synthetic corruptions rather than real web noise; byte-level 3-layer Transformer rather than tokenizer-based GPT-2-small-class model; three seeds; one corpus and one heuristic score; short Tier 1 training only.

## Claim scope

In a controlled WikiText-2-derived tiny byte-level causal LM test with matched 160k-character training budgets, a fixed naturalness quality score consistently avoids severely corrupted low-quality examples, but it does not robustly outperform random selection across three seeds.

## Why it stopped

Tier 1 direct controlled test produced mixed evidence: clear high-score-vs-low-score support, but insufficient robust confirmation over random selection.

## Recommended next action

Stop this run as no-paper useful evidence; run a bounded follow-up on real noisy web/document data with a tokenizer-based tiny GPT model and a predeclared high-vs-random threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-noise tokenizer tiny-GPT confirmation of natural quality-score data selection
- Success threshold: High-score selection must reduce clean held-out validation loss versus random by at least 0.03 in at least 4 of 5 seeds, and beat low-score selection in all seeds under the same token budget.
- Stop condition: Stop as negative/no-paper if high-score selection fails to beat random by the threshold in two seeds or if the score only separates low-quality data without improving over random.

## Evidence references

- Artifact root: `<local-path>/projects/natural-quality-score-confirmation-for-tiny-lm-data-select-64638e1bb3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
