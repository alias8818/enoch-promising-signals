# CommitRevealFederatedDigest

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commitrevealfederateddigest-111c9db5a8d8`
Run ID: `commitrevealfederateddigest-111c9db5a8d8-20260619T152505596960+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/8a8b14f4b5cd

## What looked useful

Per-record commit-reveal detected all 15,351 synthetic post-commit mutations with zero false positives, but naive stale fallback increased wrong answers. Whole-round commitments collapsed to full abstention. A per-record quarantine/tombstone policy removed wrong answers while trading off 20.1% abstention.

## Boundaries and scale limits

No real agent transcripts, no natural-language summarizer, no multi-node federation, no pre-commit falsehood detection, no collusion model, and no cryptographic implementation audit. Payload overhead was measured only on compact synthetic JSON digests.

## Claim scope

Synthetic repeated-agent memory digest replay with 80 deterministic seeds, 96 clients, 10 rounds, 20% post-commit digest-record mutation, and SHA-256 commit-reveal checks.

## Why it stopped

Local synthetic evidence is useful but not paper-ready; it validates the integrity gate under a proxy attack model and exposes a recall-policy tradeoff rather than proving a real-world federated memory result.

## Recommended next action

Run a bounded direct replay on a real repeated-agent memory corpus comparing no-commit, per-record commit, and quarantine policies under injected digest tampering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus replay for CommitRevealFederatedDigest quarantine policy
- Success threshold: Per-record commit-reveal with quarantine detects at least 99% of injected post-commit mutations with zero accepted tampered records, wrong-answer rate below 1%, and abstention below 25% at a 20% mutation attack rate.
- Stop condition: Stop if quarantine abstention exceeds 40% or wrong-answer rate remains above 5% on real replay tasks at 20% mutation despite correct tamper detection.

## Evidence references

- Artifact root: `<local-path>/projects/commitrevealfederateddigest-111c9db5a8d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
