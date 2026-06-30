# Adaptive proposal gating for n-gram KV-cache draft cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-proposal-gating-for-n-gram-kv-cache-draft-cascade-77ea4ddf20`
Run ID: `adaptive-proposal-gating-for-n-gram-kv-cache-draft-cascade-77ea4ddf20-20260522T052122818210+0000`

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

- Parent run decision: N-gram Speculative Draft Cascade for Local Inference: enoch://control-plane/projects/n-gram-speculative-draft-cascade-for-local-inference-438d6f399d20/runs/n-gram-speculative-draft-cascade-for-local-inference-438d6f399d20-20260522T012822208311+0000
- Parent run decision: End-to-end KV-cache latency test for n-gram draft cascades: enoch://control-plane/projects/end-to-end-kv-cache-latency-test-for-n-gram-draft-cascades-12a82fca62/runs/end-to-end-kv-cache-latency-test-for-n-gram-draft-cascades-12a82fca62-20260522T031033207631+0000

## What looked useful

Adaptive gating admitted about 30.7% of proposal opportunities, improved cost-adjusted speedup to 1.026x versus 0.973x for fixed always-propose and 1.003x for the best static support gate, and cut waste per token by 65.9% relative to fixed.

## Boundaries and scale limits

Trace-based verifier only; no real transformer KV-cache integration, no measured GPU wall-clock throughput, no batched serving, and no large-model acceptance distribution.

## Claim scope

On four public-domain text traces with 5 fixed seeds, an adaptive n-gram proposal gate improved verification-cost-adjusted speedup over target-only, fixed always-propose n-gram drafting, and static support-count gates while reducing fixed-cascade proposal waste.

## Why it stopped

Tier 2 trace evidence supports the mechanism but remains no-paper because neural KV-cache wall-clock behavior was proxied rather than directly measured.

## Recommended next action

Run a bounded real-model follow-up by integrating the gate into small-transformer speculative decoding and measuring tokens/sec, accepted draft tokens, target forwards, and latency versus target-only, fixed n-gram, and static support gates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model adaptive n-gram gate for small-transformer speculative decoding
- Success threshold: Adaptive gate improves measured throughput or latency-adjusted tokens/sec by at least 2% versus the best non-adaptive n-gram baseline while reducing proposal waste versus fixed always-propose by at least 50%.
- Stop condition: Stop if adaptive gating fails to beat the best static support gate on measured throughput in at least 3 of 5 fixed seeds or if KV-cache integration overhead erases the trace-level adjusted-speedup gain.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-proposal-gating-for-n-gram-kv-cache-draft-cascade-77ea4ddf20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
