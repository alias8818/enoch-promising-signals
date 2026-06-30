# 2-bit KV residual codebook for long context on small LMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-residual-codebook-for-long-context-on-small-lms-881fe50b4b2f`
Run ID: `2-bit-kv-residual-codebook-for-long-context-on-small-lms-881fe50b4b2f-20260529T222359302390+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e63c8b435f0c

## What looked useful

Residual-delta 2-bit KV coding was worse than learned scalar 2-bit coding on the tiny smoke, but on GPT-2-small it produced attention relative MSE 0.1989 vs 0.5658 at 512 tokens and 0.1835 vs 0.5498 at 768 tokens, with similar KV relative MSE. This supports a bounded mechanism worth direct inference testing, not a paper-ready claim.

## Boundaries and scale limits

Evaluated only GPT-2-small up to 768-token samples within its 1024-position limit, plus a one-layer tiny-gpt2 smoke. No packed 2-bit kernel, decode-latency benchmark, perplexity run, generation-quality test, modern long-context LM, or context beyond GPT-2's native limit.

## Claim scope

Cache-level probe on GPT-2-small-class KV tensors from WikiText-2: a strict 2-bit adjacent-token residual-delta codebook reduced causal attention-output relative MSE versus a learned scalar 2-bit codebook at 512 and 768 token sequence lengths, but the tiny-model smoke was negative and no end-to-end decoding quality was measured.

## Why it stopped

No-paper useful signal: the result is cache-level proxy evidence, not full validation of long-context model quality or serving efficiency.

## Recommended next action

Run a bounded end-to-end inference follow-up that patches generation/evaluation KV caches and compares fp16, learned scalar 2-bit, residual-delta 2-bit, and anchored residual-delta KV on long-context perplexity plus realistic memory/latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end residual-delta 2-bit KV cache evaluation on small LMs
- Success threshold: Residual-delta 2-bit KV has at least 25% lower loss/perplexity degradation than learned scalar 2-bit KV at comparable effective bits per element, while preserving a meaningful memory reduction and not adding more than 20% decode latency in the tested implementation.
- Stop condition: Stop if residual-delta KV does not beat learned scalar 2-bit KV on next-token loss/perplexity in GPT-2-small, or if the implementation overhead eliminates practical memory/latency value.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-residual-codebook-for-long-context-on-small-lms-881fe50b4b2f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
