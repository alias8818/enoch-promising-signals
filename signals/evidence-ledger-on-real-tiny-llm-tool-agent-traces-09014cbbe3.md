# Evidence Ledger on Real Tiny LLM Tool-Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-on-real-tiny-llm-tool-agent-traces-09014cbbe3`
Run ID: `evidence-ledger-on-real-tiny-llm-tool-agent-traces-09014cbbe3-20260604T010550767738+0000`

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

- Parent run decision: Evidence Ledger for Tiny Tool Agents: enoch://control-plane/projects/evidence-ledger-for-tiny-tool-agents-0e0162cbb7f1/runs/evidence-ledger-for-tiny-tool-agents-0e0162cbb7f1-20260603T221203805557+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4defc5bd2466

## What looked useful

The ledger mechanism produced 0 false positives and 0 false negatives over 16 claims, rejected 1 naturally unsupported model-final claim, rejected all unsupported mutations, verified 4/4 clean chains, and detected 4/4 tampered chains.

## Boundaries and scale limits

Only four traces; deterministic tools; constrained tool-use harness; task-aware regex claim extraction; no long ReAct traces, adversarial formatting, multi-hop evidence, or broad tiny-LLM/model-family coverage.

## Claim scope

In a four-trace controlled Tier 1 harness using local google/flan-t5-small tool-agent traces, a hash-chained evidence ledger preserved tool-backed claims, rejected unsupported model-final and mutated claims, and detected tampered tool observations.

## Why it stopped

Tier 1 mechanism support was obtained, but this is a small controlled direct test rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test on 25-50 real ReAct-style tiny-LLM traces with model-chosen tool calls, natural claim extraction, and human-audited labels before reconsidering paper readiness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger on ReAct-Style Tiny LLM Tool Traces
- Success threshold: At least 90% precision and 90% recall for unsupported-claim rejection, zero undetected tampered tool observations, and improvement over an unledgered transcript baseline on the same labeled traces.
- Stop condition: Stop as negative if unsupported-claim precision or recall is below 80%, if tampering is not reliably detected, or if natural claim extraction cannot produce auditable labels on at least 25 traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-on-real-tiny-llm-tool-agent-traces-09014cbbe3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
