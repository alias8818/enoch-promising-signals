# Perplexity Filtering Removes Harmful Samples in Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-filtering-removes-harmful-samples-in-tiny-pretraining-4a22a3fead2f`
Run ID: `perplexity-filtering-removes-harmful-samples-in-tiny-pretraining-4a22a3fead2f-20260602T153214156693+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aa233e0bb664

## What looked useful

Across 9 CPU-only runs, toxic-vs-clean AUC averaged 0.764 while shuffled-label AUC averaged 0.481. The top 5% highest-perplexity filter averaged 92.2% toxic samples versus a 50.1% base rate, and length-matched toxic examples had higher NLL in 77.3% of pairs.

## Boundaries and scale limits

No tiny transformer was pretrained; no downstream utility, safety, or memorization metrics were measured. Evidence is limited to one public toxicity sample, character n-gram reference models, 399-example evaluation splits, and 9 small seed/order robustness runs.

## Claim scope

In a 1,000-example public English toxicity corpus, a clean-reference character n-gram perplexity scorer trained on non-toxic examples preferentially ranks labeled toxic samples as high perplexity; filtering the top 5-10% highest-perplexity samples is strongly enriched for toxic samples.

## Why it stopped

Closed as no-paper useful signal: this run directly tested the filtering mechanism but did not validate end-to-end tiny pretraining behavior.

## Recommended next action

Run a bounded deepen experiment that actually pretrains parameter-matched tiny LMs on unfiltered, random-filtered, and perplexity-filtered corpora, then compares held-out LM loss and harmful-sample memorization/toxicity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny LM Pretraining With Perplexity-Filtered Toxicity Mixtures
- Success threshold: Perplexity-filtered pretraining reduces harmful memorization/toxicity by at least 25% versus unfiltered and random-filtered controls while increasing held-out benign LM loss by no more than 5%.
- Stop condition: Stop if perplexity-filtered and random-filtered runs have indistinguishable harmful memorization/toxicity or if benign LM loss degrades by more than 5% at the filter fraction needed for harm reduction.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtering-removes-harmful-samples-in-tiny-pretraining-4a22a3fead2f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
