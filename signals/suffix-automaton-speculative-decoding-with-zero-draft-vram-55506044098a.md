# Suffix-automaton speculative decoding with zero draft VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-automaton-speculative-decoding-with-zero-draft-vram-55506044098a`
Run ID: `suffix-automaton-speculative-decoding-with-zero-draft-vram-55506044098a-20260620T050129345145+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff5a6bb3738

## What looked useful

Zero-draft-VRAM suffix-history drafting is mechanically plausible for repetition-heavy workloads: distilgpt2 reduced replayed target calls by 33.6% overall and GPT-2-small by 56.8% overall, while natural text remained weak to modest.

## Boundaries and scale limits

Proxy replay only; no integrated target verifier timing, no optimized incremental suffix index, no broad corpus, no large-model serving benchmark.

## Claim scope

On four short prompts with distilgpt2 and GPT-2-small greedy traces, a CPU suffix-automaton draft source with no neural draft model reduced replayed target calls in repeat-heavy/code/dialogue contexts, but showed weak natural-text benefit.

## Why it stopped

Proxy replay produced a useful mechanism signal but is not a full validation or paper-ready serving result.

## Recommended next action

Run a bounded integrated verifier follow-up that measures real tokens/sec and target forward batching on a small code/dialogue corpus with a gating policy for no-draft cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated suffix-automaton speculative decoding latency test
- Success threshold: At least 10% end-to-end tokens/sec improvement on code/dialogue prompts with no regression worse than 5% on natural-text controls, while loading no neural draft model.
- Stop condition: Stop if integrated verifier speedup is below 5% or suffix-index CPU overhead cancels the target-call savings on the bounded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-automaton-speculative-decoding-with-zero-draft-vram-55506044098a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
