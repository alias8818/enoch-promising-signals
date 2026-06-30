# CPU-hosted n-gram draft for GPU speculative decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-hosted-n-gram-draft-for-gpu-speculative-decode-de874871fec4`
Run ID: `cpu-hosted-n-gram-draft-for-gpu-speculative-decode-de874871fec4-20260607T111900293833+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14ba056c8bbc

## What looked useful

Order-5 draft length 8 on structured synthetic logs accepted 71.19% of proposed tokens and progressed 6.15 tokens per verification with about 0.0012 ms CPU proposal time. Tiny Shakespeare best modeled speedup was only 1.08x with 6.75% accept rate for order-2 draft length 2.

## Boundaries and scale limits

No live GPU LLM serving, model tokenizer, KV-cache, batching, or utilization measurements were run. Natural-language evidence is limited to Tiny Shakespeare and controller prompt text; structured evidence includes a synthetic log-like trace.

## Claim scope

Trace-level evidence shows CPU n-gram drafting has negligible proposer overhead and can greatly reduce ideal verification calls on repetitive structured token traces, but provides only marginal gains on natural-text traces.

## Why it stopped

No-paper closure: this run produced a useful trace-level mechanism signal, but only proxy latency and held-out-token acceptance, not direct GPU speculative decoding evidence.

## Recommended next action

Run a bounded live-GPU follow-up that integrates the CPU n-gram proposer with a small decoder and compares no-speculative, CPU n-gram, and GPU-draft baselines on natural versus repetitive/code/log prompt sets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live GPU decode test for workload-selective CPU n-gram drafting
- Success threshold: CPU n-gram drafting achieves at least 1.25x tokens/sec on repetitive/code/log prompts with no more than 5% regression on natural prompts and no p95 latency regression above 10%.
- Stop condition: Stop if live decode shows less than 1.10x speedup on repetitive/code/log prompts or more than 5% regression on natural prompts after tuning n-gram order 2-5 and draft length 1-8.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-hosted-n-gram-draft-for-gpu-speculative-decode-de874871fec4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
