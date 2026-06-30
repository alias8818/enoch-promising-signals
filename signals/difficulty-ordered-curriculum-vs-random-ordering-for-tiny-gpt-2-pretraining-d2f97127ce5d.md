# Difficulty-ordered curriculum vs random ordering for tiny GPT-2 pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `difficulty-ordered-curriculum-vs-random-ordering-for-tiny-gpt-2-pretraining-d2f97127ce5d`
Run ID: `difficulty-ordered-curriculum-vs-random-ordering-for-tiny-gpt-2-pretraining-d2f97127ce5d-20260621T092051365818+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8264bf929445

## What looked useful

Curriculum ordering beat random ordering on 8/8 paired runs. Combined mean final validation-loss delta was -0.04730 cross-entropy, curriculum minus random, with an approximate 95% CI of [-0.06283, -0.03177]. This supports a bounded mechanism signal but not a paper-ready general GPT-2 pretraining claim.

## Boundaries and scale limits

Synthetic corpus only; character-level tokens; compact 4-layer 128-dimension GPT-style transformer; 4096 training examples, 512 validation examples per corpus seed; two corpus seeds and eight paired initialization seeds; no natural-language corpus, GPT-2 tokenizer, GPT-2-small-scale model, or long-run convergence test.

## Claim scope

In a controlled synthetic mixed-difficulty ASCII corpus, a small GPT-style causal transformer trained from scratch with an expanding easy-to-hard curriculum achieved lower held-out next-token validation loss than uniform random ordering after 600 fixed optimizer steps across 8 paired runs.

## Why it stopped

Closed as no-paper useful signal: direct local training evidence supports the scoped synthetic tiny-transformer hypothesis, but the result is proxy/small-scale rather than full natural-language GPT-2 pretraining validation.

## Recommended next action

Run a bounded natural-language follow-up using a GPT-2 tokenizer and a public corpus subset to test whether the same paired curriculum advantage survives outside the synthetic generator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language GPT-2-tokenizer curriculum probe
- Success threshold: Curriculum wins at least 70% of paired runs and improves mean final validation cross-entropy by at least 0.02 without worse late-stage convergence.
- Stop condition: Stop if curriculum fails to beat random on a majority of paired runs or the mean final validation-loss improvement is below 0.01 after the fixed token budget.

## Evidence references

- Artifact root: `<local-path>/projects/difficulty-ordered-curriculum-vs-random-ordering-for-tiny-gpt-2-pretraining-d2f97127ce5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
