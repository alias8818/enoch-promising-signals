# KV-cache n-gram speculative drafting on modern tiny local models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-n-gram-speculative-drafting-on-modern-tiny-local-dfe0a150f1`
Run ID: `kv-cache-n-gram-speculative-drafting-on-modern-tiny-local-dfe0a150f1-20260608T114345269116+0000`

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

- Parent run decision: N-gram speculative draft for tiny local inference: enoch://control-plane/projects/n-gram-speculative-draft-for-tiny-local-inference-28d35326be21/runs/n-gram-speculative-draft-for-tiny-local-inference-28d35326be21-20260608T044637010741+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b2be2b147e7d

## What looked useful

N-gram drafting is conditionally useful: repetitive contexts averaged 2.285x speedup with 0.740 mean acceptance and 52.3% mean forward-call reduction, while natural/code instruction prompts averaged 0.853x speedup with negative forward-call reduction. Exactness requires care because BF16 vectorized verification diverged from stepwise greedy in one condition.

## Boundaries and scale limits

Single model, six fixed prompts, 64 generated tokens each, draft sizes 2/4/8, FP32 final run; BF16 showed a divergence in one longer condition and larger models, longer prompts, sampling, batching, and production kernels were not validated.

## Claim scope

On one modern 135M local instruction model on GB10, FP32 KV-cache n-gram speculative decoding exactly matched greedy decoding across 18 prompt/draft conditions and sped up repetitive prompts while slowing down natural prompts.

## Why it stopped

Tier 1 direct evidence produced a useful but mixed mechanism signal, not publication-grade evidence; the result is no-paper because it is one small model and prompt set with a BF16 exactness caveat.

## Recommended next action

Run a bounded adaptive-gating follow-up that disables n-gram drafting after low recent acceptance and validates whether it preserves repetitive speedups without natural-prompt slowdowns.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive acceptance-gated n-gram drafting on tiny local LMs
- Success threshold: Mean speedup >= 1.8x on repetitive prompts, mean speedup >= 1.0x on natural prompts, all outputs exactly match greedy, and no prompt is below 0.95x.
- Stop condition: Stop if the gate cannot prevent natural-prompt slowdown without reducing repetitive-prompt speedup below 1.5x, or if exact-match failures persist under the chosen dtype/safeguard.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-speculative-drafting-on-modern-tiny-local-dfe0a150f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
