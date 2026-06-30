# Layer-exit self-speculative decoding without draft VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-exit-self-speculative-decoding-without-draft-vram-2643b1a0cbbb`
Run ID: `layer-exit-self-speculative-decoding-without-draft-vram-2643b1a0cbbb-20260530T073500902561+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/acb90839f3ae

## What looked useful

Naive ungated layer-exit self-speculative decoding is unlikely to speed up GPT-2-small-class greedy decoding despite avoiding draft-model VRAM. High-margin late exits are reliable over limited coverage: top 25% margin acceptance reached 81.05% at exit 9, 93.36% at exit 10, and 99.61% at exit 11, suggesting a confidence-gated follow-up.

## Boundaries and scale limits

Offline replay only; no optimized online KV-cache implementation, no sampling-mode test, no larger model family, and no trained/calibrated exit policy. The result is a bounded mechanism test, not a full serving benchmark.

## Claim scope

On GPT-2-small greedy continuations over 64 WikiText-2 validation prompts, ungated layer-exit self-drafting with shared final norm and LM head uses zero extra draft parameter bytes but does not reach fixed-window speculative break-even acceptance for exits after 3, 6, 9, 10, or 11 of 12 blocks.

## Why it stopped

Proxy/early falsification of the ungated fixed-window version: final WikiText replay showed best ungated late-exit case exit 11 gamma 2 emitted 1.642 tokens per iteration versus 2.833 needed by the simple break-even model; no full online implementation was tested.

## Recommended next action

Run a bounded online confidence-gated self-speculative decoder on GPT-2-small with KV caches and compare wall-clock latency, emitted tokens per verification, and exact-output equality against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated layer-exit self-speculative decoding
- Success threshold: At least 1.10x wall-clock speedup over greedy decoding with identical greedy outputs, zero extra draft model parameters, and at least 20% of generated positions handled by high-confidence exits.
- Stop condition: Stop if no tested margin threshold reaches 1.0x latency parity or if exact-output verification fails for any accepted token.

## Evidence references

- Artifact root: `<local-path>/projects/layer-exit-self-speculative-decoding-without-draft-vram-2643b1a0cbbb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
