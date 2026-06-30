# Blinded audit of evidence-ledger tool-error policy on frozen real traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `blinded-audit-of-evidence-ledger-tool-error-policy-on-froz-11c1dd20da`
Run ID: `blinded-audit-of-evidence-ledger-tool-error-policy-on-froz-11c1dd20da-20260601T045630766017+0000`

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

- Parent run decision: Replay evidence-ledger policy on real agent tool-error traces: enoch://control-plane/projects/replay-evidence-ledger-policy-on-real-agent-tool-error-tra-00ee1f9dc7/runs/replay-evidence-ledger-policy-on-real-agent-tool-error-tra-00ee1f9dc7-20260531T223028136502+0000
- Parent run decision: Tiny Agent Evidence Ledger for Tool-Use Reliability: enoch://control-plane/projects/tiny-agent-evidence-ledger-for-tool-use-reliability-17fb333e232c/runs/tiny-agent-evidence-ledger-for-tool-use-reliability-17fb333e232c-20260531T175620820376+0000

## What looked useful

The full audit found 4,475 high-confidence tool-error positives. Ledger policy mean held-out F1 was 1.000 versus 0.576 for the exit-code baseline and 0.868 for the keyword baseline. Removing output evidence collapsed F1 to the exit-code baseline, showing semantic output errors were the main source of baseline misses.

## Boundaries and scale limits

Labels are deterministic high-confidence audit labels derived from the same trace evidence fields used by the policy, not independent human-adjudicated labels; corpus is one Enoch CPU worker's Codex traces and does not test downstream recovery behavior.

## Claim scope

On 914 frozen Enoch Codex trace files containing 37,763 command/tool events, a deterministic evidence-ledger policy using exit/status plus output-error evidence recovered high-confidence tool-error events much better than a nonzero-exit baseline under fixed project-level splits.

## Why it stopped

Tier 2 medium real-trace confirmation met the mechanism threshold with fixed seeds, ablations, and a real baseline, but the rule-derived oracle is not independent enough for paper-positive evidence.

## Recommended next action

Run a blinded independent adjudication of a stratified held-out sample of real tool events, especially semantic-error and benign-error-phrase cases, before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Independent adjudication of evidence-ledger tool-error labels
- Success threshold: Evidence-ledger policy improves F1 over exit-code-only baseline by >=0.10 on independent labels, precision >=0.90, and output/no-output ablation gap >=0.10 F1.
- Stop condition: Stop if independent adjudication shows ledger-policy precision below 0.90 or F1 improvement over exit-code-only baseline below 0.05.

## Evidence references

- Artifact root: `<local-path>/projects/blinded-audit-of-evidence-ledger-tool-error-policy-on-froz-11c1dd20da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
