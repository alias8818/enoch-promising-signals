# Self-Speculative Decoding via Layer-Skip Early-Exit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-layer-skip-early-exit-73b4ac1780de`
Run ID: `self-speculative-decoding-via-layer-skip-early-exit-73b4ac1780de-20260629T170035722360+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/101a628c8c88

## What looked useful

Early exits are either cheap and poorly aligned or aligned only after most layers have already run. Best modeled speedup was 0.995x at layer 1; layer 11 had 53.6% agreement but only 0.801x modeled speed because it is 11/12 of the network. High-confidence layer 11 positions reached 92.0% agreement at 17.9% coverage, suggesting confidence gating is diagnostic but not enough for ungated speedup.

## Boundaries and scale limits

Single pretrained GPT-2-small model, 256 text samples, sequence length 96, top-1 agreement against the final model, and an idealized layer-depth cost model rather than a custom measured generation kernel. Does not test LayerSkip-style retraining, 7B+ models, long-context serving, or broad task suites.

## Claim scope

For ordinary pretrained GPT-2-small without early-exit training, applying the final layer norm plus tied LM head to intermediate layers does not produce modeled self-speculative layer-skip speedup on the 23,050-position local probe.

## Why it stopped

No paper-worthy positive result: public LayerSkip already covers the trained method, while this local pretrained-only variant failed to exceed baseline in the modeled speedup probe.

## Recommended next action

Run a bounded GPT-2-small-class training or fine-tuning follow-up with layer dropout plus an early-exit loss, then rerun this probe and add a measured self-speculative generation benchmark; stop treating the pretrained-only shortcut as viable.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded GPT-2-small LayerSkip-style early-exit training
- Success threshold: At least one exit layer at or before half depth achieves >= 60% top-1 agreement with the final model and measured greedy generation speedup >= 1.2x without output divergence beyond verifier-corrected speculative semantics.
- Stop condition: Stop if half-depth agreement remains below 40% after the bounded training budget or if measured generation speedup remains <= 1.0x despite agreement gains.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-layer-skip-early-exit-73b4ac1780de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
