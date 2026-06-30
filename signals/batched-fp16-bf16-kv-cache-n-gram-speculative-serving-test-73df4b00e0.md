# Batched fp16/bf16 KV-cache n-gram speculative serving test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `batched-fp16-bf16-kv-cache-n-gram-speculative-serving-test-73df4b00e0`
Run ID: `batched-fp16-bf16-kv-cache-n-gram-speculative-serving-test-73df4b00e0-20260526T190441243998+0000`

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

- Parent run decision: KV-cache serving benchmark for n-gram draft-free speculative decoding: enoch://control-plane/projects/kv-cache-serving-benchmark-for-n-gram-draft-free-speculati-fba5b4b00b/runs/kv-cache-serving-benchmark-for-n-gram-draft-free-speculati-fba5b4b00b-20260525T131701548243+0000
- Parent run decision: N-gram Context Cache for Draft-Free Speculative Decoding: enoch://control-plane/projects/n-gram-context-cache-for-draft-free-speculative-decoding-a9342d684a1e/runs/n-gram-context-cache-for-draft-free-speculative-decoding-a9342d684a1e-20260525T080315117310+0000

## What looked useful

Fixed-seed GB10 measurements support the mechanism: n-gram proposals had about 46.7% acceptance, reduced target calls/token by about 61%, and gave 1.40x-1.48x speedup by shape, while shuffled proposals accepted only about 3.2% and slowed to about 0.61x baseline.

## Boundaries and scale limits

Synthetic oracle token streams only; KV-cache attention/verification isolated from full transformer logits, sampling, tokenization, paged-cache allocation, networking, and production serving arrivals. Prompt length 192, generation length 160/request, gamma 6, n-gram 3, batch sizes up to 32.

## Claim scope

On a GB10 PyTorch microbenchmark with synthetic repetitive token streams, batched fp16/bf16 KV-cache n-gram speculative verification reduced request-level target calls to about 0.394 per emitted token and improved throughput by about 1.45x versus autoregressive batched decoding across seeds 101/202/303, batch sizes 8/16/32, and both fp16 and bf16.

## Why it stopped

No-paper closure: this is a useful medium confirmation of the KV-cache n-gram speculative mechanism, but it is still synthetic/microbenchmark evidence rather than direct full-model serving validation.

## Recommended next action

Run a real-model local follow-up using a GPT-2-small-class or small Llama-family model on repeated natural/programming text, measuring actual logits-based acceptance, end-to-end latency, and paged KV-cache behavior against the same autoregressive and shuffled controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model batched KV-cache n-gram speculative serving validation
- Success threshold: At batch sizes 16 and 32, n-gram speculative serving achieves at least 1.25x mean tokens/s versus autoregressive baseline on repeated-text workloads with exact output agreement and shuffled-control speedup below 1.0x.
- Stop condition: Stop if real-model acceptance falls below 20% or mean speedup is below 1.10x in both repeated-text workloads, or if exact target-model output agreement fails.

## Evidence references

- Artifact root: `<local-path>/projects/batched-fp16-bf16-kv-cache-n-gram-speculative-serving-test-73df4b00e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
