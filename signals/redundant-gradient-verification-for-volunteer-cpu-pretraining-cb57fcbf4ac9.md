# Redundant Gradient Verification for Volunteer CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `redundant-gradient-verification-for-volunteer-cpu-pretraining-cb57fcbf4ac9`
Run ID: `redundant-gradient-verification-for-volunteer-cpu-pretraining-cb57fcbf4ac9-20260613T173511992852+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6380573564f9

## What looked useful

Always-duplicate verification reached 0.000 corrupted accept rate and 0.000 clean false reject rate at 2.00x gradient-evaluation overhead; triplicate majority did the same for one bad replica at 3.00x; 20% auditing left about 77% of corruptions accepted; two colluding bad replicas caused 100% corrupted acceptance.

## Boundaries and scale limits

No transformer, GPT-2-class model, distributed optimizer, heterogeneous volunteer CPU fleet, network scheduler, secure identity, straggler, or cross-architecture floating-point nondeterminism was tested.

## Claim scope

In a small deterministic NumPy logistic-regression proxy, independent redundant recomputation detected injected single-replica gradient corruptions across five attack modes, while probabilistic auditing only detected its sampled fraction and colluding redundant replicas defeated majority voting.

## Why it stopped

Stopped after a bounded proxy useful-signal result; this is not direct/full volunteer pretraining validation and is not paper-ready.

## Recommended next action

Run a bounded transformer-scale follow-up with scheduler-randomized duplicate assignment and anti-collusion controls before treating redundant verification as viable for volunteer pretraining.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Scheduler-randomized redundant verification on a small transformer training loop
- Success threshold: Across at least three seeds, sampled duplicate verification catches at least the configured audit fraction of independent corruptions, always-duplicate catches at least 99% of independent corruptions with less than 1% clean false rejects, and the report explicitly quantifies collusion failure modes and throughput cost.
- Stop condition: Stop if cross-worker nondeterminism produces more than 1% clean false rejects at practical tolerances, if throughput cost makes volunteer pretraining worse than trusted local training for the tested scale, or if scheduler controls cannot prevent redundant partner collusion assumptions.

## Evidence references

- Artifact root: `<local-path>/projects/redundant-gradient-verification-for-volunteer-cpu-pretraining-cb57fcbf4ac9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
