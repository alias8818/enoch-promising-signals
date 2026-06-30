# Compressed State for Long-Context Exact Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-for-long-context-exact-anchors-1af6f2a0febf`
Run ID: `compressed-state-for-long-context-exact-anchors-1af6f2a0febf-20260605T224406379253+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f9f83ddb00d4

## What looked useful

A fixed-slot compressed anchor state fails exact localization at memory-saving ratios: at roughly one slot per anchor it uses about the same bits per anchor as the exact index but recovers only about 0.36-0.38 of inserted anchors; at half a slot per anchor recall is about 0.13-0.14. Even ten slots per anchor reaches only about 0.90 recall while costing about 10x the exact index.

## Boundaries and scale limits

No language model was trained or evaluated. The run does not test semantic retrieval, tokenizer/corpus structure, neural KV compression, learned collision resolution, or GPT-2-class parameter-matched baselines. Evidence is CPU-only mechanism evidence, not publication-grade model evidence.

## Claim scope

Synthetic deterministic benchmark of exact width-8 span-anchor localization using random token contexts up to 131,072 tokens. The tested compressed state is a fixed-slot hash/fingerprint table that rejects ambiguous collision slots.

## Why it stopped

The result is not a full validation or invalidation of learned long-context architectures, but the directly tested fixed-slot compressed-state design is non-viable for exact anchors under compression.

## Recommended next action

Stop this run as a proxy/early falsification of the naive fixed-slot compressed-state mechanism; next bounded work should test a model-integrated anchor memory with explicit collision resolution against a dense baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-integrated exact-anchor memory with collision resolution
- Success threshold: At least 95 percent exact-anchor localization recall and answer exact match at a lower measured memory budget than an exact per-anchor index or full-context baseline on held-out synthetic contexts.
- Stop condition: Stop if the model-integrated variant cannot exceed 80 percent exact localization recall at memory below the exact-index budget after a small calibrated run.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-for-long-context-exact-anchors-1af6f2a0febf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
