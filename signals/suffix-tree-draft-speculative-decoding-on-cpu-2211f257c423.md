# Suffix-Tree Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-draft-speculative-decoding-on-cpu-2211f257c423`
Run ID: `suffix-tree-draft-speculative-decoding-on-cpu-2211f257c423-20260620T211352512781+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a2accbf205cf

## What looked useful

Suffix-copy drafting is promising for structured/repetitive CPU decoding contexts but should be gated by repetition detection because random streams collapse to roughly 1.0x.

## Boundaries and scale limits

No integrated CPU LLM verifier, no real tokenizer/model KV-cache accounting, no batched verification latency measurement, and synthetic corpora only. Verifier-call reduction is a proxy and must not be read as end-to-end serving speedup.

## Claim scope

On deterministic synthetic token traces with repeated structure, an online history-only suffix-index drafter reduced trace-level verifier calls by 3.13x to 8.94x across two seeds; on random tokens it provided no useful reduction.

## Why it stopped

Trace-level proxy supports the mechanism on repeated data but is insufficient for publication-grade or deployment claims.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the suffix drafter with a small CPU LLM verifier and require at least 1.2x end-to-end tokens/sec over no-draft and prompt-lookup baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM verifier integration for suffix-index speculative drafting
- Success threshold: At least 1.2x end-to-end tokens/sec over the best baseline on repeated-structure corpora, no regression greater than 5% on low-repetition controls, and transparent acceptance/latency breakdowns.
- Stop condition: Stop if drafter overhead plus batched verifier latency fails to beat prompt-lookup by 10% on a smoke corpus or if memory overhead exceeds the model-serving budget.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-speculative-decoding-on-cpu-2211f257c423`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
