# Commit-Reveal Anti-Copying Protocol for Volunteer Gradient Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-anti-copying-protocol-for-volunteer-gradient-validation-0a092f3ad92e`
Run ID: `commit-reveal-anti-copying-protocol-for-volunteer-gradient-validation-0a092f3ad92e-20260526T050131108976+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a7ef6cb17638

## What looked useful

Bound commit-reveal reduced reactive-copy accepted fraud from 0.90818 in the no-commit baseline to 0.0 in the model, while a weak gradient-only hash still allowed 0.87292 reactive-copy fraud and bound commit-reveal still allowed 0.97862 colluding-peer fraud.

## Boundaries and scale limits

Tested with deterministic digest stand-ins rather than real tensor gradients, real coordinator infrastructure, clock skew, retries, multi-client networking, or economic incentives; 100000 CPU Monte Carlo trials per scenario.

## Claim scope

In a synthetic deadline-enforced volunteer-gradient digest model, a SHA-256 commit-reveal protocol that binds worker_id, task_id, gradient_digest, and a secret nonce prevents reactive after-reveal copying; it does not prevent pre-deadline collusion or prove independent computation.

## Why it stopped

Closed as no-paper useful signal: the local evidence supports the narrow reactive-copy mechanism but is synthetic/proxy evidence and exposes unsolved collusion and weak-commitment failure modes.

## Recommended next action

Build a minimal coordinator/validator prototype with real gradient tensors, adversarial clients, deadline skew, and duplicate-task assignment to test whether the same reactive-copy protection holds under implementation realities.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prototype Commit-Reveal Gradient Validation Under Adversarial Clients
- Success threshold: Reactive-copy accepted fraud remains 0 across adversarial client tests while honest false rejection stays below 2 percent under a documented clock-skew budget; collusion remains explicitly measured as out of scope unless an added control is tested.
- Stop condition: Stop if reactive copying is accepted in any correctly bound implementation path, if digest canonicalization is ambiguous, or if honest false rejection exceeds 2 percent under realistic skew without a simple protocol adjustment.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-anti-copying-protocol-for-volunteer-gradient-validation-0a092f3ad92e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
