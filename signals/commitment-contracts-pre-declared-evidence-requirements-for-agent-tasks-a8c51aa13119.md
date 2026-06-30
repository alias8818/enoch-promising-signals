# Commitment Contracts: Pre-Declared Evidence Requirements for Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commitment-contracts-pre-declared-evidence-requirements-for-agent-tasks-a8c51aa13119`
Run ID: `commitment-contracts-pre-declared-evidence-requirements-for-agent-tasks-a8c51aa13119-20260525T204401688413+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f235eb42fe48

## What looked useful

Commitment contracts reliably caused a pre-answer evidence declaration and improved required-evidence inclusion from 0.542 to 0.750, but grounded success moved from 0.542 to 0.500 and decoy citations increased from 0.250 to 0.354.

## Boundaries and scale limits

Single local instruction model, deterministic decoding, short synthetic documents, no real agent tool traces, no human adjudication, and no multi-model robustness check.

## Claim scope

On a 48-task synthetic document-grounding benchmark with Qwen/Qwen2.5-3B-Instruct, pre-declared evidence contracts increased required-evidence citation but did not improve combined grounded answer success.

## Why it stopped

Proxy local evidence is mixed: the simple pre-declared contract helps identify required evidence but does not improve final grounded success, so it is not paper-ready as stated.

## Recommended next action

Run a bounded follow-up that separates evidence-considered from evidence-supporting-final-answer and adds a final citation validator; stop if decoy citation remains above baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validated Commitment Contracts With Separate Support Citations
- Success threshold: Contract-plus-validator grounded success improves by at least 10 percentage points over baseline and decoy citation rate is no higher than baseline.
- Stop condition: Stop if grounded success does not improve over baseline or decoy citation rate remains above baseline on the paired benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/commitment-contracts-pre-declared-evidence-requirements-for-agent-tasks-a8c51aa13119`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
