# Exact-Anchor Ledger for Small-Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-ledger-for-small-agent-tool-calls-ad63afd98676`
Run ID: `exact-anchor-ledger-for-small-agent-tool-calls-ad63afd98676-20260528T012713250114+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9bff071dd906

## What looked useful

Exact byte-span/hash anchors achieved 1.00 accuracy, precision, recall, and specificity over 200,000 generated claims. Line-only anchors missed all 50,000 stale-source cases; no-ledger accepted all unsupported cases. Naive JSON ledger overhead was high at 11.79x source size, while compact used-anchor layout was estimated at 1.59x.

## Boundaries and scale limits

Synthetic generated records only; no real LLM agent traces, no human audit study, no heterogeneous tool formats, and no long-running production workload. Timing is a short local sanity check, not a robust benchmark.

## Claim scope

On deterministic synthetic small-agent text records, an exact-anchor ledger using source hashes plus byte spans verified supported claims and rejected wrong-value, missing-anchor, and stale-source claims better than no-ledger and line-only baselines.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not paper-ready direct evidence for real agents.

## Recommended next action

Run a deepen follow-up on captured real small-agent tool-call traces with exact-anchor emission, verifier false-positive/false-negative rates, and ledger-size overhead measured against line-only and content-hash-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor ledger on real small-agent traces
- Success threshold: Exact-anchor verification improves stale/unsupported citation detection by at least 25 percentage points over line-only anchors while preserving at least 95% recall on valid anchored claims and keeping compact ledger overhead below 2x selected evidence bytes.
- Stop condition: Stop if exact-anchor emission cannot be produced for real traces without manual repair, valid-claim recall falls below 90%, or compact ledger overhead exceeds 4x selected evidence bytes.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-ledger-for-small-agent-tool-calls-ad63afd98676`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
