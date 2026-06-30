# Suffix-Tree Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-cpu-077281303259`
Run ID: `suffix-tree-speculative-decoding-on-cpu-077281303259-20260525T121601040860+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/25f917db570d

## What looked useful

A suffix-index drafter reduced target calls by 83.68% and modeled 6.05x speedup on a highly repetitive motif workload, but only 5.08% target-call reduction and about 1.04x modeled speedup on a moderate template workload, and no reduction with a modeled slowdown on random tokens. This supports replay-heavy prompt-cache use cases and falsifies a broad general CPU speedup claim at proxy scale.

## Boundaries and scale limits

No real transformer, tokenizer, KV cache, scheduler, or end-to-end CPU serving stack was measured. Target-model latency is a transparent cost model, not direct LLM wall-clock throughput. Workloads are synthetic and medium scale: 100k training tokens and 20k test tokens per run.

## Claim scope

Standard-library CPU replay benchmark of suffix-index speculative drafting over synthetic repeated, template, and random token streams. The mechanism reduces target verification calls only when held-out continuations repeat strongly from indexed history.

## Why it stopped

No-paper useful signal: the result is a proxy/medium synthetic mechanism test, not full validation. It supports suffix drafting for replay-heavy traces but early-falsifies broad usefulness on low-repetition streams.

## Recommended next action

Run a bounded deepen follow-up inside a real CPU transformer runtime, such as llama.cpp, using repeated-prompt traces and a gating policy that disables suffix drafting when recent acceptance falls below a threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer Test of Gated Suffix-Index Drafting
- Success threshold: At least 20% end-to-end tokens/sec improvement on repeated traces and less than 5% slowdown on non-repeated traces, with memory overhead reported and bounded.
- Stop condition: Stop if real CPU integration shows less than 10% throughput gain on repeated traces or more than 5% slowdown on non-repeated traces after acceptance gating.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-cpu-077281303259`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
