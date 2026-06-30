# Anchor-eviction policy study for verbatim-anchor memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-eviction-policy-study-for-verbatim-anchor-memory-387c2920deee`
Run ID: `anchor-eviction-policy-study-for-verbatim-anchor-memory-387c2920deee-20260613T003011931612+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd00523d3f50

## What looked useful

Pinning tagged verbatim anchors is a useful engineering mechanism under noisy importance scoring: noisy_salience mean exact recall improved from the best generic baseline at 0.432255 to 0.973756. The same mechanism was redundant under perfect salience, tying salience at 0.967576.

## Boundaries and scale limits

240 synthetic episodes per scenario; no LLM generation, semantic retrieval, real agent traces, anchor detection, or full-scale memory-system validation.

## Claim scope

In a seeded synthetic replay benchmark with explicitly tagged verbatim anchors, anchor-protected eviction improves exact anchor recall when generic salience scores are noisy, but provides no lift over a salience policy when anchors are already perfectly scored.

## Why it stopped

Closed as useful no-paper evidence because the current result is synthetic and mechanism-only; it supports a bounded follow-up but not a publication-grade claim.

## Recommended next action

Run a bounded direct follow-up on real or LLM-generated repeated-agent memory traces with anchor detection, retrieval, generation, and exact-match recall against a strong salience baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct repeated-agent trace test for tagged verbatim-anchor eviction
- Success threshold: At least 15 percentage point exact-anchor recall lift over the best tuned baseline on non-overload traces, with irrelevant retrieval rate increase no greater than 5 percentage points.
- Stop condition: Stop if anchor detection F1 is below 0.80, if recall lift is below 5 percentage points across two seeds, or if irrelevant retrievals increase by more than 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-eviction-policy-study-for-verbatim-anchor-memory-387c2920deee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
