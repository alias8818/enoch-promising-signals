# Real small-transformer KV trace validation for outlier-routed int4 cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-small-transformer-kv-trace-validation-for-outlier-rou-e729bb0d7a`
Run ID: `real-small-transformer-kv-trace-validation-for-outlier-rou-e729bb0d7a-20260629T104626615757+0000`

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

- Parent run decision: Outlier-routed residual KV cache for long context on CPU: enoch://control-plane/projects/outlier-routed-residual-kv-cache-for-long-context-on-cpu-4ff16a5c2315/runs/outlier-routed-residual-kv-cache-for-long-context-on-cpu-4ff16a5c2315-20260629T082421956541+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/2449eeb394cd

## What looked useful

Outlier routing is a real mechanism when int4 scaling is coarse: tensorwise MSE fell 64.6% at 1.082x estimated cache memory. For groupwise-64 scaling, the best measured reduction was 23.4% at 1.077x memory, below the predeclared 50% threshold.

## Boundaries and scale limits

CPU-only run; untrained four-layer/four-head transformer; sequence lengths 128 and 256; no pretrained GPT trace, downstream perplexity, real decode kernel, bandwidth, or latency measurement.

## Claim scope

On deterministic NumPy small-transformer KV traces, routing the largest 1% K/V entries out of an int4 cache substantially reduced tensorwise-scale attention replay MSE, but only modestly improved a groupwise-64 int4 baseline.

## Why it stopped

Bounded direct trace produced a mixed useful signal, but the realistic groupwise baseline did not meet the predeclared success threshold; this is not a full validation.

## Recommended next action

Run the same replay on pretrained GPT-2-small-class traces with groupwise int4 and downstream next-token loss before considering this a validation result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small KV replay for groupwise outlier-routed int4 cache
- Success threshold: At least 50% mean attention replay MSE reduction versus plain groupwise int4 at <=1.2x estimated cache memory, plus lower next-token loss degradation than plain groupwise int4 on the same sample.
- Stop condition: Stop as negative if pretrained groupwise traces show less than 25% MSE reduction at <=1.2x memory or no downstream loss improvement versus plain groupwise int4.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-transformer-kv-trace-validation-for-outlier-rou-e729bb0d7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
