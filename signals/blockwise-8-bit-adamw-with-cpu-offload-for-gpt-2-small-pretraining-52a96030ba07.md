# Blockwise 8-bit AdamW with CPU-offload for GPT-2-small pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `blockwise-8-bit-adamw-with-cpu-offload-for-gpt-2-small-pretraining-52a96030ba07`
Run ID: `blockwise-8-bit-adamw-with-cpu-offload-for-gpt-2-small-pretraining-52a96030ba07-20260523T210213038253+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9716dd2a98f5

## What looked useful

Naive blockwise linear uint8 quantization of AdamW first and second moments gives about 4x optimizer-state memory reduction, but at block size 4096 the 8M-parameter probe had final update cosine 0.012 versus fp32 AdamW and final parameter relative RMS drift 2.61. Smaller blocks improved final update cosine to 0.735-0.963 on 1M parameters but made CPU updates 9.3x-34.1x slower and still left about 0.19-0.22 parameter relative RMS drift.

## Boundaries and scale limits

No PyTorch/GPU model training was available on this CPU worker. The run does not measure transformer forward/backward cost, GPU CPU-offload transfer overhead, real-token loss, perplexity, checkpoint/resume behavior, or full GPT-2-small convergence.

## Claim scope

Mechanism-level CPU NumPy probe of blockwise uint8 AdamW moment storage on dense synthetic GPT-style parameter vectors up to 8,388,608 parameters; includes analytical GPT-2-small optimizer-state memory estimates but no real language-model pretraining.

## Why it stopped

Proxy/mechanism-level early falsification: the tested blockwise uint8 CPU-offloaded AdamW state is memory-efficient but does not preserve fp32 AdamW update fidelity well enough to justify direct GPT-2-small pretraining validation.

## Recommended next action

Stop this naive quantizer as a paper path; run a bounded follow-up testing log/RMS or percentile-scaled second-moment quantization before attempting any GPT-2-small training integration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Second-moment-aware 8-bit AdamW quantization for CPU-offloaded GPT-style training
- Success threshold: At 8M parameters and at least 32 synthetic optimizer steps, final update cosine >= 0.99, final parameter relative RMS drift <= 0.05, optimizer-state reduction >= 3.5x, and CPU update overhead <= 2x fp32 AdamW; then show no obvious loss instability in a small transformer run.
- Stop condition: Stop if improved quantization cannot meet update cosine >= 0.98 and parameter relative RMS drift <= 0.10 on the 8M synthetic probe, because real GPT-2-small training is unlikely to recover from the optimizer-state distortion.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adamw-with-cpu-offload-for-gpt-2-small-pretraining-52a96030ba07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
