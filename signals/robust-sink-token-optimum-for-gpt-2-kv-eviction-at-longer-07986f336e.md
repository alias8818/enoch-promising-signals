# Robust sink-token optimum for GPT-2 KV eviction at longer contexts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `robust-sink-token-optimum-for-gpt-2-kv-eviction-at-longer-07986f336e`
Run ID: `robust-sink-token-optimum-for-gpt-2-kv-eviction-at-longer-07986f336e-20260607T075326864665+0000`

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

- Parent run decision: KV Eviction Policy Reduces Cache 40pct on GPT2 Small: enoch://control-plane/projects/kv-eviction-policy-reduces-cache-40pct-on-gpt2-small-d1bbb0182424/runs/kv-eviction-policy-reduces-cache-40pct-on-gpt2-small-d1bbb0182424-20260607T033338838596+0000
- Parent run decision: Sink-token sensitivity for 40% GPT-2 KV cache eviction: enoch://control-plane/projects/sink-token-sensitivity-for-40--gpt-2-kv-cache-eviction-e5e2c49c5d/runs/sink-token-sensitivity-for-40--gpt-2-kv-cache-eviction-e5e2c49c5d-20260607T055928214688+0000

## What looked useful

Sink-token retention remains strongly useful at 1536 tokens, recovering roughly 91-95% of the recent-only NLL gap. The robust fixed optimum claim is not supported: the best sink count shifts upward from the 1024-token parent result (sink32 for budgets 128/256) to about sink112 for budget128 and at least sink192 for budget256 in the longer harness.

## Boundaries and scale limits

Vanilla GPT-2-small is native only to 1024 positions, so the >1024 test uses an explicit position-extension control and should not be generalized to unmodified GPT-2, native long-context LMs, other corpora, downstream generation quality, serving kernels, or larger models. The budget-256 high-sink optimum was not fully bracketed because sink192 was still best among tested counts.

## Claim scope

GPT-2-small incremental KV-cache retention on WikiText-103 validation windows at seq_len 1536 under a shared repeat-last extension of learned position embeddings from 1024 to 1536 positions; direct next-token NLL compared full cache, recent-only, and sink-count ablations across fixed seeds.

## Why it stopped

Medium direct evidence supports sink retention but falsifies a stable robust fixed sink-token optimum across the longer context setting, and the >1024 GPT-2 result depends on a declared position-extension harness rather than native GPT-2 context support.

## Recommended next action

Stop this GPT-2 follow-up as no-paper useful signal; the next bounded deepen test should use a small model natively trained for 1536-2048+ context and bracket the sink optimum on two corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native long-context small-LM sink-count bracketing for KV eviction
- Success threshold: Sink retention beats recent-only by at least 80% gap recovery at two cache budgets, and the sink optimum is bracketed with a best setting whose paired delta is at least 0.05 bits/token better than adjacent lower and higher sink counts on both corpora.
- Stop condition: Stop if sink retention fails to recover at least 80% of the recent-only NLL gap, or if the optimum cannot be bracketed within a practical cache fraction under a native long-context model.

## Evidence references

- Artifact root: `<local-path>/projects/robust-sink-token-optimum-for-gpt-2-kv-eviction-at-longer-07986f336e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
