# Real tiny-LM validation of low-precision gradient accumulation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-tiny-lm-validation-of-low-precision-gradient-accumula-f7577bc287`
Run ID: `real-tiny-lm-validation-of-low-precision-gradient-accumula-f7577bc287-20260608T032816243076+0000`

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

- Parent run decision: Low-precision gradient accumulation for memory-efficient tiny model training: enoch://control-plane/projects/low-precision-gradient-accumulation-for-memory-efficient-tiny-model-training-5e92502b7b9b/runs/low-precision-gradient-accumulation-for-memory-efficient-tiny-model-training-5e92502b7b9b-20260607T174002419198+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa1218c962cc

## What looked useful

Controlled tiny-LM training supports the mechanism that low-precision gradient accumulation can preserve validation loss at small scale: at 1,000 updates BF16 was +0.0053% relative NLL vs FP32, FP16 was -0.0001%, and INT8 was +0.0202%, all across three seeds.

## Boundaries and scale limits

Not tested on Transformer LMs, standard tokenized corpora, AdamW optimizer state, GPU hardware kernels, distributed training, longer horizons, larger parameter counts, or production mixed-precision stacks.

## Claim scope

In a 76k-parameter NumPy character-level tiny LM trained on Tiny Shakespeare with SGD, context length 16, 8-way microbatch gradient accumulation, and three seeds, BF16-simulated and FP16 accumulation matched FP32 validation loss over 1,000 updates; tensorwise INT8 accumulation was stable and within 0.5% validation loss but had larger gradient error.

## Why it stopped

Strict paper gate: this is direct small-LM evidence and a useful mechanism signal, but it is too narrow for publication-grade claims about modern low-precision gradient accumulation.

## Recommended next action

Run a bounded deepen follow-up with a tiny Transformer LM plus AdamW on a standard tokenized corpus, requiring BF16/FP16 accumulation to remain within 0.5% validation loss of FP32 over at least five seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer AdamW validation of low-precision gradient accumulation
- Success threshold: BF16 and FP16 accumulation each finish within 0.5% validation loss of FP32 accumulation, show no divergence across at least five seeds, and keep accumulated-gradient cosine at or above 0.999 at initialization and mid-training.
- Stop condition: Stop as unsupported if either BF16 or FP16 accumulation diverges, exceeds 0.5% validation-loss degradation versus FP32 in at least two seeds, or shows persistent accumulated-gradient cosine below 0.999 with matching loss degradation.

## Evidence references

- Artifact root: `<local-path>/projects/real-tiny-lm-validation-of-low-precision-gradient-accumula-f7577bc287`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
