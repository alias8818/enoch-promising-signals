# 2-bit KV cache with activation-derived residual correction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-activation-derived-residual-correction-271290f6440d`
Run ID: `2-bit-kv-cache-with-activation-derived-residual-correction-271290f6440d-20260630T094503491360+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b208dfad9bd4

## What looked useful

Activation-derived summary features gave repeatable small attention-output error improvements in synthetic sweeps: +1.20% in the main run, +2.27% in the longer stress run, and +1.47% when the synthetic nonlinear KV residual was disabled. Raw K/V reconstruction MSE slightly worsened, so the mechanism appears to be attention-output compensation rather than residual reconstruction.

## Boundaries and scale limits

No pretrained model, perplexity, downstream accuracy, real decoding latency, memory bandwidth, or production cache-packing evidence was produced. The tested activation-summary side channel adds roughly 44 bytes/token in the default synthetic setup, about 34% overhead over the simple 2-bit KV plus fp16 scale/min representation.

## Claim scope

In a synthetic transformer-like causal attention layer, 2-bit groupwise KV quantization plus compact activation-summary residual correction reduced attention-output relative MSE by about 1-2% versus plain 2-bit KV quantization and beat random-feature and bias controls.

## Why it stopped

Synthetic proxy evidence is useful but not direct/full validation; stop this run as no-paper evidence rather than claiming a deployable or paper-positive 2-bit KV cache method.

## Recommended next action

Run a bounded pretrained-transformer follow-up on GPT-2-small-class decoding that compares 2-bit KV, 2-bit KV plus activation-summary correction, and matched-overhead side-information controls on perplexity, attention-output error, latency, and memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small validation of activation-summary correction for 2-bit KV cache
- Success threshold: Activation-summary correction improves loss or attention-output error by at least 5% of the fp16-to-2-bit degradation while matched-overhead random/bias controls do not, and total cache memory remains at least 3x smaller than fp16 KV.
- Stop condition: Stop if the corrected 2-bit cache fails to beat matched-overhead controls on both perplexity/loss and attention-output error, or if side-information overhead reduces memory savings below 3x versus fp16 KV.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-activation-derived-residual-correction-271290f6440d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
