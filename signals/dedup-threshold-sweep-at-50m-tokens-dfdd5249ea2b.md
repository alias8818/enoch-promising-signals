# Dedup Threshold Sweep at 50M Tokens

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dedup-threshold-sweep-at-50m-tokens-dfdd5249ea2b`
Run ID: `dedup-threshold-sweep-at-50m-tokens-dfdd5249ea2b-20260629T015657805100+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f57fe012b74

## What looked useful

A 100,000-train-document, 50,000,000-token-equivalent sweep found a sharp threshold cliff: 0.70 achieved 100% labeled contamination recall with 38.75M retained tokens, 0.80 retained 39.8445M tokens but missed 2,189 contaminated docs, and 0.88 retained 49.7655M tokens but missed 22,031 of 22,500 contaminated docs.

## Boundaries and scale limits

Synthetic token-id corpus only; no natural web text, no downstream language-model training, no production MinHash/LSH stack, and one fixed set of document length, duplicate variant rate, benign relative rate, and sketch size.

## Claim scope

In a deterministic synthetic 50M-token-equivalent corpus with known train/validation near-duplicate lineage, dedup threshold choice strongly controls the tradeoff between contamination recall and retained training tokens. Threshold 0.70 removed all labeled contamination with no clean false positives but retained only 77.5% of tokens; thresholds at or above 0.85 retained at least 94.0% of tokens but missed most labeled contamination.

## Why it stopped

Closed as no-paper useful signal: the result is direct for a controlled synthetic threshold sweep but proxy-only for natural corpora and downstream model behavior.

## Recommended next action

Run a bounded real-text deepen test on a 50M-token public corpus slice with exact/MinHash shingling and a small LM contamination-vs-clean validation check before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Text 50M Dedup Threshold Sweep With Small-LM Validation
- Success threshold: A threshold band must achieve at least 95% contamination-probe recall, no more than 1% clean false-positive removal, and no worse than 2% relative clean validation loss degradation versus a high-retention baseline.
- Stop condition: Stop if no threshold reaches 80% contamination-probe recall below 5% clean false-positive removal, or if small-LM validation shows no memorization reduction at matched retained-token budgets.

## Evidence references

- Artifact root: `<local-path>/projects/dedup-threshold-sweep-at-50m-tokens-dfdd5249ea2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
