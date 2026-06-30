# Randomized-Sparsity Gradient Verification for Volunteer CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `randomized-sparsity-gradient-verification-for-volunteer-cpu-training-14891686edcc`
Run ID: `randomized-sparsity-gradient-verification-for-volunteer-cpu-training-14891686edcc-20260621T094030734121+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/14bbe7f1f354

## What looked useful

Sparse randomized gradient checks are a useful probabilistic spot-check against broad blind corruption, with zero false positives in this bounded run, but direct sparse recomputation has mixed speedups because residual computation is still dense and sample-aware corruption evades the check.

## Boundaries and scale limits

Tested one deterministic synthetic mini-batch at dim=4096 and batch=512 with 80 trials per detection cell. Did not test large neural-network training, real volunteer clients, network protocols, optimizer state, repeated aggregation, or cryptographic commitment.

## Claim scope

Bounded CPU synthetic logistic-regression evidence: secret randomized coordinate checks detect broad blind submitted-gradient corruption with probability matching sampled-coordinate intersection, but do not provide standalone robust verification.

## Why it stopped

No-paper closure: the local proxy produced useful mechanism evidence but also showed core limits in cost and adaptive evasion; it is not a full validation of volunteer CPU training.

## Recommended next action

Run a bounded multi-worker simulated training-loop follow-up with hidden per-round verifier samples and a small neural network before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hidden-sample sparse gradient verification in simulated volunteer training
- Success threshold: At sample fraction <= 2%, reject >= 95% of workers corrupting >= 10% of coordinates, keep honest false positives <= 1%, preserve final validation loss within 5% of dense verification, and show verifier wall-clock overhead lower than dense verification.
- Stop condition: Stop if sample-aware or low-density attacks remain undetected under the commit-before-sample protocol, if sparse neural backprop is not cheaper than dense verification, or if honest false positives exceed 1%.

## Evidence references

- Artifact root: `<local-path>/projects/randomized-sparsity-gradient-verification-for-volunteer-cpu-training-14891686edcc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
