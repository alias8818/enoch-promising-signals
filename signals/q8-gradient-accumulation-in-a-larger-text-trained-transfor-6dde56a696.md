# q8 gradient accumulation in a larger text-trained transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `q8-gradient-accumulation-in-a-larger-text-trained-transfor-6dde56a696`
Run ID: `q8-gradient-accumulation-in-a-larger-text-trained-transfor-6dde56a696-20260611T044134680556+0000`

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

- Parent run decision: Quantized gradient accumulation for home training: enoch://control-plane/projects/quantized-gradient-accumulation-for-home-training-5a10341ce073/runs/quantized-gradient-accumulation-for-home-training-5a10341ce073-20260611T024142834994+0000
- Parent run decision: Quantized accumulation in a small transformer trainer: enoch://control-plane/projects/quantized-accumulation-in-a-small-transformer-trainer-f7630aa823/runs/quantized-accumulation-in-a-small-transformer-trainer-f7630aa823-20260611T025531956922+0000

## What looked useful

Q8 accumulation with fp16 error feedback reached mean validation loss 1.5694 versus FP32 1.5611 (+0.0084), using 75% of FP32 accumulator memory. Q8 without error feedback reached 1.5720 (+0.0109), using 25% of FP32 accumulator memory. Both had about 1.57% mean accumulator reconstruction error and were slower than FP32 in the prototype.

## Boundaries and scale limits

Not tested on tokenized GPT-2-small-class or larger models, long training horizons, multi-node training, or fused Q8 accumulator kernels. Throughput reflects a Python/PyTorch prototype, not an optimized implementation.

## Claim scope

On a 14.4M-parameter byte-level causal transformer trained on WikiText-2 for 1000 optimizer steps across seeds 11, 22, and 33, per-tensor Q8 gradient accumulation remains trainable and close to FP32 accumulation but has a consistent small validation-loss penalty.

## Why it stopped

Tier-2 fixed-seed evidence on a real text transformer showed reproducible trainability and memory savings, but Q8 was consistently worse than the FP32 baseline in validation loss and slower in the prototype.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement blockwise or fused Q8 accumulation and require near-FP32 validation loss before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise fused Q8 gradient accumulation in a GPT-2-small-class text model
- Success threshold: Mean paired validation-loss delta <=0.003 versus FP32 across at least three fixed seeds, accumulator memory <=35% of FP32, no seed with visible divergence, and throughput at least 80% of FP32 after fusion.
- Stop condition: Stop if blockwise/fused Q8 still has >0.01 mean validation-loss delta, any seed diverges, or throughput remains below 50% of FP32 after removing Python per-parameter loops.

## Evidence references

- Artifact root: `<local-path>/projects/q8-gradient-accumulation-in-a-larger-text-trained-transfor-6dde56a696`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
