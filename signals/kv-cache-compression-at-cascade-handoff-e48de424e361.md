# KV-Cache Compression at Cascade Handoff

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-at-cascade-handoff-e48de424e361`
Run ID: `kv-cache-compression-at-cascade-handoff-e48de424e361-20260628T184754368612+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/325fe8d4803e

## What looked useful

Simple tensorwise int8 quantization is a strong baseline for same-model KV-cache handoff: mean compression ratio 1.9999x, mean delta NLL -0.0014, mean KL 0.0021, and mean top-1 agreement 0.9792. SVD rank 4/8/16 gave worse logit fidelity and roughly 445-477 ms compression cost.

## Boundaries and scale limits

Not a production serving trace, not a heterogeneous small-model-to-large-model KV transfer, not long-context or large-model validation, and not an end-to-end network/RPC benchmark.

## Claim scope

On a bounded GPT-2 same-model handoff proxy with four prose prompts, tensorwise int8 KV-cache packing preserved suffix-token behavior while reducing estimated fp16 cache payload by about 2x; online SVD low-rank cache compression distorted logits and was much slower.

## Why it stopped

Bounded local evidence supports int8 same-model cache handoff as a practical baseline and disfavors online SVD, but the result is a proxy rather than full cascade-serving validation.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded deepen test should evaluate int8 KV handoff in a two-process serving harness with real serialization and longer prefixes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-process int8 KV-cache handoff latency benchmark
- Success threshold: Int8 handoff achieves at least 1.8x payload reduction, less than 0.02 mean delta NLL, less than 0.01 mean KL from fp16 control, at least 0.95 top-1 agreement, and lower median end-to-end transfer-plus-decode latency than fp16 for prefixes where payload transfer is material.
- Stop condition: Stop if int8 adds net latency versus fp16 at material prefix lengths or if mean delta NLL exceeds 0.02 / mean KL exceeds 0.01 on the bounded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-at-cascade-handoff-e48de424e361`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
