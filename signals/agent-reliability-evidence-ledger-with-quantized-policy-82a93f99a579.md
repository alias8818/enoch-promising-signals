# Agent Reliability Evidence Ledger with Quantized Policy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-evidence-ledger-with-quantized-policy-82a93f99a579`
Run ID: `agent-reliability-evidence-ledger-with-quantized-policy-82a93f99a579-20260609T063235816596+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/25069159f620

## What looked useful

Quantized confidence/count policies are viable as compact policy tables for evidence-ledger agents in calibrated heterogeneous evidence, but posterior-sum ledgers alone can amplify bad provenance. Retaining contradiction structure in the ledger reduced unsafe answers in adversarial and calibration-shift scenarios, at the cost of high deferral.

## Boundaries and scale limits

Synthetic/proxy evidence only: 4 scenarios, 5 seeds, 200000 episodes per seed, no LLM agents, no real tool traces, no human grading, and hand-specified source reliability and utility costs.

## Claim scope

In a synthetic sequential binary-decision benchmark, guarded quantized evidence-ledger policies can preserve continuous-ledger behavior and improve utility when evidence quality is heterogeneous, but they are brittle under adversarial first evidence and source calibration shift unless the quantized policy uses contradiction features and accepts high deferral.

## Why it stopped

Proxy benchmark produced mixed evidence: useful mechanism support in calibrated heterogeneous evidence, but early falsification of a broad reliability claim under adversarial first evidence and calibration shift.

## Recommended next action

Run a bounded deepen follow-up on replayed real or realistic agent/tool traces with oracle correctness labels, injected provenance faults, and pre-registered deferral costs; stop here for this synthetic run because it is a proxy useful signal, not full validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Contradiction-aware quantized evidence ledgers on replayed agent traces
- Success threshold: Contradiction-aware quantized ledger reduces unsafe answer rate by >=30% versus the best non-contradiction ledger baseline while keeping deferral rate <=2x that baseline and utility non-inferior within 5%.
- Stop condition: Stop if contradiction-aware policy fails to improve unsafe answer rate by 10% in a 100-trace smoke replay, or if required oracle labels/provenance fields cannot be obtained.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-evidence-ledger-with-quantized-policy-82a93f99a579`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
