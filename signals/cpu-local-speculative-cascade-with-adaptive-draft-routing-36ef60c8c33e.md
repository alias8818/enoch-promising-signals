# CPU-Local Speculative Cascade with Adaptive Draft Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-local-speculative-cascade-with-adaptive-draft-routing-36ef60c8c33e`
Run ID: `cpu-local-speculative-cascade-with-adaptive-draft-routing-36ef60c8c33e-20260521T202534476722+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f42e89d1099e

## What looked useful

Adaptive routing reached 3.189x target-only throughput and 98.3% of oracle in the primary 7-seed run, beating the best static route at 2.367x. Empirical TV was similar to target-only sampling noise, consistent with exact speculative correction. The cascade route was dominated by adaptive routing without the cascade across sensitivity checks.

## Boundaries and scale limits

No real transformer models, tokenizers, KV-cache behavior, batching, quantization, prompt features, or measured wall-clock model latency were tested. Costs are simulated units and context buckets are synthetic.

## Claim scope

In a bounded synthetic CPU cost simulator with exact categorical speculative sampling, heterogeneous context buckets, and known draft proposal distributions, adaptive draft routing improves cost-normalized throughput over fixed draft choices and recovers near-oracle routing performance. The added cheap-to-specialist cascade route is not beneficial under the tested cost model.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct real-model evidence; the cascade component was not supported, so paper-positive closure is not warranted.

## Recommended next action

Run a bounded deepen experiment with real small CPU-local language models, measured wall-clock latency, and prompt-derived routing features; stop if adaptive routing fails to beat the best static draft by at least 15% at matched output distribution checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Wall-Clock Test for Adaptive Speculative Draft Routing
- Success threshold: Adaptive routing must beat the best fixed draft by at least 15% wall-clock tokens/sec on CPU, reach at least 90% of retrospective oracle throughput, and show no output-distribution deviation beyond target-only sampling noise.
- Stop condition: Stop if real CPU timing shows adaptive routing is within 5% of the best fixed draft or if cascade overhead removes the simulated throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-local-speculative-cascade-with-adaptive-draft-routing-36ef60c8c33e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
