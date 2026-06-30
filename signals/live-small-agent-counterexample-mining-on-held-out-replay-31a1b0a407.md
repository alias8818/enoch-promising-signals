# Live Small-Agent Counterexample Mining on Held-Out Replay Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-small-agent-counterexample-mining-on-held-out-replay-31a1b0a407`
Run ID: `live-small-agent-counterexample-mining-on-held-out-replay-31a1b0a407-20260620T152832533205+0000`

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

- Parent run decision: Counterexample-Mining Pipeline for Small CPU Agents: enoch://control-plane/projects/counterexample-mining-pipeline-for-small-cpu-agents-3fd2d6741fba/runs/counterexample-mining-pipeline-for-small-cpu-agents-3fd2d6741fba-20260620T150812130028+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8478ec7cb8b7

## What looked useful

The Tier 1 threshold passed: layered_doctrine_memory scored 7/7, flat_retrieval scored 4/7, and 3 held-out counterexamples were mined against flat retrieval.

## Boundaries and scale limits

Small synthetic local suite only; no live LLM agents, no natural replay corpus, no blinded task construction, and no large-scale robustness statistics.

## Claim scope

On a 7-task synthetic held-out replay suite, deterministic layered doctrine memory beat flat retrieval by 42.86 percentage points and mined 3 flat-fail/layered-pass counterexamples across operator-doctrine, negated-memory, and threshold-recall cases.

## Why it stopped

No-paper closure: Tier 1 mechanism support is useful but the evidence is too small and synthetic for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on a larger frozen held-out replay corpus with live small-agent executions and ablations for doctrine filtering, supersession, recency, noisy metadata, and yes/no normalization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger frozen held-out replay confirmation for layered doctrine memory
- Success threshold: Layered doctrine memory accuracy exceeds flat retrieval by at least 20 percentage points and mines at least 10 flat-fail/layered-pass counterexamples without increasing private-payload leakage.
- Stop condition: Stop if layered advantage is below 20 percentage points, fewer than 10 counterexamples are mined, or doctrine filtering introduces any raw private-payload leak.

## Evidence references

- Artifact root: `<local-path>/projects/live-small-agent-counterexample-mining-on-held-out-replay-31a1b0a407`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
