# Confidence-Gated Local Cascade Router on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-local-cascade-router-on-gb10-199d8bbf1dc3`
Run ID: `confidence-gated-local-cascade-router-on-gb10-199d8bbf1dc3-20260613T032553670652+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/22a04b86cca6

## What looked useful

The tiny first-tier stress run matched or slightly exceeded the final large-model accuracy at threshold 0.58 while escalating 2.575% of validation samples, using 2.58% expected MACs and 6.56% measured GB10 batch latency versus large-only. A stronger cheap CNN solved the task alone, showing that cascade benefit depends on cheap-tier weakness and calibration rather than routing being inherently useful.

## Boundaries and scale limits

Synthetic image classification only; CNN tiers stand in for cheap and expensive local models; no real LLM routing traces, no natural-language quality evaluation, and no arrival-process or serving-concurrency study.

## Claim scope

On a synthetic 32x32 local classification proxy on GB10, confidence gating can preserve large-model-level accuracy when the cheap first tier is weaker but confidence separates accepted examples from likely errors.

## Why it stopped

Evidence supports the confidence-gating mechanism only on a toy synthetic proxy; it is insufficient for a publication-grade local cascade router claim.

## Recommended next action

Stop this run as a no-paper synthetic useful signal; the concrete next bounded test is a real local LLM small/large cascade on a labeled QA or tool-routing trace with calibrated confidence and end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated local LLM cascade on labeled routing traces
- Success threshold: At least 99% of large-model quality with at least 50% lower measured end-to-end latency or GPU compute, and accepted high-confidence small-model samples must have no more than 1% absolute excess error versus the large model.
- Stop condition: Stop if confidence is not selective enough to achieve both quality retention and at least 25% measured latency or compute reduction on the trace, or if small-only dominates the cascade at the required quality target.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-local-cascade-router-on-gb10-199d8bbf1dc3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
