# Commit-Reveal Checkpoint Scheme for Volunteer CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-checkpoint-scheme-for-volunteer-cpu-pretraining-2f97a344b47e`
Run ID: `commit-reveal-checkpoint-scheme-for-volunteer-cpu-pretraining-2f97a344b47e-20260620T111501962650+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f35330e45f6f

## What looked useful

Commit-reveal is useful as an integrity and lineage layer, reducing malicious accept rate from 100% under naive reveal-only submission to 2.20% in this simulation. The remaining accepted attacks were low-effort honestly committed checkpoints that did not regress validation loss, showing the scheme is insufficient as a standalone volunteer pretraining validation mechanism.

## Boundaries and scale limits

Synthetic 96-dimensional regression, 8 seeds, 1536 submissions, local validation gate, no language-model pretraining, no network adversary, no Sybil economics, and no proof-of-learning or reproducible gradient audit.

## Claim scope

Bounded synthetic protocol simulation shows commit-reveal checkpointing reliably detects post-commit tampering, stale parent replay, wrong-round replay, and gross validation regressions, but does not by itself prove claimed volunteer CPU training work.

## Why it stopped

Proxy early falsification of the standalone commit-reveal trust claim: the protocol proves committed bytes and lineage, but accepted 17 of 113 low-effort honestly committed checkpoints because useful computation was not directly proven.

## Recommended next action

Stop this run as no-paper useful evidence; any next bounded test should add a proof-of-work/proof-of-learning layer or blinded gradient spot checks and measure whether it closes the accepted lazy-checkpoint failure mode.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded Gradient Spot Checks for Commit-Reveal Volunteer Checkpoints
- Success threshold: Detect at least 99% of malicious submissions overall and at least 99% of lazy_noise_committed attacks while keeping honest false rejects below 1% and verifier cost below 10% of worker training cost in the toy setup.
- Stop condition: Stop if lazy committed checkpoints still pass above 1% or if verifier spot-check cost approaches full recomputation, because the mechanism would not be useful for volunteer CPU pretraining.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-checkpoint-scheme-for-volunteer-cpu-pretraining-2f97a344b47e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
