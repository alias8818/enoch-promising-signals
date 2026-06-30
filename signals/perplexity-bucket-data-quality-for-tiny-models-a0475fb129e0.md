# Perplexity-bucket data quality for tiny models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-bucket-data-quality-for-tiny-models-a0475fb129e0`
Run ID: `perplexity-bucket-data-quality-for-tiny-models-a0475fb129e0-20260525T063050901482+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4091f6725ab3

## What looked useful

Extended run over five seeds found random best at 7.1747 mean validation perplexity, mid-perplexity 0.386% worse paired, high-perplexity 1.121% worse paired, and low-perplexity 19.093% worse paired. This suggests naive perplexity bucketing is not a free data-quality improvement for tiny models and low-perplexity-only selection is a strong negative control.

## Boundaries and scale limits

Single small character-level corpus, one tiny GRU architecture, one reference scorer, one chunk size, one bucket size, five seeds for the extended run, and no modern tokenizer-level transformer or multi-domain pretraining validation.

## Claim scope

On Tiny Shakespeare with a smoothed character 5-gram reference scorer and a one-layer 128-hidden character GRU trained on equal-token 256-character chunk subsets, fixed low/mid/high reference-perplexity buckets did not outperform random subset selection on held-out validation perplexity; low-perplexity-only selection was consistently worse.

## Why it stopped

The local direct probe produced an early negative/mixed result rather than a paper-positive result: perplexity buckets changed outcomes, but none beat random, and low-perplexity selection was consistently harmful.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next action is a bounded direct follow-up on a tokenized corpus with a tiny transformer, multiple independent random subsets, and a predeclared 3% paired perplexity improvement threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level tiny-transformer validation of reference-perplexity bucket selection
- Success threshold: Mid-perplexity bucket beats the best random-subset control by at least 3% paired mean validation perplexity across seeds without worse coverage diagnostics.
- Stop condition: Stop as negative if mid-perplexity fails to beat random by 3% or if gains disappear when multiple random subset draws and coverage diagnostics are included.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-bucket-data-quality-for-tiny-models-a0475fb129e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
