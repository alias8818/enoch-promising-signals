# Curriculum Perplexity Filtering for CPU Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `curriculum-perplexity-filtering-for-cpu-tiny-pretraining-316944360ccd`
Run ID: `curriculum-perplexity-filtering-for-cpu-tiny-pretraining-316944360ccd-20260527T125830972035+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5f787d423580

## What looked useful

Perplexity filtering retained only 71 of 282 injected noisy documents versus 192 in the random keep-70 control, and improved validation loss by -0.0387 bits/char over random keep-70 and -0.0432 bits/char over full mixed data. With no injected noise, the corresponding gain over random keep-70 shrank to -0.0072 bits/char, supporting a noise-removal mechanism rather than a generic data-dropping effect.

## Boundaries and scale limits

Synthetic contamination, character-level 5-gram scorer, NumPy character-context MLP, 3 seeds, 500 optimizer steps, one source corpus, no transformer/GPT-2-small-class baseline, no real web-corpus validation, and no downstream task evaluation.

## Claim scope

In a CPU-bounded Tiny Shakespeare character-LM probe with 30% synthetic high-perplexity document contamination, lowest-70% document perplexity filtering removed most injected noisy records and improved clean held-out bits/char versus both full mixed data and a random 70% document control after a fixed 500-step tiny MLP pretraining budget.

## Why it stopped

No-paper closure: this is a useful scoped signal from synthetic contamination and a tiny CPU model, not direct publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a real noisy text subset with a standard tokenizer and a small transformer/GPT-2-small-class baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus transformer check for perplexity-filtered tiny pretraining
- Success threshold: Perplexity-filtered data improves held-out validation perplexity by at least 0.5% over random keep-fraction with paired consistency across replicates and no clear coverage regression.
- Stop condition: Stop if the filtered policy is not better than random keep-fraction on paired held-out perplexity, or if diagnostics show the filter mostly selects a narrow/easy domain rather than removing noisy records.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-perplexity-filtering-for-cpu-tiny-pretraining-316944360ccd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
