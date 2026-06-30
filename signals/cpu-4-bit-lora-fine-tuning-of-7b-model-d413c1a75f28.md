# CPU 4-bit LoRA Fine-Tuning of 7B Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-4-bit-lora-fine-tuning-of-7b-model-d413c1a75f28`
Run ID: `cpu-4-bit-lora-fine-tuning-of-7b-model-d413c1a75f28-20260628T093103058157+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9dde20d17e26

## What looked useful

CPU 4-bit LoRA is mechanically viable in current bitsandbytes, but the measured 4096x4096 train-step throughput was only 0.00749 effective dense TFLOP/s. The resulting 7B-class lower-bound estimate is about 5,187 seconds per 1,000 training tokens, making this path impractical on the assigned CPU worker despite feasible adapter memory.

## Boundaries and scale limits

No full 7B model was loaded; no real dataset/tokenizer convergence was tested; scaling uses a 4096x4096 linear proxy and a LLaMA-7B-class layer-shape estimate. The estimate excludes attention softmax, layernorms, embeddings, checkpointing, data loading, and framework overhead, so it is a lower bound.

## Claim scope

On this 8-thread CPU worker, PyTorch 2.12.1+cpu plus bitsandbytes 0.49.2 can train LoRA adapters over frozen CPU 4-bit Linear4bit layers, but measured 4096-wide CPU 4-bit linear throughput projects impractical 7B-class adapter fine-tuning wall-clock.

## Why it stopped

Early bounded falsification of practical 7B CPU fine-tuning: mechanism works, but measured CPU 4-bit linear throughput implies multi-hour runtimes for tiny token counts before full-model overhead.

## Recommended next action

Stop this PyTorch/bitsandbytes CPU path as a no-paper useful signal; only revisit if testing a materially different optimized CPU backend with an end-to-end 7B adapter-training throughput target.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Optimized CPU backend comparison for 4-bit LoRA training
- Success threshold: Demonstrate at least 10x faster end-to-end or faithful-proxy throughput than this bitsandbytes CPU run while remaining under 24 GiB RAM, with a projected cost below 10 minutes per 1,000 training tokens.
- Stop condition: Stop if the optimized backend cannot run 4-bit adapter training on CPU, exceeds 24 GiB RAM for a faithful 7B-class setup, or projects above 30 minutes per 1,000 training tokens after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-4-bit-lora-fine-tuning-of-7b-model-d413c1a75f28`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
