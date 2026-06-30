# Multi-Model Direct KV Eviction Test for Sink-Token Retention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-model-direct-kv-eviction-test-for-sink-token-retenti-f275f0b1c9`
Run ID: `multi-model-direct-kv-eviction-test-for-sink-token-retenti-f275f0b1c9-20260526T201551157428+0000`

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

- Parent run decision: KV-Cache Compression via Cross-Layer Attention Sinks: enoch://control-plane/projects/kv-cache-compression-via-cross-layer-attention-sinks-5313eef5075b/runs/kv-cache-compression-via-cross-layer-attention-sinks-5313eef5075b-20260526T035032162235+0000
- Parent run decision: Direct Incremental KV Eviction Test for Sink-Token Retention: enoch://control-plane/projects/direct-incremental-kv-eviction-test-for-sink-token-retenti-bdf78149af/runs/direct-incremental-kv-eviction-test-for-sink-token-retenti-bdf78149af-20260526T133921491031+0000

## What looked useful

The broad sink-token retention rule was not robust: sink eviction was worst in only 2 of 9 substantive model/count rows, both for one-token eviction in GPT-2-family models. At 4 and 8 evicted positions, sink eviction was not the worst intervention in any substantive model, and Pythia showed larger degradation from non-sink controls.

## Boundaries and scale limits

16 WikiText-2 samples per run, 128-token prefixes, 32-token continuations, evict counts 1/4/8, small local models only: distilgpt2, gpt2, EleutherAI/pythia-70m-deduped, plus tiny-gpt2 smoke. No long-context retrieval, no production cache policy, no large 7B+ models, and no attention-head mechanism tracing.

## Claim scope

Direct KV-cache zeroing on small pretrained decoder-only models using WikiText-2 continuations shows no robust multi-model advantage for retaining the first 4 or 8 prefix positions over middle, recent, or random cached positions; a narrower first-position sensitivity appears in GPT-2-family checkpoints only.

## Why it stopped

Tier 2 direct KV-eviction evidence is mixed and fails the robust multi-model sink-retention threshold; the result is useful for narrowing future tests but not paper-ready.

## Recommended next action

Stop as no-paper useful signal; if continuing, run a bounded mechanism study of first-token sensitivity in GPT-2-family versus non-GPT-2 architectures with attention-head attribution and longer context lengths.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Architecture-Specific First-Token KV Sensitivity Mechanism Test
- Success threshold: Support the architecture-specific hypothesis if GPT-2-family models show first-position sink-minus-best-control >= 0.05 mean NLL in at least 75% of model/context settings, while non-GPT-2 models fail that threshold, with a consistent layer/head diagnostic.
- Stop condition: Stop if first-position sink eviction is not consistently worse than controls in GPT-2-family models across two context lengths, or if non-GPT-2 models show the same effect and the architecture-specific hypothesis collapses.

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-direct-kv-eviction-test-for-sink-token-retenti-f275f0b1c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
