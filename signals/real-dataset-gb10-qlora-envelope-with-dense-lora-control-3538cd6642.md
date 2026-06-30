# Real-dataset GB10 QLoRA envelope with dense LoRA control

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-dataset-gb10-qlora-envelope-with-dense-lora-control-3538cd6642`
Run ID: `real-dataset-gb10-qlora-envelope-with-dense-lora-control-3538cd6642-20260604T132834417610+0000`

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

- Parent run decision: 4-bit base LoRA fine-tuning within 6GB on GB10: enoch://control-plane/projects/4-bit-base-lora-fine-tuning-within-6gb-on-gb10-f785846a763b/runs/4-bit-base-lora-fine-tuning-within-6gb-on-gb10-f785846a763b-20260604T081644005097+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/be144912c7ce

## What looked useful

QLoRA compatibility on GB10 is confirmed. GPT-2-small QLoRA used 10.7% more allocated CUDA memory and was 25.3% slower than dense LoRA. GPT-2-medium QLoRA used 4.5% less allocated memory, but reserved 12.27 GiB versus 1.42 GiB for dense LoRA and was 60.0% slower; final validation loss was close but slightly worse.

## Boundaries and scale limits

Only GPT-2-small for 40 steps and GPT-2-medium for 20 steps, batch size 1, block size 256, WikiText-2, LoRA rank 8. No 7B+ models, no long convergence, no batch/sequence sweep, and no nvidia-smi device-memory counter because GB10 reports memory as not supported.

## Claim scope

On GB10 with CUDA 13 / SM 12.1, PEFT bitsandbytes QLoRA can train GPT-2-small and GPT-2-medium adapters on WikiText-2, but in this short controlled harness it does not provide a compelling memory-envelope win over a dense bf16 frozen-base LoRA control.

## Why it stopped

Controlled Tier 1 direct test completed; result is useful no-paper evidence, not paper-positive validation.

## Recommended next action

Run a bounded batch/sequence/model-size sweep on GB10 to identify the actual QLoRA break-even point where dense LoRA fails to fit or QLoRA cuts both allocated and reserved memory by a meaningful margin.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 QLoRA break-even sweep against dense LoRA
- Success threshold: Identify a reproducible GB10 setting where QLoRA either fits when dense LoRA does not, or reduces both peak allocated and peak reserved memory by at least 25% while keeping validation loss within 0.1 and throughput no worse than 2x dense LoRA.
- Stop condition: Stop if GPT-2-medium/larger sweeps show QLoRA remains slower than 2x dense LoRA without at least 25% reductions in both allocated and reserved memory, or if dense LoRA fits all tested settings with acceptable memory.

## Evidence references

- Artifact root: `<local-path>/projects/real-dataset-gb10-qlora-envelope-with-dense-lora-control-3538cd6642`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
