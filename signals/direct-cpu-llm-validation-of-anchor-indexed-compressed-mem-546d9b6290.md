# Direct CPU LLM Validation of Anchor-Indexed Compressed Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-cpu-llm-validation-of-anchor-indexed-compressed-mem-546d9b6290`
Run ID: `direct-cpu-llm-validation-of-anchor-indexed-compressed-mem-546d9b6290-20260621T025705504720+0000`

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

- Parent run decision: Anchor-Indexed Compressed Memory for Long-Context CPU Inference: enoch://control-plane/projects/anchor-indexed-compressed-memory-for-long-context-cpu-inference-3dc5cf07a6fe/runs/anchor-indexed-compressed-memory-for-long-context-cpu-inference-3dc5cf07a6fe-20260621T022024140112+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd2d277891e5

## What looked useful

Anchor-indexed compressed memory reached 240/240 accuracy with 96 mean context tokens, while flat retrieval and sliding-recency controls each reached 6/240 under a 160-token budget; oracle full context was 240/240 at 1856 mean tokens.

## Boundaries and scale limits

No neural LLM runtime was available or used; tasks were synthetic; answer extraction was deterministic; robustness to natural dialogue, noisy metadata, paraphrased anchors, embeddings, and larger model generation remains untested.

## Claim scope

In a deterministic 240-task synthetic long-memory QA suite with 16 anchors, 8 facts per anchor, 32 recent same-entity/same-slot distractors, and a 160-token context budget, anchor-indexed compressed memory preserved answerable context better than recency and non-indexed flat retrieval controls.

## Why it stopped

No-paper closure: Tier-1 mechanism threshold was met, but evidence is controlled/synthetic and does not include an actual neural LLM runtime.

## Recommended next action

Run the same generated prompt suite through a small local CPU quantized LLM and score exact answers to verify the mechanism survives neural generation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU quantized LLM confirmation of anchor-indexed compressed memory
- Success threshold: Anchor-indexed compressed context accuracy >= 0.75 and at least +0.20 absolute accuracy over flat retrieval on the same tasks.
- Stop condition: Stop if no local CPU LLM runtime can be installed within the bounded run budget, or if anchor-indexed accuracy is below 0.75 or not at least +0.20 over flat retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/direct-cpu-llm-validation-of-anchor-indexed-compressed-mem-546d9b6290`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
