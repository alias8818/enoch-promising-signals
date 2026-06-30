# Proxy Quality Filtering for CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proxy-quality-filtering-for-cpu-pretraining-af594eb96a38`
Run ID: `proxy-quality-filtering-for-cpu-pretraining-af594eb96a38-20260525T033900670093+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6fb2eb850244

## What looked useful

Proxy-top validation NLL was 8.4721 versus 8.6358 random mean and 8.6036 best random seed, while proxy-bottom scored 8.9114. The proxy remained imperfect: clean-only oracle scored 8.3872 and top-50 proxy results included 31 repeated-span corruptions.

## Boundaries and scale limits

Synthetic noise, public-domain book text, 180k-character training budget, count-based target model, and no transformer/neural pretraining or natural web-corpus validation.

## Claim scope

In a dependency-free CPU proxy experiment using Gutenberg clean text, synthetic corruptions, a character n-gram quality proxy, and a fixed-vocabulary word trigram target model, proxy-top filtering improved clean held-out validation NLL versus random fixed-budget sampling.

## Why it stopped

No-paper useful signal: the result is a bounded proxy/mechanism validation and metric-pitfall diagnostic, not direct full-scale CPU pretraining evidence.

## Recommended next action

Run a bounded deepen test with a small neural language model on a naturally noisy open corpus, using fixed tokenizer/vocabulary and matched-token random, proxy-bottom, and clean-oracle controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural small-LM validation of proxy quality filtering on natural noisy text
- Success threshold: Proxy-top improves validation perplexity by at least 2% versus the random mean and beats every random seed while keeping repeat/boilerplate contamination below 10% of selected tokens.
- Stop condition: Stop if proxy-top fails to beat the random mean or if repeated/boilerplate text exceeds 25% of selected tokens after proxy scoring.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-quality-filtering-for-cpu-pretraining-af594eb96a38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
