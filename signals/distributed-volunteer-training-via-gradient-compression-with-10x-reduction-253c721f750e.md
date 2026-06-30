# Distributed Volunteer Training via Gradient Compression with 10x Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `distributed-volunteer-training-via-gradient-compression-with-10x-reduction-253c721f750e`
Run ID: `distributed-volunteer-training-via-gradient-compression-with-10x-reduction-253c721f750e-20260605T040406521852+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/53456ebdc033

## What looked useful

10x measured communication reduction is plausible for top-k compression in bounded non-IID/dropout toy training, but the method choice matters: random-k fails on dense and low-availability stress cases, and stale error-feedback residuals can hurt when worker participation drops.

## Boundaries and scale limits

Synthetic logistic-regression only; no real volunteer network, no transformer/GPT-2-scale model, no asynchronous stragglers, no adversarial workers, no serialization or transport overhead, and no long wall-clock convergence validation.

## Claim scope

In a CPU toy simulator for synchronous logistic regression with 16 non-IID volunteer-style workers and random availability, value-aware top-k gradient compression sent 5% of coordinates and achieved about 10.05x measured byte reduction including index overhead while preserving final test accuracy within 1 percentage point of dense training on sparse and dense synthetic targets. Random-k was unreliable, and naive error feedback was fragile under low availability on the dense-signal stress case.

## Why it stopped

No-paper useful signal: the evidence is reproducible and directly measures the 10x compression mechanism in a toy distributed setting, but it is still proxy/synthetic evidence rather than full volunteer training validation.

## Recommended next action

Run a bounded deepen follow-up that tests residual decay, clipping, or reset policies for error-feedback top-k under low volunteer availability before attempting larger neural-model validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stale Residual Control for Error-Feedback Top-k Under Volunteer Dropout
- Success threshold: At active probability 0.30 on dense and sparse scenarios, an error-feedback variant must achieve >=10x measured byte reduction and <=0.01 absolute accuracy gap versus dense, without increasing loss materially relative to top-k without error feedback.
- Stop condition: Stop if all residual-control variants miss the <=0.01 accuracy-gap threshold on the dense low-availability scenario or if they provide no improvement over top-k without error feedback.

## Evidence references

- Artifact root: `<local-path>/projects/distributed-volunteer-training-via-gradient-compression-with-10x-reduction-253c721f750e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
