# Suffix-Tree Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-cpu-b5b00e95d8e3`
Run ID: `suffix-tree-speculative-decoding-on-cpu-b5b00e95d8e3-20260621T205602565827+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3cfee0d59dca

## What looked useful

Suffix-index drafting reduced theoretical target verification calls by 82.3% on a repeated synthetic trace and 49.4% on local project text, but had effectively zero benefit on random traces and incurred 178-309 us/token overhead for the best long-context configs on repeat-bearing traces.

## Boundaries and scale limits

No real LLM target model, no transformer KV-cache verification, no production suffix-tree implementation, and traces are at most 16000 tokens. Results support only mechanism-level workload sensitivity, not end-to-end decoding speedup.

## Claim scope

Trace-level CPU benchmark of online suffix-index speculative drafting over bounded synthetic and local-text token traces, measuring oracle acceptance, target-call reduction, proposer overhead, and memory growth.

## Why it stopped

Bounded local trace evidence is useful but not paper-ready; this is a proxy/mechanism test rather than full validation of CPU LLM serving speedup.

## Recommended next action

Run a direct CPU LLM decoding follow-up with a small local model and an optimized suffix/prompt-lookup proposer to verify whether the trace-level call reductions survive real target verification costs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU LLM suffix-index speculative decoding benchmark
- Success threshold: At least 1.2x end-to-end tokens/sec improvement on repeated/code-like traces with no regression greater than 5% on low-repetition traces, measured over at least three seeds or prompts per workload class.
- Stop condition: Stop if proposer overhead exceeds saved target verification time on repeated/code-like traces or if acceptance remains below 0.5 accepted tokens per draft on direct model runs.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-cpu-b5b00e95d8e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
