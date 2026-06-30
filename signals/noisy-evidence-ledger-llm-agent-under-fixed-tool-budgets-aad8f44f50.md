# Noisy evidence-ledger LLM agent under fixed tool budgets

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `noisy-evidence-ledger-llm-agent-under-fixed-tool-budgets-aad8f44f50`
Run ID: `noisy-evidence-ledger-llm-agent-under-fixed-tool-budgets-aad8f44f50-20260531T173613878999+0000`

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

- Parent run decision: Evidence-ledger agent for bounded tool calls: enoch://control-plane/projects/evidence-ledger-agent-for-bounded-tool-calls-39cb225be1fa/runs/evidence-ledger-agent-for-bounded-tool-calls-39cb225be1fa-20260531T122952338069+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b3cd440f7980

## What looked useful

Prompt-only ledger wording is not enough to make small LLM agents reliably exploit reliable evidence under adversarial noise and fixed evidence budgets. The task was solvable by a reliability oracle, so the negative signal targets the prompt-only ledger mechanism rather than the evidence construction.

## Boundaries and scale limits

Synthetic evidence only; two small open models; no live retrieval, no frontier LLMs, and no external stateful ledger tool. Earlier free-generation runs were superseded because output-format and parser artifacts confounded YES/NO decisions.

## Claim scope

In a controlled synthetic fixed-budget noisy evidence task with 6 snippets per case, prompt-only evidence-ledger instructions did not robustly improve small local LLM claim decisions over non-ledger prompts. Across FLAN-T5-base and Qwen2.5-0.5B-Instruct, 5 seeds, and randomized A/B likelihood scoring, ledger accuracy was 0.57125 versus unstructured 0.61375 and recency 0.59000, while a reliability oracle reached 1.0.

## Why it stopped

Controlled Tier-1 direct test produced mixed-to-negative evidence: ledger beat a naive majority baseline but failed to beat the strongest non-ledger control and was model-dependent, so the hypothesis is not robustly supported.

## Recommended next action

Stop this prompt-only ledger line as no-paper evidence; if continuing, run a bounded external-state ledger follow-up with per-tool structured updates and the same parser-safe randomized A/B scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: External stateful evidence ledger under fixed noisy evidence budgets
- Success threshold: External-state ledger improves absolute accuracy by at least 8 percentage points over the best non-ledger LLM control on both tested models, with no label's accuracy below 0.60 and oracle accuracy remaining at 1.0.
- Stop condition: Stop if the external-state ledger fails to beat the best non-ledger control by at least 3 percentage points on either model after 5 seeds, or if label-wise results show a dominant answer prior rather than evidence use.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-evidence-ledger-llm-agent-under-fixed-tool-budgets-aad8f44f50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
