# Medium real-corpus validation of reference-PPL filtering for Tiny GPT-2 pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-real-corpus-validation-of-reference-ppl-filtering-f-1b0451512d`
Run ID: `medium-real-corpus-validation-of-reference-ppl-filtering-f-1b0451512d-20260628T143402129531+0000`

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

- Parent run decision: Reference-Model PPL Filtering for Tiny GPT-2 Pretraining: enoch://control-plane/projects/reference-model-ppl-filtering-for-tiny-gpt-2-pretraining-48154a525da6/runs/reference-model-ppl-filtering-for-tiny-gpt-2-pretraining-48154a525da6-20260628T133301983649+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cb0d99f13efd

## What looked useful

Across 200/400/600 selected-chunk budgets, low reference-PPL selection achieved validation PPL ratios of 0.9920, 0.9763, and 0.9750 versus random controls, while high-PPL selection was 1.1201, 1.0788, and 1.0517 versus random.

## Boundaries and scale limits

Order-4 word n-gram target/reference only; Wikitext-2 subset; no neural transformer, tokenizer, optimizer, or multi-epoch Tiny GPT-2 training tested; CPU-only single-process runs under 4 minutes total confirmation/sensitivity time.

## Claim scope

Real Wikitext-2 CPU n-gram proxy: low reference-PPL filtering modestly improves held-out n-gram LM perplexity versus random equal-token controls; high reference-PPL filtering is harmful. This does not validate Tiny GPT-2 transformer pretraining.

## Why it stopped

This run produced a useful real-corpus proxy signal, but direct Tiny GPT-2 pretraining evidence was not available in the CPU-only environment and the proxy is not paper-ready.

## Recommended next action

Run a bounded direct Tiny GPT-2-class transformer pretraining follow-up with the same low/mid/high/random reference-PPL selection protocol and at least 3 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Tiny GPT-2 validation of Wikitext reference-PPL filtering
- Success threshold: Low-PPL selection beats random by at least 1% held-out perplexity with confidence intervals excluding zero, and high-PPL selection is not better than random.
- Stop condition: Stop if low-PPL does not beat random after matched-token training in two independent seeds, or if selection benefit vanishes after controlling for document length/format artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-corpus-validation-of-reference-ppl-filtering-f-1b0451512d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
