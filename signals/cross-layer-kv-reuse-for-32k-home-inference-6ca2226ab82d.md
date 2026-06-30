# Cross-Layer KV Reuse for 32K Home Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cross-layer-kv-reuse-for-32k-home-inference-6ca2226ab82d`
Run ID: `cross-layer-kv-reuse-for-32k-home-inference-6ca2226ab82d-20260529T023413310947+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc97cb3bdc1b

## What looked useful

Pairwise cross-layer K/V reuse raised GPT-2 next-token NLL by 1.80-5.73 nats, reduced top-1 logit agreement to 15-26%, and produced adjacent attention-output relative L2 above 1.5 with near-zero cosine, while the validated manual baseline exactly matched Hugging Face logits.

## Boundaries and scale limits

Tested GPT-2 small only, fp16, batch 1, 128-1024 tokens. Did not test 32K contexts, long-context architectures, quantized caches, serving kernels, or models trained for K/V sharing.

## Claim scope

Naive inference-time adjacent-layer K/V reuse in an unmodified pretrained GPT-2 small decoder is not quality preserving for 128-1024 token contexts, despite offering a nominal 50% layer-wise KV-cache reduction.

## Why it stopped

Proxy early falsification: the local mechanism needed for reuse failed in a real pretrained GPT-2 model before any 32K/full-serving validation was justified.

## Recommended next action

Stop treating naive cross-layer K/V reuse as a free inference-time optimization; only revisit with a bounded training-aware experiment that explicitly aligns or shares K/V projections.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Training-aware adjacent-layer K/V sharing in a small decoder
- Success threshold: At least 40% KV-cache memory reduction with held-out NLL degradation <=0.10 nats/token and baseline-vs-variant top-1 agreement >=90% at 1024 tokens.
- Stop condition: Stop if after a bounded small-model run the sharing variant exceeds 0.25 nats/token NLL degradation or top-1 agreement remains below 80% at 1024 tokens.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-reuse-for-32k-home-inference-6ca2226ab82d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
