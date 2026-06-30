# Residual-Channel KV Cache Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-kv-cache-quantization-bce135a14229`
Run ID: `residual-channel-kv-cache-quantization-bce135a14229-20260525T154931808765+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/491c38c1b632

## What looked useful

Calibrated 12.5% residual-channel int4 reduced uniform int4 delta NLL from 0.015811 to 0.008717 (44.9% penalty reduction) and beat a same-fraction random residual control at 0.013586 delta NLL.

## Boundaries and scale limits

Evidence is limited to one 82M-parameter GPT-2-family model, 8 calibration sequences, 1,024 evaluated continuation tokens, short 96-token prefixes, fake quant-dequant tensors, and memory estimates rather than packed KV storage or fused attention kernels.

## Claim scope

On distilgpt2 with WikiText-2 teacher-forced continuations, preserving calibrated high-activation KV channels in bf16 while fake-quantizing the remaining channels to int4 reduces next-token NLL degradation versus uniform int4 and versus random residual-channel selection at the same residual fraction.

## Why it stopped

Closed as no-paper useful signal: local small-model evidence supports the mechanism, but the run is too small and uses fake quantization rather than production packed-cache evidence.

## Recommended next action

Run a bounded deepen evaluation on GPT-2-small or Pythia-class models over at least 50k continuation tokens with memory-matched baselines and, if feasible, packed KV-cache storage or a kernel-level bandwidth simulator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-matched residual-channel KV quantization on GPT-2-small-class models
- Success threshold: Residual-channel selection reduces delta NLL by at least 25% versus the strongest memory-matched baseline on two model/dataset settings without worse measured or simulated serving cost.
- Stop condition: Stop if calibrated residual channels fail to beat memory-matched random/uniform baselines by at least 10% delta-NLL reduction on the first larger model after 50k evaluated tokens.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-kv-cache-quantization-bce135a14229`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
