# Deterministic replay ledger for stochastic CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-replay-ledger-for-stochastic-cpu-agents-066d978d16a8`
Run ID: `deterministic-replay-ledger-for-stochastic-cpu-agents-066d978d16a8-20260531T130733591784+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8408ff0055b8

## What looked useful

The mechanism is viable in a bounded proxy: all record/replay trials matched, mutated/truncated ledger controls were detected, median storage was about 329 bytes per event, and record overhead was about 4.7x to 5.7x versus a cheap no-ledger baseline.

## Boundaries and scale limits

Not tested on real LLM/API sampling, real agent frameworks, concurrent agents, process restart, filesystem/network side effects, crash recovery, or long-running task suites. Python JSON overhead was measured only up to 8192 synthetic steps.

## Claim scope

For a single-process synthetic CPU-agent proxy, an append-only ledger that records entropy draws, wall-clock observations, and tool outputs produced exact replay across 15 benchmark trials even when replay used a different RNG seed and changed live tool variant; simple ledger drift was detected.

## Why it stopped

No-paper closure: this run produced useful synthetic evidence for the replay mechanism, but the evidence is proxy-only and does not validate real agent frameworks or concurrent side effects.

## Recommended next action

Run a bounded deepen test by wrapping the ledger around a real local agent/tool harness and compare exact replay, drift detection, and overhead against checkpoint-only replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay ledger on a real local agent/tool harness
- Success threshold: At least 95% exact replay success on successful recorded tasks, all tamper controls detected, and median wall-clock overhead below 25% for tasks with real tool/model latency.
- Stop condition: Stop if exact replay falls below 80% due to uncaptured nondeterministic boundaries after one instrumentation pass, or if median overhead exceeds 2x on realistic tasks.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-ledger-for-stochastic-cpu-agents-066d978d16a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
