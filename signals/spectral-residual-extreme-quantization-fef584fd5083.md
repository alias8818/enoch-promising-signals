# Spectral Residual Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spectral-residual-extreme-quantization-fef584fd5083`
Run ID: `spectral-residual-extreme-quantization-fef584fd5083-20260531T152322887450+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/58a9b8942e46

## What looked useful

Spectral residuals capture structured 1-bit quantization error: rank-32 residuals reduced mean relative output MSE from 0.4341 to 0.2219 across the medium run, while random residuals stayed near 0.4335. The method still trailed simple 4-bit row quantization at 0.0422 mean relative output MSE, so the result is mechanism-positive but not paper-ready.

## Boundaries and scale limits

No end-to-end perplexity, task, generation, packed-kernel, latency, or bandwidth validation was run. Storage is estimated analytically and residual factors remain FP16. Real-model coverage is limited to GPT-2 tensors and random Gaussian activation probes.

## Claim scope

On two synthetic controls and eight GPT-2 2D weight tensors, a 1-bit row-scaled matrix plus an FP16 spectral low-rank residual improves relative weight and random-activation output MSE over plain 1-bit quantization and random rank-residual controls.

## Why it stopped

Current evidence is a bounded matrix/output reconstruction signal, not direct end-to-end model-quality validation, and the method remains far worse than a simple 4-bit quantization baseline on mean output error.

## Recommended next action

Run a bounded deepen follow-up that applies spectral residual factors to an actual small causal LM perplexity benchmark with storage-fair residual quantization; stop here for the current no-paper matrix reconstruction result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end perplexity test for storage-fair spectral residual 1-bit quantization
- Success threshold: At matched serialized size below 4 bits per weight, spectral residual 1-bit quantization reduces the perplexity gap from dense by at least 30% versus plain 1-bit and beats random residual controls by at least 20%, without more than 25% inference latency overhead versus the plain 1-bit implementation.
- Stop condition: Stop if storage-fair residual factors fail to beat random residual controls on perplexity, or if the method remains farther from dense perplexity than a simple 4-bit baseline by more than 2x the dense-to-4-bit gap.

## Evidence references

- Artifact root: `<local-path>/projects/spectral-residual-extreme-quantization-fef584fd5083`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
