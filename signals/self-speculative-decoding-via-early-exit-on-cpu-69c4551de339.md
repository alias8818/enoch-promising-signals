# Self-Speculative Decoding via Early Exit on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-on-cpu-69c4551de339`
Run ID: `self-speculative-decoding-via-early-exit-on-cpu-69c4551de339-20260603T141930930973+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/89f02b833a35

## What looked useful

Very short draft length 2 sometimes produced a small best-case CPU speedup, but the effect was unstable and selection-sensitive. Draft lengths 4 and 8 were consistently below baseline across all tested exits and seeds because draft overhead exceeded accepted-token progress.

## Boundaries and scale limits

Not a pretrained transformer or real serving benchmark; no trained early-exit heads, real prompts, attention/KV-cache implementation, or publication-grade model-scale validation.

## Claim scope

Bounded NumPy CPU proxy for early-exit self-speculative decoding using measured residual-stack CPU costs and early/full top-1 agreement traces.

## Why it stopped

Proxy early falsification rather than full validation: longer drafts failed in the local CPU proxy, and the only wins were small draft-length-2 effects that are not robust enough for a paper claim.

## Recommended next action

Stop this run as proxy-only no-paper evidence; the only worthwhile deepen test is a bounded pretrained-small-transformer CPU benchmark with trained early-exit heads and exact speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained small-transformer CPU early-exit self-speculation
- Success threshold: At least 1.2x median CPU speedup and no worse p95 latency than greedy baseline at draft length 4 or greater, with exact greedy output matching on the evaluated prompts.
- Stop condition: Stop if trained early-exit top-1 agreement cannot support mean speculative progress above the measured break-even threshold or if end-to-end CPU speedup remains below 1.1x.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-on-cpu-69c4551de339`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
