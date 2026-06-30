# 8-bit AdamW Optimizer States for CPU-Bound GPT-2-Small Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-optimizer-states-for-cpu-bound-gpt-2-small-training-12e63fb49fd3`
Run ID: `8-bit-adamw-optimizer-states-for-cpu-bound-gpt-2-small-training-12e63fb49fd3-20260621T111404432946+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/eacd2fdc9cc6

## What looked useful

Persistent state compression is real: GPT-2-small fp32 AdamW states account for 995,518,464 bytes versus 249,365,712 bytes for 8-bit states. On a 12,000,000-parameter timed subset, naive 8-bit optimizer steps averaged 0.6754 s versus 0.1976 s for fp32, and the convergence probe diverged badly relative to fp32.

## Boundaries and scale limits

No full GPT-2-small forward/backward or token training was run; gradients were synthetic for the shape/timing benchmark; convergence was tested on a quadratic proxy; production fused or nonlinear 8-bit optimizer implementations were not evaluated.

## Claim scope

Naive blockwise 8-bit AdamW optimizer states on GPT-2-small parameter shapes reduce persistent optimizer-state memory by about 4x, but in this CPU-only NumPy implementation they are slower per optimizer step, can increase peak RSS through dequantized temporaries, and fail a small convergence sanity probe.

## Why it stopped

Bounded CPU proxy evidence falsified the naive implementation as a practical improvement: it saved persistent state memory but was slower, had higher transient RSS, and failed the convergence probe; this is not a full validation of all 8-bit optimizer designs.

## Recommended next action

Stop this run as a proxy negative for the naive design; only revisit with a fused or streaming 8-bit AdamW implementation that avoids full dequantized temporaries and demonstrates stable second-moment quantization on real GPT-2-small-class training loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused stable 8-bit AdamW state update for CPU GPT-2-small-class training
- Success threshold: At least 35% lower peak RSS or persistent training memory than fp32 AdamW, no more than 10% slower end-to-end tokens/sec, and validation loss within 2% of fp32 AdamW over the bounded run.
- Stop condition: Stop if the fused 8-bit path is more than 10% slower end to end, exceeds fp32 peak RSS, or diverges/fails to stay within 2% validation loss on the bounded training benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-optimizer-states-for-cpu-bound-gpt-2-small-training-12e63fb49fd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
