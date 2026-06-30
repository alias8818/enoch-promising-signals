# Adaptive n-gram suffix speculative decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `adaptive-n-gram-suffix-speculative-decoding-36ed22ad3618`
Run ID: `adaptive-n-gram-suffix-speculative-decoding-36ed22ad3618-20260621T174029813319+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8c1f51c1f150

## What looked useful

Fixed n=2 suffix copying produced a 1.1216x verifier-call speedup upper bound, while adaptive selection produced 1.1216x and improved over the best fixed suffix by only 0.0014%. A future-leaking oracle reached only 1.1249x, indicating less than 0.3% suffix-selection headroom on this trace.

## Boundaries and scale limits

This is a trace-level CPU simulation, not live Transformer serving. It uses WikiText-2, a simple regex tokenizer, idealized verifier-call speedup, and no GPU latency or draft overhead measurement.

## Claim scope

On a WikiText-2 test trace with regex tokenization, max draft length 8, and suffix lengths 2-6, online adaptive suffix-length selection did not materially improve n-gram suffix speculative decoding over the best fixed suffix length.

## Why it stopped

Proxy real-text trace early-falsified adaptive suffix-length selection as a meaningful improvement over fixed n=2; this is not a full model-serving validation.

## Recommended next action

Stop this paper path; if continuing, run a bounded BPE-tokenized code/chat trace test only if the success threshold is at least 5% relative verifier-call speedup over the best fixed suffix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE code/chat trace test for adaptive n-gram suffix selection
- Success threshold: Adaptive policy improves verifier-call speedup by at least 5% relative over the best fixed suffix on at least one non-synthetic domain, with oracle headroom at least 8%.
- Stop condition: Stop if adaptive improvement remains below 2% relative over best fixed suffix or oracle headroom remains below 5% on both domains.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-n-gram-suffix-speculative-decoding-36ed22ad3618`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
