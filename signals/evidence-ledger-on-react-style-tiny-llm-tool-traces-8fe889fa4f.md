# Evidence Ledger on ReAct-Style Tiny LLM Tool Traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-on-react-style-tiny-llm-tool-traces-8fe889fa4f`
Run ID: `evidence-ledger-on-react-style-tiny-llm-tool-traces-8fe889fa4f-20260604T025215829811+0000`

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

- Parent run decision: Evidence Ledger on Real Tiny LLM Tool-Agent Traces: enoch://control-plane/projects/evidence-ledger-on-real-tiny-llm-tool-agent-traces-09014cbbe3/runs/evidence-ledger-on-real-tiny-llm-tool-agent-traces-09014cbbe3-20260604T010550767738+0000
- Parent run decision: Evidence Ledger for Tiny Tool Agents: enoch://control-plane/projects/evidence-ledger-for-tiny-tool-agents-0e0162cbb7f1/runs/evidence-ledger-for-tiny-tool-agents-0e0162cbb7f1-20260603T221203805557+0000

## What looked useful

Evidence ledger formatting alone did not improve learned tiny verifier accuracy over raw traces. In the stronger derived-answer ledger run, seq ledger_trace averaged 0.4963 accuracy versus 0.4970 for raw_trace, and clean-vs-corrupt ledger delta was 0.0 accuracy/F1, even though a deterministic ledger parser solved the ledger labels with 1.0 accuracy.

## Boundaries and scale limits

Synthetic traces only; no real agent traces, no pretrained tiny LLM verifier, no large model, and no production ledger generator. The result tests small PyTorch BOW/GRU verifiers rather than all possible tiny LLM architectures.

## Claim scope

Medium synthetic ReAct-style tool-trace support verification with fixed seeds, held-out entity names, raw-trace baseline, bag-of-words controls, and clean/corrupt/no-id/ledger-only ablations.

## Why it stopped

Tier 2 fixed-seed medium validation failed to show a direct learned-model benefit from evidence ledgers over raw traces and failed the clean-versus-corrupt ledger mechanism check.

## Recommended next action

Stop this branch as no-paper evidence; a next bounded deepen test should only proceed if it changes the verifier inductive bias, such as pointer/equality-aware or pretrained tiny-model verification, while preserving the clean/corrupt ledger controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pointer-aware tiny verifier for evidence-ledger equality checks
- Success threshold: Mean ledger_trace accuracy at least 0.10 above raw_trace and mean clean-ledger accuracy at least 0.10 above corrupt-ledger accuracy across the five fixed seeds.
- Stop condition: Stop as negative if the ledger_trace improvement is under 0.03 accuracy or the clean-minus-corrupt gap is under 0.05 accuracy across the fixed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-on-react-style-tiny-llm-tool-traces-8fe889fa4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
