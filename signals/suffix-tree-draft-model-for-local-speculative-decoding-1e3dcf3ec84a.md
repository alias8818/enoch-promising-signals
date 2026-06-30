# Suffix-Tree Draft Model for Local Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-tree-draft-model-for-local-speculative-decoding-1e3dcf3ec84a`
Run ID: `suffix-tree-draft-model-for-local-speculative-decoding-1e3dcf3ec84a-20260629T021842321995+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a6fb9d2552e0

## What looked useful

A suffix-index draft model accepted 4.58-5.21 tokens per verification step on repeated traces at draft_len=6, beating the best simple baseline by 1.71-3.58 accepted tokens/step; random tokens produced essentially zero accepted draft tokens.

## Boundaries and scale limits

Synthetic/token-trace only; no live LLM target verifier, no GPU serving benchmark, no production traces, and no optimized memory-bounded suffix implementation.

## Claim scope

Online local suffix-index drafting improves exact token-trace speculative acceptance over simple local bigram and last-seen baselines on controlled repeated code/copy/natural traces, with no gain on an iid random negative control.

## Why it stopped

No-paper closure: the trace-level mechanism is useful and supported locally, but publication-grade claims require live-model verifier and latency evidence.

## Recommended next action

Run a bounded direct verifier benchmark on real tokenized code/RAG traces with a small target model and wall-clock latency measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Small-Model Verification of Local Suffix Drafting on Code and RAG Traces
- Success threshold: At least +0.5 accepted tokens per verifier step over the best simple local baseline and at least 1.15x measured wall-clock speedup on two real trace families.
- Stop condition: Stop as negative if suffix drafting fails to beat the best baseline by +0.2 accepted tokens/step or measured wall-clock speedup is below 1.05x after overhead.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-model-for-local-speculative-decoding-1e3dcf3ec84a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
