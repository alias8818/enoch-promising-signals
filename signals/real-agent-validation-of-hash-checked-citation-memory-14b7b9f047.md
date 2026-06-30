# Real-Agent Validation of Hash-Checked Citation Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-agent-validation-of-hash-checked-citation-memory-14b7b9f047`
Run ID: `real-agent-validation-of-hash-checked-citation-memory-14b7b9f047-20260609T133705271809+0000`

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

- Parent run decision: Long-Context Agent Memory With Hash-Checked Citation Pointers: enoch://control-plane/projects/long-context-agent-memory-with-hash-checked-citation-pointers-75bff08e4fc6/runs/long-context-agent-memory-with-hash-checked-citation-pointers-75bff08e4fc6-20260609T090602569956+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3ea99510e448

## What looked useful

Hash-checked citation handles are practical for a local real agent to emit in short tasks and deterministic hash verification catches altered citation handles, but this controlled run did not show an advantage over ID-only because the ID-only baseline had zero accepted unsupported outputs.

## Boundaries and scale limits

Synthetic snippets, one local 7B model, single-turn prompts, no real literature corpus, no browser/retrieval stack, no naturally occurring stale-handle failures in the ID-only baseline.

## Claim scope

In a 12-task synthetic single-turn local Qwen2.5-7B citation-memory test, the model correctly emitted both ID-only and ID+hash citations; hash verification accepted all valid hash citations and a deterministic tamper control rejected 12/12 altered hashes.

## Why it stopped

Tier 1 direct real-agent comparison did not meet the improvement threshold: hash accepted_unsupported was 0/12, but plain ID-only accepted_unsupported was also 0/12. This is not a full validation of citation truth.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a bounded multi-turn memory-contamination test that creates measurable stale-handle pressure in the ID-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-turn stale-handle stress test for hash-checked citation memory
- Success threshold: ID-only accepted stale or unsupported citation handles in at least 20% of contaminated tasks, while hash checking rejects at least 95% of stale-hash handles and false-rejects no more than 5% of valid hash citations.
- Stop condition: Stop if the ID-only baseline again has zero accepted stale/unsupported handles under the stronger multi-turn contamination setup, or if valid hash citations false-reject above 5%.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-validation-of-hash-checked-citation-memory-14b7b9f047`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
