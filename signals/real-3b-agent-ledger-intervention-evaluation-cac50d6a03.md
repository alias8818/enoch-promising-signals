# Real 3B Agent Ledger Intervention Evaluation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-3b-agent-ledger-intervention-evaluation-cac50d6a03`
Run ID: `real-3b-agent-ledger-intervention-evaluation-cac50d6a03-20260529T185843282670+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Safe Tool-Use Ledger for 3B Agent: enoch://control-plane/projects/safe-tool-use-ledger-for-3b-agent-3facbe29863f/runs/safe-tool-use-ledger-for-3b-agent-3facbe29863f-20260529T144731044873+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f20cb0e4924a

## What looked useful

The pre-set success threshold was not met: baseline accuracy 1/40, ledger accuracy 1/40, accuracy delta 0.000, JSON validity 40/40 for both conditions. Paired analysis found one baseline-only correct, one ledger-only correct, and 38 neither-correct pairs.

## Boundaries and scale limits

Single 3B-class model, single prompt family, deterministic synthetic ledger-state task family, 40 paired tasks, greedy decoding, and a strong floor effect with both conditions at 1/40 accuracy. Does not cover tool use, multi-turn autonomous agents, longer real-world ledgers, or other model families.

## Claim scope

On Qwen/Qwen2.5-3B-Instruct, an internal ledger prompt intervention did not improve exact final-balance accuracy over a baseline prompt on 40 deterministic 7-12 event ledger-state tasks with identical compact JSON output requirements.

## Why it stopped

Controlled small direct test on a real 3B model failed the pre-set ledger-intervention threshold; this is an early direct falsification for the scoped task/model/prompt slice, not a full validation or broad rejection.

## Recommended next action

Stop this run as a scoped no-paper negative/useful-signal result; a future bounded retry should first calibrate ledger-task difficulty so baseline accuracy is not at floor.

## Follow-up

- Recommended: `true`
- Type: `retry`
- Title: Difficulty-Calibrated 3B Ledger Intervention Retry
- Success threshold: Baseline accuracy must be 30-70% on the selected difficulty band, and ledger accuracy must exceed baseline by at least 10 percentage points with JSON validity delta no worse than -5 percentage points.
- Stop condition: Stop as negative if no tested difficulty band reaches at least 30% baseline accuracy, if ledger improvement is under 5 percentage points on calibrated tasks, or if JSON validity drops by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/real-3b-agent-ledger-intervention-evaluation-cac50d6a03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
