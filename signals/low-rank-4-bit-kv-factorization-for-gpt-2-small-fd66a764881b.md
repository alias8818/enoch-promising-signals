# Low-Rank 4-bit KV Factorization for GPT-2-Small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `low-rank-4-bit-kv-factorization-for-gpt-2-small-fd66a764881b`
Run ID: `low-rank-4-bit-kv-factorization-for-gpt-2-small-fd66a764881b-20260528T052129901329+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9f6fadd21e81

## What looked useful

Dense int4 K/V control achieved 3.98x K/V projection storage compression with PPL 56.64 vs baseline 53.45 (+0.058 NLL), while low-rank int4 SVD factors at the same 3.98x compression had PPL 79.67 (+0.399 NLL). Even full-rank int4 SVD factors degraded to PPL 66.17 at only 1.99x compression, pointing to quantized SVD factors as the failure mode.

## Boundaries and scale limits

Evaluated only GPT-2-small, Wikitext-2 validation text, 64x256-token sequences, post-training weight replacement, and dequantized inference. No quantized kernels, fine-tuning, long-context serving, downstream tasks, or larger models were tested.

## Claim scope

Post-training SVD low-rank factorization with signed 4-bit quantized factors for GPT-2-small attention K/V projection weights is not competitive on a bounded Wikitext-2 validation probe; dense int4 K/V quantization at matched storage is much stronger.

## Why it stopped

Proxy early falsification: direct GPT-2-small K/V weight replacement was tested, and low-rank 4-bit SVD factors were worse than dense int4 at matched storage and still degraded at full rank.

## Recommended next action

Stop this post-training SVD-factor route; the bounded evidence is a proxy early falsification, not full validation. A next bounded test should use quantization-aware factor fitting if pursuing factorized K/V further.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware factor fitting for GPT-2-small K/V projections
- Success threshold: At approximately 4x or better K/V projection storage compression, factorized int4 K/V is within +0.10 NLL of baseline and no more than +0.03 NLL worse than the dense int4 control on the same Wikitext-2 probe.
- Stop condition: Stop if optimized factorized int4 K/V remains more than +0.10 NLL behind dense int4 at matched storage after a bounded fitting run, or if fitting requires changing non-K/V weights to recover quality.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-4-bit-kv-factorization-for-gpt-2-small-fd66a764881b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
