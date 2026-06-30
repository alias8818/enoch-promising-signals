# Suffix-tree speculative decoding with adaptive AR fallback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-with-adaptive-ar-fallback-5f40a3b087fc`
Run ID: `suffix-tree-speculative-decoding-with-adaptive-ar-fallback-5f40a3b087fc-20260620T091307454699+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e6b3b3c57690

## What looked useful

Suffix speculation achieved 5.415 tokens/target-call on high-reuse traces and 2.98 on drifting-reuse traces versus 1.0 for AR. On low-reuse traces, adaptive fallback reduced zero-accept calls from about 9829 to 3250 and Python wall time from 36.27 ms to 11.33 ms, but target-call reduction fell to 3.1%.

## Boundaries and scale limits

No real LLM, tokenizer, KV-cache, GPU serving, sampling-quality, or end-to-end latency validation was run. The benchmark used 60k-token synthetic training traces, 12k-token synthetic target traces, 6 seeds per scenario, exact-token acceptance, and one Python process.

## Claim scope

Synthetic trace-level proxy only: a bounded suffix index over reusable token traces can reduce target verification calls on high-reuse and drifting-reuse sequences, and adaptive AR fallback can reduce low-reuse speculative overhead.

## Why it stopped

No-paper closure: this run produced useful synthetic mechanism evidence, but it is proxy-only and cannot validate real LLM speculative decoding performance.

## Recommended next action

Run one bounded direct small-LM follow-up using the same suffix/adaptive policies against a local GPT-2-small-class or smaller target on repetition-heavy and low-reuse text, measuring end-to-end latency, target calls, acceptance, and quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-LM validation of suffix-index speculative decoding with adaptive AR fallback
- Success threshold: Across at least 5 seeds or prompt shards, adaptive suffix speculation improves repetition-heavy end-to-end tokens/sec by at least 20% over AR with no output mismatch in greedy mode, and low-reuse tokens/sec remains no worse than 10% below AR.
- Stop condition: Stop if repetition-heavy acceptance stays below 0.20 or end-to-end tokens/sec is not improved over AR after implementation overhead is included, or if low-reuse overhead exceeds 10% despite fallback.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-with-adaptive-ar-fallback-5f40a3b087fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
