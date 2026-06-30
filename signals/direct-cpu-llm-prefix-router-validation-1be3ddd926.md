# Direct CPU LLM prefix-router validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-cpu-llm-prefix-router-validation-1be3ddd926`
Run ID: `direct-cpu-llm-prefix-router-validation-1be3ddd926-20260605T003013922240+0000`

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

- Parent run decision: Prefix KV reuse router for CPU local serving: enoch://control-plane/projects/prefix-kv-reuse-router-for-cpu-local-serving-25f824ddff05/runs/prefix-kv-reuse-router-for-cpu-local-serving-25f824ddff05-20260604T192532772861+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/cc28ee7c2dd8

## What looked useful

Core exact-prefix KV reuse worked directly on a real CPU causal LM: 74.10% nominal input-token reduction, zero max suffix-logit difference, and 1.99x median shared-prefix speedup. A first smoke run also showed that mutable cache reuse across suffixes is unsafe unless each routed request receives an isolated cache state.

## Boundaries and scale limits

Single tiny model, one synthetic-but-direct shared-prefix prompt set, sequential CPU execution, no production queueing, no batched serving, no persistent cache eviction policy, and one noisy fallback-control timing sample exceeded the predeclared all-samples threshold.

## Claim scope

On a tiny GPT-2 causal LM running on CPU, exact shared-prefix routing that computes the prefix KV cache once and gives each suffix an isolated copy of that cache preserved suffix logits exactly and improved median latency by 1.99x on a six-request shared-prefix workload.

## Why it stopped

No-paper useful signal: the direct small test supports the mechanism, but it is tiny-model evidence and the predeclared aggregate Tier 1 success flag failed because one no-shared-prefix fallback control sample exceeded the 2.0x upper bound.

## Recommended next action

Run a bounded medium confirmation on a GPT-2-small-class or comparable CPU-deployable LM with realistic mixed prefix-reuse traces, explicit cache-memory accounting, and stable fallback-overhead measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium CPU prefix-router validation on GPT-2-small-class mixed traces
- Success threshold: Max suffix-logit difference <= 1e-4, median shared-prefix speedup >= 1.3x, p95 shared-prefix speedup >= 1.0x, no-shared-prefix fallback median overhead <= 1.25x and p95 <= 1.75x, with cache memory reported for at least 8 active prefixes.
- Stop condition: Stop as negative if logits diverge above 1e-4 after correct cache isolation, if median shared-prefix speedup is below 1.1x, or if fallback overhead/memory growth removes the practical latency benefit on the mixed workload.

## Evidence references

- Artifact root: `<local-path>/projects/direct-cpu-llm-prefix-router-validation-1be3ddd926`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
