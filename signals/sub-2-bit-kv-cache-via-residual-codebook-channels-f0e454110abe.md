# Sub-2-bit KV cache via residual codebook channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-2-bit-kv-cache-via-residual-codebook-channels-f0e454110abe`
Run ID: `sub-2-bit-kv-cache-via-residual-codebook-channels-f0e454110abe-20260522T190047637252+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c268c71efb9e

## What looked useful

Baseline strength is decisive. A 1.0 bps 256-entry vector codebook reached mean attention-output NMSE 0.493 across three layers, while 1-bit per-channel scalar reached 0.272 and 2-bit per-channel scalar reached 0.0249. Residual stages did not outperform a single larger codebook at the same counted bit rate.

## Boundaries and scale limits

Only distilgpt2, batch 8, sequence length 128, layers 0/2/5, reconstruction plus causal attention-output error. No downstream perplexity, long-context serving, held-out calibration split, optimized kernel, or large-model validation.

## Claim scope

Bounded proxy test on distilgpt2 attention activations: naive residual/vector codebook KV compression over channel groups can beat weak per-head scalar quantization, but does not beat stronger per-channel scalar quantization at comparable sub-2-bit budgets.

## Why it stopped

Proxy evidence does not support the broad naive residual-codebook KV-cache hypothesis against a strong scalar baseline; this is an early bounded falsification, not a full large-model validation.

## Recommended next action

Stop this run as a no-paper useful signal; only continue with a bounded deepen test if the next variant adds attention-aware or scale/offset-aware residual codebooks and compares against per-channel scalar quantization with honest metadata accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Attention-aware residual codebooks with per-channel scaling for sub-2-bit KV cache
- Success threshold: At <=1.5 metadata-inclusive bits per scalar, reduce mean attention-output NMSE by at least 25% versus 1-bit per-channel scalar and avoid layer-level regressions above 10% on at least a GPT-2-small-class model.
- Stop condition: Stop if the normalized residual-codebook variant fails to beat 1-bit per-channel scalar on mean attention-output NMSE across all tested layers or if metadata accounting pushes the method to >=2 bits per scalar.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-kv-cache-via-residual-codebook-channels-f0e454110abe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
