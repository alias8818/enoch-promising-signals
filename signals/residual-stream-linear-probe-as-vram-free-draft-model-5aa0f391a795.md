# Residual-Stream Linear Probe as VRAM-Free Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-stream-linear-probe-as-vram-free-draft-model-5aa0f391a795`
Run ID: `residual-stream-linear-probe-as-vram-free-draft-model-5aa0f391a795-20260523T162704648703+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7d1a8c055254

## What looked useful

A trained affine tuned-lens probe at layer 5 improved final top-1 agreement to 53.30% versus 40.80% for frozen logit lens and 100% for the final-layer sanity control. The method is structurally capped at one drafted token because it has no residual-state transition for future drafted tokens.

## Boundaries and scale limits

Test used distilgpt2, Tiny Shakespeare, 16,256 train positions, 4,064 test positions, and no end-to-end serving kernel. It did not test 7B+ models, production KV-cache behavior, allocator-level VRAM traces, or multi-token state rollout.

## Claim scope

On distilgpt2 with Tiny Shakespeare 128-token windows, small affine probes from intermediate residual states can partially imitate final next-token decisions; the best tested intermediate layer reached 53.30% final top-1 agreement and KL(target||probe) 0.8682 over 4,064 test positions. This supports residual probes as a useful one-token early-exit signal, not as a standalone multi-token draft model.

## Why it stopped

Bounded local evidence supports partial one-token residual probing but early-falsifies the stronger VRAM-free draft-model claim: the probe cannot generate multi-token drafts without running the transformer or adding a separate transition model.

## Recommended next action

Stop this run as no-paper useful-signal evidence; if continuing, test a learned residual-state transition that can roll forward multiple drafted tokens and measure end-to-end speculative acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Residual-State Transition for Multi-Token Drafting
- Success threshold: At least 2.0 accepted/verified tokens per target pass on held-out text with net generation speedup after overhead and no extra vocabulary-size draft model weights beyond the frozen target LM head.
- Stop condition: Stop if 2-token agreement is below 45% or measured end-to-end latency is not faster than target-only decoding after transition/probe overhead.

## Evidence references

- Artifact root: `<local-path>/projects/residual-stream-linear-probe-as-vram-free-draft-model-5aa0f391a795`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
