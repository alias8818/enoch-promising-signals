# Layered agent memory: anchors + compressed episodic + semantic operator

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-anchors-compressed-episodic-semantic-operator-1fb37f8df844`
Run ID: `layered-agent-memory-anchors-compressed-episodic-semantic-operator-1fb37f8df844-20260621T192442148926+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9fb28cddb478

## What looked useful

Across 5 seeds with 2400 events, 64 entities, and 480 queries per seed, the layered operator reached 1.0 overall accuracy at 7 mean context tokens/query. Flat episodic retrieval reached 0.6754, 0.7629, and 0.9563 overall accuracy at 60, 120, and 240 token budgets while using 53.22, 116.44, and 234.25 mean context tokens/query. Anchor-only solved current state but failed episodic recall, and lossy compression destroyed exact recall.

## Boundaries and scale limits

No LLM, natural user dialogue, learned compression, vector embedding retrieval, multi-session agent loop, or real-world data was tested. The operator had privileged access to a clean timestamp/query schema, so the evidence is mechanism-level synthetic evidence only.

## Claim scope

In a deterministic synthetic long-horizon memory benchmark with clean entity names, timestamps, and query schemas, a layered anchor plus compact episodic record plus semantic operator design preserved exact recall while using far fewer context tokens than flat episodic retrieval.

## Why it stopped

Stopped after a synthetic mechanism benchmark because the result is useful but not direct or broad enough for a paper-positive decision.

## Recommended next action

Run a bounded direct LLM-agent follow-up using the same memory variants on paraphrased multi-session tasks with vector retrieval and structured-state controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM-Agent Evaluation of Layered Memory Under Paraphrased Multi-Session Recall
- Success threshold: Layered memory improves overall exact-answer accuracy by at least 10 percentage points over flat vector episodic retrieval at a matched context budget, or matches accuracy while reducing mean context tokens by at least 50%, with no query type below 80% accuracy.
- Stop condition: Stop as unsupported if layered memory fails to beat flat vector retrieval on either accuracy or context-token use in two independent seeds, or if operator misrouting accounts for more than 20% of layered failures.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-anchors-compressed-episodic-semantic-operator-1fb37f8df844`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
