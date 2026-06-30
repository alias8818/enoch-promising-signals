# Small-corpus suffix-index prompt lookup decoding ablation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-corpus-suffix-index-prompt-lookup-decoding-ablation-0a10618275`
Run ID: `small-corpus-suffix-index-prompt-lookup-decoding-ablation-0a10618275-20260605T155905178415+0000`

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

- Parent run decision: Prompt Lookup Decoding with Suffix Cache: enoch://control-plane/projects/prompt-lookup-decoding-with-suffix-cache-cc2712f10e5c/runs/prompt-lookup-decoding-with-suffix-cache-cc2712f10e5c-20260605T045231100342+0000
- Parent run decision: End-to-end small-model prompt lookup decoding with suffix index: enoch://control-plane/projects/end-to-end-small-model-prompt-lookup-decoding-with-suffix-be1d387128/runs/end-to-end-small-model-prompt-lookup-decoding-with-suffix-be1d387128-20260605T120254068998+0000

## What looked useful

Suffix indexing removes naive prompt-lookup scan overhead without changing proposals, but the tested exact small-corpus lookup heuristic has low accepted-token yield on held-out continuation. Improving continuation selection appears more important than further optimizing exact lookup.

## Boundaries and scale limits

Model-free retrieval/proposal benchmark only; no target language model wall-clock decoding, no GPU serving path, one corpus, 80k tokens, draft length 4, max suffix length 8.

## Claim scope

On an 80k-token small real text corpus with 3 fixed seeds and 4,500 held-out contexts, a suffix index exactly reproduced naive longest-suffix prompt-lookup proposals while reducing retrieval latency by about 14,151x; the exact lookup heuristic itself produced only about 1.123x idealized target-call speedup.

## Why it stopped

Medium fixed-seed ablation supports the suffix-index mechanism but not a publication-grade decoding claim: exact lookup speed is excellent, while direct accepted-token and ideal target-call metrics remain modest.

## Recommended next action

Stop this run as no-paper useful-signal evidence; if pursued, run a bounded model-in-the-loop follow-up focused on the frequency tie-break continuation selector versus exact longest-suffix lookup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop frequency tie-break prompt lookup decoding
- Success threshold: Frequency tie-break suffix lookup achieves at least 1.20x wall-clock decoding throughput over no lookup and at least 1.10x over exact suffix-index lookup at comparable output quality across all fixed seeds.
- Stop condition: Stop if frequency tie-break fails to exceed exact suffix-index lookup by 5% wall-clock throughput or if quality parity fails on any fixed-seed condition.

## Evidence references

- Artifact root: `<local-path>/projects/small-corpus-suffix-index-prompt-lookup-decoding-ablation-0a10618275`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
