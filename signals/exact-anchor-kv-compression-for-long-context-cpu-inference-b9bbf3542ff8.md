# Exact-Anchor KV Compression for Long-Context CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-long-context-cpu-inference-b9bbf3542ff8`
Run ID: `exact-anchor-kv-compression-for-long-context-cpu-inference-b9bbf3542ff8-20260525T191231065939+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/909231ce1912

## What looked useful

Grouped compression can be exact when K/V entries in a group are identical and softmax logits include multiplicity; sparse anchor-only compression is not exact for ordinary K/V because retained anchors carry too little full attention mass. In the medium proxy, anchor-only retained 16.4% of attention mass, gave 3.81x speedup, and had mean relative L2 error 2.53.

## Boundaries and scale limits

No full transformer model, real trained-model KV trace, quantized cache, task accuracy, or optimized inference runtime was tested. Sequence lengths were 128-8192 with 8 heads and dim 64 in NumPy on a CPU worker.

## Claim scope

Single-token CPU attention proxy with synthetic random K/V and an exact grouped-identical positive control. Sparse exact-anchor caching every 4-32 tokens plus a 128-token recent window reduces attention work but does not preserve full attention outputs on unconstrained K/V.

## Why it stopped

Proxy early falsification rather than full validation: sparse exact anchors alone fail to approximate exact attention on synthetic unconstrained K/V, while exactness only appears in the redundant grouped-control case.

## Recommended next action

Stop this run as a proxy early negative; a bounded follow-up should test the same retained-attention-mass and logit-error metrics on real long-context traces from a small local transformer before considering larger inference-runtime work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Exact-Anchor KV Compression Error on a Small Local Transformer
- Success threshold: At least one compression setting retaining no more than 25% of tokens must keep mean next-token logit KL below 0.01 or top-1 agreement above 99% across at least 100 decode positions while showing a measured CPU attention speedup.
- Stop condition: Stop if all tested settings with at most 25% retained tokens have mean logit KL above 0.05, top-1 agreement below 95%, or no measured CPU latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-long-context-cpu-inference-b9bbf3542ff8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
