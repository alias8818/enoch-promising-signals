# Perplexity-bucket quality filtering for GPT-2-tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-bucket-quality-filtering-for-gpt-2-tiny-pretraining-abbba31415ae`
Run ID: `perplexity-bucket-quality-filtering-for-gpt-2-tiny-pretraining-abbba31415ae-20260630T071642025813+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a87d697cf665

## What looked useful

Low reference-perplexity buckets enriched clean Wikitext documents and improved clean validation NLL from 2.4544 to 2.4058; mid buckets helped less at 2.4342; high-perplexity buckets degraded clean NLL to 2.9409 while improving noisy validation, supporting the bucket-quality mechanism at toy scale.

## Boundaries and scale limits

Tested only about 0.86M-parameter char-token Transformers for 400 steps per condition on Wikitext-plus-injected-noise and a synthetic corpus; not GPT-2 BPE, not naturally noisy web data, not long pretraining, and not publication-grade scale.

## Claim scope

In a bounded local character-token tiny GPT-style pretraining probe on Wikitext-2 clean documents mixed with 30% injected noise, selecting the lowest 70% of documents by a clean-reference 4-gram perplexity score improved clean held-out NLL versus the unfiltered mixed pool across 3 seeds.

## Why it stopped

No-paper closure: evidence is a bounded toy/local useful signal, not a full GPT-2 or web-scale validation.

## Recommended next action

Run a bounded deepen experiment with GPT-2/BPE tokenization on a naturally noisy public text mixture, preserving matched-token training budgets and reporting clean, noisy, and general validation losses.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-tokenized perplexity bucket filtering on naturally noisy public text
- Success threshold: Lowest-perplexity bucket improves clean validation NLL by at least 0.03 over the unfiltered matched-token baseline across 3 seeds without a larger mixed-validation regression than the stated target-task tradeoff allows.
- Stop condition: Stop if low-perplexity filtering fails to beat the unfiltered baseline on clean validation in at least 2 of 3 seeds or if gains disappear when using naturally noisy text.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-bucket-quality-filtering-for-gpt-2-tiny-pretraining-abbba31415ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
