# Blinded live-repo replay validation for layered operator-doctrine memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `blinded-live-repo-replay-validation-for-layered-operator-d-ee4f91a741`
Run ID: `blinded-live-repo-replay-validation-for-layered-operator-d-ee4f91a741-20260619T132952366206+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Live-agent repeated dev-task replay for operator-doctrine memory: enoch://control-plane/projects/live-agent-repeated-dev-task-replay-for-operator-doctrine-393e1e7445/runs/live-agent-repeated-dev-task-replay-for-operator-doctrine-393e1e7445-20260619T120430510134+0000
- Parent run decision: Live-agent repo replay for layered operator-doctrine memory: enoch://control-plane/projects/live-agent-repo-replay-for-layered-operator-doctrine-memor-06d1b2669d/runs/live-agent-repo-replay-for-layered-operator-doctrine-memor-06d1b2669d-20260619T125801272635+0000

## What looked useful

On 3,072 generated replay cases and 18,432 strategy-case records, layered_doctrine_memory achieved 1.0000 accuracy and 0.0000 forbidden/stale/cross-scope hit rate versus flat_retrieval at 0.8200 accuracy and 0.1667 forbidden/stale/cross-scope hit rate. Paired bootstrap layered-vs-flat accuracy delta was +0.1797 with 95% interval [+0.1660, +0.1937]. Doctrine and scope ablations both reduced accuracy.

## Boundaries and scale limits

The workspace contained no real blinded live-repo trace corpus; results are synthetic and use deterministic answerers rather than a full LLM coding-agent loop. This is not publication-grade live-repo validation.

## Claim scope

In a deterministic synthetic repeated-repo replay harness with fixed seeds, scoped layered operator-doctrine memory improved replay answer accuracy and eliminated stale/cross-scope errors relative to no-memory, transcript-search, flat-retrieval, and ablated layered controls.

## Why it stopped

Paper gate failed because the scaffold supplied only placeholder data, so the validation is a synthetic mechanism test rather than direct live-repo replay evidence.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded deepening step is to rerun the same harness on an authorized blinded live-repo replay corpus with hidden oracle labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded live-repo trace replay for layered operator-doctrine memory
- Success threshold: Layered operator-doctrine memory improves accuracy over flat retrieval by >= 0.10 with 95% paired bootstrap interval lower bound > 0 and forbidden/stale/cross-scope hit rate <= flat retrieval.
- Stop condition: Stop if layered accuracy improvement over flat retrieval is < 0.05 or stale/cross-scope errors increase on the real trace corpus; otherwise report useful_signal unless the live corpus is large and diverse enough for paper-grade claims.

## Evidence references

- Artifact root: `<local-path>/projects/blinded-live-repo-replay-validation-for-layered-operator-d-ee4f91a741`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
