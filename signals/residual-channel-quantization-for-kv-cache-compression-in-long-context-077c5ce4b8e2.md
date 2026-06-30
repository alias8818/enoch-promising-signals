# Residual Channel Quantization for KV-Cache Compression in Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-quantization-for-kv-cache-compression-in-long-context-077c5ce4b8e2`
Run ID: `residual-channel-quantization-for-kv-cache-compression-in-long-context-077c5ce4b8e2-20260528T021603355753+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93bf42d03423

## What looked useful

Residual-channel 3-bit variants were worse than plain int4 despite similar or higher memory, while residual-channel 4-bit variants reduced mean attention-output relative MSE from 0.04898-0.05587 for int4 baselines to 0.03857 at 4.76 bits/value and 0.02766 at 5.51 bits/value. This supports residual channels as an above-int4 quality knob, not as an equal-budget compression win with the tested salience policy.

## Boundaries and scale limits

No end-to-end perplexity, retrieval, latency, packed-cache kernel, or true long-context transformer validation was run. GPT-2-small evidence is limited to 1024-token activations; 2048-8192 context evidence is synthetic only.

## Claim scope

Bounded probe on GPT-2-small layers 0, 5, and 11 at 1024 tokens plus synthetic KV-like tensors at 1024-8192 tokens: naive energy-selected residual-channel quantization does not beat plain int4 KV quantization at a comparable memory frontier, but retaining fp16 residual channels improves attention-output error when allowed a larger bits/value budget.

## Why it stopped

Proxy/early falsification of the equal-budget naive residual-channel hypothesis: direct attention-output metrics did not Pareto-dominate int4, and full validation would require end-to-end long-context model quality and packed-cache performance evidence.

## Recommended next action

Run a bounded deepen test with sensitivity-selected or learned residual channels and matched bits/value against per-token int4 on a real long-context model metric; stop treating the current naive energy-selected method as paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sensitivity-selected residual channels for matched-budget KV-cache quantization
- Success threshold: At matched bits/value within 5%, sensitivity-selected residual-channel quantization must reduce attention-output relative MSE by at least 25% versus the best int4 baseline and show no degradation on the chosen end-to-end model metric beyond the int4 baseline.
- Stop condition: Stop if sensitivity-selected masks fail to beat the best int4 baseline by 10% relative attention-output MSE at matched bits/value on two representative layers or if end-to-end quality is worse than int4.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-quantization-for-kv-cache-compression-in-long-context-077c5ce4b8e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
