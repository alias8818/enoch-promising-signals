# N-Gram Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-on-cpu-767426187e9f`
Run ID: `n-gram-draft-speculative-decoding-on-cpu-767426187e9f-20260609T084011847839+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47ec9868743a

## What looked useful

N-gram drafting can reduce target calls in repetitive text, but for CPU inference the win depends strongly on cheap draft tokens and efficient batched verification. A batch-12 matmul proxy cost 3.50x a batch-1 call; with that adjustment, the best setting estimates about 1.07x speedup at 1% draft-token cost and 0.94x at 5% draft-token cost.

## Boundaries and scale limits

No real transformer, tokenizer, KV cache, or production CPU inference runtime was tested. The target model is a cheap n-gram proxy, and the CPU batch-cost proxy is one dense NumPy matmul rather than a full transformer verification pass.

## Claim scope

On a byte-level Tiny Shakespeare proxy with an order-8 n-gram target, an order-6 n-gram draft with draft_k=12 reduced target calls to about 3.86 decoded tokens per target call across four runs, but CPU batch-cost and draft-token overhead reduce the modeled speedup to a narrow or negative margin.

## Why it stopped

Proxy evidence is mixed: target-call reduction is supported, but actual toy runtime is slower and batch-adjusted CPU speedup is too marginal for a paper-positive claim.

## Recommended next action

Stop this worker run as no-paper useful signal; run a bounded direct CPU benchmark in a real small-LLM runtime before making any serving-speedup claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM Benchmark for N-Gram Draft Speculative Decoding
- Success threshold: At least 1.15x wall-clock tokens/s over baseline greedy decoding with exact greedy-output parity on two or more prompt domains, and no domain below 0.95x.
- Stop condition: Stop if exact parity cannot be maintained, if acceptance stays below 20% at draft_k<=12, or if wall-clock throughput remains below 1.05x after measuring and tuning verification batch size.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-cpu-767426187e9f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
