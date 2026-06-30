# SVD-Rotate KV Cache for 2x Longer Local Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `svd-rotate-kv-cache-for-2x-longer-local-context-7f46d0c121b4`
Run ID: `svd-rotate-kv-cache-for-2x-longer-local-context-7f46d0c121b4-20260531T165450953022+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6fcd819485b5

## What looked useful

Half-rank SVD retained about 97% key energy and 89-92% value energy on distilgpt2/gpt2 and beat truncate/random controls on KL and top-1 match. DistilGPT-2 remained relatively stable through 256 tokens, but GPT-2 degraded at 256 tokens with SVD KL 1.589 and top-1 match 0.500, falsifying a naive drop-in 2x whole-cache compression claim at this scale.

## Boundaries and scale limits

Tested only distilgpt2 and gpt2 on a fixed small text corpus with contexts up to 256 tokens. The experiment reconstructs full KV tensors before decode and does not measure compressed attention kernels, basis overhead, standard long-context benchmarks, 7B+ models, or production serving latency.

## Claim scope

Small GPT-2-class next-token cache-reconstruction probe: per-layer/head half-rank SVD of real KV caches preserves substantially more information and next-token distribution fidelity than truncation or random projection, but naive whole-cache half-rank compression is not stable enough to support a 2x local-context claim.

## Why it stopped

No-paper closure: the direct small-model probe produced a useful mechanism signal but mixed fidelity evidence, including sharp GPT-2 degradation at 256 tokens. This is not full validation of 2x longer local context.

## Recommended next action

Run a bounded segmented-cache follow-up that keeps a recent exact window and applies SVD only to older blocks under an equal-memory 2x-context budget; stop if GPT-2-class KL/top-1 drift remains near the naive whole-cache half-rank result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Segmented SVD KV Cache With Exact Recent Window
- Success threshold: At 2x total context and equal estimated KV memory, segmented SVD should reduce GPT-2 mean KL by at least 50% versus naive whole-cache half-rank SVD and keep top-1 match at or above 0.75 on the tested next-token probe.
- Stop condition: Stop as negative if segmented SVD fails to improve GPT-2 mean KL by at least 25% over naive whole-cache half-rank SVD or if basis overhead eliminates the intended memory saving for practical block sizes.

## Evidence references

- Artifact root: `<local-path>/projects/svd-rotate-kv-cache-for-2x-longer-local-context-7f46d0c121b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
