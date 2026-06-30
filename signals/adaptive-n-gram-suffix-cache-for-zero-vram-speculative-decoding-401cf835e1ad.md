# Adaptive N-Gram Suffix Cache for Zero-VRAM Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-n-gram-suffix-cache-for-zero-vram-speculative-decoding-401cf835e1ad`
Run ID: `adaptive-n-gram-suffix-cache-for-zero-vram-speculative-decoding-401cf835e1ad-20260521T211138364359+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5bc501b97cbf

## What looked useful

Corrected proxy benchmark showed adaptive cache target-call reduction of 0.6223 mean across five traces versus 0.6286 for the best fixed n-gram; random control showed 0.0000 reduction, while repetitive/code-like traces showed large modeled reductions.

## Boundaries and scale limits

No live LLM, tokenizer-specific serving stack, GPU/KV-cache interaction, batching, stochastic sampling, or real prompt/output corpus was evaluated. Corpora were small local repeated/code/synthetic/random traces.

## Claim scope

In a deterministic token-trace simulator, a CPU-only n-gram suffix cache can reduce modeled target verification calls on repetitive held-out streams, but the tested adaptive suffix-length policy does not outperform the best fixed n-gram baseline on average.

## Why it stopped

Proxy evidence is useful but not paper-ready: it supports suffix-cache drafting on repetition and early-falsifies the adaptive-policy advantage against fixed n-gram baselines in this harness.

## Recommended next action

Run a bounded deepen test around a real small local LLM speculative-decoding loop and require wall-clock latency plus target-forward reductions, not trace-only modeled calls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Small-LLM Suffix-Cache Speculative Decoding Benchmark
- Success threshold: At least 15% median wall-clock latency reduction and at least 20% target-forward reduction on repeated/code-like prompts, with no output mismatches and adaptive matching or beating the best fixed n-gram baseline.
- Stop condition: Stop if CPU lookup overhead erases latency gains, output equivalence fails, or adaptive remains below the best fixed n-gram baseline on direct LLM runs.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-n-gram-suffix-cache-for-zero-vram-speculative-decoding-401cf835e1ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
