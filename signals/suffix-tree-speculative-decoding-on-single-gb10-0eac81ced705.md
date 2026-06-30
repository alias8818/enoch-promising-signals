# Suffix-tree speculative decoding on single gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-single-gb10-0eac81ced705`
Run ID: `suffix-tree-speculative-decoding-on-single-gb10-0eac81ced705-20260629T190201918345+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cdcc5f8089e1

## What looked useful

The mechanism is locally reproducible on GB10: suffix-cache drafts can be verified greedily with exact output equality and substantial target-forward-call reduction on repetitive prompts. Standalone novelty is weak because public SuffixDecoding prior art already exists, and the local timing result is not production-grade.

## Boundaries and scale limits

Synthetic prompts only; small 0.5B model; baseline and verifier use full-prefix Hugging Face forwards rather than production KV-cache/vLLM decoding; no real agent/code/text-to-SQL traces; no comparison against production SuffixDecoding, REST, SpecInfer, Medusa, EAGLE, or vLLM n-gram speculative decoding.

## Claim scope

On a single GB10 with Qwen/Qwen2.5-0.5B-Instruct and six synthetic repetitive prompts, a local suffix-index speculative verifier preserved exact greedy output and reduced target forward calls by 68.75%-85.76% across draft-length controls; the clean leave-one-out max_draft=8 run reduced calls by 79.17% with 72.68% draft-token acceptance.

## Why it stopped

Useful bounded mechanism signal but not paper-ready: the algorithm is prior art and the evidence is synthetic, small-model, and non-production.

## Recommended next action

Stop this no-paper run; a bounded deepen follow-up should implement KV-cache or vLLM-backed verification and evaluate real repetitive traces against a production n-gram/suffix baseline on the same GB10.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache suffix speculative decoding on real repetitive traces
- Success threshold: At least 15% TPOT or end-to-end throughput improvement over optimized greedy on real repetitive traces, with exact greedy output equality and memory/CPU overhead documented.
- Stop condition: Stop if acceptance is below 30%, exact greedy equality fails, or production-like KV-cache overhead eliminates latency gains on the first two trace families.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-single-gb10-0eac81ced705`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
