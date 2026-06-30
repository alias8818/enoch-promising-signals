# KV-cache prompt-lookup n-gram speculative decoding on natural repeated-context prompts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-prompt-lookup-n-gram-speculative-decoding-on-natu-3ef72e79cc`
Run ID: `kv-cache-prompt-lookup-n-gram-speculative-decoding-on-natu-3ef72e79cc-20260525T055012159126+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: N-gram CPU Speculative Decode: enoch://control-plane/projects/n-gram-cpu-speculative-decode-241538880383/runs/n-gram-cpu-speculative-decode-241538880383-20260525T054001064067+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fa784b59fdfb

## What looked useful

All 16 n-gram/draft settings passed the Tier 1 threshold. Best setting was n-gram 2, max draft 32 with 15.91x mean verifier-call speedup and 96.76% accepted target-token rate on repeated-context copies, while the matching no-copy control stayed at 1.013x speedup. Stricter n-gram 3-5 settings with draft 16 still achieved 8.59x-9.94x mean speedup with controls near 1.0x.

## Boundaries and scale limits

No neural target model was run; latency, throughput, cache implementation overhead, batching behavior, tokenizer effects, and model tendency to copy on real tasks remain unmeasured. Evidence is from 72 repeated-context copy prompts and 72 no-copy controls per setting.

## Claim scope

Tier 1 controlled mechanism test on three public-domain natural-text corpora: when prompts contain a copied natural span and generation target is the continuation of that span, n-gram prompt lookup can draft exact continuations that substantially reduce verifier calls under a KV-cache-preserving speculative decoding cost model.

## Why it stopped

No-paper useful signal: the Tier 1 mechanism is supported, but the run used an oracle continuation and scored-token cost proxy rather than a real target model latency implementation.

## Recommended next action

Run a bounded deepen follow-up with an actual small causal LM and KV-cache-preserving speculative verifier, measuring wall-clock tokens/sec against greedy decoding on extractive repeated-context prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM KV-cache prompt-lookup latency validation on extractive repeated-context prompts
- Success threshold: At least 1.5x mean wall-clock tokens/sec improvement on repeated-context prompts, no more than 5% output-token disagreement versus greedy, and no more than 1.1x overhead on no-copy controls.
- Stop condition: Stop if exact-token acceptance is below 30% on real-model outputs or measured wall-clock speedup is below 1.2x for every tested n-gram/draft setting.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-prompt-lookup-n-gram-speculative-decoding-on-natu-3ef72e79cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
