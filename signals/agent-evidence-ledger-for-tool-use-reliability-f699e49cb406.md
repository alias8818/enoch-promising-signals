# Agent Evidence Ledger for Tool-Use Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-evidence-ledger-for-tool-use-reliability-f699e49cb406`
Run ID: `agent-evidence-ledger-for-tool-use-reliability-f699e49cb406-20260524T011853968704+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c67014ae553a

## What looked useful

Across 80 trials x 3000 tasks, the evidence ledger achieved 0.9169 mean accuracy and 0.0831 wrong rate versus direct trust at 0.7008 accuracy and 0.2992 wrong rate, a 72.2% wrong-rate reduction. It used 1.246 total calls/task versus 2.621 for verify-then-retry, though verify-then-retry was more accurate at 0.9541.

## Boundaries and scale limits

Synthetic-only; no deployed LLM agent, real API trace, adversarial prompt distribution, non-stationary tool drift, multi-step tool chain, or production cost/latency validation was tested.

## Claim scope

In a deterministic synthetic repeated tool-use simulator with context-dependent tool reliabilities, misleading advertised confidences, and an imperfect verifier, a persistent evidence ledger reduced wrong answers versus direct trust while using fewer total calls than an always-verify retry baseline.

## Why it stopped

Closed as no-paper useful synthetic evidence; the result supports the mechanism locally but is not direct production-agent validation.

## Recommended next action

Run a bounded trace-replay follow-up on real or realistically generated agent tool-use logs with hidden gold labels, comparing direct trust, always-verify retry, and the evidence-ledger policy under measured cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace Replay Validation for Agent Evidence Ledgers
- Success threshold: At least 30% wrong-rate reduction versus direct trust and at least 30% fewer total calls than always-verify retry, without any context showing more than 10% absolute wrong-rate regression versus direct trust.
- Stop condition: Stop if the ledger fails to beat direct trust by 15% wrong-rate reduction on two independently seeded trace splits or if cost exceeds always-verify retry.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-for-tool-use-reliability-f699e49cb406`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
