# Real-model adaptive n-gram gate for small-transformer speculative decoding

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `real-model-adaptive-n-gram-gate-for-small-transformer-spec-fca583fc8b`
Run ID: `real-model-adaptive-n-gram-gate-for-small-transformer-spec-fca583fc8b-20260522T053148328206+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Adaptive proposal gating for n-gram KV-cache draft cascades: enoch://control-plane/projects/adaptive-proposal-gating-for-n-gram-kv-cache-draft-cascade-77ea4ddf20/runs/adaptive-proposal-gating-for-n-gram-kv-cache-draft-cascade-77ea4ddf20-20260522T052122818210+0000
- Parent run decision: End-to-end KV-cache latency test for n-gram draft cascades: enoch://control-plane/projects/end-to-end-kv-cache-latency-test-for-n-gram-draft-cascades-12a82fca62/runs/end-to-end-kv-cache-latency-test-for-n-gram-draft-cascades-12a82fca62-20260522T031033207631+0000

## What looked useful

Strict no-TF32 validation produced 0 checksum failures across 192 prompts. Always n-gram saved 18.90% target calls with 1.263x mean wall throughput; static gate saved 18.13% with 1.236x; adaptive gate saved 16.64% with 1.211x, so the adaptive gate is not supported over simpler controls.

## Boundaries and scale limits

One 135M target model, one WikiText test corpus, greedy decoding only, 96 generated tokens per prompt, 180k-token n-gram table, proposal length 4, max n-gram order 5; no larger model, sampling, multi-domain, long-context, or serving-stack validation.

## Claim scope

On 192 WikiText prompts using HuggingFaceTB/SmolLM2-135M-Instruct greedy decoding, corpus n-gram speculative proposals reduce exact target forward calls, but the tested adaptive online count gate underperforms always-propose and static-count controls.

## Why it stopped

Bounded direct validation found a useful n-gram speculative-decoding signal but falsified the adaptive-gate improvement claim for this implementation; earlier TF32 runs also showed rare exact-output checksum mismatches, making numerical controls mandatory.

## Recommended next action

Stop this follow-up as no-paper useful evidence: use always-propose or a simple static count gate as the local baseline, and do not claim adaptive gating improvement without a new gate that beats those controls under strict numerical settings.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-model-adaptive-n-gram-gate-for-small-transformer-spec-fca583fc8b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
