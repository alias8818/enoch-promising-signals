# Suffix-Trie Tree Speculation Without Draft-Model VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-trie-tree-speculation-without-draft-model-vram-0c972fae9be2`
Run ID: `suffix-trie-tree-speculation-without-draft-model-vram-0c972fae9be2-20260629T142803699253+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f114b7da08bd

## What looked useful

Suffix-trie speculation without draft-model VRAM produced exact greedy-equivalent outputs and a measurable but small target-call reduction on distilgpt2. The effect was parameter-sensitive and absent on tiny-gpt2.

## Boundaries and scale limits

Only tiny-gpt2 and distilgpt2 were tested; workload was Tiny Shakespeare, prompt count was 16 for measurement runs, generation length was 64 tokens, and the harness does not implement production KV-cache serving or large-model inference.

## Claim scope

On a small public text stream with distilgpt2 greedy decoding, a CPU suffix-trie proposer can preserve exact target-model output while reducing target forward calls by 3.2% to 14.6% without loading a draft model.

## Why it stopped

Bounded local evidence supports the mechanism but is too small, synthetic, and parameter-sensitive for a paper-ready claim.

## Recommended next action

Stop as no-paper useful signal; a bounded deepen follow-up should test GPT-2-small-class or similar local models with KV-cache-aware verification on a less repetitive held-out text workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware suffix-trie speculation on a GPT-2-small-class target
- Success threshold: At least 10% target-call reduction and at least 1.10x wall-clock speedup versus a KV-cache greedy baseline while preserving exact output on all prompts.
- Stop condition: Stop if acceptance remains below 3% or wall-clock speedup is below 1.05x after suffix/block tuning on the stronger target model.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-trie-tree-speculation-without-draft-model-vram-0c972fae9be2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
