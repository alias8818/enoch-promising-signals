# Bounded Gradient Compression for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-gradient-compression-for-volunteer-training-6673c15f2037`
Run ID: `bounded-gradient-compression-for-volunteer-training-6673c15f2037-20260613T071801984813+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e553faf733bb

## What looked useful

Bounded error feedback was the key mechanism: 5% Top-K with bounded error feedback reached 0.8497 mean accuracy versus 0.8496 for dense clipped, while 5% Top-K without error feedback fell to 0.7855 at the same estimated byte ratio. More aggressive 1% Top-K and sign-only compression saved more bytes but degraded accuracy.

## Boundaries and scale limits

This does not validate full volunteer training, asynchronous real networks, heterogeneous devices, adversarial clients, or neural models such as CNNs, transformers, or GPT-2-small-class baselines. Byte counts are payload estimates, not transport measurements.

## Claim scope

In a deterministic CPU-only non-IID federated logistic-regression proxy with 40 clients, 60% client participation, 128-dimensional gradients, and five seeds, 5% sparse compression with bounded error feedback matched dense-clipped test accuracy while using about 8.2% of estimated dense uplink bytes and keeping transmitted update norms within the configured bound.

## Why it stopped

Closed as no-paper useful signal because the evidence is a convex local proxy, not direct volunteer neural-training validation.

## Recommended next action

Run a bounded deepen follow-up on a small neural model and real dataset, reusing the same norm-bound, residual-bound, byte-accounting, and no-error-feedback controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Error-Feedback Compression on a Small Neural Federated Task
- Success threshold: Mean compressed-model accuracy is at least 95% of dense-clipped accuracy, estimated uplink byte ratio is at most 0.10, and transmitted update norms never exceed the configured bound.
- Stop condition: Stop if the compressed model falls below 90% of dense-clipped accuracy in a smoke or medium run, if residual bounding causes persistent divergence, or if the run requires datacenter-scale training outside this deployment.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-gradient-compression-for-volunteer-training-6673c15f2037`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
