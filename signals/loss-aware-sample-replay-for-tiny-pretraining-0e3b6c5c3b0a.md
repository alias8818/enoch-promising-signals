# Loss-aware sample replay for tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `loss-aware-sample-replay-for-tiny-pretraining-0e3b6c5c3b0a`
Run ID: `loss-aware-sample-replay-for-tiny-pretraining-0e3b6c5c3b0a-20260630T024912414441+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1c0250eb2d34

## What looked useful

Raw training loss is an unsafe replay priority when high loss can reflect irreducible noise. In the primary proxy, loss-aware replay increased noisy sample fraction by 4.28 percentage points, slightly improved noise loss, and consistently worsened clean and rare-clean validation across all 3 seeds. A no-noise control was near-neutral/slightly helpful for rare-clean loss, pointing to learnability filtering as the relevant next mechanism.

## Boundaries and scale limits

Evidence is synthetic and small-scale: 2-layer 128-wide transformer, 64-token documents, 3 seeds, 500 updates per seed/strategy. It does not validate real web-corpus pretraining, tokenizer effects, downstream tasks, or larger/longer training regimes.

## Claim scope

In a controlled synthetic tiny-transformer pretraining proxy with 10% irreducible noisy documents, naive document-level raw-loss-aware replay oversampled noise and worsened clean validation loss versus uniform sampling at matched updates and samples.

## Why it stopped

Proxy early falsification of the naive raw-loss replay rule, not a full-scale validation: loss-aware replay chased irreducible high-loss noise and worsened clean held-out losses at matched compute.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded deepen follow-up comparing raw-loss replay against learnability-filtered replay on the same noisy proxy before any real-corpus scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learnability-filtered replay for noisy tiny pretraining
- Success threshold: Learnability-filtered replay must improve rare-clean validation loss by at least 5% relative to uniform without worsening clean mean validation loss and without increasing noisy sample exposure by more than 1 percentage point.
- Stop condition: Stop if the filtered rule still oversamples noise above the threshold or fails to improve rare-clean validation in at least 4 of 5 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/loss-aware-sample-replay-for-tiny-pretraining-0e3b6c5c3b0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
