# Suffix-Tree Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-for-cpu-inference-027c540d3538`
Run ID: `suffix-tree-speculative-decoding-for-cpu-inference-027c540d3538-20260613T233302145575+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e0f0c362574a

## What looked useful

Suffix-index drafting produced 3.31x-3.96x estimated speedup on high-copy repetitive traces and 3.09x-3.58x on noisy repetitive traces, while low-repetition controls stayed near 1.0 accepted token/pass and could regress slightly. Brute PLD showed high CPU scan overhead on low-repetition histories.

## Boundaries and scale limits

No real LLM, tokenizer, attention/tree verification implementation, real agent trace, or end-to-end CPU serving latency was tested. Speedups use a fixed 5 ms target-pass cost assumption plus measured Python lookup overhead.

## Claim scope

Bounded synthetic CPU proxy: an online suffix-index drafter reduces estimated target-model verification passes on repetitive token traces compared with greedy decoding, with much lower lookup overhead than brute prompt-lookup scanning.

## Why it stopped

Proxy-only mechanism evidence is useful but insufficient for a publication-grade CPU inference claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should integrate the suffix-index drafter into a real local CPU LLM decoder and measure end-to-end tokens/sec and latency against greedy and PLD baselines on real repetitive traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU LLM validation of suffix-index speculative decoding
- Success threshold: At least 1.5x end-to-end tokens/sec improvement over greedy on repetitive traces, at least 20% improvement over brute PLD when PLD is enabled, and no more than 5% slowdown on low-repetition controls.
- Stop condition: Stop if real decoder integration shows less than 1.2x speedup on repetitive traces or more than 5% slowdown on low-repetition controls after one bounded tuning pass.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-for-cpu-inference-027c540d3538`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
