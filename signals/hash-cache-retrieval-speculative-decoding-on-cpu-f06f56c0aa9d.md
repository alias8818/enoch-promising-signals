# Hash-Cache Retrieval Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-cache-retrieval-speculative-decoding-on-cpu-f06f56c0aa9d`
Run ID: `hash-cache-retrieval-speculative-decoding-on-cpu-f06f56c0aa9d-20260620T024640717492+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1c521c1789c1

## What looked useful

Hash-cache drafts were exact after verification and gave modeled speedups at verification cost 0.25 of 2.50x for high_reuse_clean and 2.03x for medium_reuse_clean, but collapsed to about break-even for adversarial_random. A 12-bit collision stress test stayed exact but pushed low_reuse below break-even.

## Boundaries and scale limits

No real transformer, tokenizer, KV-cache, batching, or serving stack was tested. Wall-clock speedups are modeled from oracle-call reductions plus assumed verification costs, not measured LLM latency. Synthetic recurrence regimes may overstate real workload reuse.

## Claim scope

In a deterministic synthetic oracle-stream proxy, multi-token hash-cache retrieval speculative decoding preserved exact output under verification and reduced modeled oracle calls when decode contexts recurred from the cache-build half of the stream.

## Why it stopped

Stopped after bounded CPU proxy evidence: the mechanism is recurrence-dependent and promising enough for direct model-serving follow-up, but proxy-only modeled speedups are not sufficient for a paper-positive claim.

## Recommended next action

Implement the same exact-verification protocol around a small CPU-served transformer and measure real tokens/sec against greedy decoding on recurrent and low-reuse prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer CPU hash-cache speculative decoding latency test
- Success threshold: At least 1.20x measured end-to-end decode tokens/sec on recurrent prompts with exact output match and no more than 5% slowdown on low-reuse controls.
- Stop condition: Stop if exact verification cannot be integrated locally, or if recurrent prompts show less than 1.10x measured speedup after context/draft/cache ablations.

## Evidence references

- Artifact root: `<local-path>/projects/hash-cache-retrieval-speculative-decoding-on-cpu-f06f56c0aa9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
