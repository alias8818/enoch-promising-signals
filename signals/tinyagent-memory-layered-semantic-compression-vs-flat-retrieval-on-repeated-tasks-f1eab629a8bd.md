# TinyAgent Memory: Layered Semantic Compression vs Flat Retrieval on Repeated Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tinyagent-memory-layered-semantic-compression-vs-flat-retrieval-on-repeated-tasks-f1eab629a8bd`
Run ID: `tinyagent-memory-layered-semantic-compression-vs-flat-retrieval-on-repeated-tasks-f1eab629a8bd-20260619T024714147363+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9c36983d595

## What looked useful

Layered memory used 6.5% to 21.5% of flat stored tokens and 13.5% to 45.1% of flat retrieval latency. Accuracy delta was +0.03 to +0.51 percentage points when cues were intact and about -1.29 to -1.38 percentage points when 25% of stable cues were omitted, showing both compression benefit and a fragmentation failure mode.

## Boundaries and scale limits

Synthetic text tasks only; no real TinyAgent harness, learned embeddings, LLM/tool execution, production task distribution, long-context effects, or end-to-end cost measurement. Medium run covered 24 task families, 60 repeats per family, 8 seeds, and six noise/omission conditions.

## Claim scope

In a deterministic synthetic repeated-task benchmark with bag-of-words cosine retrieval, layered semantic compression preserved or slightly improved accuracy when stable semantic cues were visible and reduced stored-token footprint and retrieval latency substantially versus flat raw-trace retrieval; under 25% cue omission it saved resources but lost about 1.3 percentage points of accuracy.

## Why it stopped

No-paper closure: this run produced synthetic useful-signal evidence but not direct publication-grade TinyAgent evidence.

## Recommended next action

Run a bounded deepen follow-up in a real TinyAgent harness with embedding retrieval and repeated held-out task variants; require no more than 1 percentage point task-success loss while reducing memory tokens or retrieval cost by at least 50%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: TinyAgent layered memory with embeddings on repeated held-out task variants
- Success threshold: Layered memory reduces memory tokens or retrieval cost by at least 50% while end-to-end task success is no more than 1 percentage point below flat retrieval across the bounded task suite.
- Stop condition: Stop if layered memory loses more than 3 percentage points task success in two independent task orderings or fails to reduce memory tokens/retrieval cost by at least 25%.

## Evidence references

- Artifact root: `<local-path>/projects/tinyagent-memory-layered-semantic-compression-vs-flat-retrieval-on-repeated-tasks-f1eab629a8bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
