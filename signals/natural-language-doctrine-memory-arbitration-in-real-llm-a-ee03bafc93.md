# Natural-language doctrine memory arbitration in real LLM agents

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `natural-language-doctrine-memory-arbitration-in-real-llm-a-ee03bafc93`
Run ID: `natural-language-doctrine-memory-arbitration-in-real-llm-a-ee03bafc93-20260619T103531490585+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Operator-Doctrine Memory: Layered Agent Memory Beyond Facts: enoch://control-plane/projects/operator-doctrine-memory-layered-agent-memory-beyond-facts-506f8cb73a07/runs/operator-doctrine-memory-layered-agent-memory-beyond-facts-506f8cb73a07-20260619T101703368618+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/06fb855ec8bb

## What looked useful

Baseline accuracy was 67/72 exact answer codes (93.06%) versus 64/72 (88.89%) with doctrine. Recency and specificity conflicts were solved perfectly by both conditions; authority conflicts degraded from 19/24 baseline to 16/24 with doctrine.

## Boundaries and scale limits

Single 3B instruction model, synthetic fictional memory snippets, deterministic single-turn prompts, compact JSON answers, no persistent memory store, no tool retrieval, no human-authored histories, and no larger multi-model benchmark.

## Claim scope

In a controlled Tier 1 direct test using Qwen/Qwen2.5-3B-Instruct on 24 fictional conflicting-memory cases, a prompt-only natural-language arbitration doctrine did not improve exact memory-answer selection over a no-doctrine memory-using baseline.

## Why it stopped

Tier 1 controlled direct evidence did not support the prompt-only natural-language doctrine improvement hypothesis; the result is not a full validation of all doctrine-memory arbitration designs.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should compare prompt-only doctrine against structured metadata or retrieval-time arbitration on authority-vs-recency conflicts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured authority arbitration versus prompt-only doctrine for conflicting LLM memories
- Success threshold: Structured pre-arbitration improves exact answer-code accuracy by at least 10 percentage points over both no-doctrine and prompt-only doctrine conditions on authority conflicts, with no degradation on recency or specificity controls.
- Stop condition: Stop if structured pre-arbitration fails to beat both prompt baselines on authority conflicts or introduces any measurable degradation on recency/specificity controls.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-doctrine-memory-arbitration-in-real-llm-a-ee03bafc93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
