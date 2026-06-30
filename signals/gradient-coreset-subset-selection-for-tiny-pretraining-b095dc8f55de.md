# Gradient coreset subset selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-coreset-subset-selection-for-tiny-pretraining-b095dc8f55de`
Run ID: `gradient-coreset-subset-selection-for-tiny-pretraining-b095dc8f55de-20260523T044554618644+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/796b6c3ba0ff

## What looked useful

Gradient herding and gradient k-center beat random on all five paired seeds by mean final validation NLL deltas of -0.0200 and -0.0230 respectively; highest-loss selection was worse than random on all five seeds by +0.2185 NLL.

## Boundaries and scale limits

Synthetic data only; approximate output-layer gradient features only; tiny GRU only; 700 candidate sequences, 320 validation sequences, 180 updates per subset, five seeds. No real corpus, GPT-style transformer, exact full-model per-example gradients, downstream transfer, or token-scale persistence tested.

## Claim scope

On a reproducible synthetic topic-mixture language with a tiny GRU causal LM, selecting 20% of candidate sequences using approximate initial output-layer gradient features improved validation NLL versus same-size random subsets across five seeds under equal update budgets.

## Why it stopped

No-paper closure: this run is a proxy-only useful signal, not direct publication-grade evidence for real tiny pretraining.

## Recommended next action

Run a bounded deepen follow-up on a small real text corpus with a tiny transformer, comparing exact or improved per-example gradient coreset selection against random, loss-top, and embedding-diversity baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny transformer gradient coreset subset selection
- Success threshold: Gradient coreset selection beats random and loss-top on mean validation perplexity with paired wins in at least 3 of 3 seeds, without selection cost exceeding the saved pretraining compute for the tested budget.
- Stop condition: Stop if gradient coreset does not beat random in at least 2 of 3 paired seeds or if exact gradient collection costs more wall-clock than simply training on the full candidate pool at this scale.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-subset-selection-for-tiny-pretraining-b095dc8f55de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
