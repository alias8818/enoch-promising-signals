# Sliding Window Residuals for 4-bit Context Extension

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-residuals-for-4-bit-context-extension-fe562eafce48`
Run ID: `sliding-window-residuals-for-4-bit-context-extension-fe562eafce48-20260525T102431729502+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7766e9134d7c

## What looked useful

Across 96 Wikitext-2 examples at context 256 and 512, last-window-only KV caused catastrophic drift (mean KL 8.71 and 10.55 nats). Both 4-bit old-KV methods stayed close to full KV (mean KL about 0.009-0.012 nats). Residual4 reduced old-KV RMSE versus direct4 and improved target-token NLL, but direct4 had lower mean KL at both main context lengths and residual4 had worse p95 KL at context 512.

## Boundaries and scale limits

No training, no GPT-2-small-class parameter-matched architectural baseline, no long-context task benchmark, no >1024 token context, no larger modern model, and no optimized serving kernel or wall-clock throughput measurement. Metrics are next-token distribution drift only.

## Claim scope

Bounded inference-time proxy on GPT-2/Wikitext-2: keeping a 64-token full-precision recent KV window and compressing older KV entries to 4-bit values preserves next-token distributions far better than discarding old KV, but residual 4-bit old-KV storage is not consistently better than direct 4-bit old-KV quantization.

## Why it stopped

Proxy evidence supports 4-bit old-KV preservation over sliding-window-only caching, but the residual-specific hypothesis is mixed and not publication-grade.

## Recommended next action

Stop this run as no-paper useful-signal evidence; if continuing, run a bounded deepen test comparing direct4 and residual4 on a longer-context-capable model and task-level long-context benchmark with equal effective memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Task-level direct4 versus residual4 KV compression at equal memory
- Success threshold: Residual4 must beat direct4 by at least 5% relative target loss or task error at matched effective memory while not increasing p95 KL or runtime by more than 10%.
- Stop condition: Stop if direct4 matches or beats residual4 on task accuracy/loss at matched memory for two window/block settings, or if residual metadata/dequantization cost removes the memory/runtime advantage.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-residuals-for-4-bit-context-extension-fe562eafce48`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
