# Self-Speculative Decoding via Layer-Early-Exit Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-layer-early-exit-drafting-adecf224dc1a`
Run ID: `self-speculative-decoding-via-layer-early-exit-drafting-adecf224dc1a-20260516T121501553194+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d3ba195640b7

## What looked useful

Early-layer top-1 agreement was only 12-24% through layer 6 and 46% at layer 8; layer 10 reached 63% but was too late for the proxy to show a speedup. Best idealized parallel-verifier proxy was 0.960x at layer 1 with draft length 2. Final-token top-5 inclusion rose to 84% at layer 10, suggesting trained exits may be worth testing.

## Boundaries and scale limits

Tested one GPT-2-small-class pretrained model, 24 fixed prompts, 64 greedy tokens per prompt, 1,536 next-token positions. Speedup is an iid acceptance latency proxy, not an optimized wall-clock serving benchmark. Trained early-exit heads and larger models were not tested.

## Claim scope

On GPT-2 with no additional training, intermediate hidden states projected through the final tied LM head do not provide enough greedy top-1 agreement for layer-early-exit self drafting to beat an idealized parallel-verifier latency proxy.

## Why it stopped

Bounded proxy run failed the success threshold: no tested early layer and draft length produced an idealized parallel-verifier latency speedup estimate above 1.0, so this is not a full validation of the broader trained self-speculative family.

## Recommended next action

Stop this no-training tied-head variant as an early proxy falsification; the concrete next bounded test is to train lightweight early-exit heads or auxiliary losses at GPT-2-small scale and rerun exact-match acceptance plus wall-clock self-speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train GPT-2-small early-exit heads for exact self-speculative acceptance
- Success threshold: At least one exit at layer 6 or earlier achieves 70% or higher top-1 agreement and a verified wall-clock speedup of at least 1.2x versus greedy decoding with exact output preservation.
- Stop condition: Stop if trained exits remain below 50% top-1 agreement at layer 6 or earlier, or if verified wall-clock speedup is below 1.0x despite exact-match acceptance improvements.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-layer-early-exit-drafting-adecf224dc1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
