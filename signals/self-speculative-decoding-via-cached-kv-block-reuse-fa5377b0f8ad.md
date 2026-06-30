# Self-speculative decoding via cached KV-block reuse

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-cached-kv-block-reuse-fa5377b0f8ad`
Run ID: `self-speculative-decoding-via-cached-kv-block-reuse-fa5377b0f8ad-20260609T145511376015+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/93c206f86f51

## What looked useful

Copying a true cached KV block is much cheaper than recomputing K/V projections in the GPT-2-small-class NumPy proxy, but valid reuse requires the same parent prefix. Sequential text had zero valid parent-qualified hits at block sizes 1, 2, 4, 8, and 16; content-only repeats were high but invalid for KV reuse. Request-reset controls showed limited valid prefix reuse, indicating the mechanism belongs to repeated-prompt/prefix caching rather than single-stream self-speculative decoding.

## Boundaries and scale limits

No real transformer, no GPU paged-attention implementation, no draft/verifier acceptance loop, and no end-to-end tokens/s measurement. The result is an early falsification/useful signal, not full serving validation.

## Claim scope

CPU-only NumPy proxy and token-trace simulation show that true parent-prefix-qualified KV-block hits are absent in a single sequential text continuation, so cached KV-block reuse does not help the proposed self-speculative decoding path beyond standard prefix/tree KV reuse.

## Why it stopped

Corrected prefix-qualified cache simulation produced zero valid hits for single-stream sequential decoding, so the proposed speedup has no local source of reusable blocks despite cheap cache-copy economics.

## Recommended next action

Stop this self-speculative KV-block reuse line unless a real decoder can demonstrate repeated parent-qualified branch KV blocks not already handled by standard prefix/tree KV caching; the local result is a proxy early falsification, not full validation.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Parent-qualified KV prefix caching for repeated templated requests
- Success threshold: At least 10% end-to-end latency or throughput improvement on repeated-template workloads with no regression above 3% on the non-repeated control.
- Stop condition: Stop if parent-qualified hit rate is below 5% on realistic repeated-template traces or if cache management overhead removes the measured latency gain.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-cached-kv-block-reuse-fa5377b0f8ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
