# Agent Reliability Evidence Ledger with Bounded Counterexamples

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-reliability-evidence-ledger-with-bounded-counterexamples-dad3e142bb01`
Run ID: `agent-reliability-evidence-ledger-with-bounded-counterexamples-dad3e142bb01-20260608T194144048341+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/69b8a2ecfe2c

## What looked useful

Corrected 500-trial confirmation showed ledger certification precision 0.9312 versus naive 0.7096, false-certified domain-mass rate 0.0874 versus 0.2904, and 61.9% lower false-certified domain mass. A no-counterexample ablation reduced false-certified mass by 32.4%, indicating bounded counterexample probes added value beyond scoping alone.

## Boundaries and scale limits

Only toy arithmetic/comparison domains and hand-designed failure regimes were tested. No real LLM agent traces, real tool-use benchmarks, opaque model failures, or broad deployment distributions were evaluated.

## Claim scope

On deterministic synthetic finite task domains with exhaustive ground truth, a scoped evidence ledger with bounded counterexample probes reduced coverage-weighted false reliability certification versus naive pass-rate certification.

## Why it stopped

Synthetic evidence supports the mechanism as a useful signal, but it is proxy-only and not direct publication-grade evidence for real agent reliability.

## Recommended next action

Run a bounded deepen follow-up on public agent/tool-use benchmark traces with held-out labeled failures before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger on Public Agent Trace Benchmarks
- Success threshold: At least 30% relative reduction in coverage-weighted false-certified domain or trace mass versus baseline while retaining at least 50% certified coverage on held-out traces.
- Stop condition: Stop if ledger false-certified mass is not lower than the calibrated baseline on two benchmark/task families or if certified coverage falls below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-evidence-ledger-with-bounded-counterexamples-dad3e142bb01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
