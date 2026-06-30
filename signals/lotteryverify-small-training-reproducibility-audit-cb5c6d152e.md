# LotteryVerify Small Training Reproducibility Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lotteryverify-small-training-reproducibility-audit-cb5c6d152e`
Run ID: `lotteryverify-small-training-reproducibility-audit-cb5c6d152e-20260610T063453004172+0000`

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

- Parent run decision: LotteryVerify: Sparse Subnet Assignment with Deterministic Reproducibility Audit: enoch://control-plane/projects/lotteryverify-sparse-subnet-assignment-with-deterministic-reproducibility-audit-46b61f88451b/runs/lotteryverify-sparse-subnet-assignment-with-deterministic-reproducibility-audit-46b61f88451b-20260610T020724973684+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7d69054757c

## What looked useful

Zero false positives across 80 honest replayed steps; 16/16 tamper-detection grid cells had the theoretical detection probability inside the empirical 95% Wilson interval; mean absolute empirical-theory gap was 0.0125 over 400 trials per cell.

## Boundaries and scale limits

Small favorable setting only: synthetic data, tiny MLP, SGD without momentum, single-process GB10 CUDA execution, simple skip-update tampering, no distributed training, no cryptographic overhead measurement, no adaptive adversary, and no realistic transformer-scale data pipeline.

## Claim scope

On a deterministic 80-step CUDA training trace for a tiny MLP on synthetic classification data, honest optimizer-step replay is exactly reproducible and randomized audits detect injected invalid post-step commitments at probabilities matching 1 - (1 - alpha)^m.

## Why it stopped

Tier 1 direct small test supports the bounded mechanism but is not publication-grade evidence; stopping as no-paper useful signal rather than over-claiming a tiny favorable setup.

## Recommended next action

Run one bounded deepen test on a larger realistic small model with multiple tamper classes and verifier-cost measurements before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LotteryVerify tamper-class audit on a realistic small model
- Success threshold: Honest replay false-positive rate <= 0.1% at declared tolerance, all tested tamper classes' theoretical detection probabilities inside 95% empirical intervals or within 0.05 absolute error, and verifier cost <= 10x audited-step training cost for the tested setup.
- Stop condition: Stop if honest replay is not deterministic under fixed seeds/tolerances, if any tamper class falls below the success threshold after enough trials, or if verifier cost makes the mechanism impractical for the tested small-model setting.

## Evidence references

- Artifact root: `<local-path>/projects/lotteryverify-small-training-reproducibility-audit-cb5c6d152e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
