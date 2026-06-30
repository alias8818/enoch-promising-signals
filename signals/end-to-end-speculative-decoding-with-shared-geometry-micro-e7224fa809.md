# End-to-End Speculative Decoding With Shared-Geometry Micro Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-speculative-decoding-with-shared-geometry-micro-e7224fa809`
Run ID: `end-to-end-speculative-decoding-with-shared-geometry-micro-e7224fa809-20260526T140951376154+0000`

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

- Parent run decision: Shared-Embedding Micro-Draft Network for Spec Decoding: enoch://control-plane/projects/shared-embedding-micro-draft-network-for-spec-decoding-1dd4e00f003c/runs/shared-embedding-micro-draft-network-for-spec-decoding-1dd4e00f003c-20260526T022911539795+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d456810f23e

## What looked useful

Shared geometry produced high one-step teacher match on held-out data prefixes (0.8984) but collapsed to 0.0151 acceptance on generated prefixes and was slower than target-only decoding (0.4894x). The independent control was slightly better (0.9099 one-step match, 0.0169 acceptance, 0.4917x), so shared geometry did not provide a useful advantage in this direct small test.

## Boundaries and scale limits

Synthetic data, small target model, no KV-cache serving implementation, greedy decoding only, 16 prompts x 96 generated tokens for end-to-end timing. This does not rule out larger pretrained LLMs, stronger draft architectures, or on-policy distillation.

## Claim scope

Controlled small direct test of greedy speculative decoding on a synthetic next-token language with a 2-layer target transformer and micro drafts. The shared-geometry draft reused the target token/output geometry and was compared with an independent-geometry control.

## Why it stopped

Early direct falsification at Tier 1: exact speculative decoding worked, but generated-prefix acceptance was about 1.5% and end-to-end speculative decoding was about 2x slower than target-only. This is not a full-scale LLM validation.

## Recommended next action

Stop this recipe as no-paper evidence; the only worthwhile bounded next test is on-policy distillation of the micro draft on target-generated prefixes, then repeat the same exact acceptance and speed benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: On-policy shared-geometry micro draft for generated-prefix acceptance
- Success threshold: Shared draft acceptance on generated prefixes at least 0.45 and end-to-end speedup greater than 1.10x versus target-only, while beating the independent draft control on both acceptance and speed.
- Stop condition: Stop if on-policy training still yields acceptance below 0.25 or no speedup after a matched short training budget, because the mechanism would remain too weak for local speculative decoding.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-speculative-decoding-with-shared-geometry-micro-e7224fa809`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
