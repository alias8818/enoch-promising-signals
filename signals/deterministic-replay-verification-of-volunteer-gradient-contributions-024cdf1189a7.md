# Deterministic Replay Verification of Volunteer Gradient Contributions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-replay-verification-of-volunteer-gradient-contributions-024cdf1189a7`
Run ID: `deterministic-replay-verification-of-volunteer-gradient-contributions-024cdf1189a7-20260609T183129739976+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d107f24872fd

## What looked useful

Across 640 contributions with 94 malicious submissions, full replay verification rejected all 94 malicious contributions and falsely rejected 0 of 546 honest contributions; max honest replay difference was 0.0 and the repeat run matched stable fields and final model hashes exactly. Partial verification caught roughly the sampled fraction and accepted unsampled malicious contributions.

## Boundaries and scale limits

Does not test cross-hardware CPU/GPU nondeterminism, large models, real volunteer networks, privacy-preserving data access, signed transport, optimizer-state edge cases, or adaptive adversaries. Sampling verification only detects malicious work when that contribution is sampled.

## Claim scope

Single-process NumPy float64 softmax-regression simulation with fixed model snapshots, fixed batch identities, transcript hashes, and non-adaptive tampering attacks. In this scope, deterministic replay exactly reproduced honest gradients and rejected every malicious contribution that was sampled for verification.

## Why it stopped

No-paper useful signal: local deterministic replay mechanism worked in a toy direct protocol test, but heterogeneous real-world volunteer verification remains unvalidated.

## Recommended next action

Run a bounded cross-hardware deterministic replay test using a real training stack and signed transcripts before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-hardware deterministic replay verification with signed volunteer transcripts
- Success threshold: At least 1000 honest cross-environment replays with false reject rate below 0.1% under a predeclared tolerance, plus 100% rejection of sampled sign-flip, scaling, stale-model, wrong-batch, and loss-only tampering attacks.
- Stop condition: Stop if deterministic settings cannot keep honest replay below tolerance on the first 200 cross-environment replays, or if replay overhead exceeds 2x generation time for the bounded model without a credible optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-verification-of-volunteer-gradient-contributions-024cdf1189a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
