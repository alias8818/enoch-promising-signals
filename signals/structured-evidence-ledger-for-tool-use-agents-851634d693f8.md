# Structured Evidence Ledger for Tool-Use Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-for-tool-use-agents-851634d693f8`
Run ID: `structured-evidence-ledger-for-tool-use-agents-851634d693f8-20260517T170608934802+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2e8dc4035b73

## What looked useful

At full coverage, the structured ledger reached 0.8375 mean end-to-end accuracy versus 0.7876 for the strongest transcript baseline, reducing unsupported answers by 23.5% relative. With a stricter margin threshold, it reduced unsupported answered errors by 85.0% relative at 0.6913 coverage.

## Boundaries and scale limits

Local synthetic evidence only: 30 seeds, 300 calibration tasks and 1000 evaluation tasks per seed. No live LLM, real tool APIs, real traces, human audit labels, nonstationary sources, or long-horizon agent workflows were tested.

## Claim scope

In a deterministic synthetic benchmark where tool evidence has persistent source-specific reliability and conflicting values, a structured evidence ledger with calibration-derived source weights improved answer-all end-to-end accuracy over transcript-style baselines and provided an abstaining mode that sharply reduced unsupported answered errors.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and mechanism-level rather than direct publication-grade validation on real tool-use agents.

## Recommended next action

Run a bounded real-trace follow-up using replayed tool-use transcripts with human-labeled evidence support to test whether the synthetic source-reliability mechanism survives parsing noise and nonstationary tools.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Evidence Ledger Evaluation for Tool-Use Agents
- Success threshold: At matched coverage of at least 0.80, reduce unsupported final-answer rate by at least 20% relative to the best transcript baseline without lowering end-to-end accuracy by more than 2 percentage points.
- Stop condition: Stop if evidence extraction noise or nonstationary source reliability eliminates the unsupported-answer reduction on two independently sampled trace sets.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-tool-use-agents-851634d693f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
