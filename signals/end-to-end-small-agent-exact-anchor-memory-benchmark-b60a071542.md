# End-to-end small-agent exact-anchor memory benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-small-agent-exact-anchor-memory-benchmark-b60a071542`
Run ID: `end-to-end-small-agent-exact-anchor-memory-benchmark-b60a071542-20260604T074403941511+0000`

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

- Parent run decision: Compressed State Agent with Exact Anchor Retrieval: enoch://control-plane/projects/compressed-state-agent-with-exact-anchor-retrieval-91bde995faf8/runs/compressed-state-agent-with-exact-anchor-retrieval-91bde995faf8-20260604T042835717297+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d1eff6718125

## What looked useful

Exact-anchor lookup is a strong bounded mechanism for old anchored facts: 100% accuracy and 3.5-3.7 us p95 latency in direct runs. Full-history lexical retrieval remained accurate at low distractor density (92.2%) but degraded to 73.7% and 3262 us p95 at high distractor density.

## Boundaries and scale limits

No LLM planner, natural-language task corpus, learned retriever, persistence/restart test, anchor-corruption sweep, or large-scale deployment was tested. Evidence is local CPU-only synthetic Tier 1 validation.

## Claim scope

In a deterministic synthetic small-agent loop with exact query anchors, an exact-anchor memory index retrieves old anchored facts with 100% accuracy and microsecond p95 latency; it clearly beats recency windows and beats full-history lexical retrieval by more than 20 accuracy points only under high similar-anchor distractor density.

## Why it stopped

Tier 1 direct synthetic validation is complete; result is useful but not paper-ready, and the accuracy advantage over full-history lexical retrieval is conditional rather than universal.

## Recommended next action

Run a bounded deepen test with a small real LLM agent using persisted exact-anchor memory on multi-step natural-language tasks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small LLM agent persisted exact-anchor memory test
- Success threshold: At least 95% exact answer accuracy after restart, at least 15 percentage points over the strongest baseline, and p95 retrieval overhead below 10 ms on 1000 or more held-out queries.
- Stop condition: Stop if exact-anchor memory falls below 90% accuracy after restart or fails to beat the strongest baseline by 10 percentage points in two independently seeded task sets.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-small-agent-exact-anchor-memory-benchmark-b60a071542`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
