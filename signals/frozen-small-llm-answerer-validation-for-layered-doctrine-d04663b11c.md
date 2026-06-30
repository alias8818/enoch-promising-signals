# Frozen small-LLM answerer validation for layered doctrine replay conflicts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `frozen-small-llm-answerer-validation-for-layered-doctrine-d04663b11c`
Run ID: `frozen-small-llm-answerer-validation-for-layered-doctrine-d04663b11c-20260621T144100423750+0000`

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

- Parent run decision: LLM-in-the-loop layered doctrine memory replay benchmark: enoch://control-plane/projects/llm-in-the-loop-layered-doctrine-memory-replay-benchmark-dc52aff568/runs/llm-in-the-loop-layered-doctrine-memory-replay-benchmark-dc52aff568-20260621T134821977045+0000
- Parent run decision: LLM answerer validation for layered doctrine memory replay conflicts: enoch://control-plane/projects/llm-answerer-validation-for-layered-doctrine-memory-replay-64062c44a4/runs/llm-answerer-validation-for-layered-doctrine-memory-replay-64062c44a4-20260621T142007881573+0000

## What looked useful

Across 10,000 tasks and 50,000 predictions, layered_doctrine_memory reached 1.00 exact accuracy versus flat_retrieval at 0.25, transcript_search at 0.00, no_memory at 0.00, and layered_no_supersession at 0.75. The +0.25 supersession ablation delta directly supports keeping explicit supersession filtering in layered memory.

## Boundaries and scale limits

The main evidence uses generated synthetic conflicts and an extractive proxy answerer. The only real small-model generation probe used flan-t5-small on 4 tasks and showed poor output-format reliability plus slow CPU throughput, so this is not a broad validation of frozen small LLM behavior.

## Claim scope

In a fixed-seed synthetic replay-conflict benchmark with a deterministic frozen extractive answerer, layered doctrine memory eliminated stale and lower-priority doctrine-token picks and outperformed transcript-search, flat-retrieval, no-memory, and no-supersession controls.

## Why it stopped

The mechanism signal is strong in the controlled synthetic benchmark, but the main result is proxy-based and the flan-t5-small probe was too small and unreliable for publication-grade frozen small-LLM validation.

## Recommended next action

Stop this run as no-paper useful evidence; run one bounded deepen follow-up with a prompt-constrained frozen small model and a human-authored replay corpus before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-constrained frozen small-model replay validation for layered doctrine memory
- Success threshold: Layered doctrine memory improves exact accuracy by at least 0.20 over flat retrieval and at least 0.10 over layered_no_supersession while reducing stale plus lower-priority picks below 0.10 on the curated corpus.
- Stop condition: Stop if the constrained frozen model cannot achieve at least 0.70 exact accuracy on oracle contexts or if layered memory fails to beat flat retrieval by 0.10 on the first 100 curated tasks.

## Evidence references

- Artifact root: `<local-path>/projects/frozen-small-llm-answerer-validation-for-layered-doctrine-d04663b11c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
