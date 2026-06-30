# Small-LLM serving test for dynamic n-gram speculative cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-llm-serving-test-for-dynamic-n-gram-speculative-cach-7eef9f09cc`
Run ID: `small-llm-serving-test-for-dynamic-n-gram-speculative-cach-7eef9f09cc-20260609T013340496686+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Dynamic n-gram cache for speculative decoding: enoch://control-plane/projects/dynamic-n-gram-cache-for-speculative-decoding-8d0d083cc3fa/runs/dynamic-n-gram-cache-for-speculative-decoding-8d0d083cc3fa-20260608T223915352511+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0547e56fa3bc

## What looked useful

Calibrated Tier 1 run had 0 exact-output failures, 5.099x median best dynamic speedup on repeat/mixed prompts, 3.208x best dynamic speedup on low-repeat prompt after generated structure emerged, and +0.866x median dynamic advantage over prompt-static ablation.

## Boundaries and scale limits

The target model is not a transformer and the per-call cost is a deterministic CPU simulation of serving overhead; results do not validate GPU kernels, transformer KV-cache behavior, tokenizer effects, real request traces, batching contention, or quality on natural corpora.

## Claim scope

In a controlled CPU word-level n-gram target-model serving harness with chunk verification, a dynamic n-gram speculative cache preserved exact target-greedy output and improved throughput on repeated-structure prompts.

## Why it stopped

No-paper closure: this Tier 1 direct mechanism test passed its threshold but remains a controlled n-gram target proxy rather than publication-grade transformer serving evidence.

## Recommended next action

Run a bounded real-transformer follow-up using a small causal LM with logits/KV-cache verification, comparing greedy decoding, prompt-static n-gram speculation, and dynamic n-gram speculation on repeated-prefix and low-repeat prompt traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer serving ablation for dynamic n-gram speculative cache
- Success threshold: Zero exact-output mismatches; at least 1.15x median throughput improvement for dynamic n-gram speculation over greedy on repeated-prefix/mixed prompts; dynamic must outperform prompt-static by at least 10% on prompts where repetition emerges after generation starts; no more than 10% regression on low-repeat prompts.
- Stop condition: Stop if real-transformer verification cannot preserve exact greedy output, if repeated-prefix speedup is below 1.15x, or if low-repeat prompts regress by more than 10% after tuning draft length and n-gram order.

## Evidence references

- Artifact root: `<local-path>/projects/small-llm-serving-test-for-dynamic-n-gram-speculative-cach-7eef9f09cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
