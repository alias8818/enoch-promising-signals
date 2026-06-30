# Unified Entropy and Acceptance Controller for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `unified-entropy-and-acceptance-controller-for-speculative-decoding-ae0e751c63ff`
Run ID: `unified-entropy-and-acceptance-controller-for-speculative-decoding-ae0e751c63ff-20260519T232009327995+0000`

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

- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

A unified entropy-plus-acceptance controller beat the best non-oracle baseline by 2.75% on entropy-misleading traces and 2.60% on bursty traces, but lost by 1.86% to fixed k=8 on benign traces.

## Boundaries and scale limits

No real target/draft model logits, tokenizer behavior, KV-cache effects, batching, GPU utilization, or wall-clock serving latency were tested; the signal is proxy-only and not paper-ready.

## Claim scope

Synthetic speculative-decoding controller simulation with three acceptance/entropy trace regimes, six policies, forty seeds per regime, and cost measured as target calls plus draft-token cost.

## Why it stopped

Closed as no-paper useful signal because the result is mixed and synthetic/proxy-only, not a full validation of speculative decoding latency or model behavior.

## Recommended next action

Run a bounded real-model follow-up with a small target/draft pair and logged entropy/acceptance traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model entropy and acceptance controller probe for speculative decoding
- Success threshold: Unified controller improves tokens-per-cost or wall-clock tokens/sec by at least 2% over the best non-oracle baseline on mismatch-heavy corpora without losing more than 2% on benign corpora.
- Stop condition: Stop if the unified controller fails to beat the best non-oracle baseline on mismatch-heavy real-model traces or if benign-trace regression exceeds 2%.

## Evidence references

- Artifact root: `<local-path>/projects/unified-entropy-and-acceptance-controller-for-speculative-decoding-ae0e751c63ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
