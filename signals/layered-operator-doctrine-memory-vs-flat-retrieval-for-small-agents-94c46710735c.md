# Layered Operator-Doctrine Memory vs Flat Retrieval for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-operator-doctrine-memory-vs-flat-retrieval-for-small-agents-94c46710735c`
Run ID: `layered-operator-doctrine-memory-vs-flat-retrieval-for-small-agents-94c46710735c-20260621T215403248838+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2852c88656c4

## What looked useful

Primary run: layered_doctrine_memory 480/480 accuracy, flat_retrieval 0/480, transcript_search 0/480, no_memory 101/480. Sensitivity sweep showed flat retrieval at 0.750 only in the easiest no-decoy/no-stale setting, dropping to 0.431 with stale same-slot records and to 0.075 or lower with two or more decoys; layered remained 1.000 in all swept settings.

## Boundaries and scale limits

Evidence is mechanism-level and synthetic. It does not test an end-to-end LLM agent, natural task phrasing, embedding retrieval, tool use, long-horizon sessions, multi-user privacy boundaries, or production memory storage. Primary stress condition used 480 tasks, 8 decoys per task, conflict_rate 0.55, stale_same_slot_rate 0.45, seed 20260621.

## Claim scope

On a deterministic synthetic replay benchmark with typed operator/doctrine memories, stale memories, and noisy transcript decoys, layered operator-doctrine memory with explicit active-state and precedence metadata selected the correct policy value more reliably than flat lexical/recency retrieval.

## Why it stopped

No-paper useful signal only: this run directly tested the memory-selection mechanism but only through synthetic typed records and deterministic strategy rules, not full small-agent behavior.

## Recommended next action

Run a bounded end-to-end small-agent replay using the same generated corpus plus an actual small LLM or deterministic agent prompt, comparing layered memory against flat retrieval on answer accuracy and evidence selection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-agent replay for layered memory vs flat retrieval
- Success threshold: Layered memory improves answer accuracy by >= 0.10 absolute over flat retrieval with non-overlapping or clearly separated confidence intervals on at least 300 replay tasks.
- Stop condition: Stop if layered memory is within 0.05 absolute accuracy of flat retrieval or if failures are dominated by prompt/model answer extraction rather than memory selection.

## Evidence references

- Artifact root: `<local-path>/projects/layered-operator-doctrine-memory-vs-flat-retrieval-for-small-agents-94c46710735c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
