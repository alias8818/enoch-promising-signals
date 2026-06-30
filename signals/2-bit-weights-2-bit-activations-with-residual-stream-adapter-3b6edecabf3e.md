# 2-bit weights + 2-bit activations with residual-stream adapter

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weights-2-bit-activations-with-residual-stream-adapter-3b6edecabf3e`
Run ID: `2-bit-weights-2-bit-activations-with-residual-stream-adapter-3b6edecabf3e-20260630T101614053288+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b208dfad9bd4

## What looked useful

The residual-stream adapter gave a modest early 600-step validation-loss improvement over raw q2 in 3/3 seeds, but the longer 2000-step q2-vs-adapter sweep reversed the result in 2/3 seeds. The tested adapter is not a reliable from-scratch fix for 2-bit W/A training, though it may be useful as a target for adapter-only or stability-focused follow-up.

## Boundaries and scale limits

No GPT-2-small-class run, no packed 2-bit kernels, no downstream tasks, no production inference measurement, and only three seeds for the bounded local sweeps.

## Claim scope

Tiny character-level GPT on Tiny Shakespeare with simulated straight-through 2-bit linear weights and activations; tested dense FP, raw q2, and q2 plus full-precision residual-stream bottleneck adapters.

## Why it stopped

Bounded local evidence is mixed: the short proxy signal is positive, but the longer direct q2-vs-adapter check is seed-sensitive and mostly negative, so the hypothesis is not reliably supported.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing locally, test adapter-only recovery on a frozen pretrained tiny GPT after simulated 2-bit quantization rather than joint from-scratch training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adapter-only recovery after simulated 2-bit quantization of a pretrained tiny GPT
- Success threshold: Adapter-only recovery improves frozen raw q2 validation loss by at least 0.15 nats mean over three seeds without any seed regressing by more than 0.03 nats, while closing at least 25% of the raw q2-to-dense gap.
- Stop condition: Stop if the adapter-only method fails to improve mean validation loss by 0.05 nats after three seeds or if any two seeds show worse validation loss than the frozen raw q2 baseline.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weights-2-bit-activations-with-residual-stream-adapter-3b6edecabf3e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
