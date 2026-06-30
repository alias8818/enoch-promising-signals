# Self-Speculative Early Exit with Shared KV for Zero-VRAM Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-early-exit-with-shared-kv-for-zero-vram-draft-4dfa960e91d9`
Run ID: `self-speculative-early-exit-with-shared-kv-for-zero-vram-draft-4dfa960e91d9-20260527T185643351980+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1f0ab6a3dfc7

## What looked useful

The zero-extra-draft-KV accounting is mechanically valid, but draft quality is insufficient: best calibrated setting was exit layer 10 with temperature 1.7, expected sampled acceptance 0.569, top-1 agreement 0.472, and modeled 8-token draft throughput 0.664x baseline.

## Boundaries and scale limits

Single pretrained GPT-2-small-class model, short generated continuations, simple layer-timing cost model, no optimized production decoder, no larger instruction-tuned models, no long-context or batch-serving validation.

## Claim scope

On GPT-2 fp16 with 625 evaluated next-token positions, shared lower-layer KV eliminates additional draft KV memory, but naive untrained early-exit logits do not reach break-even modeled throughput for self-speculative decoding.

## Why it stopped

Bounded direct small-model evidence supports the memory premise but falsifies the naive speedup premise under the tested proxy cost model; this is not a full validation or universal rejection for larger trained variants.

## Recommended next action

Stop this naive early-exit line as no-paper evidence; only revisit with a bounded trained early-exit calibration/adaptor test that must exceed 1.05x modeled throughput on GPT-2-small-class before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a calibrated early-exit draft head for shared-KV self-speculation
- Success threshold: At least one exit depth must reach expected sampled acceptance sufficient for >=1.05x modeled throughput for 4- or 8-token drafts on held-out prompts, while adding 0 extra draft KV bytes/token.
- Stop condition: Stop if calibrated exits remain below 1.0x modeled throughput or require enough extra parameters/cache to erase the zero-VRAM-draft advantage.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-early-exit-with-shared-kv-for-zero-vram-draft-4dfa960e91d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
