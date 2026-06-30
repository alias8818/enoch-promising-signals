# N-gram Speculative Draft for Local GPU Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-local-gpu-serving-c81b7ab29dfe`
Run ID: `n-gram-speculative-draft-for-local-gpu-serving-c81b7ab29dfe-20260529T054453296436+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/84537678186a

## What looked useful

N-gram speculative drafting has a real local mechanism signal but is workload-sensitive: copy prompts reached about 2.3x target-call reduction while structured/code/freeform prompts were closer to 1.2x-1.6x. The result justifies a direct serving benchmark, not a paper claim.

## Boundaries and scale limits

Proxy-only acceptance simulation; no end-to-end serving latency, scheduler overhead, batched verification, larger model, longer context, or production trace validation was run.

## Claim scope

On eight small local-generation traces from SmolLM2-135M-Instruct, offline vLLM-style n-gram prompt lookup reduced idealized conservative target calls by 1.46x-1.66x across tested settings, with strongest benefit on copy-heavy prompts.

## Why it stopped

Stopped after a bounded proxy useful-signal run because end-to-end serving evidence is required before any paper or production throughput claim.

## Recommended next action

Run a direct vLLM GB10 serving benchmark with n-gram speculation enabled versus disabled on the same prompt suite, recording tokens/s, TTFT, ITL, GPU utilization, and speculative acceptance counters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GB10 vLLM Serving Benchmark for N-gram Speculative Decoding
- Success threshold: >=15% measured throughput or ITL improvement on aggregate and >=25% on copy-heavy prompts, with <=10% TTFT regression and no correctness failures.
- Stop condition: Stop if measured aggregate throughput/ITL improvement is <5% or TTFT regresses >20% after tuning one reasonable n-gram/draft setting.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-local-gpu-serving-c81b7ab29dfe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
