# Real Quantized-Model Agent Ledger Recovery Probe

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-quantized-model-agent-ledger-recovery-probe-624f745db5`
Run ID: `real-quantized-model-agent-ledger-recovery-probe-624f745db5-20260604T201816672089+0000`

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

- Parent run decision: Quantized Agent Ledger: Q4_0 Reliability Recovery: enoch://control-plane/projects/quantized-agent-ledger-q4-0-reliability-recovery-7220bdc5d57c/runs/quantized-agent-ledger-q4-0-reliability-recovery-7220bdc5d57c-20260604T133841195470+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45c91285252e

## What looked useful

The prior Q4_0 simulation's byte-preserving repeated-bit ledger mechanism does not transfer automatically to a real quantized language model: model-side parsing/recovery can be the binding failure, and repeated-bit payloads added token and latency overhead while underperforming compact tuples.

## Boundaries and scale limits

This was a small CPU-only Tier 1 test on GPT-2-small INT8 ONNX, not GGUF Q4_0 and not an instruction-tuned agent model. It used forced-choice log-likelihood scoring over 2-, 4-, and 6-record ledgers rather than a full tool-using agent loop or long-horizon memory task.

## Claim scope

In a 24-case forced-choice final-balance recovery probe using a real locally cached GPT-2-small INT8 ONNX model, repeated-bit ledger prompts did not improve model recovery versus compact controls. Repeated-bit accuracy was 20.8%, compact tuple accuracy was 33.3%, hex payload accuracy was 20.8%, no-ledger control accuracy was 29.2%, and explicit-answer control accuracy was 100.0%. Deterministic repeated-bit ledger decode was 100.0%, so the observed failure is model-side recovery rather than encoded-ledger corruption.

## Why it stopped

Direct Tier 1 real-model evidence failed the stated threshold: repeated-bit ledger prompts did not reduce ledger-state recovery errors by 80% versus compact controls and did not preserve task success.

## Recommended next action

Stop this run as a no-paper useful negative signal; a bounded retry should use a real quantized instruction-tuned model with decoder exemplars before any larger agent-loop validation.

## Follow-up

- Recommended: `true`
- Type: `retry`
- Title: Instruction-Tuned Quantized Ledger Decoder Probe
- Success threshold: The redundant/isolated ledger condition must reduce exact final-state errors by at least 80% versus the best compact non-answer control and must not reduce accuracy by more than 5 percentage points versus the natural-language ledger condition, with zero prompt truncation on the bounded suite.
- Stop condition: Stop if the instruction-tuned quantized model still fails to outperform compact controls, if repeated/redundant prompts exceed context budget, or if explicit-answer control is below 95% accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/real-quantized-model-agent-ledger-recovery-probe-624f745db5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
