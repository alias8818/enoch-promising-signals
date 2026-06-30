# Predictive Operator Updates from Agent Trace Evidence

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `predictive-operator-updates-from-agent-trace-evidence-8c400e9185a6`
Run ID: `predictive-operator-updates-from-agent-trace-evidence-8c400e9185a6-20260628T022203534027+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/795ee7683651

## What looked useful

At noise 0.35 across 10 seeds, trace evidence NB reached 0.3294 mean accuracy and 0.1509 mean macro-F1 versus 0.3146 accuracy and 0.0798 macro-F1 for majority/schedule baselines. The lift was stable but small, and accuracy advantage disappeared at high observation noise.

## Boundaries and scale limits

No real labeled operator-update corpus was available in the project. The evidence is synthetic/proxy-only, CPU-scale, and short-run; it does not validate production traces, human update text, or broad agent/operator workflows.

## Claim scope

In a controlled synthetic hidden-phase benchmark, rolling observable trace-event features modestly improve next operator-update-category prediction over majority and schedule-only baselines, but do not approach an oracle that knows the current hidden phase.

## Why it stopped

No-paper closure: this is a synthetic mechanism probe with modest mixed results, not direct production or human-operator evidence.

## Recommended next action

Run a bounded real-trace deepen study with timestamped operator-update labels and require trace-evidence models to beat schedule, last-update, and simple sequence baselines by at least 5 absolute macro-F1 points on held-out traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of operator update prediction from observable agent events
- Success threshold: Trace-evidence model improves held-out macro-F1 by >=0.05 absolute over every non-oracle baseline while maintaining non-degenerate per-class recall for blocked, verifying, and deciding.
- Stop condition: Stop if labels cannot be obtained locally, if trace-evidence lift is <0.03 macro-F1 over baselines, or if predictions collapse to phase priors rather than event evidence.

## Evidence references

- Artifact root: `<local-path>/projects/predictive-operator-updates-from-agent-trace-evidence-8c400e9185a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
