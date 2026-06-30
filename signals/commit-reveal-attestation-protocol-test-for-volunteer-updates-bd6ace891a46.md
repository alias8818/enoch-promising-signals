# Commit-Reveal Attestation Protocol Test for Volunteer Updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `commit-reveal-attestation-protocol-test-for-volunteer-updates-bd6ace891a46`
Run ID: `commit-reveal-attestation-protocol-test-for-volunteer-updates-bd6ace891a46-20260620T181112314424+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/addb2b44e416

## What looked useful

Commit-reveal increased modeled attack detection by 0.7899 to 0.8199 absolute at nonzero attack rates, reduced accepted malicious updates by 100% relative to the direct baseline, preserved 100% honest acceptance, and added roughly 63-65 ms median synthetic latency plus about two hashes per honest update.

## Boundaries and scale limits

Synthetic CPU-only protocol simulation: 1,000 rounds, 50 volunteers, attack rates 0 to 0.2, no real identities, signatures, wall-clock distributed deadline enforcement, live volunteer behavior, operator review UX, or coordinated adversarial strategy search.

## Claim scope

In a deterministic synthetic simulator with stable volunteer ids, round-bound SHA-256 commitments, one commit per volunteer per round, and reveal deadlines, commit-reveal detects or rejects modeled adaptive rewrites, equivocation, withholding, late reveals, and replay attempts that a direct last-write-wins channel partly accepts.

## Why it stopped

Synthetic mechanism support is not direct deployment evidence or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should implement a signed, trace-driven prototype with clock skew and operator review costs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed trace-driven commit-reveal volunteer update prototype
- Success threshold: Across at least 10,000 trace-driven update events, honest acceptance >= 0.99, adaptive rewrite plus equivocation detection >= 0.95, replay detection >= 0.99, and median added operator-visible latency documented below the deployment's tolerance.
- Stop condition: Stop if signed prototype false rejects exceed 1% under realistic clock skew, if operator review cannot distinguish missing reveals from benign absence, or if the protocol adds latency outside the target workflow tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-attestation-protocol-test-for-volunteer-updates-bd6ace891a46`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
