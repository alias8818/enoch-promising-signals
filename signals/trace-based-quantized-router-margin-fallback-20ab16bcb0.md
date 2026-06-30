# Trace-Based Quantized Router Margin Fallback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-based-quantized-router-margin-fallback-20ab16bcb0`
Run ID: `trace-based-quantized-router-margin-fallback-20ab16bcb0-20260529T013545580354+0000`

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

- Parent run decision: Quantization-Aware Agent Tool Routing: enoch://control-plane/projects/quantization-aware-agent-tool-routing-57d352e42685/runs/quantization-aware-agent-tool-routing-57d352e42685-20260528T230131015982+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4b7f37f21ef6

## What looked useful

Across six seeds, 6-bit quantized routers passed the >=90% recovery and <=30% fallback threshold in 5/6 seeds with mean 92.3% flip recovery at 2.2% fallback. 4-bit passed in 4/6 seeds with mean 90.1% recovery at 8.5% fallback. 3-bit consistently improved routing but missed the threshold with mean 89.0% recovery at 17.8% fallback. 8-bit had very few flips and unstable recovery, with 0/6 threshold passes. Margin fallback strongly beat random fallback at the same fallback rate.

## Boundaries and scale limits

Synthetic clustered token traces only; no real MoE router, no end-to-end task quality, no serving latency measurement, no activation quantization, and no distribution-shift persistence test. Six seeds were run with 60k train, 20k calibration, and 30k held-out test tokens each.

## Claim scope

In a controlled synthetic router-trace test with a trained linear 16-expert router, trace-calibrated quantized top-1/top-2 margin fallback recovered most quantization-induced routing flips at moderate weight quantization levels while falling back on a minority of tokens.

## Why it stopped

Tier 1 direct controlled test completed; evidence is a useful mechanism signal but remains synthetic and mixed, so it is not paper-ready.

## Recommended next action

Run the same calibrated-margin fallback on real trained MoE router traces with measured fallback latency and distribution-shift persistence before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real MoE Router Trace Margin Fallback Validation
- Success threshold: At 4-bit or 6-bit router weight quantization, recover >=90% of quantization-induced top-1 routing flips on held-out real router traces with <=10% fallback rate and at least 5x the matched random-fallback recovery.
- Stop condition: Stop if real-router held-out recovery is <80% at <=10% fallback for both 4-bit and 6-bit, or if fallback overhead removes any practical serving benefit.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-quantized-router-margin-fallback-20ab16bcb0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
