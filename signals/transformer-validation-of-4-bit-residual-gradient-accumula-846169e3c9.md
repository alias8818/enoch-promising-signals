# Transformer Validation of 4-Bit Residual Gradient Accumulation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `transformer-validation-of-4-bit-residual-gradient-accumula-846169e3c9`
Run ID: `transformer-validation-of-4-bit-residual-gradient-accumula-846169e3c9-20260619T090247261841+0000`

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

- Parent run decision: 4-Bit Residual Gradient Accumulation for Home Training: enoch://control-plane/projects/4-bit-residual-gradient-accumulation-for-home-training-6308a8402168/runs/4-bit-residual-gradient-accumulation-for-home-training-6308a8402168-20260619T084232000426+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/d1eab8914979

## What looked useful

Across three CUDA GB10 seeds, residual int4 accumulation stayed within 5% of FP32 final eval loss and improved mean relative L2 error versus naive int4, but mean gradient cosine was only about 0.972 and failed the 0.995 threshold in 0/3 seeds.

## Boundaries and scale limits

Tiny 2-layer Transformer only; no real corpus, GPT-2-small-class model, packed int4 kernel, memory-bandwidth measurement, distributed training, mixed-precision interaction, or long-horizon stability test.

## Claim scope

Toy-scale direct Transformer training test on a deterministic modular next-token task: per-tensor symmetric 4-bit residual gradient accumulation improves over naive 4-bit accumulation but does not preserve accumulated-gradient direction to the predeclared high-fidelity threshold.

## Why it stopped

No-paper closure: controlled direct small Transformer evidence supports a mechanism improvement over naive int4, but the residual method failed the predeclared gradient-fidelity threshold in every seed.

## Recommended next action

Run a bounded deepen test using blockwise or groupwise 4-bit residual accumulation on the same harness, requiring >=0.995 mean gradient cosine and <=2% eval-loss delta versus FP32 across three seeds before considering a larger Transformer validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise 4-bit residual gradient accumulation fidelity test
- Success threshold: Residual blockwise/groupwise int4 passes all three seeds with mean accumulated-gradient cosine >= 0.995, final eval loss within 2% of FP32, and lower mean relative L2 error than both naive int4 and per-tensor residual int4.
- Stop condition: Stop if blockwise/groupwise residual int4 still has mean accumulated-gradient cosine below 0.990 in two seeds or final eval loss exceeds FP32 by more than 5%; record as a likely non-viable 4-bit accumulation path at this scale.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-validation-of-4-bit-residual-gradient-accumula-846169e3c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
