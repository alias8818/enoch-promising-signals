# Substring Dedup Threshold Sweep for Tiny Pretraining Corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `substring-dedup-threshold-sweep-for-tiny-pretraining-corpora-959c648c2703`
Run ID: `substring-dedup-threshold-sweep-for-tiny-pretraining-corpora-959c648c2703-20260612T211934712196+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2961e3a1fc9d

## What looked useful

Aggressive substring dedup removed about 67.5% of documents and reduced boilerplate memorization, but no-dedup had the best mean validation loss and best-threshold identity was seed-sensitive. Retention and duplicate-pressure metrics alone are insufficient to justify a threshold for tiny pretraining corpora.

## Boundaries and scale limits

Synthetic corpus only; character-level GRU only; 320 optimizer steps per threshold; no real pretraining corpus, GPT-2-small-class Transformer, tokenizer study, downstream task, or long-run convergence validation.

## Claim scope

Controlled synthetic tiny-corpus proxy: substring-containment dedup thresholds strongly changed retained document count and boilerplate memorization, but did not produce a robust validation-loss improvement for a small character LM over five seeds.

## Why it stopped

Proxy early falsification: controlled local evidence did not support a robust validation-loss benefit from substring dedup threshold sweeping, though it did show the expected retention and memorization mechanism.

## Recommended next action

Stop this run as a no-paper useful signal; a next bounded test should use a real tiny corpus with documented near-duplicates and a tokenizer-matched small Transformer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny-Corpus Substring Dedup Sweep With Small Transformer
- Success threshold: An intermediate threshold improves mean held-out loss by at least 1% versus no dedup and beats aggressive dedup across at least 3 seeds while retaining at least 60% of source tokens.
- Stop condition: Stop if the real corpus has negligible near-duplicate mass, if no threshold beats no dedup by the predefined margin, or if the result remains seed-sensitive after three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/substring-dedup-threshold-sweep-for-tiny-pretraining-corpora-959c648c2703`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
