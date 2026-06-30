# 8-bit Adam Quantization for GPT-2-Small on 10GB VRAM

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `8-bit-adam-quantization-for-gpt-2-small-on-10gb-vram-82bed9943aee`
Run ID: `8-bit-adam-quantization-for-gpt-2-small-on-10gb-vram-82bed9943aee-20260604T173351793369+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6ee94b19fb2f

## What looked useful

8-bit AdamW reduced GPT-2-small optimizer state from about 996 MB to 254 MB in fp32 and from about 498 MB to 254 MB in bf16, but batch 4 sequence 1024 fit under 10GB with standard AdamW while batch 8 sequence 1024 exceeded 10GB with both optimizers.

## Boundaries and scale limits

Synthetic random-token batches only; short one-step to three-step runs; no physical 10GB discrete GPU; no real corpus convergence or long-run fragmentation validation; no gradient checkpointing or alternate attention kernels.

## Claim scope

On an NVIDIA GB10 running synthetic GPT-2-small-class CUDA training steps, bitsandbytes AdamW8bit reduces optimizer-state memory substantially, but does not move the observed 10GB feasibility boundary for the tested sequence-1024 GPT-2-small configurations.

## Why it stopped

No-paper useful signal: optimizer-state compression was verified, but direct memory probes show standard AdamW already fits the viable GPT-2-small 10GB settings and 8-bit AdamW does not rescue the first over-budget long-context batch.

## Recommended next action

Stop this standalone GPT-2-small 10GB optimizer-quantization project; future work should target activation-memory methods or a larger model where optimizer state is the limiting component.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-quantization-for-gpt-2-small-on-10gb-vram-82bed9943aee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
