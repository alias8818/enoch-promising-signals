# Evidence-ledger auditing on labeled real agent traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-auditing-on-labeled-real-agent-traces-31f67d61a0`
Run ID: `evidence-ledger-auditing-on-labeled-real-agent-traces-31f67d61a0-20260525T105500991751+0000`

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

- Parent run decision: Counterexample Mining for Agent Reliability via Evidence Ledger Auditing: enoch://control-plane/projects/counterexample-mining-for-agent-reliability-via-evidence-ledger-auditing-7b8cb88550e5/runs/counterexample-mining-for-agent-reliability-via-evidence-ledger-auditing-7b8cb88550e5-20260525T095401192632+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/74ba39470e6c

## What looked useful

Initial labeled-set ledger F1 was 1.00 versus 0.57 for a keyword baseline, but holdout ledger F1 fell to 0.40 with recall 0.25, exposing brittle claim extraction despite high precision.

## Boundaries and scale limits

Tested on 16 initial labeled trace cases and 8 controlled holdout cases; only a few cases were directly derived from current-run real Codex logs, and no large independent human-labeled trace corpus was available.

## Claim scope

A deterministic evidence-ledger auditor can catch some unsupported or contradicted claims in small Codex-style labeled traces with high precision, but the tested implementation does not generalize across common holdout paraphrases.

## Why it stopped

No-paper useful signal: the controlled Tier 1 test supports the ledger mechanism on seen patterns but the holdout directly fails the stated recall/F1 threshold.

## Recommended next action

Deepen with an independently labeled 50-100 trace corpus and frozen auditor/parser before evaluation; stop paper work until holdout recall and F1 reach at least 0.80.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen evidence-ledger audit on independently labeled real traces
- Success threshold: Ledger F1 >= 0.80, recall >= 0.80, precision >= 0.80, and F1 at least 0.20 above both baselines on the frozen independent corpus.
- Stop condition: Stop as negative if frozen-auditor holdout recall or F1 remains below 0.80, or if most misses require semantic interpretation unavailable from local trace evidence.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-auditing-on-labeled-real-agent-traces-31f67d61a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
