# Real-token tiny LM INT8-QAT with post-conversion evaluation

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `real-token-tiny-lm-int8-qat-with-post-conversion-evaluatio-b86f910799`
Run ID: `real-token-tiny-lm-int8-qat-with-post-conversion-evaluatio-b86f910799-20260605T082214063473+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Parent run decision: INT8 Quantization-Aware Tiny Pretraining: enoch://control-plane/projects/int8-quantization-aware-tiny-pretraining-4aed84240327/runs/int8-quantization-aware-tiny-pretraining-4aed84240327-20260605T035514381529+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9386228f9296

## What looked useful

Across three real-token direct replicates, QAT met the predeclared post-conversion W8A8 penalty-reduction threshold in 1 of 3 seeds. The other two seeds failed and the PTQ/QAT conversion penalties were near zero with inconsistent sign, so the mechanism was not robust in this bounded setting.

## Boundaries and scale limits

Very small model and short training; converted INT8 is backend-independent quantize/dequantize simulation rather than hardware int8 kernels; longer 120-step and 500-step runs were externally terminated around 14 seconds in this deployment.

## Claim scope

Fast Tier-1 direct test of a 1-layer 64-dimensional causal transformer trained for 40 steps on WikiText-2 GPT-2 tokens, comparing float, PTQ-converted simulated W8A8, QAT-float, and QAT-converted simulated W8A8 evaluation on fixed validation windows.

## Why it stopped

Replicated fast direct Tier-1 evidence was mixed and the next meaningful medium confirmation exceeded the observed per-process runtime limit in this deployment.

## Recommended next action

Stop this run as no-paper useful signal; if revisited, run a medium direct confirmation on an environment without the observed 14-second process termination, using longer training, more validation tokens, multiple seeds, and backend-specific int8 converted inference.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-token QAT INT8 confirmation with backend int8 inference
- Success threshold: Mean QAT post-conversion NLL penalty is at least 25% lower than mean PTQ post-conversion NLL penalty across at least three seeds, all evaluated on the same fixed real-token validation windows, with QAT-float perplexity increase <=10%.
- Stop condition: Stop negative if PTQ penalty remains at the noise floor or QAT fails the 25% penalty-reduction threshold in two or more seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-token-tiny-lm-int8-qat-with-post-conversion-evaluatio-b86f910799`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
