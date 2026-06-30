# Layer-Drop Speculative Draft: Skip-Layer Forward as Zero-VRAM Draft Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `layer-drop-speculative-draft-skip-layer-forward-as-zero-vram-draft-model-9744db38ee59`
Run ID: `layer-drop-speculative-draft-skip-layer-forward-as-zero-vram-draft-model-9744db38ee59-20260529T102903440750+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5213de7fb002

## What looked useful

Skipping layers saved only 6-54% of forward latency while reducing sampled speculative acceptance to 0.13-0.54; every non-full schedule modeled below 1.0x speedup, with best non-trivial case 0.881x.

## Boundaries and scale limits

This was a bounded GPT-2-small-class proxy with measured GPU forward costs and modeled speculative cycles, not an end-to-end KV-cache serving benchmark, not a long-context study, and not a 7B+ validation.

## Claim scope

Raw untrained GPT-2-small layer skipping, implemented by replacing selected transformer blocks with identity modules, did not produce a useful zero-extra-weights speculative draft on 128 Wikitext-2 validation contexts.

## Why it stopped

Proxy early falsification: measured GPT-2-small distribution drift and latency ratios imply sub-break-even speculative speed for all tested raw layer-drop schedules, but this is not a full serving validation.

## Recommended next action

Stop the raw skip-layer zero-VRAM draft line unless a bounded real speculative-decoder implementation first shows above-1.0x speedup on GPT-2-small-class models.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/layer-drop-speculative-draft-skip-layer-forward-as-zero-vram-draft-model-9744db38ee59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
