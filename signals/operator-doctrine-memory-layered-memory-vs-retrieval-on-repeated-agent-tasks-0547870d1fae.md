# Operator-Doctrine Memory: Layered Memory vs Retrieval on Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-layered-memory-vs-retrieval-on-repeated-agent-tasks-0547870d1fae`
Run ID: `operator-doctrine-memory-layered-memory-vs-retrieval-on-repeated-agent-tasks-0547870d1fae-20260620T100357176864+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c84521348d45

## What looked useful

Layered doctrine memory reached 0.9857 static post-warmup accuracy versus 0.9850 for keyed retrieval and 0.5927 for lexical retrieval. In the drift regime it reached 0.9006 post-drift accuracy versus 0.7513 for keyed retrieval and 0.5466 for lexical retrieval, while using 2.52 mean context items versus 2.81 for keyed retrieval and 3.99 for lexical retrieval.

## Boundaries and scale limits

The run used synthetic tasks only: 800 episodes, 40 seeds, 12 operators, 8 domains, 4 action options, and two regimes. It did not test live agents, LLM prompt execution, embedding retrieval, noisy memory extraction, real operator logs, or long-horizon production workloads.

## Claim scope

In a deterministic synthetic repeated-task benchmark with normalized operator/domain keys, mixed alias prompts, fixed context slots, and preference drift, layered doctrine memory matched exact keyed episodic retrieval in static preferences and outperformed it after drift while using fewer context items.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy evidence, not direct publication-grade validation on real repeated agent tasks.

## Recommended next action

Run a bounded direct benchmark where layered, keyed episodic, and embedding retrieval policies feed actual agent or local LLM prompts on repeated operator-preference tasks with noisy memory extraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Agent-Prompt Benchmark for Layered Operator Doctrine Memory
- Success threshold: Layered doctrine memory improves post-drift task success by at least 10 percentage points over keyed episodic retrieval and uses no more context items on average across at least 20 seeds or equivalent repeated-task traces.
- Stop condition: Stop if layered memory fails to beat keyed episodic retrieval by 5 percentage points post-drift or requires more context items than keyed retrieval in the direct agent-prompt benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-layered-memory-vs-retrieval-on-repeated-agent-tasks-0547870d1fae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
