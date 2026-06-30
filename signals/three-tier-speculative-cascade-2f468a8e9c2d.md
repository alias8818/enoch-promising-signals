# Three-Tier Speculative Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `three-tier-speculative-cascade-2f468a8e9c2d`
Run ID: `three-tier-speculative-cascade-2f468a8e9c2d-20260526T074400959934+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dfba6690e973

## What looked useful

The cascade mechanism can filter weak cheap-draft proposals, but the correct control is best one-tier speculative decoding. Under the default cost model, cascade won 8/15 cases versus cheap-to-target and 0/15 cases versus best one-tier; median speed versus best one-tier was 0.781x.

## Boundaries and scale limits

No real transformer, GPU kernel, KV-cache, batching, prompt distribution, or wall-clock serving benchmark was run. The evidence is a bounded CPU simulation over stationary categorical distributions.

## Claim scope

In a synthetic categorical exact-speculative-decoding proxy with target cost 100, intermediate cost 12, cheap cost 1, chunk length 8, 15 mismatch cases, and 10 seeds per case, a cheap-mid-target cascade sometimes reduces target calls and beats cheap-to-target, but does not beat the best available one-tier draft baseline.

## Why it stopped

Proxy simulation did not support the broad three-tier cascade claim; it produced conditional evidence that target-call reductions are usually outweighed by intermediate-stage overhead when the best one-tier baseline is included.

## Recommended next action

Stop this run as no-paper useful signal; any next test should use small real transformer drafts and compare against both cheap-to-target and mid-to-target one-tier baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer adaptive cascade versus best one-tier speculative decoding
- Success threshold: Adaptive cascade improves tokens per second by at least 10% over the best one-tier baseline in at least two model triples without measurable output-distribution degradation.
- Stop condition: Stop if static and adaptive cascade both fail to beat the best one-tier baseline in the first two model triples or if intermediate-stage wall-clock overhead exceeds the saved target time.

## Evidence references

- Artifact root: `<local-path>/projects/three-tier-speculative-cascade-2f468a8e9c2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
