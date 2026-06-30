# GQA with Periodic Re-Anchor for CPU Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gqa-with-periodic-re-anchor-for-cpu-long-context-86268f756297`
Run ID: `gqa-with-periodic-re-anchor-for-cpu-long-context-86268f756297-20260628T100307219844+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9dde20d17e26

## What looked useful

Periodic re-anchor can close a controlled old-fact retrieval gap, but capacity and refresh cadence are decisive: 3072-capacity/512-period reached 8192/8192 accuracy, 768-capacity fell to 2419/8192, and 2048-period introduced stale/missing errors.

## Boundaries and scale limits

Synthetic symbolic retrieval only; no trained transformer, no real grouped-query-attention kernel, no natural-language dataset, and the successful anchor capacity equals the full live key-value state.

## Claim scope

In a deterministic synthetic long-context QA probe, periodic full-state re-anchor recovered old entity-attribute facts that a finite sliding window missed.

## Why it stopped

No-paper useful signal: the evidence is a synthetic mechanism probe, not direct full validation of CPU long-context GQA with periodic re-anchor.

## Recommended next action

Run a bounded direct transformer/GQA follow-up with controlled anchor capacity and a parameter-matched sliding-window or dense baseline before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded transformer GQA re-anchor validation
- Success threshold: At least +0.20 absolute old-fact QA accuracy over the baseline with less than 2x CPU latency and a non-full-state anchor budget.
- Stop condition: Stop if the re-anchor model cannot beat the matched baseline by +0.10 absolute accuracy in two seeds or requires full-state anchors/comparable full-context memory.

## Evidence references

- Artifact root: `<local-path>/projects/gqa-with-periodic-re-anchor-for-cpu-long-context-86268f756297`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
