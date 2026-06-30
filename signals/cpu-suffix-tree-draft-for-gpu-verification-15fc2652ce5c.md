# CPU Suffix-Tree Draft for GPU Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-suffix-tree-draft-for-gpu-verification-15fc2652ce5c`
Run ID: `cpu-suffix-tree-draft-for-gpu-verification-15fc2652ce5c-20260609T001642921234+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48099f486882

## What looked useful

The verifier accepted 48/48 generated reference trees and detected all injected invalid-span, suffix-index, duplicate-dispatch, and dropped-leaf mutations. Median verification time at 4096-byte payloads was 0.0415 s, while median build time was 4.01 s.

## Boundaries and scale limits

No real GPU suffix-tree output was available; the test used CPU-exported edges as candidate output plus injected mutations. The reference builder is simple and memory-heavy, reaching 2882348 KiB RSS at 4096-byte payloads, so it is not a scalable CPU construction method.

## Claim scope

A deterministic CPU reference suffix-tree oracle can verify small-to-medium candidate suffix-tree edge outputs up to 4096-byte payloads across random, DNA, periodic, and unary synthetic inputs, catching the four injected structural defect classes tested here.

## Why it stopped

Bounded CPU-only proxy evidence supports the verifier mechanism but is not direct GPU evidence or publication-grade validation.

## Recommended next action

Use this CPU verifier as a regression oracle for a real GPU suffix-tree candidate buffer and add an independent suffix-array/LCP cross-check before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU Candidate Buffer Verification With Independent Suffix-Array Cross-Check
- Success threshold: Zero false accepts on injected malformed GPU candidate buffers and zero disagreements among GPU candidate output, CPU suffix-tree verifier, and suffix-array/LCP oracle for all bounded cases.
- Stop condition: Stop as negative if any valid bounded GPU candidate is rejected without a verifier bug fix, any malformed injected candidate is accepted, or the independent suffix-array/LCP oracle disagrees on suffix coverage.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-suffix-tree-draft-for-gpu-verification-15fc2652ce5c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
