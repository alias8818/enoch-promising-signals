# GPT-2-tokenized perplexity bucket filtering on naturally noisy public text

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-tokenized-perplexity-bucket-filtering-on-naturally-n-28a17fd44f`
Run ID: `gpt-2-tokenized-perplexity-bucket-filtering-on-naturally-n-28a17fd44f-20260630T072934583615+0000`

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

- Parent run decision: Perplexity-bucket quality filtering for GPT-2-tiny pretraining: enoch://control-plane/projects/perplexity-bucket-quality-filtering-for-gpt-2-tiny-pretraining-abbba31415ae/runs/perplexity-bucket-quality-filtering-for-gpt-2-tiny-pretraining-abbba31415ae-20260630T071642025813+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a87d697cf665

## What looked useful

Top GPT-2 perplexity quintile spam rate was 0.810 on train sample versus 0.513 base rate and 0.825 on test sample versus 0.550 base rate. Perplexity AUC was 0.713 on train and 0.696 on test, while character length and punctuation controls were near or below 0.5.

## Boundaries and scale limits

Single public email spam dataset; 128-token truncation; no downstream model training, no multi-domain web corpus, no multilingual/code robustness, and no human quality adjudication beyond existing spam labels.

## Claim scope

On 600-row train and 600-row held-out test samples from SetFit/enron_spam, GPT-2-tokenized perplexity quintiles ranked public Enron email rows such that high-perplexity buckets were enriched for spam/noisy labels compared with the base rate and simple length/punctuation controls.

## Why it stopped

No-paper useful-signal closure: evidence supports the local mechanism but does not validate broad web-corpus filtering or downstream training improvement.

## Recommended next action

Run a bounded deepen follow-up that applies percentile filtering as an actual data-cleaning intervention across at least two public noisy-text datasets and measures downstream held-out quality against length and lexical baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Downstream validation of GPT-2 perplexity percentile filtering on public noisy text
- Success threshold: Across at least two datasets, GPT-2 perplexity filtering must improve the primary held-out metric over random and simple-feature baselines at the same retention rate, with non-overlapping or clearly favorable bootstrap confidence intervals.
- Stop condition: Stop if perplexity filtering fails to beat simple baselines on either dataset or if gains only appear on Enron-like email and do not transfer to another public noisy-text domain.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-tokenized-perplexity-bucket-filtering-on-naturally-n-28a17fd44f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
