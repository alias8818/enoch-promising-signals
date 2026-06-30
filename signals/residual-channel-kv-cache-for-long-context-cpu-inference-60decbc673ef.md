# Residual Channel KV Cache for Long-Context CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-kv-cache-for-long-context-cpu-inference-60decbc673ef`
Run ID: `residual-channel-kv-cache-for-long-context-cpu-inference-60decbc673ef-20260526T001711086683+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2f775d23480f

## What looked useful

Channel-pruned KV cache mechanically reduces cache bytes and can speed CPU decode when many channels are removed, but the simple fixed residual-channel proxy causes large attention/output distortion. Isotropic synthetic K/V had median output relative L2 0.837-0.965 for 12.5%-50% kept channels, with 0/3 top-1 matches at every fraction. Even favorable anisotropic K/V needed 75% kept channels to reach median output relative L2 0.217, leaving only 25% memory reduction and about 1.02x median speedup.

## Boundaries and scale limits

No pretrained LLM, no end-to-end generation, no perplexity, no learned correction, no quantized production kernel, and no multi-layer accumulated error were tested. Results are useful for screening the mechanism, not for validating a deployable cache.

## Claim scope

Local NumPy CPU proxy for single-token long-context decode attention with synthetic K/V tensors at dim 128 and sequence lengths 4096, 16384, and 65536. The tested mechanism keeps a fixed high-variance subset of K/V channels and reconstructs dropped V output channels as zero.

## Why it stopped

Proxy evidence is mixed and not paper-ready: the CPU speed/memory mechanism works, but fidelity fails at compression ratios large enough to matter except in a favorable synthetic anisotropy case.

## Recommended next action

Stop this worker run as a no-paper useful signal; the concrete next action is a bounded pretrained small-transformer KV trace replay to test whether real layer K/V distributions are anisotropic enough for channel retention at useful compression ratios.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained small-transformer KV trace replay for residual-channel cache fidelity
- Success threshold: At 50% or lower retained channels, median output relative L2 <= 0.20, attention L1 <= 0.15, top-1 attention match >= 80%, and language-model loss increase <= 5% on the tested corpus.
- Stop condition: Stop as unsupported if 50% retained channels exceeds output relative L2 0.35 or loss increase 10% in most layers/prompts, or if only 75% retention is viable.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-kv-cache-for-long-context-cpu-inference-60decbc673ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
