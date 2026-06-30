# Suffix-Tree Prompt-Recycling Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-prompt-recycling-speculative-decoding-be0b66d10f98`
Run ID: `suffix-tree-prompt-recycling-speculative-decoding-be0b66d10f98-20260525T005540966616+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ef73a7cda2a2

## What looked useful

Suffix-longest recycling accepted more total held-out tokens than a fixed 4-gram prompt-recycling baseline on the tested local corpora and failed cleanly on a drift control. Longer drafts increased wasted proposals while accepted-token counts saturated, suggesting short adaptive drafts are necessary.

## Boundaries and scale limits

CPU-only exact-match verifier proxy; no GPU serving benchmark, no real model verifier, no tokenizer/model-specific KV behavior, no batch scheduler effects, no public benchmark corpus after external download timeout.

## Claim scope

Bounded proxy evidence shows that a longest-suffix prompt-recycling draft source can reduce simulated verifier calls on repetitive synthetic answers and local code/instruction-like text, but it has low acceptance rates on non-synthetic local text and was not tested in a live LLM serving loop.

## Why it stopped

No-paper useful signal: this was a proxy/early mechanism test, and related SuffixDecoding work already covers a close suffix-tree speculative-decoding idea; direct LLM serving evidence is required before any paper claim.

## Recommended next action

Run a bounded real-model follow-up that plugs this suffix draft source into speculative decoding for a small open model and reports wall-clock speed, accepted tokens, verifier passes, and quality invariance against no-speculation and n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model verifier test for prompt-suffix recycling drafts
- Success threshold: At least 10% wall-clock decode speedup over no speculation on repetitive/code-like prompts with identical outputs, no regression on non-repetitive controls beyond measurement noise, and acceptance/call metrics explaining the speedup.
- Stop condition: Stop if suffix recycling gives less than 5% wall-clock speedup or changes outputs/quality under the same verifier settings, even if proxy accepted-token counts look favorable.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-prompt-recycling-speculative-decoding-be0b66d10f98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
