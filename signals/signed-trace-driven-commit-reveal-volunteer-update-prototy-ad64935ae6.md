# Signed trace-driven commit-reveal volunteer update prototype

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `signed-trace-driven-commit-reveal-volunteer-update-prototy-ad64935ae6`
Run ID: `signed-trace-driven-commit-reveal-volunteer-update-prototy-ad64935ae6-20260620T184132127639+0000`

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

- Parent run decision: Commit-Reveal Attestation Protocol Test for Volunteer Updates: enoch://control-plane/projects/commit-reveal-attestation-protocol-test-for-volunteer-updates-bd6ace891a46/runs/commit-reveal-attestation-protocol-test-for-volunteer-updates-bd6ace891a46-20260620T181112314424+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/addb2b44e416

## What looked useful

Commit binding over nonce, update payload, and trace root plus signed commit/reveal envelopes produced a clean mechanism signal: honest accept rate 1.0, adversarial reject rate 1.0, and naive adversarial accept rate 1.0 across the controlled Tier 1 cases.

## Boundaries and scale limits

Synthetic traces, local single-process verifier, 5 trials with 8 volunteers each, prototype textbook RSA signatures, no distributed timing, no production cryptographic implementation, no privacy analysis, and no quorum or large-coordinator throughput test.

## Claim scope

A deterministic local Tier 1 prototype accepted honest signed trace-driven commit/reveal volunteer updates and rejected targeted tampering, trace mutation, forged identity, replay, missing commit, late reveal, and equivocal commit cases.

## Why it stopped

Tier 1 direct mechanism test passed, but evidence is synthetic and prototype-scoped, so this is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up replacing prototype RSA with production signatures and adding a small asynchronous coordinator/network schedule to test reveal timing, duplicate delivery, and quorum aggregation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-signature asynchronous commit/reveal coordinator test
- Success threshold: Across at least 20 deterministic seeds with at least 16 volunteers per seed, honest update acceptance is at least 0.99, targeted adversarial rejection is 1.0, and quorum aggregate output matches the honest reference in all non-byzantine-majority scenarios.
- Stop condition: Stop if any validly signed tampered trace/update is accepted, any replay/equivocation changes the accepted aggregate, or honest acceptance drops below 0.99 after implementation defects are ruled out.

## Evidence references

- Artifact root: `<local-path>/projects/signed-trace-driven-commit-reveal-volunteer-update-prototy-ad64935ae6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
