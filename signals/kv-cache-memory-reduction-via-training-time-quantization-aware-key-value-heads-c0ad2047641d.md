# KV-Cache Memory Reduction via Training-Time Quantization-Aware Key-Value Heads

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `kv-cache-memory-reduction-via-training-time-quantization-aware-key-value-heads-c0ad2047641d`
Run ID: `kv-cache-memory-reduction-via-training-time-quantization-aware-key-value-heads-c0ad2047641d-20260602T200830926830+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/534646c74c6b

## What looked useful

Analytical KV-cache memory falls by 50% at int8, 75% at int4, and 87.5% at int2 for the tested architecture, but 4-bit QAT's loss-delta advantage over FP training was effectively zero across three seeds: about -0.000056 at int8, +0.000092 at int4, and +0.000287 at int2.

## Boundaries and scale limits

Toy synthetic data, two-layer d_model 128 model, 500 training steps per variant, fake-quantized full-sequence attention rather than a real autoregressive paged KV-cache serving stack; no natural-language GPT-2-small-class or larger validation.

## Claim scope

On a three-seed tiny synthetic causal-Transformer probe, 4-bit training-time fake quantization of K/V tensors did not provide a meaningful quality advantage over FP training evaluated with the same simulated low-precision KV cache.

## Why it stopped

Proxy/early falsification: the bounded three-seed CUDA experiment found no meaningful QAT robustness gain beyond ordinary KV bit-width memory savings.

## Recommended next action

Stop this run as a bounded proxy/early falsification of the tested mechanism; only reopen with a direct GPT-2-small-class natural-language and real decode-cache validation plan with a predeclared QAT advantage threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-memory-reduction-via-training-time-quantization-aware-key-value-heads-c0ad2047641d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
