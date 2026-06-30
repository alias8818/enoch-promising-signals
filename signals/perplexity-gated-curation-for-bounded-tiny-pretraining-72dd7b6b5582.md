# Perplexity-gated curation for bounded tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-gated-curation-for-bounded-tiny-pretraining-72dd7b6b5582`
Run ID: `perplexity-gated-curation-for-bounded-tiny-pretraining-72dd7b6b5582-20260528T075832380544+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1290e91868e3

## What looked useful

Across three main seeds, low teacher-perplexity gating beat random once but was worse twice; mean low-vs-random PPL ratio was 1.0122, so the simple gating rule was slightly worse than random on average. High-perplexity gating was also not better, indicating perplexity alone is an unreliable curation key in this setup.

## Boundaries and scale limits

Small corpus slice, short training horizon, tiny student model, one teacher model, one dataset, no topic or length matching beyond token budget, and no GPT-2-small-class or full pretraining-scale validation.

## Claim scope

In a bounded WikiText-2 experiment with distilgpt2 teacher scoring and 2-layer GPT-2-style tiny students trained for 200 steps on about 50k tokens per arm, naive lowest-teacher-perplexity filtering did not reliably improve held-out validation perplexity versus a random token-matched subset.

## Why it stopped

Bounded direct evidence contradicted the simple low-perplexity-gating hypothesis; this is not a full-scale validation, but it is enough to avoid treating naive perplexity gating as paper-ready.

## Recommended next action

Stop this run as a bounded negative/useful signal; a next local deepen test should evaluate quantile-band or diversity-aware perplexity gating with matched length/topic controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-aware perplexity bands for tiny pretraining curation
- Success threshold: Middle or diversity-aware gating improves mean held-out perplexity versus random token-matched selection by at least 2% with the same sign in at least 4 of 5 seeds, while not reducing selected-text diversity below the random control.
- Stop condition: Stop if the proposed band fails to beat random in at least 3 of 5 seeds or the mean improvement is below 1% held-out perplexity.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-gated-curation-for-bounded-tiny-pretraining-72dd7b6b5582`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
