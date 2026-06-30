# Promotion-Gate Evidence Requirements

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `promotion-gate-evidence-requirements-c5e1a39b1e08`
Run ID: `promotion-gate-evidence-requirements-c5e1a39b1e08-20260611T010959901474+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cd48ab272cb1

## What looked useful

The audit found 245 legacy .omx promotion candidates and zero current .enoch promotion candidates. All 245 legacy candidates failed the strict gate: 245 lacked paper_positive outcome, bounded_paper_ready true, explicit claim scope, and explicit scale limits; 223 lacked logs; 105 lacked result files; 172 disclosed proxy or synthetic limitations.

## Boundaries and scale limits

Audited local artifacts only: 8372 decision files across current .enoch and legacy .omx records. The run did not test live controller behavior, human reviewer labels, or recall on true paper-ready positives because the current .enoch corpus had zero paper-promotion candidates.

## Claim scope

A strict artifact-only promotion gate for Enoch paper-ready decisions is implementable and rejects historical legacy promotion-looking records that lack current-schema paper-positive evidence, durable logs/results, explicit claim scope, scale limits, and non-proxy direct evidence.

## Why it stopped

Closed as no-paper useful operational signal: the artifact audit supports strict evidence requirements but cannot validate recall on genuine publication-grade positives.

## Recommended next action

Use the gate as a controller regression guard, then run a labeled reviewer calibration set before allowing it to make final paper-promotion decisions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reviewer-labeled calibration of Enoch paper-promotion gate sensitivity
- Success threshold: Reject at least 95% of reviewer-labeled non-paper-ready candidates while preserving at least 90% of reviewer-labeled paper-ready candidates, with all accepted cases having logs, results, scope, scale limits, and direct evidence.
- Stop condition: Stop if no reviewer-labeled positive examples are available or if tuned recall on paper-ready positives remains below 80% at 95% non-ready rejection.

## Evidence references

- Artifact root: `<local-path>/projects/promotion-gate-evidence-requirements-c5e1a39b1e08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
