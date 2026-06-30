# Tiny-VRAM LoRA via gradient low-rank projection during backprop

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-vram-lora-via-gradient-low-rank-projection-during-backprop-c6c1993f700e`
Run ID: `tiny-vram-lora-via-gradient-low-rank-projection-during-backprop-c6c1993f700e-20260605T110351202030+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/33df213a6f69

## What looked useful

The mechanism is not immediately falsified: projected gradients retained 19.3%, 35.8%, 53.3%, and 74.6% mean gradient energy at ranks 1, 2, 4, and 8, while all variants converged on the low-rank task. The practical tiny-VRAM claim remains unproven because the projection oracle was slower than standard LoRA and did not implement memory-saving backward or optimizer-state compression.

## Boundaries and scale limits

CPU-only NumPy proxy; exact SVD projection; full dense gradient materialized before projection; no PyTorch/custom autograd, GPU peak-memory measurement, transformer fine-tuning, tokenizer/data pipeline, or perplexity benchmark.

## Claim scope

On a controlled NumPy rank-8 linear adaptation task, ordinary rank-8 LoRA can still optimize when its factor gradients are formed from exact low-rank projections of the dense layer gradient; projection ranks 4 and 8 matched or exceeded standard LoRA final error in this toy setting.

## Why it stopped

No-paper closure: bounded proxy evidence supports the mechanism but does not directly validate tiny-VRAM LoRA or a production-feasible backprop path.

## Recommended next action

Stop this proxy run; next run should implement a PyTorch custom-autograd prototype that avoids dense-gradient materialization and measures peak memory, step time, and held-out loss against ordinary LoRA.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Custom-autograd projected-gradient LoRA memory probe
- Success threshold: At least 25% measured peak-memory reduction versus ordinary LoRA, held-out loss within 5% of ordinary LoRA, and step-time overhead no more than 20% on the tested small-transformer setup.
- Stop condition: Stop if the implementation must materialize dense gradients, if measured peak memory is not reduced by at least 10%, or if step-time overhead exceeds 50% before quality reaches the standard LoRA baseline.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-vram-lora-via-gradient-low-rank-projection-during-backprop-c6c1993f700e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
