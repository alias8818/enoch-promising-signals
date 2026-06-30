# Small-transformer validation of 2-bit base plus 4-bit residual adapters

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-validation-of-2-bit-base-plus-4-bit-resi-b257afd9ad`
Run ID: `small-transformer-validation-of-2-bit-base-plus-4-bit-resi-b257afd9ad-20260619T184552410283+0000`

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

- Parent run decision: Home CPU fine-tuning: 2-bit base + 4-bit residual adapter: enoch://control-plane/projects/home-cpu-fine-tuning-2-bit-base-4-bit-residual-adapter-14a636b63b6b/runs/home-cpu-fine-tuning-2-bit-base-4-bit-residual-adapter-14a636b63b6b-20260619T182502865378+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/38572eb15e20

## What looked useful

Static 2-bit quantization raised mean validation loss from 0.4581 to 1.3719. Training 4-bit residual adapters reduced mean validation loss to 0.3924 across seeds 7, 11, and 13, exceeding the predeclared 50% gap-recovery and 0.10 loss-improvement thresholds in all seeds.

## Boundaries and scale limits

Tiny synthetic corpus, tiny CPU-only transformer, full-shape residual tensors, no real text corpus, no GPT-2-small-class baseline, no activation quantization, no inference kernel or throughput validation.

## Claim scope

In a deterministic 48,736-parameter synthetic character-language transformer, a frozen 2-bit affine-quantized base plus trainable full-shape 4-bit residual tensors recovered the validation loss lost to static 2-bit quantization across three seeds.

## Why it stopped

No-paper closure: the Tier 1 direct small test supports the mechanism but is limited to a tiny synthetic model and is not publication-grade validation.

## Recommended next action

Run a bounded medium confirmation on a real text corpus with a GPT-2-small-class or parameter-matched transformer, including dense, static 2-bit, 2-bit-plus-4-bit-residual, and LoRA-style residual controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-text confirmation of 2-bit base plus 4-bit residual adapters
- Success threshold: Across at least three seeds, recover >=50% of the dense-to-2-bit validation-loss gap, improve loss by >=0.10 versus static 2-bit, and remain below 25% of fp32 dense parameter storage.
- Stop condition: Stop as negative if the residual method fails the recovery threshold in two or more seeds or if a similarly budgeted LoRA-style residual matches or exceeds it with lower storage.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-validation-of-2-bit-base-plus-4-bit-resi-b257afd9ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
