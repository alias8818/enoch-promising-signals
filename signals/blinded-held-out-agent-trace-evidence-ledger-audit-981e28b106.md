# Blinded Held-Out Agent Trace Evidence Ledger Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `blinded-held-out-agent-trace-evidence-ledger-audit-981e28b106`
Run ID: `blinded-held-out-agent-trace-evidence-ledger-audit-981e28b106-20260602T203900699096+0000`

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

- Parent run decision: Compressed Evidence Ledger for Tool-Use Agents: enoch://control-plane/projects/compressed-evidence-ledger-for-tool-use-agents-0f8d62b8f19e/runs/compressed-evidence-ledger-for-tool-use-agents-0f8d62b8f19e-20260602T112211185029+0000
- Parent run decision: Realistic Tool-Trace Evidence Ledger Evaluation: enoch://control-plane/projects/realistic-tool-trace-evidence-ledger-evaluation-b460fb74ff/runs/realistic-tool-trace-evidence-ledger-evaluation-b460fb74ff-20260602T161846611772+0000

## What looked useful

Across two 20,000-claim fixed-seed held-out suites, the ledger auditor achieved F1 1.0000. Shuffling ledger IDs collapsed F1 to about 0.13, supporting provenance binding as the mechanism. The lexical-stress suite separated ledger F1 1.0000 from cited-overlap F1 0.9054, but the canonical suite was also solved by cited overlap.

## Boundaries and scale limits

The result is synthetic and structured. It does not validate real agent traces, ambiguous natural-language evidence, parser robustness, multi-hop support, or stronger NLI/LLM-judge baselines.

## Claim scope

A structured evidence-ledger auditor can perfectly identify supported versus unsupported claims on a fixed-seed synthetic held-out trace benchmark, and it outperforms lexical baselines on a verbose contrastive stress variant.

## Why it stopped

Medium synthetic evidence supports the mechanism but is not publication-grade because one canonical suite is solved by cited overlap and all traces/evidence are generated from structured templates.

## Recommended next action

Stop as no-paper useful signal; run a bounded deepen follow-up on real or LLM-generated agent traces with hidden human labels and stronger NLI/LLM-judge baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Agent Trace Evidence Ledger Audit With Human Labels
- Success threshold: Ledger auditor improves false accept rate by at least 10 percentage points over the best non-ledger baseline at no more than 5 percentage points recall loss, with the shuffled-provenance ablation losing at least 20 F1 points.
- Stop condition: Stop if the best NLI or LLM-judge baseline matches ledger false accept rate within 5 percentage points at equal or better recall, or if human-label agreement is too low to support adjudication.

## Evidence references

- Artifact root: `<local-path>/projects/blinded-held-out-agent-trace-evidence-ledger-audit-981e28b106`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
