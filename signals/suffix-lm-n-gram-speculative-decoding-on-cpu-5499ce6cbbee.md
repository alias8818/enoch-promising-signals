# Suffix-LM N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-lm-n-gram-speculative-decoding-on-cpu-5499ce6cbbee`
Run ID: `suffix-lm-n-gram-speculative-decoding-on-cpu-5499ce6cbbee-20260620T084830973100+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d42d75976a94

## What looked useful

Suffix-index n-gram drafting can preserve exact greedy output and reduce verifier calls by about 9x when suffix reuse is near perfect, but without adaptive gating it is not a broad CPU speedup because rejected drafts score extra positions and slow mixed/low-reuse regimes.

## Boundaries and scale limits

No real transformer or KV-cache verifier was run. Corpora are synthetic. Wall-time speedup appeared only in a heavier verifier proxy and high-reuse regime; mixed and low reuse slowed down.

## Claim scope

Pure Python/NumPy CPU experiment with an order-4 n-gram target, suffix-index drafter, synthetic high/mixed/low suffix-reuse corpora, and exact-match verification against greedy target output.

## Why it stopped

Synthetic/proxy evidence is mixed: the mechanism works in high-reuse verifier-dominated conditions but does not support a general CPU speculative-decoding speedup claim.

## Recommended next action

Run a bounded direct CPU causal-LM follow-up with KV-cache verification and an online acceptance gate; stop this run as no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache CPU causal-LM suffix drafter with online acceptance gating
- Success threshold: At least 1.2x geometric-mean wall-time speedup in the high-reuse bucket with no more than 5% slowdown in mixed/low-reuse buckets and exact greedy-equivalent outputs.
- Stop condition: Stop if online acceptance gating cannot prevent slowdowns on mixed/low-reuse prompts or if high-reuse real-LM speedup remains below 1.1x.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-lm-n-gram-speculative-decoding-on-cpu-5499ce6cbbee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
