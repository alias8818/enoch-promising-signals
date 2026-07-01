# Agent State Ledger with Compressed Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-state-ledger-with-compressed-memory-c6c0320f7141`
Run ID: `agent-state-ledger-with-compressed-memory-c6c0320f7141-20260525T094349054851+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f262c98f3c9e

## What looked useful

Compressed-ledger memory reached 100% sampled state/provenance accuracy with exact replay audits across all cases, about 89 mean query-context bytes, and 0.520x persistent bytes vs raw JSONL logs; raw-tail and lossy-summary baselines averaged 31.4% and 39.8% accuracy respectively.

## Boundaries and scale limits

Tested only local synthetic traces up to 10,000 events, 5 seeds, three context budgets, and deterministic structured extraction. It did not test real LLM summarization, vector retrieval, concurrent writes, crash recovery, adversarial events, or downstream agent task success.

## Claim scope

In deterministic synthetic agent traces with structured fact, decision, todo, and tool events, a compressed append-only ledger plus exact current-state index preserved latest-state/provenance query accuracy and exact replay while using far less query context than raw-tail or bounded lossy-summary baselines.

## Why it stopped

No-paper closure: the local synthetic systems benchmark supports the mechanism but is not direct real-agent evidence or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on real saved agent transcripts or a small live LangGraph workload comparing compressed-ledger memory against vector retrieval and rolling LLM summaries on task-resume success, state/provenance accuracy, and token cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed Ledger Memory on Real Agent Resume Traces
- Success threshold: At least 15 percentage points higher state/provenance accuracy than both baselines at matched sequence-item budgets, no worse than 5% absolute task-resume success regression, and p95 memory-query latency under 50 ms on the local workload.
- Stop condition: Stop as negative if structured extraction errors or ledger overhead prevent exceeding both baselines by at least 5 percentage points on state/provenance accuracy after 100 labeled resume queries.

## Evidence references

- Artifact root: `<local-path>/projects/agent-state-ledger-with-compressed-memory-c6c0320f7141`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
