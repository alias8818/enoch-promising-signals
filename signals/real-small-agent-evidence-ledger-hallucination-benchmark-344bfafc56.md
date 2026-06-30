# Real Small-Agent Evidence-Ledger Hallucination Benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-small-agent-evidence-ledger-hallucination-benchmark-344bfafc56`
Run ID: `real-small-agent-evidence-ledger-hallucination-benchmark-344bfafc56-20260525T122611903976+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-Ledger Hallucination Detection in Small Agents: enoch://control-plane/projects/evidence-ledger-hallucination-detection-in-small-agents-535a284e7eb7/runs/evidence-ledger-hallucination-detection-in-small-agents-535a284e7eb7-20260525T074151333631+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a3a61c76de48

## What looked useful

Prompt-only ledgers improved some answerable support/citation behavior on Qwen2.5-0.5B but failed on the target hallucination metric. Unanswerable hallucination worsened in both completed model runs because models fabricated support inside the ledger or failed to emit abstentions within the output budget.

## Boundaries and scale limits

Small synthetic-but-direct retrieval QA only; no real web retrieval, no multi-turn tool traces, no human grading, no broad model suite, and no verifier-enforced ledger. One deterministic seed per model.

## Claim scope

In a 24-item fictional retrieval-QA benchmark with two cached small Qwen-family instruction models, a prompt-only evidence-ledger condition did not reduce unsupported/hallucinated answers relative to a same-evidence no-ledger baseline under the predeclared threshold.

## Why it stopped

Direct Tier 1 controlled small test falsified the predeclared success threshold for the tested prompt-only evidence-ledger mechanism: ledger hallucination rate was not at least 0.20 below baseline on either completed model run.

## Recommended next action

Stop this prompt-only ledger claim as no-paper evidence; run a bounded verifier-enforced ledger follow-up if continuing, where answers are allowed only when ledger rows quote exact retrieved spans and pass an automatic support check.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-Enforced Evidence Ledger for Small Retrieval Agents
- Success threshold: Verifier-enforced ledger hallucination rate at least 0.20 lower than baseline and prompt-only ledger, with total accuracy loss no greater than 0.10 and no invalid citations.
- Stop condition: Stop if verifier-enforced ledger fails to improve hallucination rate by at least 0.10 on the first 48 items or if answerable accuracy drops by more than 0.15.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-agent-evidence-ledger-hallucination-benchmark-344bfafc56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
