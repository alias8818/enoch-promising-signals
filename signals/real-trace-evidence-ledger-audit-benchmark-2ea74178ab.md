# Real-trace evidence ledger audit benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evidence-ledger-audit-benchmark-2ea74178ab`
Run ID: `real-trace-evidence-ledger-audit-benchmark-2ea74178ab-20260611T055221843457+0000`

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

- Parent run decision: Append-only evidence ledgers for agent reliability audits: enoch://control-plane/projects/append-only-evidence-ledgers-for-agent-reliability-audits-9f0e871bf463/runs/append-only-evidence-ledgers-for-agent-reliability-audits-9f0e871bf463-20260611T052151856187+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/603d8d89d296

## What looked useful

The ledger auditor achieved 100% accuracy on 4,922 trace-derived claims while decoded raw keyword matching achieved 59.96% accuracy and produced 1,971 false positives, mainly by conflating exit/status tokens from other events in the same trace.

## Boundaries and scale limits

Validated on 1,000 command evidence records from 500 sampled trace files across 28 local projects, with deterministic trace-derived claims. Did not test human-authored summaries, LLM paraphrases, semantic entailment, adversarial rewritten claims, or publication-scale corpora.

## Claim scope

On sampled real Enoch/Codex command_execution traces, a structured evidence ledger with command, exit code, status, and output-fragment binding rejects controlled field-tampered trace-derived claims better than decoded raw keyword matching over the same traces.

## Why it stopped

Tier 1 direct trace-derived benchmark supports the field-binding mechanism but is not full validation for natural audit summaries or paper readiness.

## Recommended next action

Run a deepen follow-up with human- or LLM-written audit claims over held-out real traces and compare the ledger auditor against a stronger retrieval/NLI baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human/LLM natural-claim audit benchmark for real trace evidence ledgers
- Success threshold: Ledger auditor precision >= 0.90 on unsupported claims, recall >= 0.85 on supported claims, and at least 20 percentage-point F1 improvement over the strongest non-ledger baseline.
- Stop condition: Stop if the ledger auditor precision falls below 0.80 or recall below 0.75 on the first 100 labeled natural claims, because that would show the templated trace-derived result does not transfer.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-audit-benchmark-2ea74178ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
