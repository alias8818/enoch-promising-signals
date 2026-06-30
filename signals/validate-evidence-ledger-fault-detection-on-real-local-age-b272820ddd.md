# Validate evidence-ledger fault detection on real local agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `validate-evidence-ledger-fault-detection-on-real-local-age-b272820ddd`
Run ID: `validate-evidence-ledger-fault-detection-on-real-local-age-b272820ddd-20260612T112936370141+0000`

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

- Parent run decision: Evidence-Ledger Agent Reliability Harness on CPU: enoch://control-plane/projects/evidence-ledger-agent-reliability-harness-on-cpu-4b2d655e6e8c/runs/evidence-ledger-agent-reliability-harness-on-cpu-4b2d655e6e8c-20260611T215931945775+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b9ad3c70f5

## What looked useful

After fixing multiline command parsing, the evidence-ledger detector reached TP 67, FP 0, TN 67, FN 0 on controlled faults over real local traces, while a command-presence baseline had zero fault recall.

## Boundaries and scale limits

Only 25 command/output ledger entries and 134 generated labeled claims were tested. Claims were schema-constrained and faults were injected, not naturally occurring free-form assistant mistakes. Non-shell tools, paraphrases, and ambiguous repeated-command references were not validated.

## Claim scope

Tier 1 controlled direct test on 20 real local Codex JSONL traces: an evidence ledger linking exec_command calls to outputs detected injected exit-code, workdir, and output-token faults in schema-constrained claims.

## Why it stopped

Tier 1 useful signal achieved, but evidence is schema-constrained and injected-fault based rather than broad natural-language validation.

## Recommended next action

Run a bounded deepen test on natural assistant summary/final-answer claims from local traces with independent labels, requiring at least 90% recall and at most 10% false positives before considering a medium confirmation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate evidence-ledger detection on natural assistant claims from local traces
- Success threshold: At least 90% recall on unsupported natural claims and at most 10% false positives on supported natural claims across at least 200 labeled claims from at least 20 traces.
- Stop condition: Stop if fewer than 200 labelable natural claims can be extracted locally, or if false positives exceed 20% after parser fixes on a 50-claim calibration split.

## Evidence references

- Artifact root: `<local-path>/projects/validate-evidence-ledger-fault-detection-on-real-local-age-b272820ddd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
