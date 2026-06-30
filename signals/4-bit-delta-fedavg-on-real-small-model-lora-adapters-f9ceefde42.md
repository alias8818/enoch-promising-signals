# 4-bit delta FedAvg on real small-model LoRA adapters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-delta-fedavg-on-real-small-model-lora-adapters-f9ceefde42`
Run ID: `4-bit-delta-fedavg-on-real-small-model-lora-adapters-f9ceefde42-20260610T101757570596+0000`

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

- Parent run decision: 4-bit Delta Compression for Volunteer LoRA Averaging: enoch://control-plane/projects/4-bit-delta-compression-for-volunteer-lora-averaging-68cc05e7cf8d/runs/4-bit-delta-compression-for-volunteer-lora-averaging-68cc05e7cf8d-20260610T061435978533+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9adcfa60010b

## What looked useful

The direct Tier 1 test supports the practical mechanism that 4-bit adapter-delta FedAvg can preserve small-model LoRA validation loss relative to fp32 FedAvg at about 8x estimated communication compression. However, q4 aggregate delta cosine consistently missed the predeclared 0.995 diagnostic threshold, landing around 0.9933-0.9938 with about 10.7% relative delta error, so the result is mixed and not paper-ready.

## Boundaries and scale limits

Only 2 clients, one small pretrained model, WikiText-2 shards, 3 rounds, 12 local steps per client, one LoRA target family, and per-tensor symmetric int4 quantization were tested. No many-client non-IID setting, long training, GPT-2-small/7B-scale model, downstream task, groupwise/stochastic quantization, secure aggregation, or real network transfer validation was run.

## Claim scope

On distilgpt2 with rank-4 LoRA adapters on c_attn attention projections, 2 WikiText-2 clients, 3 FedAvg rounds, and matched local/eval minibatches, symmetric per-tensor 4-bit delta FedAvg matched fp32 delta FedAvg validation loss within 0.031% worst-case relative across 3 seeds while providing 7.99x estimated adapter-delta byte compression.

## Why it stopped

No-paper closure: this direct small controlled test produced useful mechanism evidence but missed the predeclared delta-cosine diagnostic threshold and is far below publication-grade scale.

## Recommended next action

Run a bounded medium confirmation with at least 8 clients, longer non-IID WikiText shards, more rounds, and fp32 vs per-tensor int4 vs groupwise or stochastic int4 delta FedAvg; stop paper work unless that run preserves loss within 1% and raises delta cosine or explains why cosine is not predictive.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium non-IID LoRA delta FedAvg confirmation with improved 4-bit quantization
- Success threshold: Across at least 3 seeds, 4-bit delta FedAvg must stay within 1% relative validation loss of fp32 FedAvg, achieve at least 6x estimated compression, and either reach aggregate delta cosine >=0.995 or show with ablations that loss parity is robust despite lower cosine.
- Stop condition: Stop as negative if all 4-bit variants exceed a 1% relative validation loss gap on two or more seeds, if compression drops below 6x after scale overhead, or if longer non-IID training shows divergence not present in fp32 FedAvg.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-delta-fedavg-on-real-small-model-lora-adapters-f9ceefde42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
