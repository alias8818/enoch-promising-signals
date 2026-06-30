# Delta-Compressed Agent State with Exact Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `delta-compressed-agent-state-with-exact-anchors-265a9d5cd861`
Run ID: `delta-compressed-agent-state-with-exact-anchors-265a9d5cd861-20260609T005605367747+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3202d22de330

## What looked useful

The mechanism validated every reconstructed version by SHA-256. Best anchored-delta ratios versus independently gzipped full snapshots were 0.0478 for append-heavy, 0.6771 for edit-heavy, and 0.9846 for low-redundancy traces at anchor interval 64, with bounded 63-hop replay.

## Boundaries and scale limits

Only 3 synthetic trace families, 1000 versions each, single-process Python, zlib-compressed canonical JSON records. No real LangGraph/Codex traces, production object store, concurrent writers, corruption recovery workload, or large-scale serving validation were tested.

## Claim scope

On deterministic synthetic JSON agent-state traces, exact SHA-anchored field deltas can preserve exact reconstruction and reduce storage substantially for append-heavy state, moderately for edit-heavy state, and minimally for low-redundancy state.

## Why it stopped

No-paper useful signal from a bounded synthetic benchmark: the mechanism works and has a clear regime boundary, but the evidence is proxy-only rather than direct production-agent validation.

## Recommended next action

Run the same exact-anchor codec on captured real agent-controller traces and require both storage savings and bounded random-read latency before considering a scoped paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor delta compression on real agent traces
- Success threshold: Median anchored-delta storage ratio <=0.33 versus independently compressed full snapshots, p95 random reconstruction latency <=50 ms at K<=64, and 100% SHA validation across all decoded versions.
- Stop condition: Stop if median storage ratio is >0.75 or if p95 random reconstruction latency exceeds 200 ms at K=32 on real traces, because the mechanism would not justify integration complexity.

## Evidence references

- Artifact root: `<local-path>/projects/delta-compressed-agent-state-with-exact-anchors-265a9d5cd861`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
