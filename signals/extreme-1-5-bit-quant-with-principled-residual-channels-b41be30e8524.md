# Extreme 1.5-bit Quant with Principled Residual Channels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `extreme-1-5-bit-quant-with-principled-residual-channels-b41be30e8524`
Run ID: `extreme-1-5-bit-quant-with-principled-residual-channels-b41be30e8524-20260523T191343043839+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/00855c71463b

## What looked useful

Across three runs and 144 budget/layer/case comparisons, the proposed error-activation residual-channel selector beat random selection every time. On GPT-2 projection layers the median relative output-MSE reduction versus random was 53.4%, with median reductions increasing from 39.2% at 0.5% residual channels to 64.7% at 5%. Balanced Gaussian controls showed near-zero gains, indicating the mechanism depends on real channel structure/outliers.

## Boundaries and scale limits

No full-model quantization, perplexity, downstream task, packed-kernel, or mature PTQ baseline validation was run. GPT-2 evidence covered 8 projection layers and a small prompt corpus only.

## Claim scope

Layer-local reconstruction evidence shows that preserving 0.5%-5% of input channels in full precision, selected by quantization-error times activation-energy, substantially reduces output MSE for an extreme ternary weight proxy on synthetic outlier cases and captured GPT-2-small projection layers.

## Why it stopped

Stopped after a short, reproducible mechanism probe because the evidence is useful but remains layer-local/proxy evidence rather than full validation or paper-ready support.

## Recommended next action

Run a bounded end-to-end GPT-2-small perplexity probe that applies the residual-channel policy across all projection layers and compares against random residual channels plus a strong PTQ baseline under matched effective bit budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2-small perplexity test for residual-channel ternary quantization
- Success threshold: At 1%-2% residual channels, error-activation selection should reduce perplexity degradation by at least 20% versus random residual selection and beat no-residual ternary quantization without exceeding the matched effective bit budget.
- Stop condition: Stop if the principled selector fails to improve perplexity degradation by at least 10% versus random residual channels on the bounded GPT-2-small evaluation, even if layer-local MSE remains better.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-1-5-bit-quant-with-principled-residual-channels-b41be30e8524`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
