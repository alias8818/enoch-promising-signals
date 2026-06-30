# Evidence ledger for tool-calling agents on quantized small LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-tool-calling-agents-on-quantized-small-llms-1d2bece6a81f`
Run ID: `evidence-ledger-for-tool-calling-agents-on-quantized-small-llms-1d2bece6a81f-20260527T225301443281+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/92971d789f91

## What looked useful

Evidence ledgers can act as a high-precision abstention filter for small LLM tool-output QA, but this bounded run does not show useful throughput under quantization noise. The bf16 ledger accepted 28.13% of outputs with 100% accepted accuracy; fake-int4 ledger accepted 0%.

## Boundaries and scale limits

Synthetic precomputed tool observations only; no multi-turn tool execution; fake-int4 dequantized proxy rather than production packed quantized inference; one 0.5B model; 32 confirmation cases per condition.

## Claim scope

On a 32-case synthetic tool-observation QA suite with Qwen2.5-0.5B-Instruct, evidence-ledger prompting plus deterministic support-id gating produced a high-precision accepted subset in bf16 but low coverage; under a fake-int4 dequantized-weight proxy, the verifier rejected all ledger outputs.

## Why it stopped

Proxy/early falsification for the quantized claim: the fake-int4 condition collapsed to zero accepted ledger outputs, so the ledger prevented unsupported answers but did not recover practical quantized-agent accuracy.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a real packed int4 or int8 small instruction runtime and multi-turn tool traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gating on real packed int4 small tool-calling models
- Success threshold: Ledger-gated accepted accuracy at least 60%, accept rate at least 25%, and fewer unsupported accepted answers than the direct baseline on at least 100 episodes.
- Stop condition: Stop if the quantized model has direct answer accuracy below 20% or ledger verifier accept rate below 10% after 100 episodes.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tool-calling-agents-on-quantized-small-llms-1d2bece6a81f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
