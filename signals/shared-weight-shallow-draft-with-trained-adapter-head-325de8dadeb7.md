# Shared-Weight Shallow Draft with Trained Adapter Head

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `shared-weight-shallow-draft-with-trained-adapter-head-325de8dadeb7`
Run ID: `shared-weight-shallow-draft-with-trained-adapter-head-325de8dadeb7-20260528T160433154839+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8228255b12eb

## What looked useful

The adapter mechanism works as an agreement improver: trained top-1 rose from tied-head controls of 17.5%, 22.5%, and 34.2% to 28.8%, 35.8%, and 54.1% at GPT-2 layers 3, 6, and 9. However, estimated greedy accept-run lengths remained 0.46, 0.61, and 1.22 tokens, so this does not yet support a practical speedup claim.

## Boundaries and scale limits

No true autoregressive speculative decoding latency benchmark was run; acceptance was teacher-forced and greedy-only. No sampling acceptance, KV-cache implementation, external draft baseline, multi-corpus robustness, longer training, or 7B+ validation was tested.

## Claim scope

On frozen GPT-2 small with WikiText-2, a 788k-parameter residual adapter trained from intermediate hidden states and sharing the final LM head improves held-out agreement with the target model's final argmax decisions at layers 3, 6, and 9.

## Why it stopped

No-paper useful signal: the proxy agreement test supports the adapter mechanism but does not provide direct end-to-end speedup evidence.

## Recommended next action

Run a bounded true autoregressive latency benchmark for the layer-9 adapter against greedy GPT-2 and a small external draft baseline; stop if tokens/sec does not improve by at least 10% after including draft and verification overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autoregressive latency check for shared-weight layer-9 adapter draft
- Success threshold: At least 10% wall-clock tokens/sec improvement over greedy GPT-2 with no worse generated greedy sequence under exact verification, plus acceptance metrics explaining the gain.
- Stop condition: Stop if verified tokens/sec is not above greedy baseline after accounting for adapter draft cost and verification passes, or if acceptance stays below 1.5 tokens per cycle.

## Evidence references

- Artifact root: `<local-path>/projects/shared-weight-shallow-draft-with-trained-adapter-head-325de8dadeb7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
