# Evidence-Ledger Agent Reliability Harness on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-harness-on-cpu-4b2d655e6e8c`
Run ID: `evidence-ledger-agent-reliability-harness-on-cpu-4b2d655e6e8c-20260611T215931945775+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b9ad3c70f5

## What looked useful

Evidence-ledger structure makes non-final-answer reliability faults measurable: ledger recall was 1.000 with false-positive rate 0.000 on 35000 synthetic traces, while final-answer checking had recall 0.167 because it only detected final answer mismatches.

## Boundaries and scale limits

Synthetic traces only; no live LLM or tool-using agent traces, no natural-language citation extraction, no adversarial evidence, and no human-reviewed real task corpus. Runtime was a short CPU-only local run, not a broad deployment validation.

## Claim scope

In a deterministic synthetic trace harness, an append-only evidence ledger validator detects injected provenance, contradiction, action-precondition, tampering, and final-answer faults that final-answer-only checks miss, with zero clean false positives over 35000 generated traces.

## Why it stopped

No-paper closure: this run provides synthetic mechanism evidence and a reproducible harness, but not direct live-agent validation.

## Recommended next action

Run a bounded deepen follow-up on real local agent/tool traces with oracle or human labels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate evidence-ledger fault detection on real local agent traces
- Success threshold: At least 80% recall on labeled non-final-answer reliability faults and below 5% false-positive rate on clean real traces, with better recall than final-answer-only checking.
- Stop condition: Stop as negative if ledger recall is below 50%, clean false-positive rate exceeds 10%, or most real traces cannot produce auditable ledger fields without manual reconstruction.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-harness-on-cpu-4b2d655e6e8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
