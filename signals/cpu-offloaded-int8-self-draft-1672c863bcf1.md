# CPU-Offloaded INT8 Self-Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-int8-self-draft-1672c863bcf1`
Run ID: `cpu-offloaded-int8-self-draft-1672c863bcf1-20260529T212530999642+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/46409790d22f

## What looked useful

Measured CPU INT8 streaming throughput is sufficient for tiny/GPT-2-small-class draft projections but projects to only about 16.3 tok/s for a 7B-class self-draft, causing modeled speculative slowdowns of 0.37x-0.74x for 20-40 tok/s targets at 0.70-0.85 acceptance.

## Boundaries and scale limits

This was a local proxy benchmark, not a full transformer serving run. It omits KV-cache attention, dequantization, sampling, CPU/GPU synchronization, trained-draft acceptance distributions, and direct target verification timing.

## Claim scope

On this GB10 host, a streaming INT8 GEMV proxy reaches about 114 GMAC/s on the CPU, which projects to useful throughput for small separate draft models but not for a same-size 7B-class CPU INT8 self-draft paired with a 20-40 tok/s GPU target.

## Why it stopped

Proxy early falsification: measured CPU INT8 streaming throughput is too low for a same-size 7B-class self-draft to improve realistic GPU target decoding, though the result is not a full serving validation.

## Recommended next action

Stop this self-draft claim as an early proxy falsification; next run a bounded direct serving test with a real small CPU INT8 draft and GPU target if pursuing the small-draft variant.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GB10 serving test for small CPU INT8 draft plus GPU target
- Success threshold: At least 1.15x end-to-end throughput improvement over target-only decoding on the fixed prompt set with no worse than 10% p95 latency regression.
- Stop condition: Stop if speculative decoding is below 1.05x target-only throughput after two draft lengths or if CPU draft latency exceeds 25% of target verification latency per cycle.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-int8-self-draft-1672c863bcf1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
