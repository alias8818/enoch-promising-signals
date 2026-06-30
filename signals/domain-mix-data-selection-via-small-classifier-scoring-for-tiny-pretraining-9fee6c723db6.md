# Domain-mix data selection via small-classifier scoring for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `domain-mix-data-selection-via-small-classifier-scoring-for-tiny-pretraining-9fee6c723db6`
Run ID: `domain-mix-data-selection-via-small-classifier-scoring-for-tiny-pretraining-9fee6c723db6-20260621T174312112334+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41859764a854

## What looked useful

Classifier scoring selected a target-heavy mix (0.7538 target fraction vs about 0.333 for uniform/random) and improved target validation NLL/char by 3.747% versus uniform and 3.758% versus random, while worsening all-domain validation loss versus uniform/random.

## Boundaries and scale limits

No real corpus, no transformer pretraining, no downstream transfer, no noisy/nonseparable classifier setting, and no full-scale validation. The classifier achieved AUC 1.0, so this is mechanism evidence rather than robustness evidence.

## Claim scope

Synthetic six-domain proxy with a small hashed character n-gram classifier, classifier-scored document selection, and a smoothed character-bigram tiny causal LM. Within this setup, classifier-top selection lowered held-out target-domain NLL/char versus uniform and random selection.

## Why it stopped

No-paper closure: this run produced a useful synthetic proxy signal and tradeoff evidence, but not direct paper-grade validation.

## Recommended next action

Run a bounded real-corpus follow-up with a GPT-2-small-class or similarly tiny transformer baseline, preserving uniform/random/oracle/anti-score controls and reporting target plus broad validation losses.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny-transformer domain-mix classifier scoring
- Success threshold: Classifier-top improves target validation loss by at least 2% relative to both uniform and random across at least three seeds, remains within 1% of oracle-target target loss, and does not worsen broad validation loss by more than 3%.
- Stop condition: Stop if classifier-top fails to beat both uniform and random on target validation loss, if gains vanish across seeds, or if broad validation regression exceeds 3% without a clearly scoped target-specialization use case.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mix-data-selection-via-small-classifier-scoring-for-tiny-pretraining-9fee6c723db6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
