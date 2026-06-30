# Distilled Quality Gate for Home-Local Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `distilled-quality-gate-for-home-local-cascade-e3af4a7e3729`
Run ID: `distilled-quality-gate-for-home-local-cascade-e3af4a7e3729-20260613T084143221245+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/22a04b86cca6

## What looked useful

The mechanism is useful: local model confidence/logit/entropy/span features can route low-quality answers and reduce escalation versus always-remote. The learned gate achieved held-out AUC 0.8422 and reached a post-hoc 0.95 final-F1 frontier with 22.02% escalation, compared with 26.76% for a single-feature confidence gate. The margin over confidence is too modest and the proxy setting too narrow for a paper-positive decision.

## Boundaries and scale limits

This is a bounded extractive-QA proxy. Escalation used oracle gold answers, not a real remote model. It did not test a home-local generative assistant, human preference quality, factuality, latency, production cost, domain shift, or multi-seed robustness.

## Claim scope

On a seeded 4,096-example SQuAD validation subset with a DistilBERT extractive local QA model, a lightweight learned gate using local-output features improved oracle-cascade final F1 from a local-only 0.8655 to 0.9583 while escalating 25.34% of held-out requests.

## Why it stopped

Bounded local evidence supports the routing mechanism but not a publication-grade distilled quality gate for home-local cascades; the strongest evidence is an extractive-QA oracle-escalation proxy.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a bounded generative-cascade test that uses a real local instruction model, a reproducible stronger fallback or teacher, and a predeclared margin over confidence gating.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Generative local-assistant quality gate versus confidence baseline
- Success threshold: Achieve at least 0.90 held-out final judged quality with at least 5 percentage points lower escalation than the best simple confidence/self-score gate at matched quality.
- Stop condition: Stop if the learned gate fails to beat the best simple gate by at least 3 percentage points escalation at matched quality on the first held-out generative evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/distilled-quality-gate-for-home-local-cascade-e3af4a7e3729`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
