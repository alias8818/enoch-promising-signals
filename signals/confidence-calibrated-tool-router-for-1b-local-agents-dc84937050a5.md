# Confidence-Calibrated Tool Router for 1B Local Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-calibrated-tool-router-for-1b-local-agents-dc84937050a5`
Run ID: `confidence-calibrated-tool-router-for-1b-local-agents-dc84937050a5-20260525T233641277541+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/74ed5f3bb060

## What looked useful

Temperature scaling on clean calibration prompts produced near-perfect IID accuracy/ECE, but made the router overconfident under hard/ambiguous shift. A threshold selected for <=5% calibration error yielded mean routed error of 32.3% on hard/OOD prompts and 30.9% on ambiguous/OOD prompts across five seeds.

## Boundaries and scale limits

No real 1B local model, organic agent traces, live tool loop, or human-authored adversarial set was evaluated. Evidence is a five-seed synthetic benchmark using a small transparent linear router.

## Claim scope

Synthetic early falsification of naive clean-split confidence calibration for a lightweight local-agent tool router. IID calibration worked, but confidence/error control failed on hard and ambiguous shifted routing prompts.

## Why it stopped

Proxy/early falsification rather than full validation: clean-split confidence calibration did not control OOD routed error in the synthetic benchmark, so this run should not proceed to paper writing.

## Recommended next action

Run a bounded deepen test with representative risk calibration: include ambiguous prompts and hard no-tool negatives in the calibration split, then require <=10% routed error at >=50% coverage on a held-out human-authored or independently generated routing set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Representative Risk Calibration for Local Tool Routers
- Success threshold: On held-out hard plus ambiguous prompts, routed error <=10% at >=50% coverage across at least five seeds, while IID routed error remains <=5% at >=90% coverage.
- Stop condition: Stop if representative calibration still has >20% routed error at 50% coverage or if it requires abstaining on more than 75% of shifted prompts.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-calibrated-tool-router-for-1b-local-agents-dc84937050a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
