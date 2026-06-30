# Self-Speculative Layer-Skip Decode on GB10

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `self-speculative-layer-skip-decode-on-gb10-d585b39a63b5`
Run ID: `self-speculative-layer-skip-decode-on-gb10-d585b39a63b5-20260614T002845605346+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/915e27ae2b3e

## What looked useful

Untrained early-exit self-speculation is a poor fallback on GB10. SmolLM2-135M assistant_early_exit median speedups were 0.395x, 0.341x, 0.346x, 0.255x, 0.223x, and 0.132x for exits 1, 2, 4, 8, 12, and 20. GPT-2 intermediate-layer probing showed early exits are cheap but low-agreement, while late exits are higher-agreement but too costly.

## Boundaries and scale limits

Short local probes only: 16 prompt hidden-state/timing proxy for GPT-2; four-prompt, 32-token greedy generation benchmark for SmolLM2-135M; no trained LayerSkip checkpoint, no optimized cache/activation reuse implementation, no long benchmark, and no large model validation.

## Claim scope

On this GB10 worker, applying Transformers assistant_early_exit to ordinary ungated checkpoints did not produce a viable speedup path: GPT-2 failed in the API path and SmolLM2-135M was slower than greedy baseline for every tested exit layer. The trained Meta LayerSkip checkpoint was not directly tested because access was gated.

## Why it stopped

Proxy/early falsification of the untrained-checkpoint fallback, not full validation or full rejection of trained LayerSkip self-speculation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; only rerun if authorized access to a trained LayerSkip checkpoint is available, then benchmark greedy decoding versus assistant_early_exit on the same GB10 prompts and dtype.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-layer-skip-decode-on-gb10-d585b39a63b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
