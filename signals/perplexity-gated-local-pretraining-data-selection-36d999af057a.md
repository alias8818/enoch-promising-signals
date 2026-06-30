# Perplexity-Gated Local Pretraining Data Selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-gated-local-pretraining-data-selection-36d999af057a`
Run ID: `perplexity-gated-local-pretraining-data-selection-36d999af057a-20260525T173101580183+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/788a76666a85

## What looked useful

Low-perplexity gating reduced held-out target perplexity by 18.99% versus the mean of 8 random equal-token selections in the main probe; low_ppl was also best across smoke, 30k budget, 90k budget, bigram, and alternate-seed probes, while high_ppl was consistently worst.

## Boundaries and scale limits

Evidence is limited to a local n-gram proxy: 60k reference tokens, 260k candidate tokens, 60k selected target-training tokens, 80k held-out eval tokens, WikiText-2 only, no neural LM training, no downstream tasks, and no cross-domain corpus mixture.

## Claim scope

On WikiText-2 raw text with small word n-gram reference and target language models, selecting equal-token training chunks by low reference perplexity produced lower held-out validation/test perplexity than random, mid-perplexity, or high-perplexity selection.

## Why it stopped

The run produced a reproducible local useful signal, but it is proxy n-gram evidence rather than direct neural pretraining evidence, so it is not paper-ready.

## Recommended next action

Run a bounded deepen follow-up with a small Transformer LM trained from scratch on the same low/mid/high/random selected subsets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer validation of perplexity-gated WikiText data selection
- Success threshold: Low_ppl must improve held-out neural LM perplexity by at least 5% versus the random-selection mean across 3 seeds, with high_ppl worse than random or clearly diagnosed.
- Stop condition: Stop after 3 seeds per selection strategy or earlier if two completed seeds show low_ppl is worse than or within 1% of the random mean.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-gated-local-pretraining-data-selection-36d999af057a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
