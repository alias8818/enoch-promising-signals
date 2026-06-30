# Layer/head-specific position-aware KV outlier selectors on real text traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `layer-head-specific-position-aware-kv-outlier-selectors-on-b6f05de403`
Run ID: `layer-head-specific-position-aware-kv-outlier-selectors-on-b6f05de403-20260523T134334492652+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Multi-layer real-model test of calibrated residual KV outlier selectors: enoch://control-plane/projects/multi-layer-real-model-test-of-calibrated-residual-kv-outl-52f5be2ae9/runs/multi-layer-real-model-test-of-calibrated-residual-kv-outl-52f5be2ae9-20260523T131838140283+0000
- Parent run decision: Position-aware residual selectors for KV outlier prediction: enoch://control-plane/projects/position-aware-residual-selectors-for-kv-outlier-predictio-023629249e/runs/position-aware-residual-selectors-for-kv-outlier-predictio-023629249e-20260523T132735004937+0000

## What looked useful

The proposed layer/head-specific position+KV selector consistently beat real baselines and ablations across two fixed-seed GPU trace validations: at seq_len 384 it improved retained attention mass over recent-token selection by +0.351, +0.393, and +0.409 at 5%, 10%, and 20% budgets while reducing relative context L2 by 0.086, 0.325, and 0.493. It also outperformed global KV norm and shared learned selectors, supporting both layer/head specificity and position awareness.

## Boundaries and scale limits

Trace-level validation only; no live KV-cache pruning intervention, no perplexity/generation-quality measurement, no latency/memory benchmark, one model size/family, one corpus, sampled query positions rather than every token.

## Claim scope

On held-out GPT-2-small WikiText-2 attention traces at sequence lengths 192 and 384, layer/head-specific position-aware KV-norm selectors preserve substantially more attention mass and lower attention-context reconstruction error than recent-token, random, global KV-norm, shared learned, and single-factor ablation selectors at 5%, 10%, and 20% cache budgets.

## Why it stopped

Mechanism supported on direct real-text attention traces, but evidence is trace/context approximation only and is not sufficient for paper-positive downstream cache-pruning claims.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is an end-to-end GPT-2-small KV-cache pruning evaluation measuring perplexity, latency, and memory against full-cache, recent-token, and global/selective baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2-small KV-cache pruning with layer/head position-aware selectors
- Success threshold: At two or more cache budgets, the layer/head position-aware selector must match full-cache perplexity within a small predefined tolerance while using less cache than recent-token and global KV-norm baselines, and must not lose its advantage in latency or memory measurements.
- Stop condition: Stop as negative if live-pruned perplexity is no better than recent-token or global KV-norm baselines at matched cache budgets, or if pruning overhead erases practical latency/memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/layer-head-specific-position-aware-kv-outlier-selectors-on-b6f05de403`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
