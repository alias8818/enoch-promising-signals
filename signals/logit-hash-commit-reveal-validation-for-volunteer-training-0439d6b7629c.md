# Logit-Hash Commit-Reveal Validation for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `logit-hash-commit-reveal-validation-for-volunteer-training-0439d6b7629c`
Run ID: `logit-hash-commit-reveal-validation-for-volunteer-training-0439d6b7629c-20260620T210405114502+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/48917399b75b

## What looked useful

All honest reveals verified and all tampered reveals failed digest verification. Without commitments the same tampered reveals had no local cryptographic detection signal and inflated weak-volunteer proxy accept rate from 0.0226 to 1.0 in the main run; five-seed sensitivity mean inflation was 0.97972.

## Boundaries and scale limits

Evidence is synthetic and CPU-only: 5,000 main tasks plus five 5,000-task sensitivity runs. It does not test real model logits, real volunteers, deployment workflow, collusion, missing-reveal incentives, or custody of commitment publication.

## Claim scope

In a deterministic synthetic multi-choice validation workflow, SHA-256 commitments over task id, model id, quantized logits, and salt make post-hoc logit edits detectable at reveal time and prevent the simulated no-commit validator-score inflation from being accepted.

## Why it stopped

Closed as useful-signal no-paper evidence because the cryptographic audit mechanism was directly tested but volunteer-training validation was only proxied synthetically.

## Recommended next action

Run a bounded direct replay using real or archived validator logits and volunteer responses, with pre-registered commitments and explicit missing-reveal accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct replay of logit-hash commit-reveal on real volunteer validation traces
- Success threshold: At least 99.9% honest reveal verification, 100% detection of injected post-commit logit edits, and no material degradation of valid volunteer scoring on a replay set large enough to include at least 1,000 scored answers.
- Stop condition: Stop if honest reveal verification falls below 99.9%, if missing-reveal handling cannot distinguish audit failure from ordinary data loss, or if no real/replayed logits can be obtained.

## Evidence references

- Artifact root: `<local-path>/projects/logit-hash-commit-reveal-validation-for-volunteer-training-0439d6b7629c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
