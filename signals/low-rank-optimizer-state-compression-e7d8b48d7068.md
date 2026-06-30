# Low-Rank Optimizer State Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-optimizer-state-compression-e7d8b48d7068`
Run ID: `low-rank-optimizer-state-compression-e7d8b48d7068-20260614T104401996296+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/49180dbfc469

## What looked useful

Rank-32 direct update compression preserved mean cosine 0.967 at 37.4% dense two-state matrix storage in post-hoc diagnostics; first-moment rank-16 and rank-32 truncation trained within about 2.2% and 1.1% final-loss delta of dense AdamW over 150 steps. Naive both-state SVD has a second-moment denominator-safety issue unless positivity is handled.

## Boundaries and scale limits

Single synthetic task, one seed, tiny transformer, short 150-300 step runs, no true factor-stored memory-saving optimizer, no real language corpus, no GPT-2-small-scale or long-horizon convergence evidence.

## Claim scope

Small GPU-trained transformer on synthetic Markov language data: AdamW first moments and oracle update directions for matrix parameters show meaningful low-rank structure, and post-step rank truncation of optimizer state can preserve short-run training behavior.

## Why it stopped

This run produced a useful small-scale mechanism signal, but it remains a proxy for real optimizer memory savings and is not full validation or paper-ready evidence.

## Recommended next action

Implement a true factor-stored low-rank Adam variant with positive second-moment representation and compare multi-seed GPT-2-small-class training on a real text dataset against AdamW and Adafactor-style baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Factor-stored positive low-rank Adam on real small-language-model training
- Success threshold: At least 30% optimizer-state memory reduction versus AdamW with validation loss within 1% of AdamW and no more than 20% throughput regression on the selected GPT-2-small-class task.
- Stop condition: Stop if the factor-stored implementation cannot maintain positive second moments, exceeds 20% throughput regression at small scale, or loses more than 1% validation performance versus AdamW across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-optimizer-state-compression-e7d8b48d7068`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
