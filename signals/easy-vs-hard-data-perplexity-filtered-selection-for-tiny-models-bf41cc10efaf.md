# Easy vs Hard Data: Perplexity-Filtered Selection for Tiny Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `easy-vs-hard-data-perplexity-filtered-selection-for-tiny-models-bf41cc10efaf`
Run ID: `easy-vs-hard-data-perplexity-filtered-selection-for-tiny-models-bf41cc10efaf-20260628T082202158351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/253d88d48df7

## What looked useful

Hard high-perplexity selection was best with mean validation NLL 3.27797 versus random 3.28698, a -0.00902 NLL delta; easy low-perplexity selection was worse than random by +0.00552 NLL. The sign is useful for designing a deeper direct test, but the effect is small relative to seed variance.

## Boundaries and scale limits

Single corpus, character-level tokenization, 5-gram filter scorer, 96 chunks per condition, 300 SGD steps per model, five seeds, no Transformer/tokenized LM, no downstream task validation.

## Claim scope

In a bounded Tiny Shakespeare character-level proxy, selecting high baseline-perplexity chunks for a NumPy tiny neural character LM slightly improved held-out next-character NLL versus random; selecting low-perplexity easy chunks did not improve over random.

## Why it stopped

This run produced a useful proxy signal but not publication-grade direct evidence; close as no-paper evidence rather than continue CPU-only sweeps.

## Recommended next action

Run a bounded tokenized tiny-Transformer follow-up comparing hard, easy, curriculum, and random selection with paired seeds on at least two corpora before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenized tiny-Transformer test of hard-perplexity data selection
- Success threshold: Hard or curriculum selection improves mean validation perplexity by at least 1 percent versus random on both corpora with paired-seed confidence intervals excluding zero or with a clearly persistent directional effect and mechanism diagnostics.
- Stop condition: Stop if hard/curriculum selection fails to beat random on either corpus after the planned paired seeds or if improvements disappear under equal-token diversity controls.

## Evidence references

- Artifact root: `<local-path>/projects/easy-vs-hard-data-perplexity-filtered-selection-for-tiny-models-bf41cc10efaf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
