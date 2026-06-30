# Exact Anchor Ledger with Rolling Compressed State for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-ledger-with-rolling-compressed-state-for-long-context-fa1ad72d1dcd`
Run ID: `exact-anchor-ledger-with-rolling-compressed-state-for-long-context-fa1ad72d1dcd-20260525T231621010677+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/239c7a000d18

## What looked useful

Anchored exact recall was 1.0 in every run; non-anchored exact recall was 0.0; mixed exact recall tracked anchor fraction. At 200000 records with sketch width 262144, memory ratio versus full ledger ranged from 0.6655 at stride 8 to 0.4961 at stride 512. In a stride-128 sketch sweep, memory ratio improved to 0.0416 with width 16384 but absent-key sketch false positives were 1.0; reducing false positives to 0.0008 required width 1048576 and 1.9845x full-ledger memory.

## Boundaries and scale limits

No transformer, natural-language, learned-anchor, multi-million-token, or serving-system validation was run. The benchmark retains a full truth table for scoring, so process RSS is not the deployed memory footprint. Results are bounded to synthetic random payloads and deterministic anchor strides.

## Claim scope

Synthetic model-free key/value streams up to 200000 records show that an exact anchor ledger with rolling compressed state gives perfect exact recall for preselected anchored records and lower theoretical storage than a full exact ledger only when anchors are sparse and compressed-state accuracy requirements are modest.

## Why it stopped

The local evidence is a synthetic mechanism probe, not publication-grade validation. It early-falsifies any broad claim that rolling compression plus sparse exact anchors provides general exact long-context recall, while preserving a narrower anchor-aligned mechanism worth a direct model follow-up.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should connect the anchor ledger to a small transformer or retrieval-augmented inference loop and measure whether a model can exploit exact anchors on long-context recall tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Toy Transformer Use of Exact Anchor Ledger for Long-Context Recall
- Success threshold: At 16000-token synthetic contexts, anchored-query recall improves by at least 20 percentage points over the baseline while total cache-plus-ledger memory is at least 25% below a full exact-cache/control configuration; unanchored limitations must be reported separately.
- Stop condition: Stop if the model cannot use supplied anchors to beat the parameter-matched baseline by 10 percentage points on anchored recall in two seeds, or if the memory accounting exceeds the full-cache/control memory at the recall-matched point.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-ledger-with-rolling-compressed-state-for-long-context-fa1ad72d1dcd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
