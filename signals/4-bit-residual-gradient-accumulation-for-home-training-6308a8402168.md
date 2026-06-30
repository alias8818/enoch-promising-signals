# 4-Bit Residual Gradient Accumulation for Home Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-residual-gradient-accumulation-for-home-training-6308a8402168`
Run ID: `4-bit-residual-gradient-accumulation-for-home-training-6308a8402168-20260619T084232000426+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/d1eab8914979

## What looked useful

Across three medium seeds, q4_resid4 matched fp32 validation accuracy (0.93185) and nearly matched validation loss (0.17232 vs 0.17218) while final-step gradient relative L2 error was 0.0264 versus 0.2596 for plain q4. In a 64-microbatch normal-gradient sweep, q4_resid4 reduced relative L2 error from 0.8384 to 0.0512 versus plain q4.

## Boundaries and scale limits

Evidence is limited to toy/generated data, small MLPs, synthetic gradient tensors, simulated packed int4 storage estimates, SGD, and runs up to 300 optimizer updates. It does not validate GPT-2-small-class or LLM fine-tuning, AdamW interactions, true packed-kernel memory behavior, throughput, or long-run stability.

## Claim scope

On a generated small-MLP CUDA training task and synthetic gradient accumulation sweeps, a blockwise 4-bit accumulator plus a blockwise 4-bit residual buffer closely approximated fp32 gradient accumulation while reducing estimated accumulator storage to about 25.8% of fp32.

## Why it stopped

Useful bounded mechanism signal, but no-paper closure because the evidence is toy/synthetic and simulated-storage rather than direct home LLM training validation.

## Recommended next action

Run a bounded deepen follow-up on a small transformer or GPT-2-small-class model with AdamW, measured peak memory, packed or realistically emulated int4 buffers, and a predeclared loss/perplexity tolerance versus fp32 gradient accumulation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer Validation of 4-Bit Residual Gradient Accumulation
- Success threshold: q4_resid4 final validation loss or perplexity within 1% of fp32 accumulation, gradient cosine at least 0.995 on sampled updates, and measured peak memory reduction attributable to compressed accumulation buffers.
- Stop condition: Stop as negative if q4_resid4 exceeds 1% validation loss/perplexity degradation, shows repeated instability/divergence, or measured memory savings are negligible after realistic storage overhead.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-residual-gradient-accumulation-for-home-training-6308a8402168`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
