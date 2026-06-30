# Token-Tree Verification for Prompt N-gram Drafts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `token-tree-verification-for-prompt-n-gram-drafts-a51965f891e9`
Run ID: `token-tree-verification-for-prompt-n-gram-drafts-a51965f891e9-20260524T003754297165+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7818fde4346a

## What looked useful

Prompt n-gram draft candidates shared enough prefixes for trie verification to cut total verifier prefix evaluations from 381,640 to 135,506 with zero equivalence failures; per-condition savings ranged from 51.56% to 79.42%.

## Boundaries and scale limits

No transformer verifier, tree-attention kernel, KV-cache integration, real prompt corpus, or wall-clock latency measurement was implemented; results measure prefix-evaluation work only.

## Claim scope

In a deterministic oracle-level simulation of prompt-local n-gram drafting, merged token-tree verification exactly matched serial greedy verification and reduced verifier prefix evaluations across 38,400 candidate sets.

## Why it stopped

Closed as no-paper useful signal because the evidence is an oracle-level mechanism test rather than direct transformer latency validation.

## Recommended next action

Run a bounded deepen test with a small transformer verifier and a tree-attention or packed-prefix implementation to measure end-to-end latency and exactness on real prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Tree Verification for Prompt N-gram Drafts
- Success threshold: At least 15% median verification-latency reduction with zero exactness failures on a small transformer benchmark and a clear overhead breakdown.
- Stop condition: Stop negative if tree/packing overhead eliminates latency gains or any exactness mismatch is found under deterministic greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/token-tree-verification-for-prompt-n-gram-drafts-a51965f891e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
