# N-gram Suffix Tree Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-49ce6782493a`
Run ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-49ce6782493a-20260619T223931938581+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/81e1a396ab58

## What looked useful

Suffix-index drafting accepted long runs on repeated/copy-heavy streams (82.27-85.69% target-call reduction, 5.65-7.23 accepted tokens/proposal) but failed on IID high entropy (0.02% target-call reduction, modeled speedup below 1x at 1 ms target step).

## Boundaries and scale limits

Test used synthetic deterministic streams and a proxy verifier over 78,000 evaluated tokens per stream; no real LLM logits, tokenizer, KV cache, batched verifier, or end-to-end CPU serving path was measured.

## Claim scope

A CPU n-gram suffix-index drafter can reduce modeled target decode calls on deterministic repeated or copy-heavy token streams, but not on high-entropy streams.

## Why it stopped

Closed as useful no-paper proxy evidence: mechanism works only when repetition is high, and this run does not validate real LLM serving speed.

## Recommended next action

Run a bounded real CPU LLM decode integration on natural prompts and repetitive/code prompts, comparing wall-clock tokens/sec against ordinary greedy or sampling decode.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM suffix-index speculative decode integration
- Success threshold: At least 20% tokens/sec improvement on repetitive/code-like prompts and no more than 5% slowdown on mixed natural prompts over a reproducible prompt set.
- Stop condition: Stop if acceptance is below 1 accepted token/proposal or end-to-end tokens/sec regresses by more than 5% on both repetitive and natural prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-on-cpu-49ce6782493a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
