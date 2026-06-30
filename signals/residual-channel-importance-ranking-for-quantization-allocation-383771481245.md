# Residual Channel Importance Ranking for Quantization Allocation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-importance-ranking-for-quantization-allocation-383771481245`
Run ID: `residual-channel-importance-ranking-for-quantization-allocation-383771481245-20260613T212800259728+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fdc72ec0d6bc

## What looked useful

Top-ranked residual channels allocated 8-bit precision with the remaining channels at 2-bit had 0.5545 mean loss increase versus FP32, compared with 0.6924 for random and 0.8743 for reverse at the same 3.5 average bits/channel; the ordering held across seeds 0, 1, and 2. Uniform 3-bit and 4-bit controls were much stronger, so the ranking signal is real but the tested allocation policy is not practical.

## Boundaries and scale limits

Synthetic next-token task, tiny 3-layer transformer, post-training fake activation quantization only, no pretrained LLM, no real corpus, no weight quantization, no hardware quantized-kernel throughput measurement.

## Claim scope

In a three-seed synthetic tiny-transformer activation-quantization test, gradient-times-activation residual channel ranking selected high-precision channels better than random or reverse equal-average-bit allocations.

## Why it stopped

No-paper closure: the local toy mechanism is supported, but the evidence is synthetic and the tested mixed allocation is far worse than simple uniform controls.

## Recommended next action

Run one bounded deepen test on a pretrained small language model with a smoother same-budget tiered allocation and real text perplexity; stop if ranked allocation does not beat uniform same-budget quantization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Small-LM Residual Channel Quantization Allocation
- Success threshold: Ranked tiered allocation reduces validation perplexity degradation by at least 10% relative to uniform same-average-bit quantization and beats random/reverse matched-budget controls on all calibration subsets.
- Stop condition: Stop as negative if ranked allocation fails to beat uniform same-budget quantization or if ranking stability is not better than random across calibration subsets.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-importance-ranking-for-quantization-allocation-383771481245`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
