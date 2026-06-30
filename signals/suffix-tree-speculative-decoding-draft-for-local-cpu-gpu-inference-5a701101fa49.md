# Suffix-tree speculative decoding draft for local CPU/GPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-draft-for-local-cpu-gpu-inference-5a701101fa49`
Run ID: `suffix-tree-speculative-decoding-draft-for-local-cpu-gpu-inference-5a701101fa49-20260630T170223138631+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3a52a3160c0f

## What looked useful

Primary medium proxy over 50k-token traces and 7 seeds showed estimated verifier-call reductions of 2.79x to 4.11x on naturalish/schema-repeat traces, 2.22x to 3.05x on RAG-copy traces, and 1.0x on random controls. Mean proposal overhead was about 3.7 to 7.4 microseconds with p99 near 20 microseconds.

## Boundaries and scale limits

No target LLM, GPU verifier, KV-cache, batching, sampling, or real serving latency was measured. The traces are generated proxies, not production request logs. Public related work already covers suffix-tree, n-gram trie, suffix automaton, and learning-free n-gram speculative decoding.

## Claim scope

In offline token-trace proxy tests, a dynamic suffix-context draft proposer achieved useful exact-match draft acceptance on repetition-heavy synthetic local-inference traces with microsecond-scale CPU lookup overhead, while providing no benefit on random traces.

## Why it stopped

Proxy evidence supports the mechanism in repeated-token regimes but does not validate end-to-end local CPU/GPU inference speedup, and current public work already covers the broad suffix-structure speculative decoding idea.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is a direct local verifier integration against llama.cpp, vLLM, or a small Transformers model with prompt-lookup and no-speculation baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local LLM suffix-draft verification benchmark
- Success threshold: At least 15% wall-clock tokens/sec improvement over no speculation on repeated agent/RAG prompts, no regression on random/no-overlap prompts beyond 5%, and identical deterministic outputs.
- Stop condition: Stop if accepted tokens per verifier call stays below 1.2x or wall-clock tokens/sec improvement is below 5% on repeated prompts after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-draft-for-local-cpu-gpu-inference-5a701101fa49`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
