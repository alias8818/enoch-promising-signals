# Gradient-coreset tiny pretraining data selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-coreset-tiny-pretraining-data-selection-12e3b466d124`
Run ID: `gradient-coreset-tiny-pretraining-data-selection-12e3b466d124-20260524T075833368954+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

Gradient k-center lost to random on all five seeds, with mean validation loss 1.8737 versus 1.8230 for random and mean token accuracy 0.5310 versus 0.5433. It also oversampled rarer synthetic domains, suggesting naive gradient-space diversity can discard useful majority-domain mass under fixed token budgets.

## Boundaries and scale limits

Synthetic token-transition corpus only; tiny Transformer only; untrained probe model; gradient feature limited to averaged LM-head-bias gradients; no real text corpus, GPT-2-small-class model, or full per-parameter gradient coreset evaluation.

## Claim scope

In a five-seed synthetic tiny-language-model pretraining benchmark, farthest-first selection over approximate LM-head-bias gradient features did not improve validation loss over random subset selection at a fixed 320-example budget and 220-step training budget.

## Why it stopped

Proxy/early falsification of the tested gradient-kcenter variant: the direct tiny synthetic pretraining test showed worse validation loss than random on every seed, but it is not a full validation or full rejection of gradient-coreset data selection.

## Recommended next action

Stop this run as a no-paper useful negative signal; a bounded follow-up should test density-weighted gradient selection on a small real text corpus before considering any larger scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Density-weighted gradient coreset on a small real text corpus
- Success threshold: Density-weighted gradient selection improves mean validation loss over random by at least 1 percent and wins at least 4 of 5 seeds without losing to embedding diversity.
- Stop condition: Stop if density-weighted gradient selection fails to beat random on at least 4 of 5 seeds or if it requires runtime beyond the local medium-run budget without a clear positive trend.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-tiny-pretraining-data-selection-12e3b466d124`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
