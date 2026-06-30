# N-Gram Suffix-Tree Speculative Decoding on Home GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-on-home-gpus-31f66d004979`
Run ID: `n-gram-suffix-tree-speculative-decoding-on-home-gpus-31f66d004979-20260610T024539765125+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a7be01676626

## What looked useful

High-overlap copy/edit and iterative-code traces reached 12.7x to 14.4x ideal target-pass speedup with Python CPU proposer throughput above 70k target tokens/s, while adjacent low-overlap prose reached only 1.16x ideal speedup with 2.8% proposal-token match rate and a random disjoint control stayed at 1.0x.

## Boundaries and scale limits

No integrated LLM verifier, vLLM/TensorRT-LLM serving run, GPU utilization measurement, batching test, CUDA graph measurement, or latency percentile measurement was performed. Workloads were local deterministic traces, not broad production traffic.

## Claim scope

Deterministic local token-trace simulation of a CPU-side n-gram/suffix exact-match proposer on five bounded workloads showed large ideal target-pass reductions only when outputs copied or lightly edited prompt/recent-context text; low-overlap and disjoint controls showed weak or no benefit.

## Why it stopped

No-paper useful signal: proxy evidence supports the mechanism in high-overlap traces but does not validate end-to-end home-GPU serving speedups, and the general n-gram/suffix speculative decoding idea has existing prior art.

## Recommended next action

Stop paper path for this run; if continuing, run a bounded integrated GB10 serving follow-up using vLLM or TensorRT-LLM n-gram/suffix speculation on high-overlap code/edit/RAG prompts plus low-overlap controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated GB10 serving benchmark for n-gram/suffix speculation on high-overlap workloads
- Success threshold: At least 1.25x end-to-end tokens/sec or p50 latency improvement on high-overlap workloads with no degradation on exact-output greedy checks and less than 5% regression on low-overlap controls.
- Stop condition: Stop if integrated overhead erases the high-overlap benefit below 1.10x, if setup cannot run a supported local model on GB10, or if low-overlap workloads regress by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-on-home-gpus-31f66d004979`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
