# Noisy replay validation for two-tier exact-anchor semantic memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `noisy-replay-validation-for-two-tier-exact-anchor-semantic-c8f9536767`
Run ID: `noisy-replay-validation-for-two-tier-exact-anchor-semantic-c8f9536767-20260613T133751500757+0000`

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

- Parent run decision: Two-tier exact-anchor memory with semantic compression: enoch://control-plane/projects/two-tier-exact-anchor-memory-with-semantic-compression-b8977705879c/runs/two-tier-exact-anchor-memory-with-semantic-compression-b8977705879c-20260613T123032060477+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd00523d3f50

## What looked useful

Two-tier exact-anchor semantic memory reached 1.000 overall accuracy, improving exact-anchor noisy accuracy from 0.792 to 1.000, but the best baseline reached 0.896 overall and saturated the semantic no-anchor slice at 1.000, leaving only a 0.104 overall margin versus the required 0.150.

## Boundaries and scale limits

Small synthetic controlled corpus only; no real agent transcripts, learned embeddings, LLM generation, long-horizon memory accumulation, or production latency/storage measurements.

## Claim scope

A deterministic Tier 1 controlled replay test with 48 synthetic cases shows exact primary-anchor binding eliminates noisy exact-anchor retrieval failures made by flat lexical and transcript-search baselines, but the full two-tier exact-anchor plus semantic fallback strategy does not clear a 15 percentage point overall margin because semantic no-anchor queries are already solved by flat retrieval.

## Why it stopped

No-paper useful signal: the controlled direct test supports exact-anchor binding but fails the predeclared overall success threshold for the full two-tier method.

## Recommended next action

Run a bounded deepen test with harder semantic-only replay queries and a tuned lexical baseline; stop paper work unless that test clears a predeclared margin on both exact-anchor and semantic fallback slices.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard semantic fallback replay validation for exact-anchor memory
- Success threshold: Two-tier overall accuracy exceeds the strongest non-anchor baseline by at least 0.15, exact-anchor noisy accuracy is at least 0.90, semantic no-anchor accuracy is at least 0.80, and neither query type is saturated by all non-empty baselines.
- Stop condition: Stop as no-paper if flat or transcript baselines remain within 0.15 overall margin after the semantic-only slice is made non-saturated, or if two-tier semantic fallback falls below 0.80 accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-replay-validation-for-two-tier-exact-anchor-semantic-c8f9536767`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
