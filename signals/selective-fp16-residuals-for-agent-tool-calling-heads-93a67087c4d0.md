# Selective FP16 Residuals for Agent Tool-Calling Heads

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `selective-fp16-residuals-for-agent-tool-calling-heads-93a67087c4d0`
Run ID: `selective-fp16-residuals-for-agent-tool-calling-heads-93a67087c4d0-20260602T180645259129+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/878afbbb9b2b

## What looked useful

Across five medium CUDA seeds, int4 tool-token agreement improved from 0.8147 to 0.8508 mean top-1 agreement while non-tool agreement moved only +0.0019; int6 improved tool agreement from 0.9612 to 0.9702 with near-zero non-tool movement; int8 gains were small. The tested memory model adds 6.25% over an ideal int4 head for 64 FP16 residual tool rows out of 4096 vocabulary rows.

## Boundaries and scale limits

No full transformer training, no real tool-call trace evaluation, no tokenizer-specific tool schema, no end-to-end JSON/tool-call exact-match metric, and no production fused-kernel latency measurement. Dense-reference accepted samples were about 1.6k-1.8k per seed from synthetic conditioned hidden states.

## Claim scope

In a synthetic CUDA output-head proxy with a 4096-token vocabulary, 768-dim hidden states, and 64 designated tool-token rows, selective FP16 residuals for only the tool rows consistently improved dense-FP16 top-1 agreement for tool-token targets under row-wise quantized output heads, especially at 4-bit quantization.

## Why it stopped

No-paper closure: this run produced a reproducible proxy mechanism signal, but it is not full validation of selective FP16 residuals for real agent tool-calling heads.

## Recommended next action

Run a bounded deepen experiment on a small trained transformer or GPT-2-small-class model with real or semi-synthetic tool-call traces, comparing FP16, fully quantized, and selective tool-row residual output heads on exact tool-call validity plus latency and memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Selective Tool-Row Residuals on a Small Trained Tool-Calling Model
- Success threshold: Selective residual recovers at least 50% of the quantized baseline's exact tool-call failures versus FP16 while adding under 10% output-head memory overhead and causing no more than 1 percentage point non-tool accuracy loss.
- Stop condition: Stop if selective residual recovers less than 20% of quantization-induced tool-call failures, or if non-tool accuracy drops by more than 2 percentage points, or if the required tool-row residual overhead exceeds 10% for the chosen tokenizer/schema.

## Evidence references

- Artifact root: `<local-path>/projects/selective-fp16-residuals-for-agent-tool-calling-heads-93a67087c4d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
