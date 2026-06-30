# Parameter-matched control for prefix-routed draft pools

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `parameter-matched-control-for-prefix-routed-draft-pools-066aae1632`
Run ID: `parameter-matched-control-for-prefix-routed-draft-pools-066aae1632-20260526T221751408205+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Prefix-Routed Speculative Draft Pool: enoch://control-plane/projects/prefix-routed-speculative-draft-pool-189110d68cb5/runs/prefix-routed-speculative-draft-pool-189110d68cb5-20260526T080421061136+0000
- Parent run decision: Small-transformer validation of prefix-routed draft pools: enoch://control-plane/projects/small-transformer-validation-of-prefix-routed-draft-pools-610c8f2551/runs/small-transformer-validation-of-prefix-routed-draft-pools-610c8f2551-20260526T153111190960+0000

## What looked useful

Across 40 paired fixed-seed/budget comparisons, prefix routing slightly underperformed the parameter-matched global draft on acceptance (mean delta -0.000602, 95% normal CI [-0.001026, -0.000178], wins 18/40), while random routing was strongly worse and an unmatched 8x-capacity routed pool was better. The useful signal is that apparent routed-pool gains can be capacity gains, and parameter matching removes the advantage in this local test.

## Boundaries and scale limits

This is not a transformer serving result: it uses character n-gram target and draft distributions, exact acceptance computation, and approximate target-call metrics rather than neural draft pools, KV-cache effects, multi-token serving overheads, or wall-clock latency on a deployed LLM.

## Claim scope

In a bounded character n-gram speculative-decoding evaluation over a controlled prefix-domain corpus and Tiny Shakespeare, an 8-expert deterministic prefix-routed draft pool did not improve expected speculative acceptance over a single global draft when total stored draft transition parameters were matched.

## Why it stopped

Medium local validation with fixed seeds, controls, and a real parameter-matched baseline did not support the prefix-routed draft-pool mechanism; remaining transformer-scale validation would test a different implementation class rather than rescue this deterministic prefix-routing result.

## Recommended next action

Stop this follow-up as a no-paper negative/useful-signal result; any future work should only proceed if it tests a genuinely different learned or semantic router with parameter-matched neural drafts and measured speculative serving latency.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/parameter-matched-control-for-prefix-routed-draft-pools-066aae1632`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
