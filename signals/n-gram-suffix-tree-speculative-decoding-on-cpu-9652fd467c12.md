# N-gram suffix tree speculative decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-9652fd467c12`
Run ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-9652fd467c12-20260609T071554448311+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7d58c3a87292

## What looked useful

Suffix-index drafting cost was tens of microseconds per draft and shuffled controls collapsed near 1.0x, supporting a real repetition-copying mechanism. Best Python-source char/byte runs reached mean accepted 2.125 tokens and a 3.125x optimistic verifier-call bound, but Shakespeare word-token runs reached only mean accepted 0.482 with near-zero exact 8-token drafts.

## Boundaries and scale limits

No real neural language model was served; no end-to-end CPU LLM tokens/sec was measured; corpora were small; speedup is an optimistic target-call bound rather than measured serving throughput; word-token prose acceptance was weak.

## Claim scope

Bounded oracle-verifier benchmark on tiny Shakespeare prose and local Python stdlib source shows that a CPU n-gram suffix index can cheaply draft accepted continuations when held-out text contains repeated sequential structure, with strongest results on code-like char/byte streams.

## Why it stopped

No-paper useful signal: this was an oracle/proxy benchmark that supports the repetition mechanism but does not validate end-to-end CPU speculative decoding with a real model.

## Recommended next action

Run a bounded direct CPU LLM integration test comparing suffix-index drafting against no speculation and a small neural drafter on the same prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM integration test for suffix-index drafting
- Success threshold: At least 1.2x end-to-end tokens/sec over no speculation on code-like prompts with no material quality regression, and no more than 5% throughput loss on prose when gating is enabled.
- Stop condition: Stop if real-model acceptance produces less than 1.1x end-to-end speedup on code-like prompts or if suffix lookup overhead erases verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-on-cpu-9652fd467c12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
