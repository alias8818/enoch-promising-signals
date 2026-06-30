# INT2 KV-Cache with Periodic Residual Flush for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-kv-cache-with-periodic-residual-flush-for-long-context-8b0d67568b02`
Run ID: `int2-kv-cache-with-periodic-residual-flush-for-long-context-8b0d67568b02-20260529T051903340748+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/112dceb5368f

## What looked useful

Corrected comparable runs found residual flushing improved smooth-query relative L2 by 33.6% at 2k, 53.9% at 8k, and 74.1% at 32k versus plain INT2, but worsened an 8k needle query by 17.4% and improved a 32k needle query by 25.1%. This supports a mechanism worth model-level testing but not a paper claim.

## Boundaries and scale limits

No pretrained model perplexity, generation, packed INT2 kernel, production runtime, or real long-context benchmark was run. Decode timings are on dequantized proxy tensors and are not speedup evidence.

## Claim scope

Synthetic GPU proxy only: 16-head, head_dim 128 decode-attention traces up to 32768 tokens show residual-feedback INT2 KV with periodic reset can reduce relative L2 error on smooth/correlated queries at about 5.3x estimated cache compression, but the effect is not robust on needle-style retrieval.

## Why it stopped

Closed as no-paper useful signal because corrected proxy evidence is synthetic and mixed: strong smooth-context gains but an 8k needle-regression early falsifies a broad robustness claim.

## Recommended next action

Run a bounded real-model decode/perplexity follow-up on a small pretrained transformer with FP16 KV, plain INT2 KV, and residual-flush INT2 KV on identical long-context prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model INT2 KV residual-flush perplexity and retrieval check
- Success threshold: Residual-flush INT2 must improve next-token loss/perplexity degradation versus plain INT2 by at least 25% relative, preserve at least 4x KV memory reduction versus FP16 including metadata, and show no statistically meaningful needle-retrieval regression at tested lengths.
- Stop condition: Stop if residual-flush INT2 is worse than plain INT2 on either perplexity/loss or needle retrieval at any primary tested context length, or if metadata/residual storage reduces effective compression below 4x.

## Evidence references

- Artifact root: `<local-path>/projects/int2-kv-cache-with-periodic-residual-flush-for-long-context-8b0d67568b02`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
