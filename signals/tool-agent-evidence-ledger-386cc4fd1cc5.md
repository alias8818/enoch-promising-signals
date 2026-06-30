# Tool Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tool-agent-evidence-ledger-386cc4fd1cc5`
Run ID: `tool-agent-evidence-ledger-386cc4fd1cc5-20260605T022444266171+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/96acb1bd8a94

## What looked useful

The mechanism worked on all tested synthetic tamper classes and had predictable local overhead, making it a useful reference harness for future agent trace integrity experiments but not enough for a paper.

## Boundaries and scale limits

Synthetic traces only; no real agent framework integration, no baseline against production observability/audit-log systems, no distributed writers, no signatures, no external witness anchoring, no privileged log-rewrite adversary, and no human audit study.

## Claim scope

A minimal canonical-JSON, hash-chained evidence ledger detects payload edits, deletion, adjacent reordering, and record splicing on synthetic tool-agent traces up to 10000 events, while sustaining roughly 42k-54k append/verify events per second on this CPU worker with about 2.115x raw-event JSON storage overhead.

## Why it stopped

Synthetic/local mechanism evidence supports feasibility but not publication-grade novelty or real-world validity.

## Recommended next action

Stop this run as no-paper useful evidence; next concrete action is integrating the ledger into one real tool-agent runtime and comparing against a baseline audit log on replayed traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Evidence Ledger Integration
- Success threshold: Detect 100 percent of injected tamper cases on replayed traces while adding less than 10 percent runtime overhead and less than 2.5x storage overhead relative to raw trace logging.
- Stop condition: Stop if real runtime integration cannot capture complete tool inputs/outputs, if any injected tamper class is missed, or if overhead exceeds the threshold by more than 2x on the replay workload.

## Evidence references

- Artifact root: `<local-path>/projects/tool-agent-evidence-ledger-386cc4fd1cc5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
