# LLM-in-the-loop layered doctrine memory replay benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-in-the-loop-layered-doctrine-memory-replay-benchmark-dc52aff568`
Run ID: `llm-in-the-loop-layered-doctrine-memory-replay-benchmark-dc52aff568-20260621T134821977045+0000`

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

- Parent run decision: Agent memory architecture: layered operator-doctrine vs flat retrieval: enoch://control-plane/projects/agent-memory-architecture-layered-operator-doctrine-vs-flat-retrieval-3531b9e27832/runs/agent-memory-architecture-layered-operator-doctrine-vs-flat-retrieval-3531b9e27832-20260621T125842067808+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f2726222032

## What looked useful

Layered doctrine memory reached 16/16 exact selections with zero layered failures; best baseline was transcript_search at 8/16, giving a 0.50 absolute margin over the best control.

## Boundaries and scale limits

Small synthetic Tier 1 mechanism test only; deterministic chooser rather than a real LLM answerer; no natural conversations, no embedding/reranker baselines, no multi-seed generated task suite, and no publication-grade robustness validation.

## Claim scope

In a 16-task controlled synthetic replay fixture, a status-aware layered doctrine memory selector chose the correct active memory under layer-precedence, stale-supersession, noisy-metadata, and session-override conflicts more reliably than no-memory, transcript-search, and flat lexical retrieval controls.

## Why it stopped

No-paper closure: the Tier 1 mechanism signal is positive, but the run did not directly validate LLM-in-the-loop behavior or broader naturalistic replay robustness.

## Recommended next action

Run a bounded deepen follow-up with an actual small or API LLM answerer on held-out paraphrased replay tasks using the same conflict families and compare against embedding/reranker retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM answerer validation for layered doctrine memory replay conflicts
- Success threshold: Layered LLM condition achieves >=0.80 exact-match accuracy, >=0.15 absolute margin over the best retrieval baseline, and <=5 stale/superseded-memory failures on the held-out suite.
- Stop condition: Stop if layered LLM accuracy is <0.70, margin over best baseline is <0.05, or stale/superseded failures exceed 10 percent of tasks.

## Evidence references

- Artifact root: `<local-path>/projects/llm-in-the-loop-layered-doctrine-memory-replay-benchmark-dc52aff568`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
