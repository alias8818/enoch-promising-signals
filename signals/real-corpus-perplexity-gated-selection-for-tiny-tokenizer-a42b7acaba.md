# Real-corpus perplexity-gated selection for tiny tokenizer-based pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-perplexity-gated-selection-for-tiny-tokenizer-a42b7acaba`
Run ID: `real-corpus-perplexity-gated-selection-for-tiny-tokenizer-a42b7acaba-20260523T064844494161+0000`

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

- Parent run decision: Perplexity-gated data selection for tiny local pretraining: enoch://control-plane/projects/perplexity-gated-data-selection-for-tiny-local-pretraining-9e951be9dab9/runs/perplexity-gated-data-selection-for-tiny-local-pretraining-9e951be9dab9-20260523T043524542036+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/afe971b0d332

## What looked useful

Low-PPL selection lost to uniform random in 5/5 seeds by +1.09% mean relative validation PPL and lost to length-matched random in 5/5 seeds by +1.69%, but beat high-PPL selection in 5/5 seeds by -4.04%, indicating the gate score is informative while low-only selection sacrifices useful diversity.

## Boundaries and scale limits

Small Wikitext-2-only experiment; tiny Transformer; 1,024-token tokenizer; 180 optimizer steps per arm; passage-level selection; no large-corpus, long-run, GPT-2-small-class, or multi-domain validation.

## Claim scope

In a corrected five-seed Tier 1 Wikitext-2 test with a freshly trained 1,024-token BPE tokenizer, 4-gram token perplexity scorer, 450 selected passages per arm, and a matched 2-layer 96-dim causal Transformer trained for 180 steps per arm, low-perplexity-only selection did not improve held-out validation perplexity over uniform-random or length-matched-random selection.

## Why it stopped

Corrected multi-seed Tier 1 direct test falsified the low-PPL-only improvement claim at small scale; this is not full-scale validation, but it is direct early negative evidence for the stated selector.

## Recommended next action

Stop this low-PPL-only claim as no-paper evidence; the bounded next test is a band-pass or mixed-perplexity selector that excludes the high-PPL tail while preserving diversity, compared against the same random controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Band-pass perplexity-gated selection for tiny tokenizer pretraining
- Success threshold: A band-pass or high-tail-excluded selector must beat both uniform-random and length-matched-random controls by at least 1% mean relative validation perplexity across five seeds, with no more than one losing seed against either control.
- Stop condition: Stop if all gated selectors fail to beat either random control on mean validation perplexity across five seeds, or if gains disappear after length and diversity diagnostics are matched.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-perplexity-gated-selection-for-tiny-tokenizer-a42b7acaba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
