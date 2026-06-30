# Cross-layer KV projection sharing for local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-layer-kv-projection-sharing-for-local-inference-ad07fb680cf3`
Run ID: `cross-layer-kv-projection-sharing-for-local-inference-ad07fb680cf3-20260524T083003159818+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/868b1785ee47

## What looked useful

Full cross-layer K/V sharing cut K/V projection parameters by 75.0% in a 4-layer model and 87.5% in an 8-layer model, but total parameter savings were only 12.0% and 14.3%. Mean 4-layer validation loss worsened from 2.0434 to 2.0812 across three seeds, and forward throughput changed by -1.29%. The 8-layer probe showed a similar validation-loss penalty with only a noise-level +0.54% throughput change.

## Boundaries and scale limits

This is a small local GPU probe, not GPT-2-small-class or 7B+ validation. It uses character language modeling, short context length 64, full forward-pass throughput rather than an optimized cached decode loop, and only one seed for the 8-layer scaling probe.

## Claim scope

On compact 4-layer and 8-layer causal Transformer character language models trained on Tiny Shakespeare, full cross-layer sharing of K/V projection matrices reduces unique model weights but does not provide a meaningful CUDA forward-throughput advantage and consistently worsens validation loss versus independent per-layer K/V projections.

## Why it stopped

Bounded local evidence shows real weight-memory savings but no meaningful local-inference throughput gain and a persistent quality regression, so the original standalone full cross-layer sharing hypothesis is not paper-ready.

## Recommended next action

Stop this full-sharing variant as no-paper evidence; if continuing locally, test grouped or low-rank K/V sharing against the same baseline because the measured loss penalty was modest but the speed benefit was absent.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Grouped K/V projection sharing for local Transformer inference
- Success threshold: A follow-up is useful if grouped or adapter sharing achieves at least 8% total parameter reduction, validation loss within 0.01 of the independent-K/V baseline, and no more than 1% throughput regression in both 4-layer and 8-layer local CUDA probes.
- Stop condition: Stop if all grouped/adapter variants still show validation loss more than 0.02 above baseline or no total parameter reduction above 8%, because that would rule out the local compression tradeoff at this scale.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-projection-sharing-for-local-inference-ad07fb680cf3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
