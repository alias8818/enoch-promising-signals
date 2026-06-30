# Compressed State Ring Buffer for Unbounded Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `compressed-state-ring-buffer-for-unbounded-context-11a41b140c20`
Run ID: `compressed-state-ring-buffer-for-unbounded-context-11a41b140c20-20260602T145603495625+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1f0cae4917f6

## What looked useful

A fixed cyclic compressed state ring does not provide unbounded context for arbitrary unique associations. At 65,536 items with 64 value classes, old-context accuracy was 0.0151 against a 0.015625 chance level. Increasing sketch width from 64 to 1024 improved recent-window accuracy from 0.299 to 0.861 but left old-context accuracy near chance.

## Boundaries and scale limits

This is a CPU-only synthetic benchmark, not a trained transformer or serving-system evaluation. It tests arbitrary unique association recall, not compressible natural-language discourse or learned memory policies.

## Claim scope

In a synthetic unique key-value associative recall task with fixed cyclic compressed segment rings, overwritten old-context recall saturates at chance as stream length grows beyond the ring capacity.

## Why it stopped

Proxy/early falsification: the direct synthetic recall probe shows cyclic overwrite prevents unbounded recall, but full transformer-scale evidence would be required to overturn this result for learned natural-language memory.

## Recommended next action

Stop this cyclic-ring version as a no-paper useful negative; a bounded follow-up should test a non-overwriting hierarchical or retrieval-indexed compressed memory against the same recall task.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Non-overwriting hierarchical compressed memory for long associative recall
- Success threshold: At 65,536 associations and 64 value classes, old-context accuracy must exceed 0.078125, five times chance, while using less memory than the exact unbounded oracle.
- Stop condition: Stop if old-context accuracy remains below 0.03125, two times chance, across three seeds at any tested bounded memory under the exact oracle footprint.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-ring-buffer-for-unbounded-context-11a41b140c20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
