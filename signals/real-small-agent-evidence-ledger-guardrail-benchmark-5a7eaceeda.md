# Real small-agent evidence-ledger guardrail benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-small-agent-evidence-ledger-guardrail-benchmark-5a7eaceeda`
Run ID: `real-small-agent-evidence-ledger-guardrail-benchmark-5a7eaceeda-20260529T123540949051+0000`

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

- Parent run decision: Local evidence-ledger guardrail for small tool agents: enoch://control-plane/projects/local-evidence-ledger-guardrail-for-small-tool-agents-0d9aa8e70557/runs/local-evidence-ledger-guardrail-for-small-tool-agents-0d9aa8e70557-20260529T082551931302+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8d22261cc54

## What looked useful

Evidence-ledger prompting appears capacity-dependent: it can harm a 0.5B agent by increasing unsupported/contradictory failures, while producing a clear safety and accuracy gain at 1.5B on the same controlled direct benchmark.

## Boundaries and scale limits

Two related Qwen checkpoints only, synthetic documents only, greedy single-turn QA only, prompt-level ledger only, no natural retrieval/tool traces, no multi-seed decoding, and no external verifier.

## Claim scope

In a 64-case controlled synthetic evidence-grounding benchmark, an evidence-ledger prompt failed to improve Qwen2.5-0.5B-Instruct but improved Qwen2.5-1.5B-Instruct strict accuracy from 53.12% to 81.25% and reduced unsafe failures from 46.88% to 17.19%.

## Why it stopped

Tier 1 direct benchmark produced mixed, capacity-dependent evidence that is useful but not publication-grade.

## Recommended next action

Run a bounded medium deepen test across at least four small model families/sizes with naturalistic retrieved documents and an explicit post-generation ledger verifier control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium multi-model evidence-ledger guardrail benchmark with verifier control
- Success threshold: Ledger or ledger-plus-verifier reduces unsafe failures by at least 30% relative to baseline on at least three of four models while not reducing strict accuracy by more than 5 percentage points; verifier must rescue at least half of the 0.5B prompt-only unsafe failures.
- Stop condition: Stop if two or more model families show no unsafe-rate reduction or if all gains disappear on naturalistic retrieved-document tasks.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-agent-evidence-ledger-guardrail-benchmark-5a7eaceeda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
