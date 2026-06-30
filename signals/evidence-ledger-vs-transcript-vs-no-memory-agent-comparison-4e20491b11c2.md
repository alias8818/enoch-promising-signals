# Evidence-ledger vs. transcript vs. no-memory agent comparison

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-vs-transcript-vs-no-memory-agent-comparison-4e20491b11c2`
Run ID: `evidence-ledger-vs-transcript-vs-no-memory-agent-comparison-4e20491b11c2-20260621T211756630608+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7fccdab20de

## What looked useful

Across 100 seeds and 19992 queries per budget, evidence-ledger accuracy exceeded transcript accuracy at budgets 24, 48, and 80 by 0.1067, 0.1825, and 0.2102 respectively; both memory policies beat no-memory.

## Boundaries and scale limits

No LLM reasoning, no real tool-use agent, no natural-language ambiguity, no external data, and no long-running workload. Budgets are synthetic units rather than tokens.

## Claim scope

Synthetic representation-level delayed-state benchmark: exact entity-attribute queries over generated fact, update, distractor, and query streams with fixed memory-unit budgets.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic and representation-level, not a direct full validation of agent performance.

## Recommended next action

Run a bounded direct agent follow-up that puts the three memory policies behind the same LLM or deterministic tool agent on hidden-drift multi-step tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct hidden-drift agent benchmark for ledger, transcript, and no-memory policies
- Success threshold: Evidence-ledger improves task success by at least 10 percentage points over transcript and reduces stale-state errors by at least 25 percent without increasing unsupported claims.
- Stop condition: Stop if evidence-ledger does not beat transcript on task success or if improvement comes from benchmark leakage rather than memory representation.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-vs-transcript-vs-no-memory-agent-comparison-4e20491b11c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
