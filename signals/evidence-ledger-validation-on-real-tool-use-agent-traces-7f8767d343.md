# Evidence-ledger validation on real tool-use agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-validation-on-real-tool-use-agent-traces-7f8767d343`
Run ID: `evidence-ledger-validation-on-real-tool-use-agent-traces-7f8767d343-20260604T175919308925+0000`

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

- Parent run decision: Evidence Ledger for Tool-Use Agent Reliability: enoch://control-plane/projects/evidence-ledger-for-tool-use-agent-reliability-7c4b6c78b407/runs/evidence-ledger-for-tool-use-agent-reliability-7c4b6c78b407-20260604T131416055624+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/051f75e5febd

## What looked useful

On the frozen real trace snapshot, the ledger accepted all 3 supported claims and rejected all 3 unsupported or contradicted controls: true_positive=3, false_negative=0, true_negative=3, false_positive=0.

## Boundaries and scale limits

Tested on one 33-line real trace snapshot with 9 extracted command-output evidence items, 3 supported claims, and 3 negative controls. No automated claim extraction, corpus-scale validation, adversarial paraphrase handling, or multi-agent trace diversity was tested.

## Claim scope

A deterministic evidence ledger can validate a small hand-authored set of factual claims against a frozen real Codex tool-use trace snapshot by requiring claim-specific evidence matches.

## Why it stopped

Tier 1 direct mechanism test passed on a real trace snapshot, but the evidence is small and hand-authored rather than a full validation.

## Recommended next action

Run a bounded deepen follow-up on at least 50 real tool-use traces with manually labeled claim/evidence pairs and independently generated negative controls; stop short of paper claims unless error rates remain low across trace diversity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Labeled multi-trace evidence-ledger validation
- Success threshold: At least 90% precision, at least 90% recall, and at most 10% false-positive rate on unsupported controls across at least 50 real traces.
- Stop condition: Stop if fewer than 50 real traces can be labeled locally, if unsupported-control false positives exceed 20% after the first 20 traces, or if supported-claim recall falls below 80% after the first 20 traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-validation-on-real-tool-use-agent-traces-7f8767d343`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
