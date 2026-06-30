# Anchor-Checkpointed Sliding Window with Exact Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-checkpointed-sliding-window-with-exact-retrieval-9465bea468eb`
Run ID: `anchor-checkpointed-sliding-window-with-exact-retrieval-9465bea468eb-20260525T190220954628+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/909231ce1912

## What looked useful

Exact retrieval restores long-range recall under a bounded active window, but the method pays substantial index/checkpoint/cache overhead and was slower than a simple in-memory exact-index baseline on the tested associative lookup task.

## Boundaries and scale limits

Tested only CPU Python synthetic streams up to 20k events and 3,999 queries per seed. Not tested inside transformer attention, natural-language tasks, learned retrieval routing, GPU serving, million-token contexts, or production storage/index implementations.

## Claim scope

On a synthetic long-range associative lookup stream with repeated updates, an anchor-checkpointed sliding window with an exact key-to-checkpoint index preserved 100% recall across three 20k-event seeds while a 512-event sliding window reached about 9.7% accuracy because about 95% of queries were outside the active window.

## Why it stopped

Synthetic bounded evidence supports the mechanism but not a paper-ready claim; the full-index control is faster and smaller for simple associative recall, and model-side evidence is absent.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should integrate exact checkpoint retrieval with a toy transformer or long-context QA harness and compare against sliding-window attention plus a simple retrieval/index control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Toy Transformer Anchor-Checkpoint Retrieval Probe
- Success threshold: Anchor-checkpoint retrieval achieves at least 95% out-of-window accuracy and no more than 2 percentage points in-window accuracy loss versus the exact retrieval control, while using less active context than full-context attention.
- Stop condition: Stop if anchor retrieval fails to exceed sliding-window out-of-window accuracy by at least 50 percentage points, if stale-update errors exceed 5%, or if simple exact retrieval dominates on all measured axes with no model-side benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-checkpointed-sliding-window-with-exact-retrieval-9465bea468eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
