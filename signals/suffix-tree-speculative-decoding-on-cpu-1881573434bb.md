# Suffix-Tree Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-cpu-1881573434bb`
Run ID: `suffix-tree-speculative-decoding-on-cpu-1881573434bb-20260619T103721982260+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/759a0ba33fa6

## What looked useful

Suffix-index drafting reached 6.200 generated tokens per simulated verifier iteration on highly repetitive traces versus 6.196 for ngram4, but tied or slightly trailed ngram4 on mixed/low-repeat workloads and had higher average proposer overhead.

## Boundaries and scale limits

Five-seed CPU-only proxy benchmark over synthetic repeated, mixed, low-repeat, and local scaffold text workloads; no tokenizer-aware LLM verifier, no KV-cache measurement, and no end-to-end CPU model serving latency.

## Claim scope

In deterministic exact-token trace replay, an online suffix-index drafter can reduce simulated verifier iterations on highly repetitive traces, but it does not materially outperform a simpler online 4-gram drafter and does not help low-repeat traces.

## Why it stopped

Proxy evidence supports a narrow repetitive-trace mechanism but not a paper-ready or generally useful CPU speculative decoding claim.

## Recommended next action

Stop this run as no-paper useful signal; the only worthwhile next test is a bounded direct CPU LLM serving benchmark comparing suffix-index, ngram4, and no-draft on real prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM verification for suffix-index drafting
- Success threshold: Suffix-index must improve end-to-end CPU tokens/second by at least 10% over ngram4 on repetitive real prompts without reducing throughput by more than 2% on mixed prompts.
- Stop condition: Stop if suffix-index is within 5% of ngram4 on repetitive prompts or is slower than ngram4 on mixed prompts after a bounded small-model benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-cpu-1881573434bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
