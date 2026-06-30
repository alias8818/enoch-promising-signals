# Counterexample probes on real agent evidence traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `counterexample-probes-on-real-agent-evidence-traces-092e372e3c`
Run ID: `counterexample-probes-on-real-agent-evidence-traces-092e372e3c-20260613T153101692214+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Counterexample Probe Harness for Agent Evidence: enoch://control-plane/projects/counterexample-probe-harness-for-agent-evidence-1df293327e1c/runs/counterexample-probe-harness-for-agent-evidence-1df293327e1c-20260613T151032545332+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d76f7b50682f

## What looked useful

The probe harness parsed 16 completed trace items, evaluated 4 real trace claims as supported, and detected 2/2 planted contradiction controls with 0 control misses.

## Boundaries and scale limits

One local trace, four real claim probes, two planted controls, hand-scoped templates, no cross-agent or multi-project corpus, no manual adjudication beyond this run.

## Claim scope

A tiny controlled local test over one real Codex evidence trace shows that simple command-backed probes can evaluate concrete agent trace claims and detect planted contradictions, but it found no natural high-confidence counterexample in the tested trace.

## Why it stopped

Tier 1 controlled direct test completed; mechanism signal is useful, but no natural counterexample or publication-grade evidence was produced.

## Recommended next action

Run the same probe design on a bounded corpus of at least 20 real agent traces with pre-registered claim templates and manual adjudication of every flagged natural counterexample.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace counterexample probe adjudication
- Success threshold: Detect 100% of planted contradiction controls and at least one manually validated natural high-confidence counterexample, with no more than 10% false positives among natural flags.
- Stop condition: Stop after 20 traces if planted controls are missed, no natural counterexample is found, or false positives exceed 10% of natural flags.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-probes-on-real-agent-evidence-traces-092e372e3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
