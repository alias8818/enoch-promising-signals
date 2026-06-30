# Trace-derived semantic operator compression for repeated agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-semantic-operator-compression-for-repeated-agent-tasks-1d842b83671a`
Run ID: `trace-derived-semantic-operator-compression-for-repeated-agent-tasks-1d842b83671a-20260613T183928762624+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e4c4acd0bf0

## What looked useful

Across 10 seeds with 400 train and 160 test traces, semantic operators reduced held-out action symbols by 65.05% before catalog cost and 48.64% after catalog cost; exact-token macros reduced 3.56% before catalog cost and 2.04% after catalog cost; random semantic windows reduced 56.34% before catalog cost and 40.33% after catalog cost. Lossless decompression was 100% in every run.

## Boundaries and scale limits

The evidence is synthetic/proxy only: schemas generated the traces, semantic labels were known by construction, no real agent loop was run, and no production latency/tool-call/token-cost measurement was taken.

## Claim scope

On a typed synthetic benchmark of repeated agent-task traces with held-out slot values, trace-mined semantic macro-operators compressed held-out traces losslessly and substantially better than exact-token macros after catalog cost was charged.

## Why it stopped

Proxy evidence supports the mechanism but is not direct/full validation on real agent workloads, so it should not be written as a paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; next run should apply the same miner to real repeated agent traces with execution-derived or human-reviewed semantic labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of trace-derived semantic macro-operator compression
- Success threshold: At least 20% net held-out trace/action reduction after catalog cost, 100% replay-equivalence on the evaluated traces, and statistically positive improvement over exact-token macros.
- Stop condition: Stop as unsupported if net reduction is below 10%, replay equivalence falls below 99%, or gains vanish versus exact-token and random semantic baselines.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-semantic-operator-compression-for-repeated-agent-tasks-1d842b83671a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
