# Perplexity-bucketed curriculum ordering for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-bucketed-curriculum-ordering-for-tiny-pretraining-e511ccf78e3f`
Run ID: `perplexity-bucketed-curriculum-ordering-for-tiny-pretraining-e511ccf78e3f-20260629T202321937407+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a1bc16d9a396

## What looked useful

Naive monotonic perplexity curriculum ordering is early-falsified in this setting: easy-to-hard was +0.0964 loss worse than random and hard-to-easy was +0.0631 worse. Mixing across perplexity buckets by round-robin was -0.0078 loss better than random across all three seeds, suggesting diversity-preserving bucket schedules are a more plausible follow-up than strict curriculum sorting.

## Boundaries and scale limits

This was a local small-corpus character-level experiment, not a subword/token-level LLM pretraining run. The difficulty score was a unigram proxy rather than a stronger teacher-model perplexity. Results should not be generalized to large corpora, larger models, downstream tasks, or long training schedules without direct validation.

## Claim scope

Tiny character-level Transformer pretraining on Tiny Shakespeare with frozen unigram-perplexity bucket scores: monotonic easy-to-hard and hard-to-easy ordering worsened validation loss versus random, while bucket round-robin produced a small consistent validation-loss gain across three seeds.

## Why it stopped

No paper-ready result: this is a small direct probe with a unigram proxy. It provides an early negative result for monotonic ordering and a narrow useful signal for mixed bucket scheduling, but not full validation.

## Recommended next action

Run a bounded token-level follow-up on a real small pretraining corpus using frozen GPT-2-small-class perplexity buckets and compare random, monotonic curricula, and bucket round-robin over at least five seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level teacher-perplexity bucket round-robin curriculum probe
- Success threshold: Bucket round-robin must improve mean held-out loss versus random by at least 0.01 with no hard-quartile regression, while both monotonic schedules must be reported as controls.
- Stop condition: Stop if bucket round-robin fails to beat random in at least four of five seeds or if the hard validation quartile regresses by more than 0.01 loss.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-bucketed-curriculum-ordering-for-tiny-pretraining-e511ccf78e3f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
