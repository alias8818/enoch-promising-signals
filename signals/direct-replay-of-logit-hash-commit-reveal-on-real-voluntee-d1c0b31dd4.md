# Direct replay of logit-hash commit-reveal on real volunteer validation traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-replay-of-logit-hash-commit-reveal-on-real-voluntee-d1c0b31dd4`
Run ID: `direct-replay-of-logit-hash-commit-reveal-on-real-voluntee-d1c0b31dd4-20260620T214057804413+0000`

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

- Parent run decision: Logit-Hash Commit-Reveal Validation for Volunteer Training: enoch://control-plane/projects/logit-hash-commit-reveal-validation-for-volunteer-training-0439d6b7629c/runs/logit-hash-commit-reveal-validation-for-volunteer-training-0439d6b7629c-20260620T210405114502+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/48917399b75b

## What looked useful

The replay verifier accepted 3/3 honest canonical reveals and rejected 3/3 tampered reveals with 0 false accepts and 0 false rejects, but the requested real-volunteer threshold was not met because no volunteer traces were present.

## Boundaries and scale limits

Six controlled fixture traces on one CPU worker; zero real volunteer traces; no networked commit timing, model-runtime float serialization, or independent provenance validation.

## Claim scope

Controlled Tier 1 fixture replay of a SHA-256 logit-hash commit-reveal verifier; not a real-volunteer validation.

## Why it stopped

Controlled mechanism replay passed, but the direct real-volunteer validation claim remains unsupported due to absent volunteer traces rather than compute limits.

## Recommended next action

Stop this run as no-paper useful mechanism evidence; next concrete action is to replay the same verifier on a small real volunteer trace bundle with pre-reveal commits and canonical revealed logits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay logit-hash commit-reveal verifier on a small real volunteer trace bundle
- Success threshold: 0 false accepts and 0 false rejects across all real volunteer traces and tamper controls; real_volunteer_trace_count >= 10.
- Stop condition: Stop as unsupported if any honest real volunteer reveal fails canonical hash verification, any tampered reveal is accepted, or provenance cannot show commits preceded reveals.

## Evidence references

- Artifact root: `<local-path>/projects/direct-replay-of-logit-hash-commit-reveal-on-real-voluntee-d1c0b31dd4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
