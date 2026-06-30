# Evidence Ledger and Rollback for Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-and-rollback-for-local-agents-df9522eeec1b`
Run ID: `evidence-ledger-and-rollback-for-local-agents-df9522eeec1b-20260526T001711499660+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b4b0386b97fe

## What looked useful

Complete write coverage is sufficient for exact byte-level rollback and is materially cheaper than full snapshots in this bounded test, but incomplete coverage leaves dirty files and is the central practical risk.

## Boundaries and scale limits

Synthetic deterministic mutations only; no real LLM agent loop, tool interception layer, deletes/renames, binary-heavy repositories, concurrent actions, or large repository scaling. Missing created-file coverage failed exact rollback in 100/100 trials.

## Claim scope

In a synthetic local filesystem benchmark with 400 small text files and complete pre-action write-set coverage, a per-file evidence ledger restored failed edits and creations exactly in 100/100 trials with lower setup time, rollback time, and storage than full-directory snapshots.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct real-agent evidence; finalize as no-paper evidence rather than claiming full validation.

## Recommended next action

Run a bounded deepen test with filesystem/tool interception on real local-agent tasks before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Intercepted Evidence Ledger on Real Local-Agent Tool Calls
- Success threshold: Exact restore rate at least 0.99 with zero unclassified dirty files and median ledger storage at least 5x smaller than snapshots.
- Stop condition: Stop if interception misses any file effect class that cannot be conservatively captured, or if exact restore rate falls below 0.95 after 20 valid failure-injection trials.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-and-rollback-for-local-agents-df9522eeec1b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
