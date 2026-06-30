# INT2 KV-cache with per-head residual channels for long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-kv-cache-with-per-head-residual-channels-for-long-context-inference-2a004ff26ed4`
Run ID: `int2-kv-cache-with-per-head-residual-channels-for-long-context-inference-2a004ff26ed4-20260619T033803611399+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4434a2c467db

## What looked useful

At 8 residual channels per 128-channel head, calibrated residual channels reduced relative attention-output MSE by 11.5x on outlier profiles and 6.9x on drift profiles versus no-residual INT2 while retaining estimated 5.12x cache compression. A matched random-residual ablation failed to recover the effect on outlier/drift profiles.

## Boundaries and scale limits

Evidence is limited to synthetic KV tensors and attention reconstruction metrics on one GB10 host; no trained LLM KV traces, end-to-end perplexity, retrieval benchmark, production packed INT2 kernel, or decode-throughput validation was run.

## Claim scope

In synthetic long-context KV-cache probes with persistent per-head channel outliers or drift, calibrated fp16 residual channels materially improve INT2 attention reconstruction at an estimated 4.0x-5.12x compression versus fp16 KV cache.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy attention reconstruction, not full validation on real LLM inference.

## Recommended next action

Run a bounded direct follow-up on real trained-model KV traces and end-to-end perplexity/retrieval metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace validation for INT2 residual-channel cache
- Success threshold: At matched cache memory, calibrated residual INT2 should improve relative attention-output MSE by at least 2x versus no-residual INT2 and improve or preserve perplexity/retrieval quality versus the strongest tested low-bit baseline while retaining at least 4x KV-cache compression versus fp16.
- Stop condition: Stop if calibrated residual channels fail to beat random residual channels on real KV traces or if end-to-end quality regresses more than the predefined tolerance at the target compression.

## Evidence references

- Artifact root: `<local-path>/projects/int2-kv-cache-with-per-head-residual-channels-for-long-context-inference-2a004ff26ed4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
