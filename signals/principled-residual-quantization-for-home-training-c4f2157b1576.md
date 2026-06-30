# Principled Residual Quantization for Home Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `principled-residual-quantization-for-home-training-c4f2157b1576`
Run ID: `principled-residual-quantization-for-home-training-c4f2157b1576-20260619T090242213738+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/38be93e803b3

## What looked useful

Residual quantization is useful as a convergence correction, but the straightforward dense residual buffer makes it a poor standalone memory-saving method for home training: residual 2/3/4-bit variants used 1.064x, 1.095x, and 1.126x the dense update-buffer bytes in the proxy accounting.

## Boundaries and scale limits

This run did not train a transformer or language model, did not measure real optimizer kernels or activation memory, and used theoretical update-state memory accounting rather than end-to-end home-training memory traces.

## Claim scope

In a 5-seed synthetic teacher-student MLP proxy, residual/error-feedback low-bit update quantization preserves dense-like convergence at 2-4 bits, while naive 2-bit and 3-bit update quantization degrades convergence.

## Why it stopped

Proxy evidence supports residual quantization for convergence but falsifies the simplest memory-saving interpretation; this is not full validation of home training.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should compress, offload, or sparsify the residual buffer and compare against dense and naive low-bit baselines on a small transformer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed Residual Buffers for Low-Bit Home Training
- Success threshold: At 2 or 3 bits, compressed residual training reaches validation loss within 1% of dense and uses less than 0.5x dense update/optimizer-state memory in measured or directly instrumented accounting.
- Stop condition: Stop if compressed residual variants either lose more than 3% validation performance versus dense or fail to reduce measured total update/optimizer-state memory below dense.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-quantization-for-home-training-c4f2157b1576`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
