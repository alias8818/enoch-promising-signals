# Evidence-ledger agent reliability for lane promotion decisions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-for-lane-promotion-decisions-32a2a3832c09`
Run ID: `evidence-ledger-agent-reliability-for-lane-promotion-decisions-32a2a3832c09-20260613T093751979460+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bb53858795a

## What looked useful

Naive self-report produced 280 false promotions at a 0.875 false promotion rate; the evidence-ledger gate produced 0 false promotions and 0 false rejects on the same synthetic cases.

## Boundaries and scale limits

Synthetic cases only; no live LLM agents, production telemetry, operator traces, or real lane promotion decisions were tested.

## Claim scope

In a seeded 360-case synthetic lane-promotion proxy, an evidence-ledger gate requiring present, fresh, threshold-satisfying, non-contradicted evidence eliminated seeded false promotion decisions accepted by a naive agent self-report policy.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic mechanism check, not direct production or LLM-agent reliability evidence.

## Recommended next action

Run a bounded direct-evidence follow-up using real or LLM-generated lane-promotion traces with held-out ground truth and the same pre-registered false-promotion and false-reject metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gate on LLM-generated lane-promotion traces
- Success threshold: At least 50% relative reduction in false promotions versus self-report acceptance with false reject rate under 10% on no fewer than 200 held-out direct trace cases.
- Stop condition: Stop if false-promotion reduction is below 25%, if false rejects exceed 20%, or if the corpus cannot provide auditable ground-truth labels.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-for-lane-promotion-decisions-32a2a3832c09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
