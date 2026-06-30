# Commit-Reveal Lottery Audit Against Gradient Cherry-Picking

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `commit-reveal-lottery-audit-against-gradient-cherry-picking-42021709db99`
Run ID: `commit-reveal-lottery-audit-against-gradient-cherry-picking-42021709db99-20260620T000541995778+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bbf53c67e335

## What looked useful

Across 3,000 replicates, empirical detection stayed within 0.0236 absolute error of the sampled-violation detection curve. With audit_rate 0.005, detection was 0.69 to 0.90 while auditing about 2.4 to 2.6 of 500 steps; audit_rate >= 0.02 reached at least 0.995 detection across tested settings. Cherry-picking also produced hidden side-objective drift of 0.98 to 2.03 versus honest.

## Boundaries and scale limits

No real neural-network training, no production transcript format, no distributed prover/verifier implementation, no pre-commitment manipulation adversary, and no model-scale verifier cost measurement.

## Claim scope

Synthetic protocol-level NumPy simulation: post-hoc gradient cherry-picking from a precommitted candidate set is detected by sampled commit-reveal lottery audits according to the observed violation count and audit rate.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/protocol-level rather than direct model-training validation.

## Recommended next action

Run a bounded deepen follow-up around a small real model training loop with binding gradient/minibatch commitments, honest and cherry-picked controls, and measured verifier recomputation cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model commit-reveal audit with real minibatch gradients
- Success threshold: Detection rate within 0.05 absolute error of the sampled-violation curve at two or more audit rates, measurable side-objective drift under cherry-picking, and verifier cost reported per audited step.
- Stop condition: Stop if real-model transcripts cannot be made reproducible locally, if cherry-picking creates no measurable side-objective drift, or if detection deviates by more than 0.10 absolute error after debugging transcript determinism.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-lottery-audit-against-gradient-cherry-picking-42021709db99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
