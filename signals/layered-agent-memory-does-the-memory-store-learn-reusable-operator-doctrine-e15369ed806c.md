# Layered agent memory: does the memory store learn reusable operator doctrine?

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-agent-memory-does-the-memory-store-learn-reusable-operator-doctrine-e15369ed806c`
Run ID: `layered-agent-memory-does-the-memory-store-learn-reusable-operator-doctrine-e15369ed806c-20260628T223552215297+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a06f4725978c

## What looked useful

The primary shifted run over 50 seeds showed layered_stability_doctrine success 0.7515 versus flat_episodic_knn 0.2276 and random_no_memory 0.3416; stable layered beat flat by +0.5239 success rate with bootstrap 95% CI [0.5084, 0.5385]. Diagnostics show naive doctrine rules were mostly spurious among top rules, while stability-filtered rules recovered core doctrine such as noisy+external_tool -> verify_first and stateful+repeated_subgoal -> cache.

## Boundaries and scale limits

Synthetic tasks only; explicit symbolic features; hand-coded rule induction; no real LLM agent traces, natural-language memory extraction, long-horizon planning, or production memory workload. The secondary no-shift control is not clean enough to support broad claims.

## Claim scope

In a deterministic synthetic operator-selection benchmark with shifted spurious style features, a layered memory store with cross-context stability filtering learned reusable symbolic operator-doctrine rules and outperformed flat episodic retrieval and naive rule induction on held-out tasks.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not direct/full validation of layered memory in real agents.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same stability-filtered doctrine layer on real or LLM-generated agent traces with held-out task-family shift.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Test stability-filtered operator doctrine on LLM-written agent memory traces
- Success threshold: Stability-filtered doctrine memory improves held-out operator-choice accuracy by at least 10 percentage points and task success by at least 5 percentage points over flat episodic retrieval across at least 20 random seeds or task-family splits.
- Stop condition: Stop as negative if stability-filtered doctrine memory fails to beat flat episodic retrieval on both operator-choice accuracy and task success, or if learned rules cannot be audited as stable/reusable rather than style-specific.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-does-the-memory-store-learn-reusable-operator-doctrine-e15369ed806c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
