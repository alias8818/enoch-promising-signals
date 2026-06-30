# Self-speculative decoding via KV replay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-kv-replay-6da0a4a57ea4`
Run ID: `self-speculative-decoding-via-kv-replay-6da0a4a57ea4-20260613T134752182131+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f2ba7072f820

## What looked useful

KV/activation replay is mechanically viable, but plain untrained early exits are too inaccurate at shallow layers and too expensive at accurate late layers to support a convincing self-speculative decoding speedup in this bounded probe.

## Boundaries and scale limits

Small GPT-2-family models only; Wikitext validation contexts; no production speculative decoder, fused kernels, trained early-exit checkpoint, 7B+ model, or full serving latency benchmark.

## Claim scope

On cached GPT-2 and GPT-2-medium in fp16 on one GB10, split continuation replay using prompt KV caches reproduces full-model logits within fp16 tolerance, but untrained early exits only match full-model greedy tokens at useful rates when exiting one or two layers before the end.

## Why it stopped

Proxy/early falsification: direct KV-prefix replay succeeded, but early-exit agreement and conservative work proxies do not support useful acceleration without early-exit training or layer-skip optimization.

## Recommended next action

Stop this untrained GPT-2-family variant; if continuing, evaluate a trained LayerSkip-style checkpoint with an end-to-end speculative decoder latency benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end KV-replay self-speculative decoding on a trained early-exit checkpoint
- Success threshold: At least 1.2x tokens/sec over standard greedy decoding on 100+ prompts with exact greedy-output equivalence and an exit point before 80% of model depth.
- Stop condition: Stop if the best trained early exit before 80% depth has top-1 agreement below 60% or if end-to-end latency is not at least 1.05x after cache replay is implemented correctly.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-kv-replay-6da0a4a57ea4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
