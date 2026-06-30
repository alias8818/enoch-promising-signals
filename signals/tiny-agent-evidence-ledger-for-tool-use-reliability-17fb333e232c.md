# Tiny Agent Evidence Ledger for Tool-Use Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-for-tool-use-reliability-17fb333e232c`
Run ID: `tiny-agent-evidence-ledger-for-tool-use-reliability-17fb333e232c-20260531T175620820376+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1f7c49f7f4e2

## What looked useful

The mechanism behaved as intended: no deterministic failures produced no benefit, while higher deterministic-failure rates produced larger call reductions and many skipped known-dead calls with success rates effectively unchanged.

## Boundaries and scale limits

Evidence is synthetic and CPU-local only. It does not validate LLM planning, real API error distributions, production latency/cost, stale evidence, adversarial cases, or multi-step downstream reasoning effects.

## Claim scope

In a seeded synthetic tool-use simulator with repeated task families, deterministic primary-tool failures, fallback tools, and transient failures, a tiny evidence ledger reduced redundant tool calls by about 35.7% at the main parameter point without measurable success-rate loss.

## Why it stopped

Synthetic bounded mechanism test is positive but not direct/full validation of real tool-use reliability, so the run should not proceed to paper writing.

## Recommended next action

Stop this run as no-paper useful evidence; next concrete action is replaying the same ledger policy on real or production-like agent tool traces with observed error signatures and cost/latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay evidence-ledger policy on real agent tool-error traces
- Success threshold: At least 15% total tool-call or latency/cost reduction versus blind retry, success-rate delta no worse than -0.5 percentage points, and improvement over a simple retry-cap baseline.
- Stop condition: Stop if ledger replay reduces calls by under 5%, loses more than 0.5 percentage points of success, or fails to beat a simple retry-cap baseline.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-for-tool-use-reliability-17fb333e232c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
