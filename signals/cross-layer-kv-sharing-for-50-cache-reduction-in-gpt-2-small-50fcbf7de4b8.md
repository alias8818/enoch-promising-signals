# Cross-layer KV sharing for 50% cache reduction in GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-layer-kv-sharing-for-50-cache-reduction-in-gpt-2-small-50fcbf7de4b8`
Run ID: `cross-layer-kv-sharing-for-50-cache-reduction-in-gpt-2-small-50fcbf7de4b8-20260525T011601565679+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e7f1bd0dbbd1

## What looked useful

Adjacent-pair K/V sharing reduced nominal fp16 K/V cache from 36,864 to 18,432 bytes/token but increased GPT-2 small Wikitext-2 perplexity from 50.96 to 829.58 (16.28x). Adjacent K/V tensors were nearly orthogonal, with mean absolute cosine 0.0137 for keys and 0.0058 for values.

## Boundaries and scale limits

This was a bounded full-forward loss proxy, not a production incremental decoding benchmark and not a trained shared-K/V architecture. It does not rule out models trained or fine-tuned with the sharing constraint active.

## Claim scope

Pretrained GPT-2 small without retraining, evaluated on 64 Wikitext-2 test examples, does not tolerate naive adjacent-pair cross-layer K/V sharing that nominally halves distinct K/V cache states.

## Why it stopped

Proxy/direct early falsification for naive zero-shot adjacent-layer sharing: the local target metric failed by a large margin, but this is not a full validation of trained shared-K/V architectures.

## Recommended next action

Stop this no-retraining path; only continue with a bounded training-time follow-up that enforces adjacent K/V sharing during fine-tuning or from initialization and measures real decode-cache memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train-constrained adjacent K/V sharing in GPT-2-small-class models
- Success threshold: At least 45% measured K/V-cache memory reduction with no more than 10% perplexity increase versus the matched baseline and no severe decode throughput regression.
- Stop condition: Stop if constrained fine-tuning still leaves perplexity more than 25% above baseline after a predeclared small/medium token budget, or if measured cache savings are materially below 45% after framework overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-sharing-for-50-cache-reduction-in-gpt-2-small-50fcbf7de4b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
