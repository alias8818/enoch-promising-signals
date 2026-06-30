# Zero-VRAM Suffix-Tree Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `zero-vram-suffix-tree-speculative-decoding-316f14c768c8`
Run ID: `zero-vram-suffix-tree-speculative-decoding-316f14c768c8-20260526T095611030619+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ccd8285403a

## What looked useful

On Wikitext-2, the best tested natural setting accepted only 0.214 tokens per position with draft_len=4 and min_suffix=2; the main draft_len=8 setting accepted 0.135 tokens per position with only 0.18% full drafts. The repetitive control accepted about 6 of 8 tokens per position, confirming the mechanism works only when repetition is abundant.

## Boundaries and scale limits

No real target LLM verifier, no serving-stack wall-clock speedup, no chat/code/RAG generated-output workload, and no comparison to a neural draft model were run. The natural-text result is a proxy early falsification, not a full deployment validation.

## Claim scope

A CPU longest-previous-suffix proposer was evaluated on 120k GPT-2 BPE Wikitext-2 tokens and a same-length repetitive synthetic control. The mechanism is effective for highly repetitive streams but weak on natural text.

## Why it stopped

Proxy early falsification: natural-text exact acceptance is too low to plausibly justify a general zero-VRAM suffix-tree speculative decoder, though repetitive controls show a narrower copy-heavy mechanism.

## Recommended next action

Stop this general natural-text claim as a proxy early falsification; if continuing, run a bounded direct follow-up on copy-heavy code/RAG/transcript LLM decoding with target-model verification and wall-clock speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct suffix-replay speculative decoding on copy-heavy LLM workloads
- Success threshold: At least 1.0 accepted suffix-drafted token per decode position on copy-heavy workloads and at least 10% end-to-end tokens/sec improvement over no-draft decoding without exceeding 2 GB CPU index memory for 120k-token contexts.
- Stop condition: Stop if direct target-model acceptance remains below 0.5 tokens per position or end-to-end throughput does not improve by at least 5% on two copy-heavy workload classes.

## Evidence references

- Artifact root: `<local-path>/projects/zero-vram-suffix-tree-speculative-decoding-316f14c768c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
