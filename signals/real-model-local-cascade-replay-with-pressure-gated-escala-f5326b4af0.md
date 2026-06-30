# Real-Model Local Cascade Replay With Pressure-Gated Escalation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-local-cascade-replay-with-pressure-gated-escala-f5326b4af0`
Run ID: `real-model-local-cascade-replay-with-pressure-gated-escala-f5326b4af0-20260528T173440985968+0000`

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

- Parent run decision: Real Local-Serving Replay for Pressure-Gated Cascade Routing: enoch://control-plane/projects/real-local-serving-replay-for-pressure-gated-cascade-routi-6ff404cd1c/runs/real-local-serving-replay-for-pressure-gated-cascade-routi-6ff404cd1c-20260528T151223810789+0000
- Parent run decision: Pressure-Gated Cascade Routing for Local Serving: enoch://control-plane/projects/pressure-gated-cascade-routing-for-local-serving-f3ca80d30a7e/runs/pressure-gated-cascade-routing-for-local-serving-f3ca80d30a7e-20260528T112953612209+0000

## What looked useful

Pressure replay reached mean NLL 3.9609 versus 4.4482 small-only and 4.1331 random same-budget gating. Replay reduced large-call rate from 0.3009 for pressure-no-replay to 0.1003 with identical NLL on the repeated stream. Large-only remained much better at NLL 3.3165, so the result is mechanism support, not paper readiness.

## Boundaries and scale limits

Tested only 3 fixed seeds, 360 unique prompts per seed repeated 3x, 70M/410M causal LMs, exact prompt replay, and next-token NLL. It does not validate end-task answer quality, semantic replay, production latency, larger instruction-tuned models, or long-running serving.

## Claim scope

On a Wikitext-2 repeated next-token serving workload with local Pythia-70M/Pythia-410M models, entropy pressure gating improves NLL versus small-only and same-budget random gating, and exact replay reduces large-model calls on repeated high-pressure prompts without changing NLL.

## Why it stopped

Tier-2 local evidence supports the mechanism but remains bounded to next-token NLL and exact replay, with a large residual quality gap to large-only.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same pressure-replay mechanism on a real downstream QA or reasoning benchmark with answer accuracy, semantic replay, and latency measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Downstream Accuracy Test for Pressure-Gated Semantic Replay
- Success threshold: Pressure semantic replay must retain at least 95% of large-only task accuracy or F1 while reducing large-model calls by at least 50% versus large-only and beating same-budget random gating across all fixed seeds.
- Stop condition: Stop if pressure gating fails to beat same-budget random gating on task accuracy/cost in at least two of three seeds, or if replay introduces more than a 1 percentage point absolute correctness drop versus pressure-no-replay.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-local-cascade-replay-with-pressure-gated-escala-f5326b4af0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
