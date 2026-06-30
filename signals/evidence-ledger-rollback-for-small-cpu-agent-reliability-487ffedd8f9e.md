# Evidence-Ledger Rollback for Small CPU Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-for-small-cpu-agent-reliability-487ffedd8f9e`
Run ID: `evidence-ledger-rollback-for-small-cpu-agent-reliability-487ffedd8f9e-20260607T101138468234+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/536a305805e4

## What looked useful

Rollback matched an oracle recompute policy on the synthetic benchmark, raised mean accuracy from 0.67425 to 0.84842, reduced MAE from 0.80260 to 0.32756, and reduced active stale group-sum claims from 38.3404 to 0 per trial.

## Boundaries and scale limits

Evidence is limited to 5,000 synthetic trials plus six 1,000-trial sensitivity points. It does not validate real small CPU LLM agents, natural-language evidence notes, software-agent workflows, or long-horizon planning.

## Claim scope

In a deterministic synthetic incremental group-sum benchmark with noisy initial observations and later corrections, dependency-aware evidence-ledger rollback removed active stale derived claims and improved final retrieval accuracy versus a no-rollback ledger.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic and mechanism-level, not direct validation in real small CPU LLM agents.

## Recommended next action

Run a bounded direct follow-up using an actual small CPU LLM agent on contradiction-injected multi-step tasks, comparing identical prompts and tools with versus without dependency-aware rollback.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dependency-aware rollback in real small CPU LLM contradiction tasks
- Success threshold: Rollback improves final-answer accuracy by at least 10 percentage points or reduces stale-note-caused errors by at least 50% without more than 20% runtime overhead on the tested CPU-agent benchmark.
- Stop condition: Stop if rollback does not reduce stale-note-caused errors by at least 20% after 100 paired tasks, or if instrumentation cannot reliably identify evidence dependencies and stale-note usage.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-small-cpu-agent-reliability-487ffedd8f9e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
