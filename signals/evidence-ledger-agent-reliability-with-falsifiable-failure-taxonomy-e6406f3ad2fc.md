# Evidence-ledger agent reliability with falsifiable failure taxonomy

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-reliability-with-falsifiable-failure-taxonomy-e6406f3ad2fc`
Run ID: `evidence-ledger-agent-reliability-with-falsifiable-failure-taxonomy-e6406f3ad2fc-20260621T214844464776+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/73774bf46032

## What looked useful

Evidence references, local provenance checks, temporal ordering, command exit checks, and numeric consistency checks caught missing evidence, contradicted values, wrong provenance, stale evidence, scope creep, failed commands, and arithmetic inconsistency in all injected cases.

## Boundaries and scale limits

Synthetic templated traces only; no real LLM/tool-agent transcripts, no adversarial phrasing, no human-labeled corpus, and no deployed-agent reliability measurement.

## Claim scope

On a deterministic 800-case synthetic benchmark with seven templated invalid failure modes and supported controls, explicit evidence-ledger checks eliminated false accepts that a permissive claim-only baseline accepted.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not full validation or paper-ready evidence for real agent reliability.

## Recommended next action

Stop this run as no-paper useful signal; next run should validate the same verifier on a small human-labeled corpus of real LLM/tool-agent transcripts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate evidence-ledger failure taxonomy on real tool-agent transcripts
- Success threshold: At least 50% relative reduction in false accept rate versus baseline with false reject rate on supported claims at or below 10%.
- Stop condition: Stop as negative if the verifier fails to reduce false accepts by 25% or if supported-claim false rejects exceed 20% on the labeled corpus.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-with-falsifiable-failure-taxonomy-e6406f3ad2fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
