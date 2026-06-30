# Dedup-threshold sweep for tiny pretraining corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dedup-threshold-sweep-for-tiny-pretraining-corpora-b74e0b8f7e34`
Run ID: `dedup-threshold-sweep-for-tiny-pretraining-corpora-b74e0b8f7e34-20260611T220947225179+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c05ce8741705

## What looked useful

For tiny corpora, threshold sweeps should track both validation loss and collateral unique-document deletion. In this controlled run, the best clean-loss threshold removed about 51 unique documents on average, so validation-only selection would choose a risky threshold.

## Boundaries and scale limits

Synthetic corpus only; approximately 338 training documents before dedup; 350 training steps per condition; character-level modeling; no real public pretraining corpus, standard tokenizer, GPT-2-small-class baseline, or full-scale training validation.

## Claim scope

Controlled synthetic tiny-corpus experiment with character 5-shingle Jaccard near-deduplication and a tiny Transformer language model shows that dedup thresholds have non-monotonic effects: threshold 0.70 slightly improved clean held-out loss versus no dedup over 10 paired seeds, while threshold 0.80 was worse and high thresholds were neutral.

## Why it stopped

No-paper useful signal: the result is direct for a controlled synthetic proxy but not a full validation on real pretraining data.

## Recommended next action

Run a bounded real-corpus deepen test on a 1-10M token public subset with injected and naturally occurring near-duplicates, paired seeds, retained-token accounting, duplicate-removal precision, and clean held-out validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-corpus dedup threshold sweep with retention accounting
- Success threshold: A threshold must improve paired clean validation loss by at least 0.01 nats or one paired standard error versus no dedup while deleting less than 5% audited unique documents/tokens; otherwise conclude no robust local benefit.
- Stop condition: Stop after the bounded real-corpus sweep if no threshold beats no dedup by the success threshold or if the best threshold requires unacceptable unique-token collateral deletion.

## Evidence references

- Artifact root: `<local-path>/projects/dedup-threshold-sweep-for-tiny-pretraining-corpora-b74e0b8f7e34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
