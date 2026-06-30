# Direct small-agent quantized residual memory on natural-language household safety traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-small-agent-quantized-residual-memory-on-natural-la-7918c0a503`
Run ID: `direct-small-agent-quantized-residual-memory-on-natural-la-7918c0a503-20260527T073953194937+0000`

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

- Parent run decision: Quantized residual memory for safer small home agents: enoch://control-plane/projects/quantized-residual-memory-for-safer-small-home-agents-b7558d52af4d/runs/quantized-residual-memory-for-safer-small-home-agents-b7558d52af4d-20260525T070120899490+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/278e45695bb5

## What looked useful

Quantized memory improved macro-F1 over a recent-window agent by +0.3481 while using 23.99% of raw trace bytes, but a simpler non-residual quantized count memory outperformed QRM by +0.0428 macro-F1.

## Boundaries and scale limits

Generated traces only; binary intervention labels only; no human-collected logs, no embodied execution, no language-model policy, and no long-horizon deployment.

## Claim scope

Controlled Tier 1 generated natural-language household safety traces with early decisive cues, a small hashed linear policy, and 64-byte 4-bit quantized memory.

## Why it stopped

No-paper useful signal: direct Tier 1 evidence supports compressed quantized memory, but the residual-specific mechanism is mixed because the non-residual quantized count control was stronger.

## Recommended next action

Run a bounded deepen test that stresses residual memory against count memory on longer traces with repeated distractors, stale cue cancellation, and contradictory updates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual versus count quantized memory under stale and contradictory household safety cues
- Success threshold: Residual QRM macro-F1 exceeds quantized count memory by at least 0.03 while also beating recent-window by at least 0.10 and staying at or below 30% of raw trace bytes.
- Stop condition: Stop if residual QRM fails to beat quantized count memory by 0.03 macro-F1 on the stale/contradictory trace suite or if the compression target cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-agent-quantized-residual-memory-on-natural-la-7918c0a503`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
