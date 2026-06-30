# Real-Model Exact Anchor KV Retention Probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-exact-anchor-kv-retention-probe-73b6b05056`
Run ID: `real-model-exact-anchor-kv-retention-probe-73b6b05056-20260529T170213155820+0000`

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

- Parent run decision: Exact-Anchor Retrieval Probe for Compressed KV States: enoch://control-plane/projects/exact-anchor-retrieval-probe-for-compressed-kv-states-0289a6dbd66f/runs/exact-anchor-retrieval-probe-for-compressed-kv-states-0289a6dbd66f-20260529T133631049837+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a8589b716432

## What looked useful

A controlled real-model cache intervention found strong mechanism evidence that exact anchor KV retention can recover recall signal beyond a sliding window; the 0.5B run met the predeclared operational threshold and the 1.5B run restored log-probability but missed the absolute rank threshold because the full-cache baseline was already outside that rank bound.

## Boundaries and scale limits

Only two checkpoints from one model family, synthetic prompts, one recent-window size, attention-mask cache accessibility intervention, and next-token scoring were tested. No deployable cache policy, end-to-end generation benchmark, natural long-context dataset, latency/memory tradeoff, or cross-family robustness was validated.

## Claim scope

On synthetic single-anchor recall prompts in Qwen2.5 0.5B/1.5B instruct models, exact retention of the anchor token KV entries plus a 32-token recent window restored nearly all target-token log-probability lost by a recent-window-only KV mask, while same-budget non-anchor early-token controls did not.

## Why it stopped

Tier 1 direct evidence produced a useful mechanism signal, but the evidence is synthetic, narrow, and not publication-grade; strict paper gate remains negative.

## Recommended next action

Run a medium direct follow-up using full-cache-normalized success thresholds on natural long-context recall prompts across at least three model families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Baseline-Normalized Multi-Model Anchor KV Retention Probe
- Success threshold: Mean full-cache-normalized log-probability recovery for anchor_plus_window is at least 0.80, median rank is no worse than 1.25x the full-cache median rank, and same-budget non-anchor controls recover less than 0.25 across at least two of three model families.
- Stop condition: Stop as unsupported if anchor_plus_window recovery is not at least 0.50 or fails to beat same-budget controls on two or more model families.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-exact-anchor-kv-retention-probe-73b6b05056`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
