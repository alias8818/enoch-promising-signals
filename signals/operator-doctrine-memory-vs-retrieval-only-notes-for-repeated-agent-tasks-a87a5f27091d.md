# Operator-Doctrine Memory vs Retrieval-Only Notes for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `operator-doctrine-memory-vs-retrieval-only-notes-for-repeated-agent-tasks-a87a5f27091d`
Run ID: `operator-doctrine-memory-vs-retrieval-only-notes-for-repeated-agent-tasks-a87a5f27091d-20260621T215702186512+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf76d8b746b8

## What looked useful

Retrieval-only nearest-note baselines beat doctrine-only memory by 9.73 to 13.33 accuracy points across 60 seeds; hybrid doctrine+retrieval improved over doctrine-only but still trailed retrieval_k12.

## Boundaries and scale limits

LLM-free synthetic proxy only; no real natural-language note extraction, semantic retrieval, human operator preferences, or full agent-task execution were tested.

## Claim scope

In a deterministic synthetic repeated-agent-task proxy with hidden operator preferences and online feedback, a distilled global/feature/pairwise doctrine memory did not outperform retrieval-only episodic notes.

## Why it stopped

The local synthetic proxy directly tested memory/retrieval mechanics and did not support doctrine-only memory; full real-agent validation would require separate LLM/human-note evidence.

## Recommended next action

Stop this run as a proxy early falsification; next bounded test should use an LLM-in-the-loop repeated-task benchmark with fixed context budgets and semantic retrieval controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop operator doctrine versus semantic retrieval under fixed context budgets
- Success threshold: Doctrine or hybrid memory must improve preference-adherence accuracy by at least 5 percentage points over semantic retrieval-only at equal prompt budget across at least three task families.
- Stop condition: Stop if doctrine/hybrid fails to beat semantic retrieval-only by 2 percentage points on a 30-task pilot or if gains disappear when local exceptions are included.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-retrieval-only-notes-for-repeated-agent-tasks-a87a5f27091d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
