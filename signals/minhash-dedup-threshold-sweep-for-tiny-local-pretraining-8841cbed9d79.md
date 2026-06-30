# MinHash dedup threshold sweep for tiny local pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `minhash-dedup-threshold-sweep-for-tiny-local-pretraining-8841cbed9d79`
Run ID: `minhash-dedup-threshold-sweep-for-tiny-local-pretraining-8841cbed9d79-20260620T082824332657+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd9b07e16388

## What looked useful

Threshold 0.55 collapsed all three seeded corpora to one retained document. Threshold 0.70 removed many true duplicates but also a mean 44.3 hard non-duplicates and worsened clean loss by 0.00236. Threshold 0.82 removed a mean 73 true duplicates, only 1.3 hard non-duplicates, and was best in all three seeds with mean clean-loss delta -0.000717 versus no dedup.

## Boundaries and scale limits

Synthetic corpus only; 360 train families and 80 eval families per seed; 2-layer 128-dim tiny Transformer; 260 steps per threshold; not validated on real web/code corpora or long fixed-token pretraining.

## Claim scope

On a controlled synthetic tiny-pretraining corpus with true near-duplicates and hard non-duplicate neighbors, a conservative MinHash threshold near 0.82 removed duplicates with minimal false-positive data loss and slightly improved clean held-out loss across three seeds; lower thresholds were harmful or collapsed the corpus.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and small; the result guides a bounded real-corpus follow-up but is not a full validation.

## Recommended next action

Run the same threshold sweep on a small real corpus with fixed-token budgets and duplicate/memorization validation slices before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus MinHash threshold sweep with fixed-token tiny pretraining
- Success threshold: A threshold band must remove at least 20% of near-duplicate candidates, keep audited false-positive removals below 5%, and improve or match clean validation loss within 0.001 versus no dedup across at least two of three seeds.
- Stop condition: Stop if all trainable thresholds either worsen clean validation loss by more than 0.002 or require false-positive removals above 10% to remove meaningful duplicate volume.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-sweep-for-tiny-local-pretraining-8841cbed9d79`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
