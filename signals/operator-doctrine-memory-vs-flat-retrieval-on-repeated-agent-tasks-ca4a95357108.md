# Operator-Doctrine Memory vs Flat Retrieval on Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-ca4a95357108`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-ca4a95357108-20260621T145133593620+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/66dd9f608611

## What looked useful

Across 30 seeds and 5,000 episodes, doctrine memory beat flat retrieval by +0.049 mean reward and +0.051 accuracy at the final checkpoint, with 27/30 positive paired seeds, 256.7x lower choice latency, and 55.6x fewer memory items. Early adaptation was stronger: at 250 episodes doctrine beat flat by +0.139 reward and +0.136 accuracy in 30/30 seeds.

## Boundaries and scale limits

The evidence is synthetic and proxy-only: no real LLM agents, no human-authored operator doctrine, no semantic embedding retrieval, no long-horizon tool workflows, and no production indexing. The flat baseline is literal episodic retrieval, so the latency gap should not be treated as a universal retrieval-system result.

## Claim scope

In a synthetic online repeated-task benchmark with sparse latent family/context/action doctrine, compact doctrine statistics outperformed unindexed flat episodic nearest-neighbor retrieval on cumulative reward, best-action accuracy, memory footprint, and choice latency.

## Why it stopped

Useful bounded synthetic signal produced, but it is proxy-only and not sufficient for a paper or broad claim about real agent memory systems.

## Recommended next action

Run a bounded deepen follow-up on real or LLM-generated repeated agent traces comparing learned doctrine summaries against indexed semantic retrieval under matched token and storage budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Doctrine summaries vs indexed semantic retrieval on repeated agent traces
- Success threshold: Doctrine memory beats indexed retrieval by at least 5 percentage points on held-out task success or feedback-aligned action accuracy while using no more than half the retrieval tokens/storage, across at least 20 seeds or task batches.
- Stop condition: Stop if doctrine summaries fail to beat indexed retrieval on task success/accuracy or if gains disappear after matching token/storage budgets.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-ca4a95357108`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
