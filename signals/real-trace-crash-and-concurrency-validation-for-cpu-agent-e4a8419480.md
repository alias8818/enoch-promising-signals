# Real-trace crash and concurrency validation for CPU agent evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-crash-and-concurrency-validation-for-cpu-agent-e4a8419480`
Run ID: `real-trace-crash-and-concurrency-validation-for-cpu-agent-e4a8419480-20260527T221053264063+0000`

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

- Parent run decision: Cryptographic Evidence Ledger for CPU Agent Tool Calls: enoch://control-plane/projects/cryptographic-evidence-ledger-for-cpu-agent-tool-calls-5e9b72700233/runs/cryptographic-evidence-ledger-for-cpu-agent-tool-calls-5e9b72700233-20260527T191941085746+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/eb1767320215

## What looked useful

Atomic temp-file/fsync/rename commits met the crash/concurrency threshold: 50/50 acknowledged crash-run records recovered with 0 corrupt committed files and 0 missing acknowledged records; no-crash control recovered 400/400. The unsafe chunked JSONL control failed, with 75 corrupt committed units and 83 missing/mismatched acknowledged records under crash injection, and 315 corrupt units plus 360 missing/mismatched acknowledged records without crashes.

## Boundaries and scale limits

Single machine, local filesystem, 400 trace events, 8 Python worker processes, process SIGKILL crash model. Does not cover power loss below fsync semantics, network/distributed filesystems, multi-machine concurrency, very large traces, or downstream evidence-consumer semantics.

## Claim scope

Tier 1 local direct evidence: an atomic file-per-record, fsync, atomic-rename evidence ledger preserved all acknowledged records and exposed zero corrupt committed records during 8-process replay of 400 real Enoch/Codex trace events with crash-stop injection.

## Why it stopped

Tier 1 mechanism support was obtained, but evidence is a small local direct validation rather than publication-grade robustness evidence.

## Recommended next action

Stop as no-paper useful signal; run a bounded deepen follow-up with multiple seeds, explicit restart/recovery scans, and a manifest/index layer before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Restart recovery and manifest validation for atomic evidence ledgers
- Success threshold: Across all seeded restart trials, the atomic ledger plus rebuilt manifest has 0 corrupt committed records, 0 missing/mismatched acknowledged records, and identical manifest hashes across repeated recovery scans; the unsafe control fails at least one integrity metric.
- Stop condition: Stop early if any acknowledged atomic-ledger record is missing or mismatched after recovery, if any committed atomic record is corrupt, or if manifest hashes are nondeterministic for the same recovered ledger.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-crash-and-concurrency-validation-for-cpu-agent-e4a8419480`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
