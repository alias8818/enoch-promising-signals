# Falsifiable Decision Traces for Agent Trust

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `falsifiable-decision-traces-for-agent-trust-0b128f0c15cb`
Run ID: `falsifiable-decision-traces-for-agent-trust-0b128f0c15cb-20260610T053000399206+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/313a4d193b87

## What looked useful

Falsifiable traces are useful only when their checkable claims cover the relevant failure mode. Local edge/arithmetic checks caught arithmetic and invalid-edge errors but accepted 100% of locally coherent suboptimal paths; adding a global optimality check caught those failures in this task family.

## Boundaries and scale limits

Synthetic graph tasks only; no natural-language trace parsing, real LLM/tool agents, human trust calibration, adversarially optimized traces, or deployment-scale workflows were tested.

## Claim scope

On synthetic random weighted-DAG shortest-path decisions with structured trace fields, mechanically checked falsifiable trace claims improved trust filtering over confidence and rationale-length baselines; strong checks that included an optimality claim achieved 100% accepted-decision accuracy in the 5,000-decision run.

## Why it stopped

No-paper closure: this run produced a synthetic useful signal, not direct publication-grade evidence for agent trust in real LLM or human-facing settings.

## Recommended next action

Run a bounded direct-evidence follow-up using real LLM/tool agents on programmatic tasks with parsed checkable trace claims, confidence/rationale baselines, and coherent-wrong plus omitted-trace controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parsed falsifiable traces for real LLM programmatic decisions
- Success threshold: Strong falsifiable traces improve accepted-decision accuracy by at least 15 percentage points over confidence-only filtering at comparable or better incorrect-decision recall, with parse failures below 20%.
- Stop condition: Stop if trace parsing fails on more than 40% of outputs or strong trace checks do not improve accepted-decision accuracy by at least 5 percentage points over confidence-only filtering.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-decision-traces-for-agent-trust-0b128f0c15cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
