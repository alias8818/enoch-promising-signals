# Residual-Channel Extreme Quantization for VRAM Reduction

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `residual-channel-extreme-quantization-for-vram-reduction-b6bfb64fd164`
Run ID: `residual-channel-extreme-quantization-for-vram-reduction-b6bfb64fd164-20260603T193532483380+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fd1189fd69cb

## What looked useful

Best residual variant, int2 plus int8 residuals for top 25% channels, reduced relative output MSE vs int2 by 56.5% but used 4.025 effective bits/weight and still had 1.98x the relative MSE of uniform int3, which used 3.017 effective bits/weight.

## Boundaries and scale limits

No end-to-end perplexity, generation, latency, custom kernel, KV-cache, or full VRAM-pressure measurement; activations were random calibration samples rather than corpus-derived hidden states; only four GPT-2 small matrices were tested.

## Claim scope

Layer-level proxy on four pretrained GPT-2 small first-block attention/MLP matrices: int2 base quantization plus int8 residuals on selected high-error output channels improves over uniform int2 but is not storage-error competitive with uniform int3 under explicit metadata accounting.

## Why it stopped

Bounded pretrained-weight proxy falsified the practical efficiency threshold for the int2 plus selected int8 residual-channel design; this is an early proxy falsification, not a full end-to-end validation.

## Recommended next action

Stop this exact design as no-paper evidence; only revisit if a new residual representation can beat uniform int3 at <=3 effective bits/weight on layer-output error before end-to-end tests.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-extreme-quantization-for-vram-reduction-b6bfb64fd164`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
