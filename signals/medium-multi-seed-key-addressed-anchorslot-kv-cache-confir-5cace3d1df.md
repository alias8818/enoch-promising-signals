# Medium Multi-Seed Key-Addressed AnchorSlot KV Cache Confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-multi-seed-key-addressed-anchorslot-kv-cache-confir-5cace3d1df`
Run ID: `medium-multi-seed-key-addressed-anchorslot-kv-cache-confir-5cace3d1df-20260518T041100835353+0000`

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

- Internal Enoch project: Medium Multi-Seed Key-Addressed AnchorSlot KV Cache Confirmation: internal_generated:medium-multi-seed-key-addressed-anchorslot-kv-cache-confir-5cace3d1df

## What looked useful

Across 45 fixed-seed context/budget configs, AnchorSlot improved match_dense_acc over segment_count by +0.1476 and target_acc by +0.1296, winning both metrics in 45/45 paired trials. However, segment_count had better average relative L2, 0.7131 versus AnchorSlot 0.7308, and AnchorSlot won relative L2 in only 20/45 paired trials and 3/9 summary cells.

## Boundaries and scale limits

No trained language-model perplexity, generation-quality, real long-context QA, optimized serving kernel, or 7B+/production-scale validation was run. The evidence is medium synthetic direct-KV confirmation only.

## Claim scope

Synthetic associative KV-cache benchmark with fixed seeds, exact dense attention reference, sliding-window/random/segment baselines, and key-addressing/count ablations. Key-addressed AnchorSlot improves discrete dense-decision and target retrieval fidelity under fixed cache budgets, but does not consistently improve continuous dense-output relative L2 versus segment averaging.

## Why it stopped

Medium synthetic confirmation produced a useful but mixed signal: key addressing helps retrieval fidelity, yet the real segment baseline remains stronger on the continuous dense-output error metric, so this is not paper-ready.

## Recommended next action

Run a bounded GPT-2-small-class inference follow-up with exact dense, sliding-window, random-token, segment_count, AnchorSlot, and ablation caches; require AnchorSlot to beat segment_count on both perplexity delta and retrieval/needle accuracy before further escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-Small Inference Validation of Key-Addressed AnchorSlot KV Cache
- Success threshold: AnchorSlot must beat segment_count by at least 5% relative on retrieval/needle error and have no worse perplexity delta than segment_count at two or more cache budgets across at least three fixed seeds.
- Stop condition: Stop if AnchorSlot fails to beat segment_count on either perplexity delta or retrieval/needle accuracy in the first two fixed-seed medium LM configs, or if integration overhead prevents a faithful matched-budget comparison.

## Evidence references

- Artifact root: `<local-path>/projects/medium-multi-seed-key-addressed-anchorslot-kv-cache-confir-5cace3d1df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
