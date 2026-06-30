# Counterexample-Disciplined Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `counterexample-disciplined-agent-evidence-ledger-8bc4102c2a77`
Run ID: `counterexample-disciplined-agent-evidence-ledger-8bc4102c2a77-20260610T123830514984+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5322e31cb5c

## What looked useful

Counterexample discipline can suppress overclaiming in noisy/adversarial evidence streams, but fixed penalties require calibration; otherwise recall and overall decision quality can collapse.

## Boundaries and scale limits

Synthetic proxy only: 30 seeds, 3 regimes, 2000 tasks per regime per seed, 16 evidence items per task. No real LLM agents, natural-language extraction, human evaluation, or threshold-matched ROC/PR sweep.

## Claim scope

In a synthetic noisy binary hypothesis-evaluation benchmark, an unresolved-counterexample penalty reduced false-positive support claims and improved precision, but mainly by becoming conservative and losing many true positives versus a balanced evidence ledger.

## Why it stopped

Bounded proxy produced a useful mixed signal but not direct or publication-grade evidence; finalize as no-paper evidence.

## Recommended next action

Run a threshold-matched ROC/PR deepen study on synthetic tasks and then a small real agent trace benchmark before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Threshold-Matched Counterexample Ledger Operating Curves
- Success threshold: Counterexample-ledger policy achieves at least 5 percentage points higher precision than both baselines at matched recall >= 0.50, without more than 10 percentage points higher abstention, and repeats on a small real trace benchmark.
- Stop condition: Stop if the threshold sweep shows the counterexample policy is Pareto-dominated by either baseline or if gains appear only at recall below 0.30.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-disciplined-agent-evidence-ledger-8bc4102c2a77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
