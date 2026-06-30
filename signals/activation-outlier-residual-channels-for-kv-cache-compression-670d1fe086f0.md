# Activation-Outlier Residual Channels for KV-Cache Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-outlier-residual-channels-for-kv-cache-compression-670d1fe086f0`
Run ID: `activation-outlier-residual-channels-for-kv-cache-compression-670d1fe086f0-20260522T005226764313+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/130c0d3912f4

## What looked useful

Residual full-precision capacity materially helps low-bit KV-cache fidelity, but activation-outlier channel selection only weakly outperformed a same-budget random residual control on the primary mixed-window run: mean CE-delta improvement 0.064 with 95% CI crossing zero and 7/12 wins. Same-budget random controls are necessary before claiming novelty.

## Boundaries and scale limits

Short local mixed text windows, one small pretrained model, fake quantization rather than packed kernels, one bit width and residual fraction in the primary run, one random residual draw per sample, no serving throughput or memory-bandwidth measurement, and no standard benchmark corpus.

## Claim scope

On a local distilgpt2 KV-cache fake-quantization probe with 96-token contexts and 31 evaluated continuation tokens per sample, keeping the top 12.5% activation-magnitude KV head channels in full precision at an approximate 3.75 bits/value reduced damage versus 2-bit quantize-all and produced a small, not clearly robust advantage over same-budget random residual channels.

## Why it stopped

Primary evidence is a bounded proxy/local mechanism test: it supports residual capacity and mildly favors activation-outlier selection, but does not beat the same-budget random residual control strongly enough for a paper claim or full validation.

## Recommended next action

Run a bounded deepen follow-up on GPT-2-small-class scale with a real benchmark corpus, multiple random residual seeds, generated-token recompression, and residual-fraction/bit-width ablations; stop this run as no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Benchmark-scale activation-outlier residual KV-cache ablation
- Success threshold: Activation-outlier residuals beat same-budget random residuals by at least 0.05 mean CE-delta or 5% relative KL reduction with paired 95% CI above zero across at least 100 benchmark windows, while preserving a clear advantage over quantize-all.
- Stop condition: Stop if activation-outlier residuals fail to beat same-budget random residuals under paired statistics for two bit-width/residual-fraction settings or if improvements disappear when generated tokens are recompressed.

## Evidence references

- Artifact root: `<local-path>/projects/activation-outlier-residual-channels-for-kv-cache-compression-670d1fe086f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
