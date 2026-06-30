# Compressed-State Agent Memory with Exact Anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-state-agent-memory-with-exact-anchors-dc9601f4b701`
Run ID: `compressed-state-agent-memory-with-exact-anchors-dc9601f4b701-20260614T114343910552+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/293290b77429

## What looked useful

Exact anchors are necessary for grounded compressed memory in this setup: unanchored compressed state reached 1.0000 answer accuracy but 0.0000 grounded accuracy, while compressed state with exact anchors reached 1.0000 answer, anchor, and grounded accuracy under the same budget.

## Boundaries and scale limits

Synthetic corpus only; deterministic extractive memory construction; no LLM summarization, embedding retrieval, privacy redaction, adversarial traces, production memory store, or large-scale latency evaluation.

## Claim scope

On a deterministic synthetic repeated-session replay benchmark with 64 projects, 512 fact queries, and a 1400-character memory budget, compressed state with exact source anchors preserved both latest fact values and exact source-turn grounding, outperforming unanchored compressed state and transcript suffix baselines on grounded accuracy.

## Why it stopped

Closed as no-paper useful signal because the local evidence is synthetic/proxy evidence rather than real repeated-agent memory validation.

## Recommended next action

Run a bounded follow-up using real or LLM-generated repeated-agent traces where summaries may drift, with exact-anchor validation and privacy-redaction checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor compressed memory on real or LLM-generated repeated-agent traces
- Success threshold: Anchored compressed memory improves grounded accuracy by at least 0.20 absolute over the best unanchored or transcript baseline while keeping anchor precision at or above 0.95 and passing redaction checks.
- Stop condition: Stop if anchored memory fails to exceed the best baseline by 0.05 grounded accuracy or if exact anchors systematically violate redaction constraints.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-agent-memory-with-exact-anchors-dc9601f4b701`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
