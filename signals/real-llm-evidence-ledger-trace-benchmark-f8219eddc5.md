# Real-LLM Evidence-Ledger Trace Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-llm-evidence-ledger-trace-benchmark-f8219eddc5`
Run ID: `real-llm-evidence-ledger-trace-benchmark-f8219eddc5-20260601T001201049257+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Evidence-Ledger Constraint for Tool-Calling Agents: enoch://control-plane/projects/evidence-ledger-constraint-for-tool-calling-agents-8f2e887775e7/runs/evidence-ledger-constraint-for-tool-calling-agents-8f2e887775e7-20260531T183513739735+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4e31330fce0a

## What looked useful

Ledger traces can provide valid, digest-verifiable citations even when the model answer is wrong. This exposes a misgrounded-citation failure mode: citation structure improves auditability but is not sufficient grounding or decoy resistance for these small real LLMs.

## Boundaries and scale limits

Tier 1 small direct test only: cached local 0.5B full run, 1.5B one-task smoke, five small local tasks, one prompt template per variant, CPU inference, no human audit-time measurement, no larger/frontier models, no long-horizon real agent traces.

## Claim scope

On five controlled local file/code QA tasks with Qwen2.5-0.5B-Instruct, an evidence-ledger prompt improved machine-checkable citation coverage and digest verification versus a plain prompt, but did not improve answer correctness and failed the anti-decoy threshold. A Qwen2.5-1.5B-Instruct smoke check reproduced the first-task decoy failure.

## Why it stopped

Controlled direct real-LLM test failed the stated answer-correctness and decoy-resistance thresholds; this is an early bounded falsification, not a full validation across larger models.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should test constrained evidence extraction or answer-verification gates rather than treating prompt-only ledgers as a grounding solution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained Evidence-Ledger Answer Verification Gate
- Success threshold: Verifier-gated ledger reaches answer correctness >= 0.8, citation coverage >= 0.8, digest verification >= 0.8, decoy contamination = 0.0, and does not reduce parseability below 0.8 on the five-task controlled benchmark.
- Stop condition: Stop if the verifier cannot detect the max_number decoy failure or if fewer than 4/5 tasks produce parseable verified answers.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-evidence-ledger-trace-benchmark-f8219eddc5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
