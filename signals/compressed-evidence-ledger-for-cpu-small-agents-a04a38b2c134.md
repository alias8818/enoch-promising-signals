# Compressed Evidence Ledger for CPU Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-evidence-ledger-for-cpu-small-agents-a04a38b2c134`
Run ID: `compressed-evidence-ledger-for-cpu-small-agents-a04a38b2c134-20260529T141019021423+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/18d97d379b2d

## What looked useful

Compact serialization mattered: a verbose provenance ledger underperformed tail buffering, while a compact ledger reached 0.2973 overall accuracy at 4096 tokens versus 0.1497 for tail buffering. Naive summary reached 0.4145 overall by excelling at latest-value and join queries but scored 0 on provenance and conflicts, so ledger value is task-dependent.

## Boundaries and scale limits

Proxy-only local CPU benchmark; no real LLM agent, no natural-language extraction, no tokenizer-specific budget, no adversarial/noisy source study, and no full-scale serving or long-horizon agent validation.

## Claim scope

On deterministic synthetic structured evidence streams with 2,000 observations, 160 subjects, 800 queries, 8 seeds, and 512-4096 approximate-token memory budgets, a compact provenance-preserving ledger outperformed a raw tail buffer on overall evidence-retention accuracy and preserved provenance/conflict answers that a naive latest-fact summary could not answer.

## Why it stopped

Current result is a local synthetic proxy useful signal, not direct small-agent evidence or a paper-ready validation.

## Recommended next action

Run a bounded deepen follow-up with a local small LLM on natural-language evidence, using the same three memory policies and measuring answer accuracy plus provenance/conflict faithfulness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM Natural-Language Test of Compact Evidence Ledgers
- Success threshold: Compact ledger beats tail buffer by at least 25% relative on provenance+conflict accuracy and retains at least 80% of naive-summary latest-fact accuracy at 2048 and 4096 token budgets.
- Stop condition: Stop if compact ledger fails to beat tail buffer on provenance+conflict accuracy in two independent seeds or if CPU latency makes the local small-LLM run exceed the bounded worker budget.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-evidence-ledger-for-cpu-small-agents-a04a38b2c134`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
