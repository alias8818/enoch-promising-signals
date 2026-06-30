# N-gram draft speculative decode for CPU-GPU cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decode-for-cpu-gpu-cascade-326f0911e853`
Run ID: `n-gram-draft-speculative-decode-for-cpu-gpu-cascade-326f0911e853-20260527T115253214782+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/be54152da6c1

## What looked useful

History/prompt lookup n-grams are a plausible CPU drafter mechanism for CPU-GPU speculative decode; static corpus n-grams alone look weak under this bounded probe.

## Boundaries and scale limits

Trace simulation and small-model GPU forward probes only; no integrated speculative serving loop, no large model validation, no sampling-mode validation, and no production scheduler or batching effects.

## Claim scope

On 96 WikiText-2 validation prompts with distilgpt2 greedy continuations, history-based n-gram drafting reduced simulated verifier calls by about 72-74%, while a static corpus n-gram drafter reduced calls by only about 16%.

## Why it stopped

Evidence supports a bounded mechanism but not a publication-grade or production-speed claim; current result is trace simulation plus latency probing rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement an integrated KV-cache speculative decode path and require at least 1.25x end-to-end tokens/s speedup on two small-to-medium causal LMs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated history n-gram speculative decode wall-clock benchmark
- Success threshold: At least 1.25x end-to-end tokens/s speedup on both target models with identical greedy outputs and no material memory-pressure regression.
- Stop condition: Stop as negative if integrated speedup is below 1.10x on either model or if CPU draft overhead/scheduler effects erase the simulated verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decode-for-cpu-gpu-cascade-326f0911e853`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
