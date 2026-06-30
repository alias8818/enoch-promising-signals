# Suffix-Anchor Speculative Decoding for Tool-Use Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-anchor-speculative-decoding-for-tool-use-traces-61c93ea4895d`
Run ID: `suffix-anchor-speculative-decoding-for-tool-use-traces-61c93ea4895d-20260621T002334129607+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8637e62a1db0

## What looked useful

Anchor-aware clipping roughly doubled accepted/proposed draft efficiency and cut zero-accept attempts from 38-46% to 7-18% in the main run, but plain suffix lookup remained faster on target-call speedup proxy in all tested conditions.

## Boundaries and scale limits

Synthetic traces only; no real LLM logits, tokenizer effects, public tool-call corpus, batching, GPU verification kernel, or wall-clock serving latency. Main run used 5000 train and 5000 test traces; sweep varied max draft length over 2, 4, 8, 12, and 16.

## Claim scope

On synthetic JSON-like tool-use traces with oracle longest-prefix verification, a conservative suffix-anchor policy reduces proposed-token waste and zero-accept draft attempts versus plain suffix lookup, but does not improve target-call speedup proxy.

## Why it stopped

Proxy mechanism test is complete and not paper-positive: the conservative suffix-anchor policy improves draft quality but fails to beat the plain suffix speed baseline under the tested target-call proxy.

## Recommended next action

Run a bounded follow-up on real tool-call traces with a latency-aware cost model to determine whether reduced draft waste can translate into wall-clock gains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Latency Test for Anchor-Clipped Suffix Drafting
- Success threshold: Anchor variant matches or exceeds plain suffix wall-clock speed by at least 5% while reducing zero-accept attempts by at least 30% on real traces.
- Stop condition: Stop if anchor variants remain slower than plain suffix under latency-calibrated costs or if the real trace dataset lacks enough repeated tool-call structure for suffix matches.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-anchor-speculative-decoding-for-tool-use-traces-61c93ea4895d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
