# Exact-anchor hybrid memory in a real small-agent trace loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-hybrid-memory-in-a-real-small-agent-trace-loo-81b679c6d2`
Run ID: `exact-anchor-hybrid-memory-in-a-real-small-agent-trace-loo-81b679c6d2-20260525T064101485724+0000`

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

- Parent run decision: Exact-Anchor Episodic Memory for Small Agents: enoch://control-plane/projects/exact-anchor-episodic-memory-for-small-agents-38b3219c09d4/runs/exact-anchor-episodic-memory-for-small-agents-38b3219c09d4-20260525T035831395822+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7a13d09d61dc

## What looked useful

Exact side storage keyed by stable anchors achieved 240/240 exact answers and 100% anchor retrieval after 48 distractors, while window-only and lossy-summary baselines scored 0/240 in the main threshold condition. Sensitivity confirmed window-only succeeds only while the target remains inside the working window.

## Boundaries and scale limits

Synthetic deterministic traces only; no LLM planner, no embedding/vector retrieval baseline, no noisy production traces, no multi-session persistence, and no large-memory latency or robustness testing.

## Claim scope

In a deterministic controlled small-agent observe/retrieve/answer trace loop with stable exact anchors, an exact-anchor hybrid memory preserved exact anchored facts after distractors and exceeded window-only and lossy-summary baselines.

## Why it stopped

Tier 1 controlled small direct threshold was met, but the evidence is synthetic and deterministic, so this is useful mechanism support rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up in an actual LLM-driven small-agent loop with natural trace text, noisy/missing anchors, and a stronger exact-capable retrieval baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor hybrid memory in an LLM-driven small-agent loop
- Success threshold: Hybrid exact-answer accuracy at least 95%, at least 15 percentage points above the best exact-capable baseline, anchor retrieval at least 95%, and median retrieval latency under 50 ms at the tested trace scale.
- Stop condition: Stop if hybrid accuracy falls below 90%, if the best exact-capable baseline is within 5 percentage points while simpler, or if retrieval latency/memory growth makes the method impractical at the tested small-agent scale.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-hybrid-memory-in-a-real-small-agent-trace-loo-81b679c6d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
