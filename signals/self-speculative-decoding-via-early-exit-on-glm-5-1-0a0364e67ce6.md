# Self-Speculative Decoding via Early Exit on GLM-5.1

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-on-glm-5-1-0a0364e67ce6`
Run ID: `self-speculative-decoding-via-early-exit-on-glm-5-1-0a0364e67ce6-20260530T035121121257+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e8ab10a9b95e

## What looked useful

Cheap exits had very low exact-verification acceptance (4.4-17.2%); the near-final 5/6-layer exit improved to 26.2% acceptance but was too costly. Theoretical speedup stayed below 1.0 for every exit and the no-cache prototype measured 0.53-0.62x greedy throughput.

## Boundaries and scale limits

Single small GPT-style model, 24 prompts, 288 agreement positions per exit, 64 timing tokens per method, no production KV-cache implementation, no trained auxiliary exit heads, no GLM-5.1 weights.

## Claim scope

On a local distilgpt2 proxy, raw intermediate-layer early exits using the shared final LM head do not draft accurately enough for greedy self-speculative decoding to break even; this is not direct evidence on GLM-5.1.

## Why it stopped

Proxy early falsification: the tested raw early exits did not meet a plausible break-even acceptance/cost threshold, but this was not a full GLM-5.1 validation.

## Recommended next action

Stop this naive raw-early-exit path; run a bounded follow-up that trains or calibrates lightweight exit heads and tests exact acceptance plus KV-cache throughput before considering GLM-5.1 scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit heads for exact self-speculative acceptance
- Success threshold: Acceptance >= 60% at <= 50% layer cost and measured end-to-end speedup >= 1.15x over warmed greedy decoding on a held-out prompt suite.
- Stop condition: Stop if trained/calibrated exits remain below 45% acceptance at <= 50% layer cost or KV-cache timing remains below 1.0x greedy after implementation sanity checks.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-on-glm-5-1-0a0364e67ce6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
