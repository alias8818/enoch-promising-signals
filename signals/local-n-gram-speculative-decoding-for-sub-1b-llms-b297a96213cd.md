# Local n-Gram Speculative Decoding for Sub-1B LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-n-gram-speculative-decoding-for-sub-1b-llms-b297a96213cd`
Run ID: `local-n-gram-speculative-decoding-for-sub-1b-llms-b297a96213cd-20260607T231445347675+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e3a7643c1d8a

## What looked useful

Coding prompts improved from 110.4 tok/s baseline to 180.8-200.8 tok/s for k4/k8 lookup (1.64x-1.82x); repetitive prompts improved to 131.1-147.8 tok/s (1.19x-1.34x); natural prompts slowed to 101.5-103.8 tok/s (0.92x-0.94x). Candidate match/proposed ratios were highest for coding k1 at 0.624 and very low for natural k8 at 0.026. Longer lookup runs mismatched greedy baseline outputs in most samples, so this is not a drop-in exact speedup result.

## Boundaries and scale limits

Single sub-1B model, synthetic prompt categories, 12 prompts, 2 repeats, 96 generated tokens, no serving stack, no batching, no multi-model robustness, no production latency distribution, and exactness issue not root-caused.

## Claim scope

Bounded local benchmark on cached Qwen/Qwen2.5-0.5B-Instruct using Transformers prompt_lookup_num_tokens on one GB10 GPU: prompt-local n-gram lookup can improve greedy generation throughput for coding/template and repetitive prompts, but slows natural prompts and did not preserve greedy-output identity in longer generations.

## Why it stopped

Bounded direct evidence found workload-sensitive speedups but also a blocking exactness caveat for paper claims; this is a useful local signal rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should isolate token-level exactness in the installed prompt lookup path and test a corrected greedy-equivalent implementation before any broader throughput validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exactness audit for local n-gram prompt lookup speculative decoding
- Success threshold: Zero output mismatches across the benchmark suite while preserving at least 1.3x mean throughput on coding/template prompts and no more than 5% slowdown on natural prompts.
- Stop condition: Stop if exact greedy equivalence cannot be achieved in a minimal verifier or if enforcing exactness removes the coding/template speedup below 1.1x.

## Evidence references

- Artifact root: `<local-path>/projects/local-n-gram-speculative-decoding-for-sub-1b-llms-b297a96213cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
