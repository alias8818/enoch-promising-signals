# Model-tokenized serving replay for prompt-prefix lookup latency

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `model-tokenized-serving-replay-for-prompt-prefix-lookup-la-0c3c1292ce`
Run ID: `model-tokenized-serving-replay-for-prompt-prefix-lookup-la-0c3c1292ce-20260523T093842821145+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Serving endpoint prompt-lookup latency distribution on natural repeated-context workloads: enoch://control-plane/projects/serving-endpoint-prompt-lookup-latency-distribution-on-nat-057e7fad9b/runs/serving-endpoint-prompt-lookup-latency-distribution-on-nat-057e7fad9b-20260523T092544597224+0000
- Parent run decision: Integrated prompt-lookup latency benchmark on a local 3B-8B serving model: enoch://control-plane/projects/integrated-prompt-lookup-latency-benchmark-on-a-local-3b-8-5724d3b8eb/runs/integrated-prompt-lookup-latency-benchmark-on-a-local-3b-8-5724d3b8eb-20260523T072915198369+0000

## What looked useful

Model-tokenized replay substantially changes measured prompt-prefix lookup latency by removing online tokenization from the lookup path. Raw text plus tokenization measured 276.05 us median versus 10.46 us for pre-tokenized token lookup, with 0 validation mismatches across 48,000 generated queries.

## Boundaries and scale limits

Synthetic serving-like prompts only; Python trie rather than production vLLM/SGLang/TensorRT-LLM prefix-cache code; no real production/public chat trace; no end-to-end GPU serving, scheduler, KV-memory, or multi-tenant contention measurement.

## Claim scope

In a deterministic CPU prefix-cache benchmark using GPT-2 tokenization, 3 fixed seeds, 48,000 total replay queries, and the same token-prefix trie backend, pre-tokenized replay measured prompt-prefix lookup directly and avoided the online tokenization cost that made raw-text replay about 26.4x slower at median latency.

## Why it stopped

Bounded local evidence supports the mechanism, but the result is synthetic and implementation-local rather than direct production-serving evidence.

## Recommended next action

Stop as no-paper useful signal; next run should replay the same harness on a public ShareGPT/LMSYS-style trace with at least two production tokenizers and one production prefix-cache implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public-trace tokenized replay validation for prompt-prefix lookup latency
- Success threshold: Median and p95 raw-text replay latency are at least 5x slower than pre-tokenized replay on both tokenizers, with zero token-prefix validation mismatches and the production implementation showing the same direction of effect.
- Stop condition: Stop if public-trace validation shows less than 2x median benefit, any unresolved token-prefix mismatch, or production implementation measurements are dominated by unrelated overhead that cannot be isolated.

## Evidence references

- Artifact root: `<local-path>/projects/model-tokenized-serving-replay-for-prompt-prefix-lookup-la-0c3c1292ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
