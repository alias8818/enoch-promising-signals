# Anchor-Indexed Compressed State for Agent Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-compressed-state-for-agent-memory-7fe3ab239bdc`
Run ID: `anchor-indexed-compressed-state-for-agent-memory-7fe3ab239bdc-20260527T203553962041+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a2aefe682a45

## What looked useful

Compression into latest fact slots is useful, but anchor indexing alone was not a meaningful accuracy improvement over global compressed key-value memory in this probe.

## Boundaries and scale limits

CPU-only synthetic traces; no LLM summarization, embedding retrieval, entity-resolution noise, real agent task outcomes, or production-scale memory pressure were tested.

## Claim scope

On synthetic interleaved agent-session traces with exact anchor labels and fixed fact-slot budgets, anchor-indexed compressed state improves retrieval accuracy and latency over recent-window memory but does not improve accuracy over a simpler global compressed key-value LRU baseline.

## Why it stopped

Synthetic proxy evidence was mixed: anchor-indexed memory beat recent-window memory but failed to beat the stronger global compressed-state baseline, so the current novelty claim is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; any follow-up should test whether anchor indexing helps under realistic noisy entity resolution and natural-language summarization errors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Entity-Resolution Test for Anchor-Indexed Agent Memory
- Success threshold: At least a 5 percentage point paired exact-answer accuracy gain over global compressed key-value memory with no worse than equal false-merge rate at two or more memory budgets.
- Stop condition: Stop if anchor indexing fails to exceed global compressed key-value memory by 2 percentage points on a 3-seed pilot or if entity-resolution errors dominate all methods equally.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-compressed-state-for-agent-memory-7fe3ab239bdc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
