# Gradient Correlation Puzzle for CPU-Verifiable Volunteer Work

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-correlation-puzzle-for-cpu-verifiable-volunteer-work-73e8eab69ed1`
Run ID: `gradient-correlation-puzzle-for-cpu-verifiable-volunteer-work-73e8eab69ed1-20260609T042315334328+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4890047f9ba5

## What looked useful

Verifier cost was cheap, around 4.2% of worker aggregate time, but the mechanism failed: at alpha=0.0 and K=128 honest pass was 0.915 while replay pass was 0.950 and a reusable 65536-sample template passed 1.000; at alpha=1.0 honest pass collapsed to random-like rates around 0.01.

## Boundaries and scale limits

Evidence is CPU-only and synthetic: d=512 logistic regression, N=4096 worker samples, K=32-256 verifier samples, 200 main trials per condition, plus a 65536-sample reusable-template attack. Real training tasks, cryptographic protocol binding, and adaptive adversaries were not tested.

## Claim scope

For a correlation-only gradient puzzle in synthetic logistic regression, cheap verifier cosine checks either measure a reusable population-gradient direction or fail when the expected gradient is near zero; they do not reliably verify nonce-specific volunteer work.

## Why it stopped

Bounded proxy early falsification: the verifier accepts replay/template aggregates when the expected gradient is strong, and cannot distinguish honest work when the expected gradient is weak.

## Recommended next action

Stop this correlation-only puzzle line as non-viable; a separate bounded branch should test nonce-bound gradient sketches rather than fresh-sample population correlation.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Nonce-bound gradient sketch puzzle
- Success threshold: At K<=256 equivalent verifier work, honest pass >=0.90 and replay/template/12.5%-partial pass <=0.05 in at least 200 trials per condition.
- Stop condition: Stop negative if nonce-bound sketching either costs more than 10% of worker compute at target settings or any reusable-template/replay attack passes above 0.10.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-correlation-puzzle-for-cpu-verifiable-volunteer-work-73e8eab69ed1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
