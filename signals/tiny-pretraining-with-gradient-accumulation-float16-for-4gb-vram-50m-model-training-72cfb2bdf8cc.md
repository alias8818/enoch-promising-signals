# Tiny pretraining with gradient accumulation + float16 for <4GB VRAM 50M model training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-pretraining-with-gradient-accumulation-float16-for-4gb-vram-50m-model-training-72cfb2bdf8cc`
Run ID: `tiny-pretraining-with-gradient-accumulation-float16-for-4gb-vram-50m-model-training-72cfb2bdf8cc-20260608T011215238441+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/87067f92a14c

## What looked useful

Float16 plus gradient accumulation gave a reproducible memory-feasible 50M-class training mechanics result under a 4 GB allocator budget. Controls showed fp32 accumulation peaked at 1.134 GB and fp16 batch-8 without accumulation peaked at 1.688 GB for the same effective 4096 tokens/step, while fp16 accumulation peaked at 0.630 GB.

## Boundaries and scale limits

Synthetic random tokens only; 10 measured optimizer steps; no real dataset, tokenizer, checkpoint stress, long-run convergence, or direct discrete <=4 GB VRAM telemetry. GB10 nvidia-smi reports memory usage as Not Supported, so the memory result is a PyTorch CUDA allocator measurement rather than hardware VRAM telemetry.

## Claim scope

On the local GB10 PyTorch CUDA stack, a 49.88M parameter GPT-style decoder-only model with fp16 parameters, sequence length 512, micro-batch 1, and gradient accumulation 8 ran a short synthetic next-token training loop with stable loss scale at 0.630 GB peak CUDA allocated and 0.671 GB peak CUDA reserved.

## Why it stopped

Closed as no-paper useful signal because the run directly supports only a short synthetic memory-mechanics claim, not full pretraining viability or publication-grade training evidence.

## Recommended next action

Run the same harness with a real small text dataset and either a runtime-enforced CUDA memory cap or a discrete 4 GB GPU for at least 1000 optimizer steps with checkpoint save/load and loss-scale stability telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data 4GB-capped 50M fp16 gradient-accumulation pretraining probe
- Success threshold: Complete at least 1000 optimizer steps with no OOM, no sustained loss-scale collapse, successful checkpoint save/load, and peak memory below 4 GB while maintaining a non-divergent real-data loss curve.
- Stop condition: Stop if the real-data run exceeds the 4 GB memory cap, repeatedly overflows until loss scale collapses below 16, cannot checkpoint within the budget, or shows clear loss divergence for 100 consecutive optimizer steps after warmup.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pretraining-with-gradient-accumulation-float16-for-4gb-vram-50m-model-training-72cfb2bdf8cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
