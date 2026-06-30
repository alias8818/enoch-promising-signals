# Tokenizer-Level Suffix Drafting With GPT-2-Small Verification

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `tokenizer-level-suffix-drafting-with-gpt-2-small-verificat-59f5d18c41`
Run ID: `tokenizer-level-suffix-drafting-with-gpt-2-small-verificat-59f5d18c41-20260614T123131759717+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Suffix-Tree Draft Heads for Local Speculative Decoding: enoch://control-plane/projects/suffix-tree-draft-heads-for-local-speculative-decoding-f0994ff821cc/runs/suffix-tree-draft-heads-for-local-speculative-decoding-f0994ff821cc-20260614T121512038472+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d3101b0c3e95

## What looked useful

The tokenizer-derived suffix graph produced opportunities on about 50.3% of generated tokens, but rank-1 and rank-2 suffix drafts had 0/2059 acceptance; oracle top-8 candidate recall was only 1/2059, directly missing the pre-set Tier 1 threshold.

## Boundaries and scale limits

Single GPT-2-small verifier, greedy decoding only, small validation prompt sample, no learned/context-conditioned drafter, no wall-clock serving benchmark, and no other tokenizers or model scales.

## Claim scope

Tokenizer-only suffix proposals derived from exact GPT-2 vocabulary split structure were evaluated against GPT-2-small greedy continuations on 128 WikiText-2 validation prompts with 32 generated tokens each.

## Why it stopped

Controlled small direct test failed the pre-set threshold by a wide margin: 0 accepted rank-1 tokenizer suffix drafts across 2059 verifier opportunities and only 1/2059 oracle top-8 candidate-set recall.

## Recommended next action

Stop this tokenizer-only suffix-drafting line as a no-paper negative; only revisit with a clearly different context-conditioned or learned drafter tested against the same GPT-2-small verifier metric.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-level-suffix-drafting-with-gpt-2-small-verificat-59f5d18c41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
