# Shared-Embedding Micro-Draft Network for Spec Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `shared-embedding-micro-draft-network-for-spec-decoding-1dd4e00f003c`
Run ID: `shared-embedding-micro-draft-network-for-spec-decoding-1dd4e00f003c-20260526T022911539795+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d456810f23e

## What looked useful

Across three seeds and 24,576 held-out token positions, shared target geometry averaged 33.46% greedy agreement versus 26.54% for frozen random geometry, a mean +6.92 percentage-point advantage. The shared draft also had lower CE to target top-1 labels (4.25 vs 6.42) and measured 1.74x target forward throughput for the tested batch shape.

## Boundaries and scale limits

This run used distilgpt2, 512 train blocks, 128 held-out blocks, sequence length 64, 300 steps per draft, and three random seeds. It did not test larger LMs, actual speculative decoding verifier loops, KV-cache behavior, sampling acceptance, or generated-output quality.

## Claim scope

On a bounded distilgpt2/WikiText-2 imitation probe, a 702,720-trainable-parameter GRU draft that reuses the target token embedding/output geometry matched the target greedy next-token argmax more often than the same trainable architecture with frozen random token geometry.

## Why it stopped

No-paper closure: the evidence supports the shared-token-geometry mechanism in a small imitation proxy, but it is not a full speculative decoding validation.

## Recommended next action

Run a bounded end-to-end speculative decoding follow-up that trains the shared-geometry draft and measures accepted tokens per verifier pass, exact greedy equivalence, and wall-clock tokens/s against a standard small draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Speculative Decoding With Shared-Geometry Micro Draft
- Success threshold: On held-out prompts, shared-geometry speculative decoding preserves greedy target outputs exactly and achieves at least 1.1x wall-clock tokens/s plus at least 10% relative accepted-token-rate improvement over the best bounded control.
- Stop condition: Stop as negative if shared geometry fails exact greedy equivalence, fails to exceed 1.0x wall-clock speed, or has accepted-token rate within 10% relative of the best control after the same training budget.

## Evidence references

- Artifact root: `<local-path>/projects/shared-embedding-micro-draft-network-for-spec-decoding-1dd4e00f003c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
