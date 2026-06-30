# Suffix-tree draft beats small DNN draft on repeated prompt streams

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-tree-draft-beats-small-dnn-draft-on-repeated-prompt-streams-d265a32f5124`
Run ID: `suffix-tree-draft-beats-small-dnn-draft-on-repeated-prompt-streams-d265a32f5124-20260629T123622025351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/218ac87ce6e2

## What looked useful

Suffix-context drafting strongly exploited repeated continuations: primary high-repeat acceptance was 0.5888 vs 0.0054 for the default tiny MLP, and the stronger-DNN ablation remained 0.5820 vs 0.1270. Absolute suffix utility collapsed in low-repeat controls, indicating the effect is repetition-dependent.

## Boundaries and scale limits

Synthetic motif streams only; no real prompt traces, no target-model speculative decoding integration, no production serving latency, no transformer draft baseline, and no privacy/security evaluation for suffix memory.

## Claim scope

In a bounded synthetic repeated-prompt-stream benchmark, suffix-context continuation lookup achieved higher accepted draft-token rates than small NumPy MLP drafters trained on the same prior streams, including a stronger one-seed MLP ablation.

## Why it stopped

Closed as useful no-paper evidence because the local result is synthetic/proxy evidence, not direct publication-grade validation of real speculative decoding throughput.

## Recommended next action

Run one bounded direct speculative-decoding integration on real or realistic repeated prompt traces, comparing suffix lookup with an optimized n-gram baseline and a small neural drafter.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct suffix-draft speculative decoding test on repeated traces
- Success threshold: At least 20% higher accepted draft tokens than the best local baseline and a measurable end-to-end throughput gain on the repeated-trace subset, without regression on low-repeat controls.
- Stop condition: Stop if suffix lookup fails to beat optimized n-gram acceptance or if verifier/integration overhead eliminates wall-clock throughput gains on repeated traces.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-beats-small-dnn-draft-on-repeated-prompt-streams-d265a32f5124`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
