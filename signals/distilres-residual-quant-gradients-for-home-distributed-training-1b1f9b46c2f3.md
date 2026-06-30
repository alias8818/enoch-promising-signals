# DistilRes: Residual-Quant Gradients for Home Distributed Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `distilres-residual-quant-gradients-for-home-distributed-training-1b1f9b46c2f3`
Run ID: `distilres-residual-quant-gradients-for-home-distributed-training-1b1f9b46c2f3-20260604T044842874650+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/84a2084c144e

## What looked useful

Across three bounded runs, plain int2 averaged 0.5264 test accuracy, 9.19 percentage points below full precision. Residual int2 averaged 0.6236 test accuracy, 0.53 percentage points above full precision, at the same 15.98x nominal payload reduction. Int4 residual matched full precision at about 8.00x reduction; int8 variants matched full precision at about 4.00x reduction.

## Boundaries and scale limits

No real distributed networking, home uplinks, heterogeneous workers, stragglers, GPT-2-small-class model, real corpus, or multi-node all-reduce was tested. Python single-process compression overhead was measured, but communication-bound wall-clock speedup was only modeled by transmitted bytes.

## Claim scope

In a deterministic GPU-resident simulator of four-worker data-parallel MLP training on synthetic teacher-labeled classification data, residual error feedback makes aggressive 2-bit gradient quantization converge like full precision while preserving about 16x nominal gradient-payload reduction; int4 and int8 quantization are already near full precision in this setup.

## Why it stopped

Evidence is direct for the residual quantized-gradient mechanism in a simulator, but proxy-only for home distributed training and insufficient for a paper or broad validation.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with a bounded localhost or small-LAN torch.distributed GPT-style language modeling test that measures validation loss, actual/estimated communication time, and payload bytes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Quantized Gradients in Local torch.distributed Language Modeling
- Success threshold: Residual int2 or int4 keeps validation loss within 2% of full precision, achieves at least 8x gradient-payload reduction, and has lower estimated communication-bound step time after compression overhead.
- Stop condition: Stop if residual variants diverge, exceed full-precision validation loss by more than 5% in two seeds, or fail to improve estimated communication-bound step time at bandwidths representative of home uplinks.

## Evidence references

- Artifact root: `<local-path>/projects/distilres-residual-quant-gradients-for-home-distributed-training-1b1f9b46c2f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
