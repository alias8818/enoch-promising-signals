# Evaluate evidence-ledger detection on natural assistant claims from local traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evaluate-evidence-ledger-detection-on-natural-assistant-cl-6fb2701d08`
Run ID: `evaluate-evidence-ledger-detection-on-natural-assistant-cl-6fb2701d08-20260612T223238034143+0000`

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

- Parent run decision: Validate evidence-ledger fault detection on real local agent traces: enoch://control-plane/projects/validate-evidence-ledger-fault-detection-on-real-local-age-b272820ddd/runs/validate-evidence-ledger-fault-detection-on-real-local-age-b272820ddd-20260612T112936370141+0000
- Parent run decision: Evidence-Ledger Agent Reliability Harness on CPU: enoch://control-plane/projects/evidence-ledger-agent-reliability-harness-on-cpu-4b2d655e6e8c/runs/evidence-ledger-agent-reliability-harness-on-cpu-4b2d655e6e8c-20260611T215931945775+0000

## What looked useful

Evidence-ledger checks achieved 0.909 accuracy and 1.000 unsupported-claim recall, versus 0.854 accuracy and 0.752 unsupported-claim recall for a lexical-overlap baseline. Ablations showed cited-reference binding, required-term matching, and numeric checks each prevent false accepts.

## Boundaries and scale limits

No private or external real assistant trace corpus was present in the project. The result is generated from local project text and does not establish robustness on human-authored or model-authored traces.

## Claim scope

On 396 deterministic natural-assistant-style claim/evidence cases generated from local project scaffold and controller traces, a rule-based evidence-ledger detector improved unsupported-claim recall over a lexical-overlap baseline.

## Why it stopped

Tier 2-style local generated benchmark completed with fixed seeds, baseline, and ablations, but the absence of real natural assistant traces prevents publication-grade closure.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to evaluate the unchanged detector and baseline on a held-out corpus of real assistant traces with human labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate evidence-ledger detection on real assistant traces with human labels
- Success threshold: At least 0.90 unsupported-claim recall with no more than 0.15 false-reject rate on supported claims, and at least +0.10 unsupported-F1 over the lexical baseline.
- Stop condition: Stop if unsupported recall falls below 0.80 or the detector fails to beat the lexical baseline by at least +0.05 unsupported-F1 on the real-trace corpus.

## Evidence references

- Artifact root: `<local-path>/projects/evaluate-evidence-ledger-detection-on-natural-assistant-cl-6fb2701d08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
