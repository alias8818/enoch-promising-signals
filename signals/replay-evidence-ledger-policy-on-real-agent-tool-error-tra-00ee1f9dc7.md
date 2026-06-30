# Replay evidence-ledger policy on real agent tool-error traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-evidence-ledger-policy-on-real-agent-tool-error-tra-00ee1f9dc7`
Run ID: `replay-evidence-ledger-policy-on-real-agent-tool-error-tra-00ee1f9dc7-20260531T223028136502+0000`

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

- Parent run decision: Tiny Agent Evidence Ledger for Tool-Use Reliability: enoch://control-plane/projects/tiny-agent-evidence-ledger-for-tool-use-reliability-17fb333e232c/runs/tiny-agent-evidence-ledger-for-tool-use-reliability-17fb333e232c-20260531T175620820376+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1f7c49f7f4e2

## What looked useful

Across 283 blocking tool-error episodes from 177 real logs, the ledger policy rejected 7/7 unresolved silent errors and had 0/276 false rejections on recovered or disclosed cases; a naive final-message baseline rejected 0/7 unresolved silent errors.

## Boundaries and scale limits

300 local Codex JSONL logs; deterministic command-signature and disclosure-lexicon labels; no human adjudication, live agent generation, concurrent tool execution, or production runtime integration.

## Claim scope

A rule-based evidence-ledger replay policy over real local Codex/Enoch traces can reject unresolved silent blocking tool-error episodes while accepting matching-success recoveries or explicit disclosures in a bounded 300-log Tier 1 sample.

## Why it stopped

No-paper useful signal: Tier 1 direct replay supports the mechanism on real traces, but labels are rule-derived and scope is too narrow for publication readiness.

## Recommended next action

Run a blinded label audit on a frozen larger trace corpus and compare this policy against last-command and final-message baselines before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded audit of evidence-ledger tool-error policy on frozen real traces
- Success threshold: At least 90% precision and 90% recall on consequential unresolved tool errors with statistically lower false positives than a simple any-error gate.
- Stop condition: Stop as negative if precision or recall falls below 80% on the labeled sample or if most apparent wins are label/parser artifacts rather than real consequential tool-error catches.

## Evidence references

- Artifact root: `<local-path>/projects/replay-evidence-ledger-policy-on-real-agent-tool-error-tra-00ee1f9dc7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
