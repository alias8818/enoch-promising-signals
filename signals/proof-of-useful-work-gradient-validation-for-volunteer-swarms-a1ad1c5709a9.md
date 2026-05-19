# Proof-of-Useful-Work Gradient Validation for Volunteer Swarms

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proof-of-useful-work-gradient-validation-for-volunteer-swarms-a1ad1c5709a9`
Run ID: `proof-of-useful-work-gradient-validation-for-volunteer-swarms-a1ad1c5709a9-20260518T072539271638+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/87ce680fc6cc

## What looked useful

With 40% malicious workers computing only 25% of chunks, two random chunk checks per worker detected about 95.7-96.5% of malicious workers across random/sign-flip/stale attacks, reduced accepted bad chunks to about 1.7-2.1%, and kept final test loss near the honest baseline at 25% validator chunk overhead.

## Boundaries and scale limits

Tested only 5 seeds, one small dataset, one convex-ish model, local synchronous execution, non-adaptive attackers, and direct chunk-gradient access without cryptographic commitments, networking, latency, Sybil resistance, or large-model training.

## Claim scope

In a deterministic local simulation using softmax regression on sklearn digits, random chunk recomputation can detect lazy volunteer gradient fabrication and restore attacked training close to an honest baseline at measured verifier overhead.

## Why it stopped

No-paper useful signal: the run supports the statistical validation mechanism in a toy/proxy setting but does not provide direct production swarm, cryptographic, or large-model evidence.

## Recommended next action

Run a bounded neural-network follow-up with cryptographic-style chunk commitments and adaptive lazy attackers before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Chunk-Commitment Gradient Validation Under Adaptive Lazy Workers
- Success threshold: Validation loss within 3% of honest baseline, malicious detection rate at least 90%, accepted bad chunk rate at most 5%, honest false rejection below 1%, and verifier overhead no more than 50% of worker chunk compute.
- Stop condition: Stop if the protocol cannot meet the detection and training thresholds on the small neural model after two validator sampling budgets or if matched redundant recomputation dominates it on both loss and overhead.

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-useful-work-gradient-validation-for-volunteer-swarms-a1ad1c5709a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
