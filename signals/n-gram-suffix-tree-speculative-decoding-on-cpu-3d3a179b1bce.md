# N-gram suffix-tree speculative decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-3d3a179b1bce`
Run ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-3d3a179b1bce-20260619T092302523436+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2aca5cca4c60

## What looked useful

Deployable last-occurrence suffix lookup reached 3.075x ideal verifier-call speedup on a templated repeat positive control and 1.318x on a shifted-repeat control, but only 1.013x on contiguous held-out tiny Shakespeare. A non-deployable oracle selector reached only 1.022x on tiny Shakespeare, suggesting the natural-text limitation is low reusable continuation availability rather than just selector quality.

## Boundaries and scale limits

No real CPU LLM verifier, no serving-engine integration, no KV-cache or batching measurement, no tokenizer-specific LLM test, and no broad prompt trace corpus. The speedup metric is generated_tokens / verifier_calls and excludes model forward-pass cost.

## Claim scope

Bounded token-level proxy on tiny Shakespeare plus synthetic repeat controls: a simple bounded n-gram suffix index gives material ideal verifier-call reduction only when repeated continuations are present; it gives essentially no useful upper-bound speedup on ordinary contiguous held-out natural text.

## Why it stopped

Early bounded proxy falsifies the broad/simple claim for ordinary held-out natural text while preserving a narrower workload-dependent mechanism signal for repetitive prompts.

## Recommended next action

Stop this run as no-paper useful signal; only pursue a follow-up if it uses a real CPU LLM serving benchmark on repetition-heavy prompt traces with an end-to-end latency baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM prompt-lookup speculative decoding on repetition-heavy traces
- Success threshold: At least 10% end-to-end tokens-per-second improvement on repetition-heavy traces with no more than 2% regression on ordinary/control traces.
- Stop condition: Stop if accepted draft tokens remain below 5% or end-to-end throughput gain is below 5% after integrating with the real verifier.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-on-cpu-3d3a179b1bce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
