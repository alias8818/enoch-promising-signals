# End-to-end KV-cache latency test for n-gram draft cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-kv-cache-latency-test-for-n-gram-draft-cascades-12a82fca62`
Run ID: `end-to-end-kv-cache-latency-test-for-n-gram-draft-cascades-12a82fca62-20260522T031033207631+0000`

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

- Parent run decision: N-gram Speculative Draft Cascade for Local Inference: enoch://control-plane/projects/n-gram-speculative-draft-cascade-for-local-inference-438d6f399d20/runs/n-gram-speculative-draft-cascade-for-local-inference-438d6f399d20-20260522T012822208311+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/097ee83fc7b8

## What looked useful

Exact n-gram speculative verification can convert repeated context structure into fewer target forwards and lower latency, but proposal gating matters: unigram fallback caused ordinary-prompt regressions in 2 of 4 cases, and removing unigrams eliminated those regressions in this small run.

## Boundaries and scale limits

Small Tier 1 direct test only: GPT-2, 8 prompts, 64 generated tokens per prompt, Hugging Face Python implementation, greedy decoding only, no batching, no paged attention, no production serving, no 7B+ model, and no real traffic traces.

## Claim scope

On GPT-2 batch-size-1 greedy decoding with real CUDA KV-cache inference, n-gram draft cascades preserved exact greedy outputs and reduced end-to-end latency on repetition-heavy prompts; naive unigram fallback can regress ordinary prompts, while a no-unigram gate improved this small ordinary-prompt suite.

## Why it stopped

Small direct evidence is useful but mixed and not publication-grade; this closes as no-paper useful signal rather than full validation.

## Recommended next action

Run a bounded deepen follow-up with no-unigram and adaptive acceptance-gated cascades across a larger prompt suite and at least one larger local model; stop short of paper claims until the latency benefit survives broader prompt/model coverage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive proposal gating for n-gram KV-cache draft cascades
- Success threshold: Adaptive or no-unigram gating achieves at least 1.2x mean speedup with no more than 5% prompt-level latency regressions and exact greedy equivalence across the tested prompt/model suite.
- Stop condition: Stop if exactness fails, if mean speedup is below 1.1x, or if more than 10% of ordinary prompts regress after gating.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-kv-cache-latency-test-for-n-gram-draft-cascades-12a82fca62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
