# Medium cache-aware GPT-2 suffix n-gram speculative decoding confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-cache-aware-gpt-2-suffix-n-gram-speculative-decodin-4b3a63fe3a`
Run ID: `medium-cache-aware-gpt-2-suffix-n-gram-speculative-decodin-4b3a63fe3a-20260609T104355236320+0000`

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

- Parent run decision: Speculative Suffix: N-Gram Draft for GPT-2 Decoding: enoch://control-plane/projects/speculative-suffix-n-gram-draft-for-gpt-2-decoding-d7cc67e01b74/runs/speculative-suffix-n-gram-draft-for-gpt-2-decoding-d7cc67e01b74-20260609T031634307240+0000
- Parent run decision: Held-out GPT-2 suffix n-gram speculative decoding benchmark: enoch://control-plane/projects/held-out-gpt-2-suffix-n-gram-speculative-decoding-benchmar-48a02c3fe0/runs/held-out-gpt-2-suffix-n-gram-speculative-decoding-benchmar-48a02c3fe0-20260609T065255334197+0000

## What looked useful

Across seeds 0, 1, and 2, suffix n-gram draft 8 produced 2.42 generated tokens per target call, 37.1% accepted/proposed draft tokens, 58.7% fewer target calls than greedy, and exact output match on all 6912 generated tokens. Draft 4 reduced calls by 51.1%; random draft accepted 0 of 53280 proposed tokens and reduced no calls.

## Boundaries and scale limits

Single model size, one dataset, greedy decoding only, short continuations, simple Python implementation, and no production prompt-lookup baseline or larger-model robustness. Seed 1 and seed 2 wall-clock timing included concurrent GPU contention, so target-call metrics are stronger than absolute throughput claims.

## Claim scope

GPT-2 small greedy decoding on 72 fixed-seed WikiText-2 prompts with 128-token prompts and 96 generated tokens: cache-cropped suffix n-gram speculative verification exactly matches greedy output and reduces target-model calls by 58.7% for draft length 8 versus a one-token KV-cache greedy baseline; random draft control gives 0% call reduction.

## Why it stopped

Tier 2 direct confirmation completed with a useful mechanism signal, but the evidence is not broad or controlled enough for paper-positive closure.

## Recommended next action

Run a bounded robustness follow-up comparing the cache-cropped suffix verifier against a production prompt-lookup/speculative decoding baseline on GPT-2 small and GPT-2 medium with longer continuations and non-overlapping GPU timing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust GPT-2 prompt-lookup baseline comparison for cache-aware suffix speculative decoding
- Success threshold: Exact greedy match on all prompts, at least 40% target-call reduction on both model sizes, and wall-clock throughput at least 1.3x greedy without losing to the production prompt-lookup baseline by more than 10%.
- Stop condition: Stop as negative if either model has output mismatches, less than 25% target-call reduction, or wall-clock throughput below greedy after implementation overhead is controlled.

## Evidence references

- Artifact root: `<local-path>/projects/medium-cache-aware-gpt-2-suffix-n-gram-speculative-decodin-4b3a63fe3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
