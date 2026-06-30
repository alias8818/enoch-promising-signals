# Validate evidence-ledger failure taxonomy on real tool-agent transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `validate-evidence-ledger-failure-taxonomy-on-real-tool-age-f244e84e06`
Run ID: `validate-evidence-ledger-failure-taxonomy-on-real-tool-age-f244e84e06-20260621T223602887562+0000`

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

- Parent run decision: Evidence-ledger agent reliability with falsifiable failure taxonomy: enoch://control-plane/projects/evidence-ledger-agent-reliability-with-falsifiable-failure-taxonomy-e6406f3ad2fc/runs/evidence-ledger-agent-reliability-with-falsifiable-failure-taxonomy-e6406f3ad2fc-20260621T214844464776+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/73774bf46032

## What looked useful

The Tier 1 harness achieved exact claim accuracy 1.0, label precision 1.0, and label recall 1.0 on missing refs, empty refs, unsupported anchors, forbidden-anchor contradictions, stale placeholders, and paper-gate overclaims.

## Boundaries and scale limits

Single transcript, curated claims, deterministic anchor checks, no blinded annotation, no comparison against naturally occurring multi-agent transcript failures.

## Claim scope

A deterministic evidence-ledger taxonomy caught six controlled failure modes across eleven curated claims grounded in one real local Codex tool-agent transcript.

## Why it stopped

Tier 1 direct test completed with useful mechanism support, but the evidence is curated and too small for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on 5-10 independent real tool-agent transcripts with blinded expected labels and compare against a baseline schema-only checker.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded multi-transcript evidence-ledger taxonomy validation
- Success threshold: At least 0.85 label recall and at least 0.80 label precision, with recall at least 0.25 absolute above schema-only baseline on actionable failure labels.
- Stop condition: Stop if label precision falls below 0.70, if recall improvement over schema-only baseline is below 0.10 absolute, or if independent transcripts cannot be gathered without private data exposure.

## Evidence references

- Artifact root: `<local-path>/projects/validate-evidence-ledger-failure-taxonomy-on-real-tool-age-f244e84e06`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
