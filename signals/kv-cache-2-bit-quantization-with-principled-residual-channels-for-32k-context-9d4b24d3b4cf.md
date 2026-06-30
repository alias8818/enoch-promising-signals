# KV cache 2-bit quantization with principled residual channels for 32k+ context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-2-bit-quantization-with-principled-residual-channels-for-32k-context-9d4b24d3b4cf`
Run ID: `kv-cache-2-bit-quantization-with-principled-residual-channels-for-32k-context-9d4b24d3b4cf-20260621T081422131909+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/114ecde8251c

## What looked useful

Across 20 injected-outlier synthetic cases, calibration-scored residual channels reduced relative L2 attention-output error by 72.89% on average versus plain 2-bit KV while preserving about 81.18% analytical KV memory reduction versus fp16. However, it tied magnitude selection in all injected-outlier cases. In 20 no-outlier controls, residuals improved only 3.89% on average and the calibration rule was slightly worse than magnitude on average.

## Boundaries and scale limits

No pretrained LLM perplexity, retrieval, generation, real KV activation trace, packed 2-bit kernel, or serving latency measurement. Synthetic tensors only; 32k length is direct for attention shape but not direct for deployed model quality.

## Claim scope

Synthetic Q/K/V attention-output probe up to 32k context with 2-bit per-channel K/V quantization and 6.25% residual channels. Residual channels reduce error when salient channel outliers exist, but the tested calibration-scored selector does not outperform a simpler magnitude selector.

## Why it stopped

Bounded synthetic evidence supports residual channels as an error-reduction mechanism but does not support the principled-selector novelty over magnitude controls; this is proxy evidence, not full 32k LLM validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same residual selectors on real GPT-2-small-class KV tensors with perplexity or next-token loss and require calibration-scored residuals to beat magnitude and random controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV residual selector control on GPT-2-small-class traces
- Success threshold: Calibration-scored residuals must beat magnitude residuals by at least 5% relative reduction in output error or recover at least 0.02 nats/token more loss than magnitude at the same memory budget, without reducing analytical memory savings below 75% versus fp16.
- Stop condition: Stop if calibration-scored residuals fail to beat magnitude controls on two independent text shards or if plain 2-bit KV degradation is too small to measure reliably in the chosen local model.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-2-bit-quantization-with-principled-residual-channels-for-32k-context-9d4b24d3b4cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
