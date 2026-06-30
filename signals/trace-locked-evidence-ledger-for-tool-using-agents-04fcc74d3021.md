# Trace-Locked Evidence Ledger for Tool-Using Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-locked-evidence-ledger-for-tool-using-agents-04fcc74d3021`
Run ID: `trace-locked-evidence-ledger-for-tool-using-agents-04fcc74d3021-20260621T053402392492+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/299036acf659

## What looked useful

A minimal trace-locked evidence ledger produced 5 true accepts, 5 true rejects, 0 false accepts, and 0 false rejects on the clean synthetic corpus; a tampered evidence hash was rejected with an evidence-lock error.

## Boundaries and scale limits

Synthetic predicate corpus only; no real agent logs, no natural-language entailment, no adversarial paraphrase set, no multi-hop provenance, and no production-scale trace volume.

## Claim scope

In a deterministic synthetic tool-agent ledger with 5 trace events, 5 evidence items, and 10 labeled predicate claims, trace-output hashes plus explicit predicates accepted all supported claims, rejected all unsupported claims, and detected a tampered evidence hash.

## Why it stopped

Closed as a no-paper useful signal because the evidence is synthetic/proxy-only rather than a full validation on real tool-using agents.

## Recommended next action

Run a bounded real-trace follow-up using 50-100 independently labeled tool-agent summary claims and compare false accepts against a no-trace-lock baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace-Locked Ledger Evaluation for Tool-Agent Claims
- Success threshold: At least 80% reduction in false accepts versus the no-trace-lock baseline with no more than 10% absolute increase in false rejects on independently labeled real traces.
- Stop condition: Stop if trace locking fails to reduce false accepts by at least 30% or if supported real claims require semantic evidence outside the explicit predicate vocabulary in more than half of cases.

## Evidence references

- Artifact root: `<local-path>/projects/trace-locked-evidence-ledger-for-tool-using-agents-04fcc74d3021`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
