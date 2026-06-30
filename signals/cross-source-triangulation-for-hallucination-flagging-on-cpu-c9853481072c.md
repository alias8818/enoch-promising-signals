# Cross-Source Triangulation for Hallucination Flagging on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-source-triangulation-for-hallucination-flagging-on-cpu-c9853481072c`
Run ID: `cross-source-triangulation-for-hallucination-flagging-on-cpu-c9853481072c-20260613T131256136803+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bc227371e8f

## What looked useful

Cross-source triangulation reached accuracy 0.7556 and F1 0.8204 versus single-source structured accuracy 0.6583 and F1 0.5591, and lexical-overlap accuracy 0.5194 and F1 0.2445. Bootstrap mean accuracy delta was +0.0973 vs single-source and +0.2368 vs lexical. The benefit is recall-heavy: recall was 1.0, but specificity was only 0.4465 at five sources.

## Boundaries and scale limits

Synthetic generated facts only; no real web/news/citation corpus, no human labels, no retrieval pipeline, no NLI baseline, and no source reliability model. Source-count ablation shows specificity degrades as noisy sources increase.

## Claim scope

On a deterministic synthetic structured-claim benchmark with 360 cases and five generated sources per case, a simple cross-source triangulation rule improved hallucination-flagging F1 over lexical-overlap and single-source structured baselines, mainly by increasing recall for unsupported or conflicted claims.

## Why it stopped

Synthetic proxy evidence supports the mechanism but also exposes a specificity failure mode, so the result is not publication-grade or real-world validated.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should evaluate a calibrated triangulation/conflict-resolution rule on a small real multi-source claim-verification dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus calibrated cross-source conflict resolution for hallucination flagging
- Success threshold: On a real labeled dataset, improve F1 by at least 0.05 over the strongest non-triangulation baseline while keeping specificity at or above 0.75.
- Stop condition: Stop if the calibrated triangulation variant cannot exceed the strongest baseline F1 or if specificity remains below 0.65 after threshold calibration.

## Evidence references

- Artifact root: `<local-path>/projects/cross-source-triangulation-for-hallucination-flagging-on-cpu-c9853481072c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
