# Automatic Doctrine Induction from Real Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `automatic-doctrine-induction-from-real-agent-traces-124b3b657b`
Run ID: `automatic-doctrine-induction-from-real-agent-traces-124b3b657b-20260621T074531958582+0000`

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

- Parent run decision: Semantic Compression for Reusable Operator Doctrine in Agent Memory: enoch://control-plane/projects/semantic-compression-for-reusable-operator-doctrine-in-agent-memory-d05dff83b217/runs/semantic-compression-for-reusable-operator-doctrine-in-agent-memory-d05dff83b217-20260621T065842030126+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/c306aceb6219

## What looked useful

Doctrine induction should evaluate action sets or temporal action spans rather than only a single selected action. With action-set traces and an operating-action scope, hidden doctrine recovery was reliable in this controlled Tier 1 test.

## Boundaries and scale limits

No archived production Codex/Hermes traces were tested. The doctrine set was small, the trace generator was controlled, and the F1-lift threshold passed in 3/5 seeds even though doctrine recovery was 5/5 in every seed.

## Claim scope

In a controlled executable-agent setting with five hidden operating doctrines and action-set traces, a simple rule inducer with a predeclared operating-action scope recovered all doctrines across five seeds and improved held-out doctrine-action F1 over a prior baseline on the primary split.

## Why it stopped

Controlled Tier 1 mechanism evidence is useful but not publication-grade evidence for real unmanaged agent traces.

## Recommended next action

Run the same induction/evaluation protocol on a small archived natural agent-trace corpus with human-labeled doctrine expectations and held-out trace segments.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Doctrine induction on archived natural agent traces
- Success threshold: Recover at least 80% of labeled doctrines with at least 80% precision and improve held-out doctrine-action micro-F1 by at least 0.15 over the strongest baseline on at least 4/5 random splits.
- Stop condition: Stop as no-paper negative if doctrine precision or recall stays below 0.6 on two independently labeled trace subsets, or if action-set annotations are unavailable and only single final actions can be evaluated.

## Evidence references

- Artifact root: `<local-path>/projects/automatic-doctrine-induction-from-real-agent-traces-124b3b657b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
