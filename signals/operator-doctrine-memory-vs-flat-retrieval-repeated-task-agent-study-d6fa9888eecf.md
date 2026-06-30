# Operator-Doctrine Memory vs Flat Retrieval: Repeated-Task Agent Study

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-repeated-task-agent-study-d6fa9888eecf`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-repeated-task-agent-study-d6fa9888eecf-20260621T194203093681+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/800ffea83752

## What looked useful

Across 720 tasks per strategy, layered_doctrine_memory reached 1.000 success with 0.000 stale items per task, while flat_retrieval reached 0.179 success with 0.821 stale items per task. The result supports stale-doctrine filtering as a concrete failure mode and benchmark axis.

## Boundaries and scale limits

Synthetic policy simulation only; no real LLM agent, no real operator traces, no private workflows, and no production memory system were evaluated. The layered strategy has explicit doctrine/stale metadata, so this is mechanism evidence rather than broad agent validation.

## Claim scope

In a deterministic synthetic repeated-task replay with explicit current doctrine, stale superseded doctrine, and noisy episodic entries, a layered doctrine memory policy avoided stale-rule contamination and outperformed flat retrieval on exact rule-compliance success.

## Why it stopped

The local result is synthetic/proxy evidence that supports the mechanism but is not full validation of real repeated-task agent behavior.

## Recommended next action

Stop this run as no-paper useful signal; next run should perform a bounded LLM-in-the-loop replay using the same task schema and hand-authored transcript noise.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop operator-doctrine memory replay with noisy transcripts
- Success threshold: Layered doctrine memory improves exact compliance success over flat retrieval by >=0.15 absolute and reduces stale-rule inclusions by >=50% on the bounded LLM replay.
- Stop condition: Stop as negative if the layered strategy improves success by <0.05 absolute or fails to reduce stale-rule inclusions by at least 25% on the bounded replay.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-repeated-task-agent-study-d6fa9888eecf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
