# Live-agent false-premise contradiction flag benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-agent-false-premise-contradiction-flag-benchmark-96cd1fead3`
Run ID: `live-agent-false-premise-contradiction-flag-benchmark-96cd1fead3-20260630T035012509938+0000`

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

- Parent run decision: False-Premise Injection Harness: Contradiction-Flag Rate by Agent Class: enoch://control-plane/projects/false-premise-injection-harness-contradiction-flag-rate-by-agent-class-a9d8b431cfa8/runs/false-premise-injection-harness-contradiction-flag-rate-by-agent-class-a9d8b431cfa8-20260630T032951993256+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fb5311bfaa9a

## What looked useful

The run produced a reusable local benchmark harness, labeled replay tasks, deterministic baselines, category metrics, and failure cases showing alias handling and stale-fact retrieval as key failure modes for contradiction flags.

## Boundaries and scale limits

This was not live LLM evaluation. Claims and prior facts were provided as structured fields, the dataset was small and synthetic, and no raw-dialogue extraction, model variability, tool-use behavior, or production retrieval noise was tested.

## Claim scope

In a 16-task structured synthetic replay suite, false-premise contradiction flagging improved when memory retained latest entity facts, alias links, and an explicit contradiction-flag doctrine; layered_doctrine_memory reached 1.000 F1 versus 0.000 for no_memory, 0.778 for transcript_search, and 0.824 for flat_retrieval.

## Why it stopped

Closed as no-paper useful signal because the evidence is a structured synthetic/proxy benchmark, not full live-agent validation.

## Recommended next action

Run a bounded live-agent deepen test using these same task families as raw dialogue prompts with at least two LLM agents, blinded labels, and the same flag/fact-match scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM false-premise contradiction flag replay
- Success threshold: At least 0.80 false-premise flag F1, at least 0.75 contradicted-fact match rate, no more than 0.10 false-positive rate on true-premise controls, and at least 0.15 F1 improvement over transcript-only prompting.
- Stop condition: Stop if both tested LLMs score below 0.65 F1 with memory-plus-doctrine prompting or if false-positive rate on true-premise controls exceeds 0.20.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-false-premise-contradiction-flag-benchmark-96cd1fead3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
