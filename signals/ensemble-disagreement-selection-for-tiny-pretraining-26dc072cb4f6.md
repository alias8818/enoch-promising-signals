# Ensemble Disagreement Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ensemble-disagreement-selection-for-tiny-pretraining-26dc072cb4f6`
Run ID: `ensemble-disagreement-selection-for-tiny-pretraining-26dc072cb4f6-20260604T201316144888+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd0adc3b10ec

## What looked useful

Pure ensemble disagreement was not a reliable standalone selector: balanced NLL versus random changed by only -0.0075 with high seed variance, while selection strongly improved rare domains but hurt common-domain NLL and oversampled noisy candidates. The mechanism looks like hard/rare-domain detection rather than a complete pretraining data-selection recipe.

## Boundaries and scale limits

No natural-language corpus, no transformer target model, no tokenizer/document effects, no downstream tasks, and no large-scale or long-horizon pretraining. Results are bounded to a CPU/GPU-local synthetic proxy.

## Claim scope

Synthetic Markov-token tiny-pretraining proxy with bootstrap bigram proxy ensembles, fixed-budget top-k data selection, and a shared tiny GRU target LM over 12 paired repeats.

## Why it stopped

Proxy/early bounded evidence is mixed and not paper-ready: standalone top-k disagreement did not show a robust balanced improvement over random, despite useful rare-domain mechanism diagnostics.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate constrained or quota-based disagreement selection that preserves rare-domain gains while limiting noise and common-domain coverage loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quota-Constrained Ensemble Disagreement for Tiny Pretraining Selection
- Success threshold: Quota-constrained disagreement beats random balanced NLL by at least 0.03 on average, wins at least 9/12 paired repeats, keeps rare-domain improvements, and limits noise selection to no more than 1.5x random.
- Stop condition: Stop if constrained disagreement fails to beat random by 0.03 balanced NLL, wins fewer than 9/12 repeats, or removes rare-domain gains while only reducing noise.

## Evidence references

- Artifact root: `<local-path>/projects/ensemble-disagreement-selection-for-tiny-pretraining-26dc072cb4f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
