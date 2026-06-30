# Cross-Layer KV Cache Sharing for GPT-2-Small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `cross-layer-kv-cache-sharing-for-gpt-2-small-10e2babe39c1`
Run ID: `cross-layer-kv-cache-sharing-for-gpt-2-small-10e2babe39c1-20260604T235026207138+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9386228f9296

## What looked useful

Raw per-layer KV tensors in pretrained GPT-2 small are not interchangeable across layers: adjacent-layer key/value cosine similarities at token 32 were near zero, and direct cache aliasing caused large next-token quality degradation even for selective late-layer policies.

## Boundaries and scale limits

Single pretrained GPT-2-small model, WikiText-2 test stream, one deterministic 1024-token medium confirmation after 64-token smoke tests, context length capped by GPT-2 positional limit, no retraining, no learned adapters, no larger models, no downstream generation human evaluation.

## Claim scope

Pretrained GPT-2 small does not tolerate direct raw cross-layer KV cache aliasing during autoregressive cached inference on WikiText-2: all-layer pair sharing saves 50% estimated KV memory but increases perplexity 58x over 1024 evaluated tokens; sharing only the final layer pair saves 8.3% estimated KV memory but still increases perplexity 36%.

## Why it stopped

Proxy-bounded but direct inference early falsification: the run directly tested raw KV aliasing in pretrained GPT-2 small and found the memory-quality tradeoff too poor for a paper claim; it does not fully validate or refute trained shared-KV architectures.

## Recommended next action

Stop this post-hoc raw-cache-sharing line as an early negative; only revisit with a separately scoped trained or adapter-projected shared-KV architecture and a direct GPT-2-small-class baseline comparison.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-cache-sharing-for-gpt-2-small-10e2babe39c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
