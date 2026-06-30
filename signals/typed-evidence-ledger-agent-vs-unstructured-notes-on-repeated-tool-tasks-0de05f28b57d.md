# Typed Evidence-Ledger Agent vs Unstructured Notes on Repeated Tool Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `typed-evidence-ledger-agent-vs-unstructured-notes-on-repeated-tool-tasks-0de05f28b57d`
Run ID: `typed-evidence-ledger-agent-vs-unstructured-notes-on-repeated-tool-tasks-0de05f28b57d-20260621T050402134045+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db62ea746c91

## What looked useful

Typed keyed evidence state matched recency notes when there were no historical decoys, then maintained 100% task success in low/high decoy conditions where recency notes fell to 45.01% and 44.72% success.

## Boundaries and scale limits

36,000 synthetic task decisions; deterministic state policies only; no real LLM controller, no production tools, no human-authored notes, and no long-running deployment.

## Claim scope

In a deterministic synthetic repeated-tool-task benchmark, a typed revisioned evidence ledger avoided stale/historical note selection errors that affected unstructured lexical and recency-first note baselines.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic and mechanism-level, not direct production or LLM-agent validation.

## Recommended next action

Run a bounded LLM-agent follow-up with the same hidden drift/decoy task family and randomized state backend assignment before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM controller test for typed evidence ledger versus unstructured notes under hidden drift
- Success threshold: Typed ledger improves task success by at least 10 absolute percentage points or cuts stale-fact errors by at least 50% versus unstructured notes without increasing tool-call cost by more than 20%.
- Stop condition: Stop if the LLM controller shows less than 3 absolute percentage points success difference and no stale-fact error reduction across paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/typed-evidence-ledger-agent-vs-unstructured-notes-on-repeated-tool-tasks-0de05f28b57d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
