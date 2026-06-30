# Surprise-Scored Data Pruning for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `surprise-scored-data-pruning-for-tiny-pretraining-8bc950c26145`
Run ID: `surprise-scored-data-pruning-for-tiny-pretraining-8bc950c26145-20260519T224323422391+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/66d2e6062b08

## What looked useful

High-surprise retention was consistently harmful at 25% and 50% retention, up to +0.050841 NLL / 5.2% relative perplexity for an order-5 target at 25% retention. Low-surprise retention was also generally worse than random. Middle-surprise retention produced only tiny improvements over the random mean, about 0.02% to 0.25% relative perplexity, suggesting surprise may be more useful as an outlier/diversity filter than as a monotone keep-high-surprise rule.

## Boundaries and scale limits

No neural transformer training, no subword tokenization, no large or diverse corpus, and no datacenter-scale pretraining were run. Results apply only to the tiny count-based character LM proxy and should not be presented as full pretraining validation.

## Claim scope

In a small public-domain English-text proxy with fixed 512-character chunks, a weak char 3-gram surprise scorer, and char 3-gram/5-gram target LMs, monotone surprise pruning did not beat equal-token random pruning; high-surprise and low-surprise retention were usually worse, while middle-surprise retention was only marginally better at some budgets.

## Why it stopped

Proxy early falsification of simple monotone surprise-scored pruning: the local count-LM evidence does not support retaining high-surprise or low-surprise chunks, and the middle-surprise signal is too small for a paper-ready claim.

## Recommended next action

Run one bounded neural follow-up using a tiny transformer or GPT-2-small-class model with equal token budgets, multiple random seeds, and middle-surprise filtering versus random before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Middle-surprise filtering for tiny neural LM pretraining
- Success threshold: Middle-surprise retention improves validation loss over the random baseline by at least 1% relative perplexity at one retention budget and is not worse than random at the other tested budgets.
- Stop condition: Stop if middle-surprise retention fails to beat random by 1% relative perplexity or if high/low/middle surprise policies are all within random-seed noise.

## Evidence references

- Artifact root: `<local-path>/projects/surprise-scored-data-pruning-for-tiny-pretraining-8bc950c26145`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
