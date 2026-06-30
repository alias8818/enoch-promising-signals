# Gradient fingerprint audit for volunteer federated updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-fingerprint-audit-for-volunteer-federated-updates-9237af52dbf8`
Run ID: `gradient-fingerprint-audit-for-volunteer-federated-updates-9237af52dbf8-20260609T071114766918+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed565345b183

## What looked useful

Non-IID sign-gradient retrieval reached top-1 0.7233 versus chance 0.0083, while strict IID/no-style sign-gradient retrieval was 0.0092. Unit-normalized gradients showed a similar non-IID top-1 of 0.6800; top-k and Gaussian noise reduced but did not erase raw projected linkability in the non-IID condition.

## Boundaries and scale limits

Synthetic Gaussian features, softmax classifier, fixed participation, no real volunteer population, no secure aggregation protocol implementation, and no neural model or production optimizer.

## Claim scope

In a deterministic synthetic federated-learning proxy with 120 volunteer clients, persistent non-IID label skew and client feature style produce linkable gradient fingerprints across rounds; a strict IID/no-style control stays near chance.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic mechanism probe rather than direct deployment-grade validation.

## Recommended next action

Run a bounded real-benchmark follow-up on FEMNIST or another user-partitioned dataset with a small neural model, partial participation, clipping, and DP-noise sweeps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real user-partitioned gradient fingerprint audit with clipping and DP noise
- Success threshold: At least 3x chance top-1 linkage persists for raw or sign gradients on the real non-IID benchmark, and a clipping/noise setting reduces linkage by at least 75 percent while preserving nontrivial model utility.
- Stop condition: Stop if identity-shuffled and IID controls are not near chance, or if raw/sign gradients on the real benchmark do not exceed 2x chance top-1 linkage after a reproducible small run.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-fingerprint-audit-for-volunteer-federated-updates-9237af52dbf8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
