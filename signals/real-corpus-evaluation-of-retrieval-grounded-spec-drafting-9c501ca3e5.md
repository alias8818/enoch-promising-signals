# Real-Corpus Evaluation of Retrieval-Grounded Spec Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-evaluation-of-retrieval-grounded-spec-drafting-9c501ca3e5`
Run ID: `real-corpus-evaluation-of-retrieval-grounded-spec-drafting-9c501ca3e5-20260621T102222712619+0000`

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

- Parent run decision: Retrieval-Based Spec Draft from Local Document Store: enoch://control-plane/projects/retrieval-based-spec-draft-from-local-document-store-6fb35da485b7/runs/retrieval-based-spec-draft-from-local-document-store-6fb35da485b7-20260621T100602031200+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4ee2f99f8a58

## What looked useful

Primary top-k 5 run: retrieval_grounded mean fact recall 0.625 and cited support 0.625 versus random_grounded 0.25/0.25 and ungrounded 0.0/0.0; retrieval had zero unsupported generic claims versus eight for ungrounded.

## Boundaries and scale limits

Only four tasks, one documentation family, deterministic extractive drafting rather than an LLM, simple lexical retrieval, and no human quality assessment. This is not publication-grade evidence for general retrieval-grounded spec drafting.

## Claim scope

In a four-task Tier 1 real-corpus benchmark using CPython documentation, a retrieval-grounded extractive spec drafter achieved higher corpus-specific fact recall and cited support than random-corpus and no-retrieval controls.

## Why it stopped

Tier 1 direct small test produced a useful mechanism signal but remains too small and extractive-drafter-limited for paper readiness.

## Recommended next action

Run a bounded deepen follow-up with an actual LLM spec drafter on at least 25 real repository issue-or-doc tasks, preserving citation verification and random/no-retrieval controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Real-Repository Evaluation of Retrieval-Grounded Spec Drafting
- Success threshold: Retrieval-grounded LLM drafts improve mean cited project-specific requirement recall by >= 0.20 over both controls and do not increase unsupported-claim rate by more than 0.05 absolute.
- Stop condition: Stop if retrieval-grounded recall improvement is < 0.10 after 25 tasks or unsupported-claim rate is higher than both controls.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-evaluation-of-retrieval-grounded-spec-drafting-9c501ca3e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
