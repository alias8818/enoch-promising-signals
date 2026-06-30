# Predictive Operator Updates: Anticipating Repeated Task Needs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `predictive-operator-updates-anticipating-repeated-task-needs-64ebaefc6111`
Run ID: `predictive-operator-updates-anticipating-repeated-task-needs-64ebaefc6111-20260610T235652091785+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9d36ccd668d

## What looked useful

Top-1 recency transition prediction improved utility per step from 0.0247 to 0.1958 at recurrence 0.65 and from 0.0695 to 0.3899 at recurrence 0.90 versus the best non-transition baseline. In the iid control, top-1 transition utility was nearly indistinguishable from frequency (-0.0313 versus -0.0326), supporting recurrence-specific rather than universal predictive value.

## Boundaries and scale limits

Evidence is synthetic and label-level only. It does not validate real operator behavior, natural-language update quality, trust effects, latency savings, or production task traces. Top-2 prediction was confounded by two-step horizon coverage and should not be used as mechanism-specific evidence without a stricter cost model.

## Claim scope

In a deterministic synthetic trace-replay benchmark with recurring task templates, top-1 transition-based predictive updates anticipated near-future operator needs better than reactive or frequency-only baselines when recurrence was moderate to high, while showing no meaningful advantage in the iid control.

## Why it stopped

Closed as no-paper useful signal because the supporting evidence is a controlled synthetic proxy, not direct validation on real operator workflows.

## Recommended next action

Run a bounded deepen study on real or semi-real operator task traces with labeled next needs and a calibrated false-positive cost model before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replay Validation of Predictive Operator Updates on Real Task Logs
- Success threshold: At least 20% utility-per-step improvement over the strongest non-transition baseline on held-out traces, with false-positive rate no more than 10% above baseline and loss of advantage under shuffled-order control.
- Stop condition: Stop if transition prediction fails to beat the strongest non-transition baseline by 10% utility on held-out traces or if shuffled controls retain the same advantage, indicating the effect is not driven by repeated task structure.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-updates-anticipating-repeated-task-needs-64ebaefc6111`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
