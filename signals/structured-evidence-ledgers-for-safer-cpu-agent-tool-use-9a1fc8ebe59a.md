# Structured Evidence-Ledgers for Safer CPU Agent Tool Use

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledgers-for-safer-cpu-agent-tool-use-9a1fc8ebe59a`
Run ID: `structured-evidence-ledgers-for-safer-cpu-agent-tool-use-9a1fc8ebe59a-20260604T011235754687+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4c5e4892e116

## What looked useful

The ledger mechanism improved unsafe-plan recall from 0.3077 for regex and 0.6410 for allowlist baselines to 1.0000, with 0 unsafe false accepts, 0.7368 safe accept rate, and median validation overhead of 17.93 microseconds per case.

## Boundaries and scale limits

Proxy-only evidence: synthetic cases, author-provided labels, no live LLM traces, no real command execution from benchmark cases, no adversarial adaptation, and no production policy-engine baseline.

## Claim scope

On a deterministic 155-case synthetic benchmark of CPU shell tool-use plans, a structured evidence-ledger gate rejected all labeled unsafe plans and outperformed regex and allowlist command-only baselines on unsafe recall and overall accuracy.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only; it supports the mechanism but does not validate deployed-agent safety.

## Recommended next action

Run a bounded deepen follow-up using real or replayed CPU-agent tool traces with human-reviewed safety labels and compare the ledger gate against a production-grade policy-as-code baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gating on real CPU-agent traces
- Success threshold: Ledger gate achieves at least 50% lower unsafe false-accept rate than the strongest command-only baseline, safe accept rate >= 0.80, and median validation overhead below 1 ms per tool call.
- Stop condition: Stop if ledger safe accept rate falls below 0.70, if unsafe false accepts are not reduced versus the strongest baseline, or if labels cannot be made reliable enough for adjudication.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledgers-for-safer-cpu-agent-tool-use-9a1fc8ebe59a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
