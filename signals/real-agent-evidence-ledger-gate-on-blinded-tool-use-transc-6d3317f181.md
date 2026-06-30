# Real-agent evidence-ledger gate on blinded tool-use transcripts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-agent-evidence-ledger-gate-on-blinded-tool-use-transc-6d3317f181`
Run ID: `real-agent-evidence-ledger-gate-on-blinded-tool-use-transc-6d3317f181-20260629T142759294357+0000`

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

- Parent run decision: Evidence-Ledger Mandate for Tool-Using Agents: enoch://control-plane/projects/evidence-ledger-mandate-for-tool-using-agents-794ea2d7eb52/runs/evidence-ledger-mandate-for-tool-using-agents-794ea2d7eb52-20260629T135742220114+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0b7c62679c96

## What looked useful

The stdlib verifier achieved 1.000 accuracy, 0.000 false accept rate over 7 expected rejects, and 0.000 false reject rate over 5 expected accepts; an accept-all baseline falsely accepted every reject case.

## Boundaries and scale limits

Synthetic-only corpus: 4 cases, 7 observations, 12 labeled claims, explicit support/contradiction metadata, no real agent transcript corpus, no independent annotators, and no semantic claim matching.

## Claim scope

A deterministic evidence-ledger gate over a small synthetic blinded tool-use corpus can reject missing-reference, contradicted, unsupported, and unblinded-leak claims while accepting supported claims.

## Why it stopped

No-paper closure: bounded synthetic evidence supports the mechanism, but the original real-agent claim lacks direct real-transcript evidence.

## Recommended next action

Run the same gate on a held-out real-agent blinded transcript corpus with independent claim labels before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transcript evidence-ledger gate validation
- Success threshold: Gate false accept rate at least 50% lower than citation-only baseline with false reject rate no more than 10% absolute on independently labeled real transcripts.
- Stop condition: Stop if false accept reduction is under 20% versus citation-only baseline or if false rejects exceed 20% absolute after obvious label errors are removed.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-gate-on-blinded-tool-use-transc-6d3317f181`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
