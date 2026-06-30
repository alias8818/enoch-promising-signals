# Cheating-Resistant Gradient Verification for Volunteer GB10 Cluster

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheating-resistant-gradient-verification-for-volunteer-gb10-cluster-e193a82ad58e`
Run ID: `cheating-resistant-gradient-verification-for-volunteer-gb10-cluster-e193a82ad58e-20260619T140832396407+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fbfae992bbdc

## What looked useful

Random-coordinate audits are good tripwires when cheating changes many coordinates, but a worker changing 0.1% of coordinates evades small audits at the predicted sampling rate; k=256 detected top-k reversal only 23.3%, while k around 2995 would be needed for about 95% one-round detection.

## Boundaries and scale limits

Synthetic dense/sparse logistic gradients only; no distributed volunteers, no neural-network backward pass, no CUDA training, no cryptographic commitments, and no repeated-round adversarial economics. Main run was CPU-only and completed in 36.54 seconds.

## Claim scope

In a reproducible logistic-regression proxy with 20000-dimensional gradients, batch size 256, and 30 trials per condition, post-commit random-coordinate audits cheaply detect broad or lazy gradient cheating but do not provide standalone cheating resistance against sparse coordinate modifications.

## Why it stopped

Proxy evidence falsified the standalone cheap coordinate-audit mechanism against sparse adversarial edits; this is not a full distributed-training validation.

## Recommended next action

Do not pursue standalone random-coordinate audits as the verifier; run a bounded follow-up comparing weighted/top-k audits or verifier-efficient random sketches on a small PyTorch MLP.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-efficient sketches for sparse gradient cheating
- Success threshold: At least 95% detection of 0.1% sparse harmful coordinate edits with verifier cost below 25% of full gradient recomputation on the tested model.
- Stop condition: Stop if sketch or weighted-audit verifier cost approaches full recomputation, or if detection remains below 90% at the 25% verifier-cost budget.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-gradient-verification-for-volunteer-gb10-cluster-e193a82ad58e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
