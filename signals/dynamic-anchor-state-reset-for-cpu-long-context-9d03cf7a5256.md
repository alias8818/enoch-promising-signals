# Dynamic Anchor State Reset for CPU Long-Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-anchor-state-reset-for-cpu-long-context-9d03cf7a5256`
Run ID: `dynamic-anchor-state-reset-for-cpu-long-context-9d03cf7a5256-20260531T192750821344+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1c64bc485425

## What looked useful

Dynamic anchor reset improved confirmation accuracy at cosine > 0.5 from 0.00950 for no reset and 0.01020 for fixed periodic reset to 0.02981, with mean cosine improving from 0.03994 to 0.05310 over 2,097,152 stream tokens.

## Boundaries and scale limits

No learned model, transformer KV cache, natural-language corpus, real CPU inference engine, or production latency/quality study was tested. The strongest result is on a synthetic thresholded retrieval metric; MSE gains were small.

## Claim scope

In a synthetic CPU streaming retrieval probe with anchor-delimited segments and a decayed vector recurrent state, resetting state at true anchors reduced cross-segment interference relative to no reset and fixed periodic reset.

## Why it stopped

Closed as no-paper useful signal because the result directly supports only a synthetic recurrent-state mechanism, not full CPU long-context model behavior.

## Recommended next action

Run a bounded learned-model follow-up on the same anchor-delimited retrieval task, comparing no reset, fixed reset, and dynamic anchor reset in a tiny recurrent or transformer-style CPU model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Tiny-Model Dynamic Anchor Reset Probe
- Success threshold: Dynamic anchor reset improves retrieval accuracy by at least 10% relative over both controls without more than 10% CPU latency overhead in the bounded tiny-model setup.
- Stop condition: Stop if dynamic reset fails to beat both controls on two independent seeds or if reset overhead exceeds 10% while accuracy is not improved.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-anchor-state-reset-for-cpu-long-context-9d03cf7a5256`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
