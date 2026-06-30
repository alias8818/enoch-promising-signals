# Gradient Compression for Volunteer Home Distributed Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-compression-for-volunteer-home-distributed-training-e42555ae870c`
Run ID: `gradient-compression-for-volunteer-home-distributed-training-e42555ae870c-20260608T063212286525+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f79dba4e738d

## What looked useful

Across three seeds, adaptive error-feedback top-k achieved mean validation accuracy 0.7974 versus dense 0.7965, used 0.2002x dense upload bytes, and used 0.6053x dense simulated wall-clock. Naive 1% top-k was a clear negative control at -0.1877 accuracy delta; 1% top-k with error feedback reduced the gap to -0.0316.

## Boundaries and scale limits

Synthetic data, logistic regression only, no real WAN transport, no packet loss or latency jitter, no secure aggregation overhead, no adversarial clients, no large neural-network gradients, and no true volunteer multi-host execution.

## Claim scope

In a local NumPy simulation of synchronous distributed logistic-regression SGD with 32 non-IID clients and heterogeneous home-like uplinks, bandwidth-adaptive top-k sparsification with error feedback matched dense validation accuracy while reducing uploaded bytes to about 20% of dense and simulated wall-clock to about 61% of dense.

## Why it stopped

No-paper closure: the result is a bounded synthetic useful signal, not direct volunteer home distributed training validation.

## Recommended next action

Run a process-separated small-model experiment over emulated WAN links with tc/netem to test end-to-end time-to-accuracy, serialization overhead, and churn under the same dense, fixed top-k, error-feedback, and adaptive error-feedback schemes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: WAN-emulated adaptive error-feedback gradient compression
- Success threshold: Adaptive error feedback is within 1 percentage point of dense final accuracy, uses <=30% of dense upload bytes, and reaches the dense target accuracy at least 20% faster end-to-end across at least three seeds.
- Stop condition: Stop if adaptive error feedback loses more than 2 accuracy points versus dense in two seeds, or if measured overhead reduces time-to-accuracy improvement below 10% despite upload savings.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-compression-for-volunteer-home-distributed-training-e42555ae870c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
