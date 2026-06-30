# Implementation-Level Verifier Prefix Cache Replay on SwissAI Trace

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `83`
Project ID: `implementation-level-verifier-prefix-cache-replay-on-swiss-c940701b33`
Run ID: `implementation-level-verifier-prefix-cache-replay-on-swiss-c940701b33-20260522T093604517916+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-Trace Calibrated Verifier Cache-Cost Replay: enoch://control-plane/projects/real-trace-calibrated-verifier-cache-cost-replay-68f6e85a94/runs/real-trace-calibrated-verifier-cache-cost-replay-68f6e85a94-20260522T081404903261+0000
- Parent run decision: Calibrated Verifier Cache-Cost Scheduling Test: enoch://control-plane/projects/calibrated-verifier-cache-cost-scheduling-test-f3743cc2fb/runs/calibrated-verifier-cache-cost-scheduling-test-f3743cc2fb-20260522T065625951455+0000

## What looked useful

Full chronological replay found 222,770,750 reusable prefix buckets out of 293,360,187 total buckets (75.94%), versus 121,909,836 buckets (41.56%) for exact full-prompt repeats. A 500k randomized-bucket negative control produced 0.00% reuse, and strip-first-3/10-bucket ablations remained around 75% reuse.

## Boundaries and scale limits

Validated on supplied deterministic bucket IDs for 3,994,435 trace rows, not on raw prompts, tokenizer reconstruction, live serving latency, KV-cache memory transfer, eviction policies, scheduler effects, or multiple inference engines.

## Claim scope

Exact chronological prefix-cache replay over the public SwissAI Qwen/Qwen3-32B bucketized trace shows substantial reusable 16-token prefix structure beyond exact full-prompt repeats.

## Why it stopped

Trace-level mechanism is supported, but Tier 4 paper-readiness is not met because the evidence does not include real serving-engine KV-cache replay, latency, eviction robustness, or raw-prompt/tokenizer verification.

## Recommended next action

Stop at no-paper useful signal: follow-up depth is already 4, and paper readiness would require end-to-end serving-engine replay/latency evidence rather than another controller-chained trace-only deepen run.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/implementation-level-verifier-prefix-cache-replay-on-swiss-c940701b33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
