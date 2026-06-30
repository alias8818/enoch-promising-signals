# Compressed State Anchors for 32K Context on 6GB VRAM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `compressed-state-anchors-for-32k-context-on-6gb-vram-e664a057c19b`
Run ID: `compressed-state-anchors-for-32k-context-on-6gb-vram-e664a057c19b-20260611T192537019744+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/15286057a376

## What looked useful

Anchor ratios attractive for a 6GB-class 32K context target reduce KV memory sharply, but in a favorable within-block exact-recall probe they cause near-total collision failure: 16 anchors/block and 32 anchors/block had 0/20000 exact recalls; 64 anchors/block had 0.00020 recall; full storage control was exact.

## Boundaries and scale limits

No trained transformer, no natural-language benchmark, and no hard 6GB CUDA allocation limit were evaluated. The run was a 12.67 second CPU synthetic probe plus KV-cache memory modeling on a GB10 host with unified memory.

## Claim scope

Small fixed per-block compressed anchors were tested as a substitute for exact 32K-context key/value state on a synthetic arbitrary associative-recall task with 512-token blocks. The result supports only an early negative claim for arbitrary exact recall under fixed low-ratio anchor compression.

## Why it stopped

Proxy early falsification, not full validation: fixed low-ratio anchors did not preserve arbitrary exact recall even when given the correct source block.

## Recommended next action

Stop this run as a proxy early falsification; if continuing locally, train a small learned-anchor transformer on the same 32K synthetic retrieval distribution and require it to beat the collision baseline at 64 anchors per 512-token block.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned anchor compressor versus collision baseline on 32K associative recall
- Success threshold: At least 80% held-out exact recall at 64 anchors per 512-token block, at least 20 percentage points above the fixed-anchor collision baseline, with measured inference memory below a 6GB target envelope for the tested small model.
- Stop condition: Stop if the learned-anchor model remains below 25% exact recall at 64 anchors per block after matching a dense control on short-context training cases, or if measured memory exceeds the target envelope before reaching 32K context.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-anchors-for-32k-context-on-6gb-vram-e664a057c19b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
