# Quantized Agent Residual Safety

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-agent-residual-safety-ffb017ce72fb`
Run ID: `quantized-agent-residual-safety-ffb017ce72fb-20260521T200443227399+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c09e02813723

## What looked useful

2-bit quantization severely damaged the proxy safety boundary (unsafe accept 0.3843, benign refusal 0.4419); adding a residual safety head reduced unsafe accept to 0.0594 and benign refusal to 0.1345. For 3-8 bits, quantized models were close to dense but residual correction still reduced unsafe accept from about 0.073-0.074 to about 0.059-0.060.

## Boundaries and scale limits

Synthetic embeddings only; no real LLM, no natural-language prompts, no tool-use agent, no production quantization kernels, no activation or KV-cache quantization, and no human safety labels. Main run took 7.419 seconds and should not be interpreted as broad/full-scale validation.

## Claim scope

In an 8-seed synthetic MLP proxy with generated safety-boundary and obfuscated-unsafe buckets, a small full-precision residual head trained on calibration data reduced unsafe false accepts after post-training weight quantization, with the largest recovery at 2 bits and smaller consistent gains at 3-8 bits.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only, not direct LLM agent safety validation.

## Recommended next action

Run a bounded deepen follow-up on a small real language-model safety proxy with matched dense, quantized, and quantized-plus-residual variants before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM residual safety under low-bit quantization
- Success threshold: Residual variant reduces unsafe compliance by at least 25% relative to the quantized baseline at matched or no more than 5 percentage points worse benign over-refusal, across at least 3 seeds or model checkpoints.
- Stop condition: Stop if quantization does not increase unsafe compliance versus dense, or if residual correction only trades safety gains for more than 5 percentage points additional benign over-refusal.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-residual-safety-ffb017ce72fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
