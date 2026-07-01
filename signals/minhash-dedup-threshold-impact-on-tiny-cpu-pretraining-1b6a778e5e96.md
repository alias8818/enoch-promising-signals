# MinHash dedup threshold impact on tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-dedup-threshold-impact-on-tiny-cpu-pretraining-1b6a778e5e96`
Run ID: `minhash-dedup-threshold-impact-on-tiny-cpu-pretraining-1b6a778e5e96-20260619T205752192613+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b904a67997da

## What looked useful

Light MinHash dedup at threshold 0.95 removed about 3.3% of synthetic training documents and improved mean novel validation NLL by 0.0319 versus no dedup. More aggressive thresholds removed 7.2% to 18.2% and produced weaker or mixed gains, suggesting over-aggressive near-duplicate removal can discard useful variation in tiny pretraining.

## Boundaries and scale limits

Synthetic corpus only; 324 training documents before dedup; three seeds; tiny char MLP rather than transformer; short fixed-budget CPU training; canary NLL is only a memorization-pressure proxy. This does not validate web-scale pretraining, GPT-class models, or a universal dedup threshold.

## Claim scope

In a synthetic near-duplicate corpus with a tiny NumPy character language model trained on CPU for a fixed small token budget, MinHash threshold choice measurably affected validation NLL and canary-likelihood proxy metrics. Across three seeds, threshold 0.95 gave the best mean novel-validation NLL and highest mean canary NLL among the tested thresholds.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-scale and insufficient for publication-grade validation, despite a consistent local mechanism signal.

## Recommended next action

Run a bounded deepen follow-up on a small real public text corpus with a tiny transformer or GRU baseline, fixed sequence-item budgets, and direct memorization/extraction checks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus MinHash threshold sweep for tiny transformer pretraining
- Success threshold: At least two seeds show threshold 0.95 or a nearby light-dedup threshold improving validation perplexity by at least 1% versus no dedup while not increasing memorization metrics, and aggressive thresholds underperform light dedup.
- Stop condition: Stop if real-corpus dedup changes retained tokens by less than 1%, if validation perplexity deltas are below run-to-run noise across two seeds, or if the only improvement requires compute beyond a bounded local run.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-impact-on-tiny-cpu-pretraining-1b6a778e5e96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
