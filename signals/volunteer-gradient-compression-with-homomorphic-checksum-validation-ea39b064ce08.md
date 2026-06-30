# Volunteer gradient compression with homomorphic checksum validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-gradient-compression-with-homomorphic-checksum-validation-ea39b064ce08`
Run ID: `volunteer-gradient-compression-with-homomorphic-checksum-validation-ea39b064ce08-20260607T221345447971+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa85fc0bcc9a

## What looked useful

Protected or fixed-checksum payload tampering and random checksum forgeries were detected in 100% of synthetic trials with 0% false positives and 0.4% checksum overhead over sparse top-1% payloads, but checksum-recomputing attackers were detected in 0% of trials.

## Boundaries and scale limits

Tested only synthetic Gaussian gradients up to 50,000 dimensions, 32 volunteers, 200 main trials, and small checksum/compression ablations. No real model training, convergence, secure key distribution, trusted hardware, replicated execution, or open volunteer adversary study was run.

## Claim scope

Synthetic sparse-gradient simulations show that additive homomorphic checksum words cheaply validate aggregate payload consistency after top-k quantization, but do not validate gradient honesty when an untrusted volunteer can recompute a matching checksum for a malicious payload.

## Why it stopped

Proxy synthetic evidence produced an early trust-boundary falsification of standalone homomorphic checksum validation for untrusted volunteer gradients; this is not a full validation of distributed training.

## Recommended next action

Stop this run as a no-paper useful signal; any next bounded test should add an authentication or redundancy mechanism before evaluating real training convergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Authenticated or redundant checksums for compressed volunteer gradients
- Success threshold: Detect at least 95% of malicious recompute-capable volunteer updates with less than 1% false positives and less than 5% additional bandwidth over sparse compressed payloads in a small real-training task.
- Stop condition: Stop if recompute-capable malicious volunteers can still create payloads that pass validation without relying on external trust assumptions, or if authentication overhead erases the compression bandwidth benefit.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-gradient-compression-with-homomorphic-checksum-validation-ea39b064ce08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
