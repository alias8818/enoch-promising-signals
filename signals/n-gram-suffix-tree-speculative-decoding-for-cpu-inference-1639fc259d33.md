# N-Gram Suffix-Tree Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-for-cpu-inference-1639fc259d33`
Run ID: `n-gram-suffix-tree-speculative-decoding-for-cpu-inference-1639fc259d33-20260614T014511950698+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c17567e767f8

## What looked useful

Order-4 suffix drafting with draft length 8 reached 78.78% acceptance, 85.90% verifier-call reduction, and 1.198x modeled speedup. Order-1 and order-2 drafters were below break-even, while order-6/order-8 controls reached about 1.43x modeled speedup.

## Boundaries and scale limits

No transformer LLM was run; verifier cost is proxied by NumPy dense matrix batch timings. The target is an 8-gram model, and order-8 drafter results are an upper-bound control rather than independent evidence.

## Claim scope

Bounded proxy evidence on heldout Tiny Shakespeare shows that high-order suffix n-gram drafters can reduce deterministic verifier calls enough to beat a single-thread CPU dense-matrix verifier cost model, while shallow drafters do not.

## Why it stopped

Proxy result is useful but insufficient for a paper: it validates the acceptance/call-reduction mechanism only against an n-gram target and a dense-matrix verifier cost model.

## Recommended next action

Run a bounded direct follow-up using a small CPU LLM with real KV-cache speculative verification and measure tokens/sec plus latency against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM verification for suffix n-gram speculative decoding
- Success threshold: At least 1.10x wall-clock tokens/sec improvement over greedy decoding on a small CPU LLM with no output mismatches and p95 latency not worse by more than 10%.
- Stop condition: Stop if acceptance is below 60% for draft length 4 or if measured wall-clock throughput is below 1.0x after verifier batching is enabled.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-for-cpu-inference-1639fc259d33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
