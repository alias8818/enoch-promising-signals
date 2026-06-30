# Live-agent repeated dev-task replay for operator-doctrine memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-agent-repeated-dev-task-replay-for-operator-doctrine-393e1e7445`
Run ID: `live-agent-repeated-dev-task-replay-for-operator-doctrine-393e1e7445-20260619T120430510134+0000`

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

- Parent run decision: Operator-Doctrine Memory vs Retrieval-Only on Repeated Dev Tasks: enoch://control-plane/projects/operator-doctrine-memory-vs-retrieval-only-on-repeated-dev-tasks-baf3f4411e5f/runs/operator-doctrine-memory-vs-retrieval-only-on-repeated-dev-tasks-baf3f4411e5f-20260619T112232286451+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cfd9f4a57e07

## What looked useful

Layered doctrine memory reached 1.000 exact match and zero stale/distractor leaks versus 0.375 exact match and 6 stale/distractor leaks for flat retrieval, and 0.000 exact match with 16 leaks for transcript search.

## Boundaries and scale limits

Synthetic small task set; deterministic retrieval-only agent; no live LLM repository execution; no held-out human-authored replay corpus; not a broad validation.

## Claim scope

In an 8-task deterministic repeated dev-task replay with doctrine updates and distractors, layered operator-doctrine memory improved active-doctrine retrieval over no memory, transcript search, and flat retrieval.

## Why it stopped

Tier 1 controlled direct replay met its mechanism threshold but remains synthetic retrieval evidence, not full validation or paper-ready evidence.

## Recommended next action

Run a bounded live-agent replay in disposable repos using the same doctrine/update patterns and score final actions against the active doctrine.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent repo replay for layered operator-doctrine memory
- Success threshold: Layered memory improves final-action active-doctrine compliance by at least 0.15 over the best non-layered baseline and has no more than half the stale/distractor leakage rate of flat retrieval.
- Stop condition: Stop if layered memory fails to beat the best baseline on compliance or introduces equal/higher stale leakage after the full bounded task set.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-repeated-dev-task-replay-for-operator-doctrine-393e1e7445`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
