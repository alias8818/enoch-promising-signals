# N-gram Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-cpu-inference-fc4e6ecd06aa`
Run ID: `n-gram-speculative-decoding-for-cpu-inference-fc4e6ecd06aa-20260523T064334407231+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1a2919369805

## What looked useful

Across 6000-token proxy corpora, best projected speedups at beta=0.25 were 2.42x for repeated paragraphs, 2.07x for code-like text, 1.95x for structured logs, and 1.00x for random words. The random control had zero accepted draft tokens.

## Boundaries and scale limits

No real transformer was executed; target-model cost was projected with a simple batched-verification cost model over known token streams. The result does not validate end-to-end CPU inference throughput, cache behavior, or latency on production prompts.

## Claim scope

Deterministic proxy evidence shows prompt-local n-gram speculative decoding can reduce target verification calls and projected CPU decode cost on repeat-heavy continuations such as repeated paragraphs, structured logs, and generated code-like text.

## Why it stopped

Stopped at a no-paper useful-signal result because the evidence is a deterministic controller and cost-model proxy, not direct full CPU inference validation.

## Recommended next action

Run a bounded deepen experiment around a real CPU transformer decoder using the same corpora and report exact-output parity, tokens/sec, p50/p95 latency, CPU utilization, and memory counters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer N-gram Speculative Decoding Benchmark
- Success threshold: At least 20% end-to-end tokens/sec improvement on two or more repeat-heavy corpora with exact output parity and no more than 5% slowdown on non-repetitive controls.
- Stop condition: Stop as negative if exact output parity fails, if repeat-heavy speedup is below 10%, or if non-repetitive controls slow down by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-cpu-inference-fc4e6ecd06aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
