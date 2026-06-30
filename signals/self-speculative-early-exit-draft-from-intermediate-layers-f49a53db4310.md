# Self-Speculative Early-Exit Draft from Intermediate Layers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-early-exit-draft-from-intermediate-layers-f49a53db4310`
Run ID: `self-speculative-early-exit-draft-from-intermediate-layers-f49a53db4310-20260523T041935158316+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e56aeca11e8c

## What looked useful

Cheap early layers match the final greedy token only about 10-15% of the time, while the best agreement layer is the penultimate layer at about 54.6% top-1 match but about 94.4% of full-forward median cost. This falsifies the naive unmodified early-exit draft while preserving a bounded follow-up signal from late-layer top-5 containment around 83.8%.

## Boundaries and scale limits

CPU-only inference; local mixed-domain corpus windows; greedy top-1 agreement and a simple one-token latency proxy; no optimized KV-cache speculative decoding loop, no sampling acceptance, no trained exit head, and no larger-model validation.

## Claim scope

For pretrained GPT-2-small on 18,240 local next-token positions per layer, unmodified intermediate hidden states projected through the final layer norm and LM head do not provide a useful one-token self-speculative draft path: all measured single-token speed proxies are below 1.0.

## Why it stopped

Proxy/early falsification rather than full validation: the direct intermediate-logit agreement and measured partial-forward costs do not support speedup for the naive self-speculative early-exit design.

## Recommended next action

Stop this no-paper run; if continuing locally, test a trained layer-specific exit head plus confidence gate in an actual GPT-2-small autoregressive speculative decoding loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Confidence-Gated Exit Head for GPT-2-Small Self-Speculation
- Success threshold: On held-out text, at least 1.10x tokens/sec versus standard GPT-2-small greedy decoding with at least 99% exact greedy-output preservation for gated tokens and no perplexity regression under the selected decoding policy.
- Stop condition: Stop if validation speedup is below 1.05x, exact-output preservation is below 99%, or the trained exit head only works at layers costing more than 80% of a full forward.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-early-exit-draft-from-intermediate-layers-f49a53db4310`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
