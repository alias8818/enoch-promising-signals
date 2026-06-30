# VerifiableLabelAttestation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `verifiablelabelattestation-0ad25d9da43b`
Run ID: `verifiablelabelattestation-0ad25d9da43b-20260619T173447550534+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/8a8b14f4b5cd

## What looked useful

Across one main run and five additional seeds, verified labels had hit_rate@5 1.0, leak_rate@5 0.0, and forged_return_rate 0.0. Asserted-label filtering leaked forged records at mean leak_rate@5 0.72625 in the sweep.

## Boundaries and scale limits

Synthetic corpus only; deterministic keyword/salience retrieval; HMAC local secret rather than deployed public-key provenance; no vector database, live LLM memory traces, key rotation, replay resistance, or latency study.

## Claim scope

In a deterministic synthetic repeated-agent memory benchmark with HMAC-bound tenant/topic labels and forged asserted-label poisoning, verifiable label attestation eliminated cross-label top-k leaks while preserving hit rate.

## Why it stopped

Synthetic useful-signal proxy completed; evidence is not direct or broad enough for paper-positive closure.

## Recommended next action

Run a bounded deepen test using a real vector store and LLM-generated repeated-agent memory traces with signed provenance and adversarial metadata poisoning.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Vector-store VerifiableLabelAttestation under LLM memory poisoning
- Success threshold: Verified-label retrieval cuts leak_rate@k by >=90% relative to asserted-label filtering, has forged_return_rate <=1%, preserves >=95% of clean recall, and adds <=20% retrieval latency in the bounded setup.
- Stop condition: Stop if verified-label retrieval leaks forged records above 5%, loses more than 10% clean recall, or the vector-store/LLM trace setup cannot be reproduced locally with machine-readable artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/verifiablelabelattestation-0ad25d9da43b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
