# Quantized Agent Ledger: Q4_0 Reliability Recovery

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-agent-ledger-q4-0-reliability-recovery-7220bdc5d57c`
Run ID: `quantized-agent-ledger-q4-0-reliability-recovery-7220bdc5d57c-20260604T133841195470+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45c91285252e

## What looked useful

Q4_0 ledger reliability recovery appears to depend on isolating ledger values from unrelated block-scale selection and adding redundancy/audit checks; four-bit-friendly shared-block symbols were insufficient in this simulation.

## Boundaries and scale limits

No real LLM, GGUF runtime, tokenizer, agent loop, long-horizon task, or production ledger integration was tested. The successful encoding costs roughly 6,500 to 8,000 encoded bits per ledger record in this toy layout.

## Claim scope

In a local CPU Q4_0 block-quantization simulation, a block-isolated repeated-bit binary ledger with CRC/final-state validation recovered exact ledger bytes and state across 3,600 randomized trials spanning 16, 64, and 256 records and distractor scales 1 to 32; compact shared-block analog and Q4-native nibble baselines recovered 0 of 3,600 trials each.

## Why it stopped

Simulation evidence supports the local recovery mechanism but is proxy-only and does not validate real Q4_0 model-agent reliability.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same block-isolated ledger scheme in a real small quantized-model agent loop against compact and unquantized controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Quantized-Model Agent Ledger Recovery Probe
- Success threshold: Block-isolated ledger encoding should reduce exact ledger replay failures by at least 80% versus compact shared-block encoding without reducing task success by more than 5 percentage points on the bounded task suite.
- Stop condition: Stop if the real quantized-model loop shows no reduction in ledger replay failures, if overhead prevents completing the bounded tasks, or if failures are dominated by model instruction-following rather than ledger quantization.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-ledger-q4-0-reliability-recovery-7220bdc5d57c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
