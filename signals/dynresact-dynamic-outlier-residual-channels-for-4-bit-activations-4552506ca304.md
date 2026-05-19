# DynResAct: Dynamic Outlier Residual Channels for 4-bit Activations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynresact-dynamic-outlier-residual-channels-for-4-bit-activations-4552506ca304`
Run ID: `dynresact-dynamic-outlier-residual-channels-for-4-bit-activations-4552506ca304-20260517T154011581552+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a6cce9232f27

## What looked useful

DynResAct reduced real distilgpt2 activation relative MSE from 0.018110 to 0.000573 at about 1% residual entries, and reduced model-linear projection relative MSE from 0.007740 to 0.0000755. Static residual channels were much weaker under the same budget.

## Boundaries and scale limits

No end-to-end perplexity, task accuracy, fused-kernel latency, metadata bandwidth, long-context, or 7B+ model validation was run. The result is local reconstruction/projection evidence only.

## Claim scope

Dynamic per-token residual preservation of about 1-2% activation entries substantially reduced int4 activation reconstruction and downstream linear projection error on a synthetic heavy-tail proxy and a small distilgpt2 activation sample.

## Why it stopped

No-paper closure: this run provides reconstruction/projection evidence only, not full validation of model quality or serving efficiency.

## Recommended next action

Run a bounded GPT-2-small-class end-to-end perplexity and latency probe with explicit residual metadata accounting before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2-small DynResAct perplexity and latency probe
- Success threshold: At 1-2% residual entries, dynamic residual activation quantization should reduce next-token loss degradation by at least 50% versus int4 per-row while adding less than 15% measured inference latency overhead in the local prototype.
- Stop condition: Stop if dynamic residual selection fails to improve next-token loss over static residuals at the same budget, or if measured local overhead exceeds 30% before any kernel optimization.

## Evidence references

- Artifact root: `<local-path>/projects/dynresact-dynamic-outlier-residual-channels-for-4-bit-activations-4552506ca304`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
