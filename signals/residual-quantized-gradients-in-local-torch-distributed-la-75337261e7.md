# Residual Quantized Gradients in Local torch.distributed Language Modeling

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-quantized-gradients-in-local-torch-distributed-la-75337261e7`
Run ID: `residual-quantized-gradients-in-local-torch-distributed-la-75337261e7-20260604T063233725728+0000`

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

- Parent run decision: DistilRes: Residual-Quant Gradients for Home Distributed Training: enoch://control-plane/projects/distilres-residual-quant-gradients-for-home-distributed-training-1b1f9b46c2f3/runs/distilres-residual-quant-gradients-for-home-distributed-training-1b1f9b46c2f3-20260604T044842874650+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/84a2084c144e

## What looked useful

Residual int8 gradients with error feedback were directly runnable in local torch.distributed language-model training and met the predefined Tier 1 threshold: validation loss delta -0.000109 nats/token versus fp32, 3.996x lower estimated payload, and 0.910x fp32 throughput.

## Boundaries and scale limits

Single host, CPU/Gloo backend, synthetic Markov token data, 160 optimizer steps, small Transformer model, no real text corpus, no NCCL multi-GPU or multi-node bandwidth measurement.

## Claim scope

In a two-rank local CPU/Gloo torch.distributed synthetic language-modeling test with a 114,560-parameter Transformer, residual int8 gradient synchronization matched fp32 validation loss after 160 steps while reducing estimated gradient payload by about 4x.

## Why it stopped

Tier 1 direct local test supports the mechanism but is too small and synthetic for paper readiness.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded test should use a real text dataset with GPT-2-small-class or matched small baselines and include non-residual quantization ablation plus direct communication timing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Quantized Gradients on Real Text with Communication Timing
- Success threshold: Residual-int8 validation loss within 1% of fp32 at equal token budget, at least 3.5x lower payload or measured communication cost, and better or equal stability than non-residual int8 across at least 3 seeds.
- Stop condition: Stop if residual-int8 is more than 1% worse than fp32 validation loss in 2 of 3 seeds, fails with NaNs, or measured synchronization cost is not improved despite payload reduction.

## Evidence references

- Artifact root: `<local-path>/projects/residual-quantized-gradients-in-local-torch-distributed-la-75337261e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
