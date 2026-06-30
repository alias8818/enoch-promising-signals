# 4-bit AdamW + error feedback for GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-adamw-error-feedback-for-gpt-2-small-pretraining-70780c8174cd`
Run ID: `4-bit-adamw-error-feedback-for-gpt-2-small-pretraining-70780c8174cd-20260611T160100636780+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9ad90487fc08

## What looked useful

The failure mechanism is large early second-moment quantization loss: about 46-48% of v entries quantize to zero at step 1, producing maximum updates from about 462 to 1227 at lr 3e-4. Lowering lr to 1e-5 did not prevent NaNs. Full-precision EF residuals also increase optimizer-state memory above fp32 AdamW moments.

## Boundaries and scale limits

Synthetic token data only; short traces only; GPT-2-small geometry used with reduced 8192 vocabulary; quantization payload was simulated rather than packed into production kernels; no real-corpus medium or long pretraining run was performed.

## Claim scope

Linear per-block 4-bit quantization of AdamW first and second moments, with or without persistent full-precision error-feedback residuals, is not viable as tested for GPT-style causal-LM pretraining dynamics: it diverges within a few steps and the full-residual EF version is not optimizer-state-memory-saving.

## Why it stopped

Proxy/early falsification, not full validation: short synthetic and GPT-2-small-architecture traces show immediate divergence of the tested linear 4-bit AdamW+EF design and no optimizer-memory saving for full-residual EF.

## Recommended next action

Stop this implementation path; a bounded follow-up should test nonzero-floor or log-domain 4-bit second-moment quantization with compact residual storage before any long GPT-2-small pretraining attempt.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Nonzero-floor 4-bit second-moment quantization for AdamW
- Success threshold: On a GPT-2-small-architecture synthetic or small real-token run of at least 500 steps, final and mean-last-50 loss are within 2% of AdamW, no NaNs occur, max update magnitude remains within 10x AdamW during warmup, and optimizer-state memory is at least 2x smaller than fp32 AdamW moments after all residual/metadata costs.
- Stop condition: Stop if second-moment zeroing or flooring still produces NaNs/divergence in the first 50 steps, or if residual/metadata accounting removes the 2x optimizer-state memory saving.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-adamw-error-feedback-for-gpt-2-small-pretraining-70780c8174cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
