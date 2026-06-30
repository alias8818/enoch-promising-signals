# Actual LLM-generated noisy replay counterexample mining under blind labels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `actual-llm-generated-noisy-replay-counterexample-mining-un-95021498fa`
Run ID: `actual-llm-generated-noisy-replay-counterexample-mining-un-95021498fa-20260613T020458934306+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Natural-language counterexample mining on repeated-agent replay traces: enoch://control-plane/projects/natural-language-counterexample-mining-on-repeated-agent-r-6e0bf4847b/runs/natural-language-counterexample-mining-on-repeated-agent-r-6e0bf4847b-20260613T011052081949+0000
- Parent run decision: LLM-generated noisy replay counterexample mining with blind labels: enoch://control-plane/projects/llm-generated-noisy-replay-counterexample-mining-with-blin-5a634f5dbb/runs/llm-generated-noisy-replay-counterexample-mining-with-blin-5a634f5dbb-20260613T013852903789+0000

## What looked useful

Blind replay counterexample signals are detectable, but the tested weighted combined miner is not competitive with simpler strong baselines. False positives arise from safe actions with contradiction markers and stale/mismatched memory metadata.

## Boundaries and scale limits

480000 synthetic LLM-style replay records across 20 seeds and 4 noise levels on a CPU worker. No actual LLM-generated replay text was tested because no local LLM runtime or transformer package was installed and no private API credentials were used.

## Claim scope

On a deterministic noisy replay benchmark with hidden blind labels, the proposed combined blind miner improves over random and metadata-only controls but loses clearly to contradiction-only, memory-conflict-only, and lexical violation baselines on average precision.

## Why it stopped

Bounded validation found useful blind-signal evidence but not a competitive method, and the actual LLM-generated text requirement remained untested.

## Recommended next action

Stop this run as no-paper useful evidence; only pursue a bounded deepen follow-up if actual LLM-generated replay text is available and the proposed miner is required to beat contradiction and lexical baselines by a predeclared margin.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual LLM-generated replay corpus test for blind counterexample mining
- Success threshold: Proposed miner beats contradiction-only and lexical baselines by at least +0.05 mean average precision with bootstrap p05 above 0.00, and maintains precision@1% >= 0.90.
- Stop condition: Stop if actual LLM text cannot be generated or loaded reproducibly, or if the proposed miner fails to beat either strong baseline on mean average precision after the predeclared seed/noise matrix.

## Evidence references

- Artifact root: `<local-path>/projects/actual-llm-generated-noisy-replay-counterexample-mining-un-95021498fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
