# Token Tree Verification with CPU N-grams

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `token-tree-verification-with-cpu-n-grams-9ebc6f19a696`
Run ID: `token-tree-verification-with-cpu-n-grams-9ebc6f19a696-20260603T161230830062+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/247ced2927e2

## What looked useful

CPU n-gram filtering can prune candidate token-tree edges at 0.68M-1.12M checks/sec in Python with under 125 MiB RSS, but the pruning comes with high false-negative rates on held-out true continuations. It should be treated as a lossy heuristic or cache feature, not an exact verifier.

## Boundaries and scale limits

Single corpus, simple tokenizer, synthetic Zipf decoys, no real LLM tokenizer, no draft model token trees, no target-model logits, and no end-to-end serving integration.

## Claim scope

On Tiny Shakespeare with lowercase regex word/punctuation tokens, a CPU observed-continuation n-gram membership table is fast and memory-light but is not viable as a correctness-preserving token-tree verifier: n=3 rejects 73.40% of held-out true continuations and n=4 rejects 92.83%.

## Why it stopped

Proxy early falsification rather than full validation: the direct n-gram membership verifier rejected too many true held-out continuations to be correctness-preserving.

## Recommended next action

Stop this exact-verifier line; only pursue a bounded follow-up if reframed as a lossy branch-prioritization heuristic evaluated against real draft and target model accept decisions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: N-gram Features for Lossy Draft-Branch Prioritization
- Success threshold: At a fixed zero-drop or explicitly bounded-drop policy, n-gram feature ordering improves accepted tokens per target verification call by at least 10% over the strongest baseline on two corpora.
- Stop condition: Stop if n-gram feature ordering improves accepted tokens per target call by less than 5% or requires any correctness-dropping prune policy to beat the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/token-tree-verification-with-cpu-n-grams-9ebc6f19a696`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
