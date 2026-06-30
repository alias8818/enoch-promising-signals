# Small-model evidence-ledger tool-calling validation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `small-model-evidence-ledger-tool-calling-validation-858ad694c5`
Run ID: `small-model-evidence-ledger-tool-calling-validation-858ad694c5-20260608T173918539742+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Structured Evidence Ledger for Tiny Tool-Calling Agents: enoch://control-plane/projects/structured-evidence-ledger-for-tiny-tool-calling-agents-4e68b5afe514/runs/structured-evidence-ledger-for-tiny-tool-calling-agents-4e68b5afe514-20260608T155151540920+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9b056dfa36f3

## What looked useful

Baseline achieved 16/24 accuracy versus 15/24 for the evidence-ledger condition. The ledger condition improved parse rate from 0.1667 to 0.5417 and mean latency from 1.5915 s to 1.1599 s, but paired accuracy changes were 3 improvements and 4 regressions, including unsupported answers marked supported.

## Boundaries and scale limits

Single quantized local small model, one deterministic decoding configuration, synthetic labeled traces, no production traces, no multi-model or multi-seed replication, and no end-to-end tool-use agent evaluation.

## Claim scope

On a 24-case controlled synthetic paired benchmark using local Phi-4-mini-instruct Q4_K_M via llama.cpp, evidence-ledger prompting did not improve small-model supported/unsupported validation accuracy over an ordinary chronological tool-trace prompt.

## Why it stopped

Controlled Tier 1 direct test failed to show an evidence-ledger accuracy advantage; this is an early bounded falsification, not a full validation across models or production traces.

## Recommended next action

Stop this run as a bounded early negative/useful-signal result; any next test should use real or realistically sampled tool-calling traces with multiple small models and a predefined ledger advantage threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model real-trace evidence-ledger validation benchmark
- Success threshold: Ledger condition must exceed baseline accuracy by at least 10 percentage points and must not increase unsupported-as-supported errors on any tested model.
- Stop condition: Stop as negative if ledger accuracy is not at least 5 percentage points above baseline on the first 100-case realistic benchmark or if unsupported-as-supported errors increase.

## Evidence references

- Artifact root: `<local-path>/projects/small-model-evidence-ledger-tool-calling-validation-858ad694c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
