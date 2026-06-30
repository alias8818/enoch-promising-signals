# N-Gram Speculative Draft for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-cpu-inference-e88e4b32e945`
Run ID: `n-gram-speculative-draft-for-cpu-inference-e88e4b32e945-20260522T144905139942+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/85a4b29ef1ec

## What looked useful

N-gram drafting is workload-sensitive: best simulated target-call reduction was 14.16% on package docs, 36.52% on Python stdlib code, and 84.34% on repetitive structured logs. This supports a bounded mechanism for templated/code-like workloads but not a broad CPU inference acceleration claim.

## Boundaries and scale limits

No real transformer/LLM target model was run; verifier batching cost, KV-cache behavior, tokenizer effects, sampling, and end-to-end CPU tokens/s remain untested. Calibrated run used 20k eval tokens per eligible corpus and completed in 276.85 s.

## Claim scope

Dependency-free exact-token trace simulation of online prompt-lookup and static n-gram drafters on local code/docs plus a repetitive structured-log control; reports simulated target-call reduction, acceptance, and lookup overhead, not real LLM serving latency.

## Why it stopped

Proxy evidence is useful but insufficient for paper-positive closure; it measures exact-trace call reduction rather than real CPU LLM latency.

## Recommended next action

Stop this proxy run; next bounded action is an end-to-end CPU inference benchmark with the same online n-gram drafter in a small real model/runtime.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU benchmark for online n-gram speculative drafting
- Success threshold: At least 20% tokens/s improvement on code or templated workloads, less than 5% median slowdown on prose, and byte-identical greedy outputs across paired prompts.
- Stop condition: Stop if end-to-end tokens/s gain is below 10% on both code and templated workloads or if prose regression exceeds 10% after overhead tuning.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-cpu-inference-e88e4b32e945`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
