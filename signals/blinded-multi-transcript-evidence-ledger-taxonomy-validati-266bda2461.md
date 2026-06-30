# Blinded multi-transcript evidence-ledger taxonomy validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `blinded-multi-transcript-evidence-ledger-taxonomy-validati-266bda2461`
Run ID: `blinded-multi-transcript-evidence-ledger-taxonomy-validati-266bda2461-20260621T231812472231+0000`

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
- Parent run decision: Validate evidence-ledger failure taxonomy on real tool-agent transcripts: enoch://control-plane/projects/validate-evidence-ledger-failure-taxonomy-on-real-tool-age-f244e84e06/runs/validate-evidence-ledger-failure-taxonomy-on-real-tool-age-f244e84e06-20260621T223602887562+0000

## What looked useful

Blinding source and turn IDs did not break deterministic evidence-ledger taxonomy validation on controlled real-transcript cases; baselines and ablations failed on distinct taxonomy classes, showing the value of explicit source, speaker, turn, quote, and evidence-reference checks.

## Boundaries and scale limits

Labels are controlled corruptions over real transcripts, not independently authored or human-adjudicated claims; paraphrase, partial support, ambiguous speakers, multi-evidence synthesis, and adversarial natural-language cases remain unvalidated.

## Claim scope

On 840 fixed-seed blinded ledger cases generated from 4,778 turns across four public transcript sources, a source/speaker/turn/quote/reference taxonomy verifier achieved 1.0000 support accuracy, 0.0000 false-positive rate, and 1.0000 taxonomy accuracy against controlled gold labels.

## Why it stopped

Tier 2 bounded validation succeeded, but evidence remains controlled-label mechanism support rather than publication-grade open-ended validation.

## Recommended next action

Run the same blinded taxonomy protocol on independently authored agent or human claims with adjudicated labels before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adjudicated natural-claim blinded transcript taxonomy validation
- Success threshold: Support accuracy >= 0.85, false-positive rate <= 0.10, taxonomy macro-F1 >= 0.75, and no single failure class below 0.60 F1 on adjudicated natural claims.
- Stop condition: Stop as negative if support accuracy < 0.75, false-positive rate > 0.20, or taxonomy macro-F1 < 0.60 after adjudication cleanup.

## Evidence references

- Artifact root: `<local-path>/projects/blinded-multi-transcript-evidence-ledger-taxonomy-validati-266bda2461`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
