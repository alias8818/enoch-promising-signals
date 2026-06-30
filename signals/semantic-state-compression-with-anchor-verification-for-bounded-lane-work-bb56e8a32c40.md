# Semantic State Compression with Anchor Verification for Bounded Lane Work

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-state-compression-with-anchor-verification-for-bounded-lane-work-bb56e8a32c40`
Run ID: `semantic-state-compression-with-anchor-verification-for-bounded-lane-work-bb56e8a32c40-20260612T014421752358+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0e02bdbdc90

## What looked useful

Semantic state plus redundant anchor verification is a viable mechanism on a bounded symbolic lane-work proxy: it beats fixed-window replay on accuracy at comparable or smaller byte budgets and detects injected state corruption that unanchored semantic compression cannot detect.

## Boundaries and scale limits

Synthetic symbolic traces only; no LLM-generated summaries, no real workflow corpus, no natural-language anchors, no adversarial corruption model, no multi-checkpoint persistence test, and no publication-grade external validation.

## Claim scope

In a deterministic synthetic bounded-lane state machine, compact semantic state preserved current-state query accuracy while using 20-46x fewer serialized bytes than raw logs; adding per-lane anchors retained 20-33x compression and detected all injected semantic-state corruptions observed in the runs.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only by a symbolic proxy, not by real lane-work or model-generated compression evidence.

## Recommended next action

Run a bounded direct-evidence follow-up on real or LLM-generated lane-work traces with natural-language or executable anchors and persistence checks; do not write a paper from this proxy-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-verified compression on real lane-work traces
- Success threshold: Anchor-verified summaries achieve at least 95% query accuracy, at least 90% injected-corruption detection, and no more than 25% token overhead versus unanchored semantic summaries at the same trace scale.
- Stop condition: Stop as negative if anchor-verified summaries fail to exceed fixed-window accuracy by 20 percentage points, detect under 70% of injected corruptions, or require more bytes/tokens than raw or window baselines on the bounded corpus.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-state-compression-with-anchor-verification-for-bounded-lane-work-bb56e8a32c40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
