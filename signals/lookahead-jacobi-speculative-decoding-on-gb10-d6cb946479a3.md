# Lookahead/Jacobi Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lookahead-jacobi-speculative-decoding-on-gb10-d6cb946479a3`
Run ID: `lookahead-jacobi-speculative-decoding-on-gb10-d6cb946479a3-20260621T004423372973+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ead18c512662

## What looked useful

Jacobi drafting produced useful accepted-token compression, up to 4.59 accepted tokens per verification step on distilgpt2 and 4.0 on gpt2, but extra draft forward passes dominated. Best exact fp32 wall-clock ratios were 0.899x greedy for distilgpt2 and 0.797x greedy for gpt2, so this naive local implementation is slower than greedy despite mechanism support.

## Boundaries and scale limits

Tested only small GPT-style causal LMs, short fixed prompts, greedy decoding, single-process PyTorch/Transformers execution, and a proxy Jacobi draft plus verification loop. Did not implement full Lookahead Decoding n-gram cache selection, production KV-cache scheduling, batching, 1B-7B+ models, vLLM/TensorRT-LLM integration, or multi-GPU execution.

## Claim scope

On GB10, a naive exact-greedy Jacobi self-speculative decoder tested with distilgpt2 and gpt2 preserved greedy outputs in fp32 and accepted multi-token candidate prefixes, but did not improve wall-clock throughput over greedy decoding.

## Why it stopped

Proxy/local early falsification of naive Jacobi self-speculative wall-clock speedup: exact fp32 runs showed accepted multi-token prefixes but no throughput win versus greedy.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is to implement true Lookahead Decoding n-gram cache selection and KV-cache-aware verification before considering larger-model scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware Lookahead n-gram cache versus naive Jacobi self-speculation
- Success threshold: At least 1.10x greedy wall-clock throughput with exact greedy output equality on two model scales, and forward-pass efficiency above 1.0 generated tokens per target-equivalent forward after accounting for lookahead overhead.
- Stop condition: Stop if n-gram cache selection still fails to exceed 1.0x greedy throughput on gpt2 and one larger locally runnable model, or if exactness cannot be maintained without fp32-only constraints.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-jacobi-speculative-decoding-on-gb10-d6cb946479a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
