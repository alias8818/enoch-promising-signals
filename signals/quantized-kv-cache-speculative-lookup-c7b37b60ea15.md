# Quantized KV-cache speculative lookup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-cache-speculative-lookup-c7b37b60ea15`
Run ID: `quantized-kv-cache-speculative-lookup-c7b37b60ea15-20260528T221020029599+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3af9a9903689

## What looked useful

Quantized key lookup is viable as a prefilter mechanism, but dropping the non-candidate tail failed the predefined local thresholds: at candidate_mult <= 4, neither normalized nor Gaussian-logit probes had any row with attention mass >= 0.90 or output relative L2 error <= 0.10.

## Boundaries and scale limits

Tested only NumPy synthetic normalized and Gaussian-logit key/query/value distributions up to 4096 keys, 128 queries, dimensions 64 and 128. No real LLM KV traces and no optimized int4/int8 kernel throughput measurements were run.

## Claim scope

Synthetic CPU probes show that 4-bit and 8-bit quantized key dot products can recover full-precision top-k positions inside small candidate sets, but naive speculative attention over only those candidates does not preserve enough attention mass or output accuracy.

## Why it stopped

Proxy early falsification of the naive speculative attention shortcut: quantized shortlist recall was strong, but candidate-only exact attention did not preserve attention mass or output accuracy.

## Recommended next action

Stop this run as a proxy no-paper result; the next bounded test is to repeat the same mass/error criteria on real small-transformer KV traces with an entropy or sparsity gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV-trace quantized lookup with attention sparsity gating
- Success threshold: At candidate_mult <= 4, gated real-trace cases must achieve candidate top-k recall >= 0.95, attention mass >= 0.90, and output relative L2 error <= 0.10 in at least 80% of gated layer/head/query samples, with the gate covering at least 20% of samples.
- Stop condition: Stop if the no-quantization top-candidate control also fails the mass/error thresholds or if the entropy gate covers less than 20% of samples.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-cache-speculative-lookup-c7b37b60ea15`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
