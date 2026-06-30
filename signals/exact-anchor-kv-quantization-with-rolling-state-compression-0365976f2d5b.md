# Exact-Anchor KV Quantization with Rolling State Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-quantization-with-rolling-state-compression-0365976f2d5b`
Run ID: `exact-anchor-kv-quantization-with-rolling-state-compression-0365976f2d5b-20260608T135524392571+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/92313955d92d

## What looked useful

Exact-anchor rolling residual compression lost to a conservative budget-matched uniform int5 KV quantization control on all 30 primary configs/seeds. It beat lower-budget uniform int4 only for highly smooth rho=0.97 synthetic streams, indicating the mechanism depends strongly on real K/V temporal smoothness and is not robust by itself.

## Boundaries and scale limits

No pretrained transformer traces, no downstream perplexity, no fused serving kernel, sequence lengths only 256 and 1024, synthetic AR(1)-style K/V streams only.

## Claim scope

Bounded synthetic causal-attention probe of exact fp16 anchors every 16 tokens plus int4 rolling residual K/V reconstruction versus uniform per-token K/V quantization.

## Why it stopped

Proxy early falsification for the broad paper claim: synthetic attention evidence does not support exact anchors plus simple rolling residuals as a generally superior budget-matched KV-cache compression method.

## Recommended next action

Run a bounded real-trace follow-up on GPT-2-small KV caches to measure layer/head temporal smoothness and compare budget-matched anchor-residual versus uniform quantization on attention error and perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2 KV Trace Test for Exact-Anchor Rolling Quantization
- Success threshold: At equal memory budget, anchor-residual quantization must reduce mean attention-output relative L2 by at least 20 percent versus uniform quantization and keep validation perplexity degradation no worse than the uniform control.
- Stop condition: Stop if real KV traces are not smoother than the synthetic rho=0.85 regime or if budget-matched anchor-residual loses to uniform quantization on attention error in at least two representative layers.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-quantization-with-rolling-state-compression-0365976f2d5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
