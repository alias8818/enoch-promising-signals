# Perplexity-gated data selection for tiny local pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-gated-data-selection-for-tiny-local-pretraining-9e951be9dab9`
Run ID: `perplexity-gated-data-selection-for-tiny-local-pretraining-9e951be9dab9-20260523T043524542036+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/afe971b0d332

## What looked useful

Low-PPL gating selected 93.7% target-domain chunks versus 37.8% for random and reduced mean target validation perplexity from 9.548 to 8.057 (-15.6%) across 3 seeds; mid-PPL and high-PPL controls were worse than random on every seed.

## Boundaries and scale limits

Synthetic generated data only; tiny character-level Transformer; 260 optimizer steps per condition; no natural corpus, GPT-style tokenizer, GPT-2-small-class model, downstream task, retained-fraction sweep, or noisy web-scale validation.

## Claim scope

In a reproducible synthetic mixed-domain corpus, selecting equal-token pretraining chunks with low perplexity under a small in-domain seed character trigram LM improved held-out target-domain perplexity for a tiny character-level causal Transformer versus random selection across 3 seeds.

## Why it stopped

Closed as no-paper useful signal: the mechanism worked in a synthetic proxy, but this is not direct natural-corpus or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a real mixed text corpus with GPT-style tokenization, equal-token controls, multiple retained fractions, and target validation perplexity as the primary metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus perplexity-gated selection for tiny tokenizer-based pretraining
- Success threshold: Low-PPL selection improves mean held-out target validation perplexity by at least 5% versus random across at least 3 seeds and at two retained fractions, without worse than 10% degradation on a documented general/distractor validation set unless the claim is explicitly target-specialized.
- Stop condition: Stop if low-PPL selection fails to beat random on target validation perplexity in at least 2 of 3 seeds or if gains vanish when target/distractor labels are natural rather than synthetic.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-gated-data-selection-for-tiny-local-pretraining-9e951be9dab9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
