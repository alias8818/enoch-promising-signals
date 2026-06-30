# Real-model trace replay for tiny neural tool-call draft decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-trace-replay-for-tiny-neural-tool-call-draft-de-3e959f800f`
Run ID: `real-model-trace-replay-for-tiny-neural-tool-call-draft-de-3e959f800f-20260526T131911228248+0000`

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

- Parent run decision: Tiny Draft Model for Tool-Call Speculative Decoding: enoch://control-plane/projects/tiny-draft-model-for-tool-call-speculative-decoding-ac4373435a92/runs/tiny-draft-model-for-tool-call-speculative-decoding-ac4373435a92-20260526T042101316820+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/32cdf8380d92

## What looked useful

Include strong n-gram or trie replay controls before claiming value from tiny neural tool-call draft decoding. In the primary Qwen run the GRU beat 2-gram replay but lost to 4-gram replay: 2.2178 vs 2.4659 mean accepted tokens/block and 0.8750 vs 0.8958 next-token accuracy.

## Boundaries and scale limits

Tested only Qwen/Qwen2.5-0.5B-Instruct and HuggingFaceTB/SmolLM2-135M-Instruct, short 48-token continuations, synthetic prompts, greedy traces, and offline trace acceptance rather than an integrated speculative decoder. Qwen outputs were tool-call-like but not consistently strict compact JSON; SmolLM often echoed tool specs.

## Claim scope

Small real-model greedy trace replay tests for synthetic tool-use prompts: a tiny GRU draft did not reliably outperform a strong 4-gram trace replay baseline on held-out tool-call-like continuations.

## Why it stopped

Primary direct small test failed the useful-signal threshold against the best simple replay control; this is not a full validation, but it is enough to prevent a paper claim from this branch.

## Recommended next action

Stop this branch as no-paper evidence; a bounded follow-up should use strict JSON/tool-call traces and compare neural, trie/ngram, and hybrid draft policies under the same acceptance metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Strict JSON tool-call trace replay with trie and neural-hybrid draft controls
- Success threshold: Hybrid or neural draft improves mean accepted tokens per block by at least 15% relative over the best pure trie/ngram replay control while maintaining equal or better malformed-output rate.
- Stop condition: Stop if pure replay remains within 5% of the best neural/hybrid policy or if target traces are not strict valid tool-call JSON.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-trace-replay-for-tiny-neural-tool-call-draft-de-3e959f800f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
