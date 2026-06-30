# Gradient Coreset Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-coreset-data-selection-for-tiny-pretraining-86ed4d057bcf`
Run ID: `gradient-coreset-data-selection-for-tiny-pretraining-86ed4d057bcf-20260604T055614148855+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae31537fae7b

## What looked useful

Gradient k-center was worse than random in 3/3 seeds at 100 steps by mean +0.0207 validation loss, and mixed at 500 steps with 1/3 wins and mean +0.0080 validation loss. The selected coreset skewed toward higher warm-model loss examples by about +0.063 loss over the candidate mean, suggesting the simple diversity objective may over-select hard examples rather than preserving useful corpus coverage.

## Boundaries and scale limits

Tested 64 selected 64-byte sequences from 256 candidates, 3 seeds, 100-step and 500-step training horizons, tiny 2-layer Transformer only. Not tested on GPT-2-small-class models, subword tokenization, larger corpora, longer schedules, or downstream transfer.

## Claim scope

In a tiny byte-level Transformer pretraining proxy on WikiText-2, greedy k-center selection over warm-start LM-head gradient embeddings did not outperform random selection from the same candidate pool at equal selected-example and optimization budgets.

## Why it stopped

Bounded direct proxy evidence is mixed-to-negative, not a full validation; larger evidence would be required to overturn it, but the current method is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; the simple gradient k-center method failed to beat a controlled random baseline in the bounded tiny-pretraining test.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Loss-balanced gradient diversity for tiny pretraining selection
- Success threshold: Loss-balanced gradient diversity beats same-candidate random by at least 0.02 mean validation loss with at least 4/5 wins and no worse token-frequency coverage.
- Stop condition: Stop if loss-balanced selection fails to beat random in at least 3/5 seeds or if coverage diagnostics show the method still over-selects high-loss examples.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-data-selection-for-tiny-pretraining-86ed4d057bcf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
