# Token-Budget Cascade for Long-Context Home Inference on gb10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `token-budget-cascade-for-long-context-home-inference-on-gb10-98812a8100aa`
Run ID: `token-budget-cascade-for-long-context-home-inference-on-gb10-98812a8100aa-20260609T071555579853+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/153d62b5b21c

## What looked useful

The mechanism is locally reproducible: budgeted chunk selection can retain localized evidence far better than truncation/random selection in the synthetic setting, and reduced token lengths map to lower BF16 attention proxy latency on GB10.

## Boundaries and scale limits

Synthetic retrieval only; no real tokenizer, no real long-context QA dataset, no trained LLM answer generation, no full decoder stack, no batching, no decode throughput, and no meaningful UMA memory pressure beyond small PyTorch proxy tensors.

## Claim scope

In a controlled synthetic one-hop evidence-localization benchmark with 16,384-token contexts on GB10, a cheap lexical token-budget cascade preserved the answer-bearing chunk at 99.58%-100% recall using 1,024-8,192 tokens, while matching CUDA attention proxy sequence lengths were 3.43x-42.21x faster than the 16,384-token proxy.

## Why it stopped

This run produced proxy useful-signal evidence only; it is not a full validation of long-context home inference quality or end-to-end serving performance.

## Recommended next action

Run a bounded real-model deepen test on GB10 using a small local long-context-capable model and a real long-context QA dataset, comparing cascade, full context, truncation, and retrieval baselines on answer quality plus end-to-end prefill/decode latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model GB10 validation of token-budget cascade for long-context QA
- Success threshold: Cascade retains at least 90% of full-context answer quality and reduces median end-to-end latency by at least 2x, while beating prefix truncation and random/retrieval controls on quality at the same token budget.
- Stop condition: Stop as negative if cascade quality falls below 80% of full-context quality, fails to beat truncation/retrieval controls, or latency improvement is below 1.5x at the best budget.

## Evidence references

- Artifact root: `<local-path>/projects/token-budget-cascade-for-long-context-home-inference-on-gb10-98812a8100aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
