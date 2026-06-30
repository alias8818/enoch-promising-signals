# Early-Exit Layer-Skip Self-Speculation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-layer-skip-self-speculation-cdbe4755f463`
Run ID: `early-exit-layer-skip-self-speculation-cdbe4755f463-20260619T202724916704+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:MiniMaxAI/MiniMax-M3: enoch://research-facility/provider/hf:MiniMaxAI/MiniMax-M3/de473bf63e78

## What looked useful

Layer 6 reached only 22.66% top-1 agreement and 0.313 accepted tokens per gamma-4 self-speculation round. Even layer 10 reached only 47.66% agreement and 0.500 accepted tokens per round, below the predeclared 70% agreement and 2.0 accepted-tokens-per-round gates.

## Boundaries and scale limits

Tested one 124M-parameter GPT-2 model, 20 prompts, 640 greedy token decisions, and naive exact self-speculation controls on GB10. Did not test LayerSkip-trained checkpoints, optimized shared-KV/shared-activation runtimes, larger models, or downstream task quality.

## Claim scope

Off-the-shelf GPT-2 intermediate layers decoded through the shared LM head are not accurate enough for practical static early-exit self-speculative drafting under this local greedy-generation probe.

## Why it stopped

Proxy/local early falsification: untrained GPT-2 intermediate logits fail the static draft agreement and self-speculation acceptance thresholds; this is not a full validation or a negative result for trained LayerSkip-style checkpoints.

## Recommended next action

Run a bounded deepen follow-up that trains or fine-tunes a GPT-2-small-style checkpoint with layer dropout and early-exit loss, then reruns the same agreement and gamma-4 acceptance gates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a GPT-2-small LayerSkip-style early-exit checkpoint
- Success threshold: Best draft layer reaches at least 70% top-1 agreement and at least 2.0 accepted tokens per gamma-4 verification round without degrading full-model greedy outputs.
- Stop condition: Stop if trained intermediate layers remain below 50% top-1 agreement or below 1.0 accepted token per gamma-4 round after a bounded fine-tuning budget.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-layer-skip-self-speculation-cdbe4755f463`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
