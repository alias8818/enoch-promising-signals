# FP16 Residual KV Cache for 2-bit Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fp16-residual-kv-cache-for-2-bit-long-context-1319e8109e1c`
Run ID: `fp16-residual-kv-cache-for-2-bit-long-context-1319e8109e1c-20260525T225601658415+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3eeacff15f2e

## What looked useful

At 4096 context, a 256-token FP16 residual tail reduced relative attention-output error from 0.499 to 0.093 for recency-biased targets while using 20.9% of FP16 KV memory. For uniform targets, the same residual only reduced error from 0.492 to 0.476.

## Boundaries and scale limits

No real pretrained model, perplexity, generation-quality, production kernel, or full-serving evaluation was run. Results are synthetic and bounded to one 4096-token configuration with 5 seeds.

## Claim scope

Synthetic 4096-token decode-attention simulation with 2-bit affine per-token/head K/V quantization and recent FP16 residual windows. The mechanism helps when important attention targets are recent, but does not generally repair uniform long-range targets.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports a recency-specific mechanism but early-falsifies the broad claim that a small recent FP16 residual fixes 2-bit KV quality for arbitrary long-context attention.

## Recommended next action

Run a bounded real-model follow-up on a small pretrained transformer comparing FP16 KV, pure 2-bit KV, and 2-bit plus FP16 residual windows on long-context retrieval and perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model long-context evaluation of 2-bit KV with FP16 residual tail
- Success threshold: Residual-tail variants should recover at least 75% of the pure-2-bit quality loss on recent-target tasks at no more than 30% of FP16 KV memory, while clearly reporting failures on non-recent targets.
- Stop condition: Stop if residual-tail variants fail to recover at least 50% of pure-2-bit quality loss on recent-target tasks or require more than 40% of FP16 KV memory for the effect.

## Evidence references

- Artifact root: `<local-path>/projects/fp16-residual-kv-cache-for-2-bit-long-context-1319e8109e1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
