# CPU n-gram Speculative Decoding with Adaptive Draft Length

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-with-adaptive-draft-length-b9b3203b1a96`
Run ID: `cpu-n-gram-speculative-decoding-with-adaptive-draft-length-b9b3203b1a96-20260621T041208997846+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b8cf904693c1

## What looked useful

Simple adaptive draft-length controllers (AIMD and mismatch-depth feedback) were exact and reduced target calls by about 2.31x with a 3-gram drafter, but fixed_k4 was better under an overhead-4 proxy and fixed_k8 was better under an overhead-16 proxy. With a weaker 2-gram drafter, adaptive policies still failed to beat tuned fixed lengths.

## Boundaries and scale limits

No transformer model, KV-cache implementation, or real CPU serving latency was measured. The cost model proxies target-call overhead and verified-token work, so conclusions are mechanism-level and not publication-grade serving evidence.

## Claim scope

In a deterministic Tiny Shakespeare n-gram proxy with a 5-gram target and 3-gram or 2-gram drafter, speculative decoding preserved exact greedy output and reduced target calls, but the tested adaptive draft-length policies did not outperform the best fixed draft length under CPU-oriented cost proxies.

## Why it stopped

Bounded proxy evidence does not support the adaptive draft-length hypothesis strongly enough for a paper; simple adaptive policies underperformed tuned fixed draft lengths.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete test is a CPU transformer/KV-cache implementation with wall-clock tokens/s and a latency-calibrated adaptive policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU transformer n-gram speculation with latency-calibrated adaptive draft length
- Success threshold: Adaptive policy improves wall-clock tokens/s by at least 10% over the best fixed draft length while preserving exact greedy output on all prompts.
- Stop condition: Stop if adaptive fails to beat the best fixed draft length on wall-clock tokens/s in two bounded acceptance regimes or if exactness fails.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-with-adaptive-draft-length-b9b3203b1a96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
