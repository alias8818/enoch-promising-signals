# Compressed State Checkpointing at Anchor Boundaries for On-Demand KV Reconstruction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-checkpointing-at-anchor-boundaries-for-on-demand-kv-reconstruction-274a5ba33ca7`
Run ID: `compressed-state-checkpointing-at-anchor-boundaries-for-on-demand-kv-reconstruction-274a5ba33ca7-20260524T061413387168+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/81f1d9eb3e82

## What looked useful

A favorable low-rank proxy shows limited redundancy in GPT-style K/V tensors: anchor64/rank16 gave about 1.98x compression with KL 0.034 to 0.040 and full argmax match at prefix lengths 128/192, while rank8 settings at 2.64x to 3.97x raised KL to 0.62 to 2.75 and often changed the top token.

## Boundaries and scale limits

Single small pretrained model, short built-in text prompts, one-step continuation only, SVD over true K/V tensors rather than learned hidden-state checkpoint reconstruction, and no serving/runtime or quantization baseline.

## Claim scope

On an 8-sample distilgpt2 probe, anchor-aligned truncated-SVD reconstruction of exact K/V tensors preserved next-step logits near 2x float-value compression for longer prefixes, but degraded substantially at 2.6x to 4x and beyond.

## Why it stopped

No-paper closure: the corrected proxy supports only a narrow useful signal around 2x compression and does not validate aggressive compressed state checkpointing or on-demand KV reconstruction as a serving architecture.

## Recommended next action

Run a bounded deepen test comparing learned or quantized anchor reconstruction against int8/int4 KV quantization baselines on GPT-2-small-class models with multi-step rollouts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned anchor KV reconstruction versus quantized KV baselines on GPT-2-small rollouts
- Success threshold: At 2x or better effective memory reduction, mean KL <= 0.1, mean NLL delta <= 0.1, top-1 agreement >= 95%, and no worse latency than reconstructing from exact lower-rank SVD factors for the same prompt set.
- Stop condition: Stop if matched-memory quantized KV is equal or better on KL/NLL/top-token metrics, or if anchor reconstruction exceeds mean KL 0.5 at 2x memory reduction on the first 100-prompt rollout.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-checkpointing-at-anchor-boundaries-for-on-demand-kv-reconstruction-274a5ba33ca7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
