# Medium confirmation of FLOP-matched length curriculum with longer contexts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-confirmation-of-flop-matched-length-curriculum-with-46f1ae376e`
Run ID: `medium-confirmation-of-flop-matched-length-curriculum-with-46f1ae376e-20260517T003333484070+0000`

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

- Internal Enoch project: Medium confirmation of FLOP-matched length curriculum with longer contexts: internal_generated:medium-confirmation-of-flop-matched-length-curriculum-with-46f1ae376e

## What looked useful

Ordered curriculum matched fixed-long and mixed-control at saturated 512-token validation and improved extrapolated 768-token first-answer recall: 0.960 mean accuracy versus 0.628 fixed-long and 0.746 mixed-control. Marker corruption drove first-answer accuracy to zero for curriculum at 512 and 768, supporting use of the early marker.

## Boundaries and scale limits

Synthetic marker-recall data only; small model; three seeds; relative FLOP proxy with 1.8% integer-batch compute mismatch; no natural-language corpus, GPT-2-small-class baseline, exact profiler FLOPs, or broad long-context benchmark.

## Claim scope

In a local 1M-parameter synthetic causal Transformer recall task with train lengths up to 512 and evaluation at 768, an ordered FLOP-matched length curriculum improved first-answer long-context recall over fixed-long and shuffled same-length-set controls across three fixed seeds.

## Why it stopped

Medium local confirmation produced a useful scoped signal but not publication-grade evidence; broader data, stronger baselines, exact compute accounting, and more seeds are still required.

## Recommended next action

Run a bounded deepen follow-up on less synthetic text/retrieval data with exact profiler-estimated compute matching and at least five seeds; stop if ordered curriculum does not beat both fixed-long and shuffled mixed-control on extrapolated first-retrieval accuracy by at least 10 percentage points.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Profiler-matched text retrieval length curriculum
- Success threshold: Ordered curriculum must beat both fixed_long and mixed_control by at least 10 percentage points in extrapolated first-retrieval accuracy, with no degradation greater than 2 points at the trained maximum context and with corruption reducing extrapolated first-retrieval accuracy by at least 50 points.
- Stop condition: Stop as no-paper if ordered curriculum fails to beat mixed_control by 10 percentage points on extrapolated first-retrieval accuracy or if compute parity cannot be held within 1%.

## Evidence references

- Artifact root: `<local-path>/projects/medium-confirmation-of-flop-matched-length-curriculum-with-46f1ae376e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
