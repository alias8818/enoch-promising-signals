# Counterexample-preserving compaction on real machine-checkable agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-preserving-compaction-on-real-machine-check-b025fa4191`
Run ID: `counterexample-preserving-compaction-on-real-machine-check-b025fa4191-20260610T060059539470+0000`

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

- Parent run decision: Falsifiable Agent Traces with Counterexample Preservation: enoch://control-plane/projects/falsifiable-agent-traces-with-counterexample-preservation-21903bf43e8b/runs/falsifiable-agent-traces-with-counterexample-preservation-21903bf43e8b-20260610T012651912954+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/bc71408406bd

## What looked useful

Preserving completed non-zero command events that contain counterexample markers is a simple deterministic mechanism that outperformed naive first-half, last-half, random-half, and type-only compaction on witness preservation in a bounded direct test.

## Boundaries and scale limits

No natural corpus of real failing agent traces was evaluated; only three controlled executed traces carried independent witnesses. Token counts are character/4 approximations, and the live Codex trace does not provide natural counterexample evidence.

## Claim scope

In three controlled executed JSONL agent/tool traces with machine-checkable command failures, a counterexample-aware compactor preserved all failure witnesses while reducing approximate tokens by 69.9%; a live Codex trace was used only for parser/shape coverage.

## Why it stopped

Tier 1 controlled direct test supports the mechanism, but evidence remains no-paper because it is small and controlled rather than a natural-trace corpus validation.

## Recommended next action

Run a bounded deepen follow-up on at least 30 natural machine-checkable agent or CI traces with real failures before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural failure-trace validation for counterexample-preserving compaction
- Success threshold: Witness preservation >=95%, average approximate token reduction >=50%, and strictly higher witness pass rate than every naive baseline.
- Stop condition: Stop as negative if witness preservation is below 90% or average token reduction is below 35% after 30 natural failure traces.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-preserving-compaction-on-real-machine-check-b025fa4191`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
