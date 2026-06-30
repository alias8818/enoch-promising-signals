# Agent Memory: Learned Operator Doctrine vs Retrieval Baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-memory-learned-operator-doctrine-vs-retrieval-baselines-58b6eb480f8d`
Run ID: `agent-memory-learned-operator-doctrine-vs-retrieval-baselines-58b6eb480f8d-20260613T043057603547+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3aa1f9434937

## What looked useful

Layered doctrine memory reached 18/18 accuracy versus 17/18 for the best retrieval baseline and 16/18 for transcript search; the observed gain came from noisy/stale memory handling.

## Boundaries and scale limits

Small synthetic corpus; structured signals supplied; no raw-session extraction, LLM agent, private operator corpus, or statistical robustness sweep.

## Claim scope

On an 18-task synthetic replay with structured operator-memory signals, scoped doctrine memory avoided stale/noisy recall errors that affected transcript search and flat retrieval.

## Why it stopped

Closed as no-paper useful signal because this run is a bounded synthetic mechanism probe, not direct/full validation.

## Recommended next action

Run a medium follow-up where doctrine must be extracted from raw unstructured replay transcripts and evaluated over at least 100 noisy preference probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Unstructured Operator Doctrine Extraction Replay
- Success threshold: Doctrine memory accuracy at least 5 percentage points above the best tuned retrieval baseline with no larger than a 2 percentage point regression on direct lookup tasks.
- Stop condition: Stop if doctrine extraction errors erase the advantage or if tuned retrieval matches doctrine on noisy and scoped-exception splits.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-learned-operator-doctrine-vs-retrieval-baselines-58b6eb480f8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
