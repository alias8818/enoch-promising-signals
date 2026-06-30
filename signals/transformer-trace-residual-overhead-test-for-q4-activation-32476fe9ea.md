# Transformer-trace residual overhead test for q4 activations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `transformer-trace-residual-overhead-test-for-q4-activation-32476fe9ea`
Run ID: `transformer-trace-residual-overhead-test-for-q4-activation-32476fe9ea-20260528T145015534305+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Principled Residuals for 4-Bit Activations: enoch://control-plane/projects/principled-residuals-for-4-bit-activations-6f6c21c2d840/runs/principled-residuals-for-4-bit-activations-6f6c21c2d840-20260528T011103144472+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/125b33f851bb

## What looked useful

The Tier 1 direct test supports the mechanism that q4 residual tracing can remain below 10% overhead when trace payloads are bounded summaries and the q4 activation path is otherwise unchanged. This is useful no-paper evidence, not publication readiness.

## Boundaries and scale limits

CPU-only small model: batch 4, sequence 64, d_model 192, 6 heads, 4 layers. q4 activations were emulated with per-token symmetric int4 codes stored in int8 containers. The run did not test packed nibbles, fused kernels, GPU inference, production logging sinks, long contexts, training, or 7B+ models.

## Claim scope

In a controlled small NumPy transformer-style forward with q4 quantize/dequantize at residual activation boundaries, bounded in-memory residual trace summaries added 4.34% median overhead versus the identical q4 path without tracing; the pinned-run 95% bootstrap interval was 0.93% to 7.91%, below the predeclared 10% threshold.

## Why it stopped

Controlled small direct test completed and supported the mechanism, but evidence is not broad enough for a paper because the q4 path is emulated and the trace sink is an in-memory bounded summary.

## Recommended next action

Run a bounded deepen test with packed q4 activation storage or a fused inference path to check whether trace extraction forces extra unpacking or memory traffic above the 10% overhead threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed q4 activation trace overhead in a fused or bit-packed path
- Success threshold: Median q4 trace overhead <= 10% and the upper bound of a 95% bootstrap interval <= 10% on the packed/fused q4 path.
- Stop condition: Stop as negative if packed/fused q4 trace overhead exceeds 10% median or the confidence interval remains above/straddles 10% after controlled pinned repeats.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-trace-residual-overhead-test-for-q4-activation-32476fe9ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
