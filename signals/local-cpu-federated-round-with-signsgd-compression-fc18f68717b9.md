# Local CPU Federated Round with SignSGD Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cpu-federated-round-with-signsgd-compression-fc18f68717b9`
Run ID: `local-cpu-federated-round-with-signsgd-compression-fc18f68717b9-20260524T013757961675+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d24ceda12ad

## What looked useful

SignSGD-style one-bit client upload is viable as a local compression mechanism under IID and mild feature-shift synthetic clients, but the same mechanism shows a measurable accuracy penalty under label skew, indicating that majority sign aggregation can lose important minority-client gradient magnitude information.

## Boundaries and scale limits

Synthetic binary classification only; no real federated benchmark, deep model, secure aggregation, client systems effects, multi-epoch local training, or long-run robustness validation.

## Claim scope

In a synthetic CPU-only federated logistic-regression probe with 24 clients, 128 dimensions, 80 synchronous rounds, and 5 seeds, one-bit sign-majority client updates preserved IID accuracy within 0.12 percentage points of dense FedAvg at 32x upload compression, stayed within 0.69 points under synthetic feature shift, and lost 2.54 points under synthetic label skew.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and mixed, not a direct or publication-grade validation.

## Recommended next action

Run a bounded real-dataset follow-up comparing dense FedAvg and sign-majority updates on fixed non-IID client partitions with learning-rate sweeps before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset non-IID SignSGD federated compression check
- Success threshold: Confirm the synthetic pattern: sign-majority within 1 percentage point of dense on IID partitions with 32x upload compression, plus a clearly measured label-skew degradation or mitigation effect.
- Stop condition: Stop if sign-majority is more than 3 percentage points worse than dense on IID partitions after tuned learning rates, or if real-dataset setup cannot be reproduced locally.

## Evidence references

- Artifact root: `<local-path>/projects/local-cpu-federated-round-with-signsgd-compression-fc18f68717b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
