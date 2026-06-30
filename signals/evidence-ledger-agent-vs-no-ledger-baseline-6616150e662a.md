# Evidence-Ledger Agent vs No-Ledger Baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-vs-no-ledger-baseline-6616150e662a`
Run ID: `evidence-ledger-agent-vs-no-ledger-baseline-6616150e662a-20260628T090404310030+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b02ddc9a4384

## What looked useful

The evidence-ledger gate accepted all 160 supported claims, rejected all 480 unsupported trap claims, and reduced unsupported false accepts from 1.0 in the no-ledger baseline to 0.0.

## Boundaries and scale limits

Synthetic cases only; no real LLM agent traces, no natural-language evidence ambiguity, no stronger LLM verifier baseline, and no production task overhead measurement.

## Claim scope

In a deterministic synthetic benchmark of 640 explicit claim/evidence cases, requiring evidence references to exist and match entity, metric, and value eliminated unsupported false accepts relative to a no-ledger surface-form baseline.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct full validation of real evidence-ledger agents.

## Recommended next action

Stop this run as no-paper useful signal; next run should evaluate the same ledger/no-ledger protocol on real tool-agent traces with a stronger no-ledger verifier baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger gating on real tool-agent traces
- Success threshold: At least 0.25 absolute reduction in unsupported false-accept rate versus the strongest no-ledger baseline with supported false-reject rate under 5% on at least 200 labeled real claims.
- Stop condition: Stop if the ledger gate does not beat the strongest no-ledger baseline by 0.10 absolute false-accept reduction, or if supported false rejects exceed 10%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-vs-no-ledger-baseline-6616150e662a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
