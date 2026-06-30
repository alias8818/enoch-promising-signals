# Multi-step truncated-cache decode for old-context guard versus stride hybrid

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `multi-step-truncated-cache-decode-for-old-context-guard-ve-98887aef65`
Run ID: `multi-step-truncated-cache-decode-for-old-context-guard-ve-98887aef65-20260524T044508284964+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Truncated-KV decoding check for entropy gate with old-context guard: enoch://control-plane/projects/truncated-kv-decoding-check-for-entropy-gate-with-old-cont-f9eeb0c9cf/runs/truncated-kv-decoding-check-for-entropy-gate-with-old-cont-f9eeb0c9cf-20260524T043231292223+0000
- Parent run decision: Entropy Gate with Old-Context Coverage Guard on Real Small-Model Attention Traces: enoch://control-plane/projects/entropy-gate-with-old-context-coverage-guard-on-real-small-d5d05d35a2/runs/entropy-gate-with-old-context-coverage-guard-on-real-small-d5d05d35a2-20260524T030736264925+0000

## What looked useful

Against stride-hybrid at the same KV budget, guard_multistep had lower target top-1/presence by 0.00340 absolute, lower output MSE by 0.0000324, and higher output cosine by 0.00779. The primary retention hypothesis was not supported; output-fidelity metrics showed a small mixed signal.

## Boundaries and scale limits

The run used synthetic keys/queries/values rather than real transformer hidden states, did not evaluate language-model perplexity or generation quality, and did not benchmark GPU serving kernels. Results should be treated as mechanism-level cache-policy evidence, not model-quality evidence.

## Claim scope

Bounded synthetic decode-cache validation with exact full-attention baseline: context lengths 4096, 8192, and 16384; cache budgets 128, 256, and 512; 32 fixed seeds; 384 decode steps per configuration. The proposed multi-step guard did not beat stride-hybrid on old-target retention, but slightly improved attention-output MSE and cosine.

## Why it stopped

Bounded full synthetic validation failed to support the primary claim that multi-step old-context guard improves old-target retention over stride-hybrid at equal KV budget; evidence is mixed and not paper-positive.

## Recommended next action

Stop this synthetic branch as no-paper evidence; only continue with a real-model GPT-2-small-class long-context retrieval/perplexity benchmark if the controller wants one final depth-4 direct-evidence check.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model long-context cache guard versus stride-hybrid benchmark
- Success threshold: At the same KV budget, multi-step guard improves retrieval accuracy by at least 5 absolute percentage points or reduces perplexity/loss by at least 2 percent versus stride-hybrid, with no more than 10 percent decode throughput regression, across at least 3 fixed seeds.
- Stop condition: Stop if the real-model benchmark reproduces the synthetic result: old-target/retrieval accuracy is not better than stride-hybrid or quality gains are smaller than the stated threshold while latency is worse.

## Evidence references

- Artifact root: `<local-path>/projects/multi-step-truncated-cache-decode-for-old-context-guard-ve-98887aef65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
