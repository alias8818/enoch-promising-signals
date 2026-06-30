# Frozen 1-Bit Base with Full-Precision LoRA Residuals

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `frozen-1-bit-base-with-full-precision-lora-residuals-a4d9c7a2007a`
Run ID: `frozen-1-bit-base-with-full-precision-lora-residuals-a4d9c7a2007a-20260527T031613318044+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ed176a8ddba3

## What looked useful

The quantization error was high-rank. Mean rank needed to capture 95% of quantization-error energy was 312 for Gaussian targets, 300 for Student-t targets, and 267 even for the low-rank-plus-noise positive control. At n=512, rank 256 already costs 103.3% of dense fp32 storage, while rank 192 still left relative output RMSE of 0.277, 0.328, and 0.206 respectively.

## Boundaries and scale limits

Evidence is analytic and synthetic/proxy only. It does not validate real transformer training, real pretrained weight spectra, token-level loss, or downstream task quality. An attempted GPT-2 safetensors spectral probe stalled during download and is not used as evidence.

## Claim scope

In 512x512 linear-layer proxies with per-row scaled 1-bit frozen bases, even the optimal full-precision rank-r LoRA residual does not cheaply repair quantization error for random dense, heavy-tailed dense, or low-rank-plus-noise targets.

## Why it stopped

No-paper useful negative signal: the optimistic SVD upper bound fails to make the frozen 1-bit base plus fp32 LoRA residual attractive under a dense-fp32 storage budget on direct linear proxies.

## Recommended next action

Stop this run as a proxy early falsification; only revisit if a bounded real-weight spectral probe of GPT-2-small or similar pretrained matrices shows quantization errors are much more low-rank than these proxies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Transformer Quantization Error Spectrum
- Success threshold: Median real-weight rank-128 optimal residual should leave relative output RMSE below 0.15 while using no more than 55% of dense fp32 storage, with no major layer family above 0.25 RMSE.
- Stop condition: Stop if rank-128 median RMSE is at or above 0.25, or if rank needed for 95% quantization-error capture is usually above the dense-fp32 storage break-even rank.

## Evidence references

- Artifact root: `<local-path>/projects/frozen-1-bit-base-with-full-precision-lora-residuals-a4d9c7a2007a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
