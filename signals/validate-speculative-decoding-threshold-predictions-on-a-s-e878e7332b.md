# Validate speculative-decoding threshold predictions on a small real draft/target model pair

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `validate-speculative-decoding-threshold-predictions-on-a-s-e878e7332b`
Run ID: `validate-speculative-decoding-threshold-predictions-on-a-s-e878e7332b-20260604T012610915240+0000`

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

- Parent run decision: Draft-Model Quality Thresholds for Speculative Decoding: Minimum Acceptance Rate for Net Speedup: enoch://control-plane/projects/draft-model-quality-thresholds-for-speculative-decoding-minimum-acceptance-rate-for-net-speedup-de8a2ff495d9/runs/draft-model-quality-thresholds-for-speculative-decoding-minimum-acceptance-rate-for-net-speedup-de8a2ff495d9-20260603T181343757940+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a66a38a90554

## What looked useful

distilgpt2->gpt2 matched the threshold direction for gamma 4 and 6 but gamma 2 slightly beat baseline despite a predicted slight loss. gpt2->gpt2-medium matched gamma 2 as positive, while gamma 4 and 6 were near or above break-even despite predicted losses. Cycle diagnostics indicate correlated acceptance bursts, not aggregate per-token acceptance alone, are needed for reliable threshold prediction.

## Boundaries and scale limits

The implementation is a local full-prefix greedy loop without KV-cache optimization, uses 8-16 short prompts per pair, tests only gamma 2/4/6, and covers small GPT-2-family models rather than production serving or draft models trained for a target.

## Claim scope

Tier 1 controlled greedy speculative-decoding tests on two small real GPT-2-family draft/target pairs show that speedup depends on proposal length, measured cost ratio, and target-verified acceptance, but a simple iid aggregate acceptance-rate threshold can mispredict observed speedup when acceptances are bursty.

## Why it stopped

Closed as no-paper useful signal because the direct small-model evidence is mixed and implementation-scoped; it validates the mechanism but falsifies reliability of the simple iid aggregate acceptance threshold for these controlled runs.

## Recommended next action

Run a bounded deepen test using a KV-cache or Hugging Face assisted-generation path and compare observed speedup against a cycle-level emitted-token threshold model across the same two pairs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate cycle-level speculative threshold predictions with KV-cache assisted generation
- Success threshold: Cycle-level threshold predictions classify speedup versus slowdown correctly for at least five of six pair/gamma settings and reduce absolute speedup prediction error versus the iid aggregate threshold.
- Stop condition: Stop if KV-cache assisted generation cannot expose or reconstruct per-cycle acceptance diagnostics locally, or if the cycle-level model fails to improve classification over the iid threshold on the bounded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/validate-speculative-decoding-threshold-predictions-on-a-s-e878e7332b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
