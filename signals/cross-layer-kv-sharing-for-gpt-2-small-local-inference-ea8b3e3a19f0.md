# Cross-Layer KV Sharing for GPT-2-Small Local Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cross-layer-kv-sharing-for-gpt-2-small-local-inference-ea8b3e3a19f0`
Run ID: `cross-layer-kv-sharing-for-gpt-2-small-local-inference-ea8b3e3a19f0-20260608T080405041727+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ea49e4cdc158

## What looked useful

Naive cross-layer KV sharing is not a viable drop-in GPT-2-small inference memory reduction for greedy generation. All sharing variants had zero exact greedy-sequence matches and only about 3.6% to 4.9% token agreement with baseline over 48 generated tokens. Adjacent-pair sharing retained 6 of 12 cache layers and had a small teacher-forced NLL improvement on this prompt set, but gold-token probability dropped and greedy generation diverged after roughly one token, indicating substantial distribution shift rather than preserved behavior.

## Boundaries and scale limits

Bounded to 12 custom prompt/continuation cases, 48 teacher-forced gold tokens per case, 48 greedy generation tokens per case, fp16 Hugging Face GPT-2-small on one NVIDIA GB10. The implementation estimates quality and theoretical retained-cache layers but does not implement a fused memory-saving kernel and does not train or calibrate the model for sharing.

## Claim scope

GPT-2-small local CUDA inference with naive inference-time cross-layer KV-cache sharing during incremental decode; prompt prefill is standard, selected layers reuse other layers' past keys/values during teacher-forced and greedy continuation tests.

## Why it stopped

Early bounded direct local evidence falsifies the naive drop-in hypothesis rather than fully validating all possible trained or calibrated KV-sharing architectures.

## Recommended next action

Stop the drop-in sharing line; if continuing, run a bounded calibration follow-up that learns lightweight per-layer KV projections or sharing gates and requires preserved greedy/logit agreement before any larger benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated adjacent-layer KV sharing for GPT-2-small decode
- Success threshold: At 50% retained KV-cache layers, held-out NLL delta <= 0.10 versus baseline, mean KL to baseline <= 0.05 nats/token, top-1 agreement >= 95%, and greedy token agreement >= 90% over at least 256 generated tokens per prompt across 50 prompts.
- Stop condition: Stop if calibrated adjacent-pair sharing cannot reach top-1 agreement >= 90% and NLL delta <= 0.20 on a small validation split after a bounded adapter/gate calibration run.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-sharing-for-gpt-2-small-local-inference-ea8b3e3a19f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
