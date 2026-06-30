# Suffix-Ngram Speculative Decoding for Local LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-ngram-speculative-decoding-for-local-llms-c57facfe1a5e`
Run ID: `suffix-ngram-speculative-decoding-for-local-llms-c57facfe1a5e-20260612T051125069760+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/310bf9c9a430

## What looked useful

Incremental suffix lookup matched linear prompt lookup acceptance while making lookup overhead negligible on these traces. Best settings used n=2 or n=3 with max_draft=16, yielding mean estimated speedups of 2.49x to 3.61x under the local-forward latency model. The mechanism is promising for copy-heavy code/JSON/prose continuations but not paper-ready.

## Boundaries and scale limits

No real local LLM was run. Results use synthetic traces, regex tokenization, exact-match oracle continuations, and a simple latency model with a 55 ms target-forward assumption. They do not validate wall-clock speedup, KV-cache behavior, tokenizer effects, batching, sampled decoding quality, or broad non-repetitive workloads.

## Claim scope

Trace-level oracle simulation on synthetic repetitive local-style workloads shows exact suffix/ngram drafting can reduce verifier target calls by about 61-73% when continuations reuse prior prompt/generated text.

## Why it stopped

Stopped after bounded trace evidence because the result is proxy/oracle evidence and prior art already covers suffix and n-gram speculative decoding; it is useful for selecting a direct benchmark but not sufficient for a paper.

## Recommended next action

Run a direct local inference benchmark in llama.cpp or vLLM on a small instruct/code model, comparing greedy baseline versus n-gram/suffix drafting on the same repetitive code-edit and JSON-continuation tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local-LLM benchmark for suffix/ngram drafting on repetitive continuations
- Success threshold: At least 25% median wall-clock tokens/s improvement on repetitive code/JSON workloads with output equality to greedy baseline and less than 5% slowdown on non-repetitive controls.
- Stop condition: Stop if median wall-clock speedup is below 10% on both repetitive workloads or if output equality/quality diverges under greedy verification.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-ngram-speculative-decoding-for-local-llms-c57facfe1a5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
