# 4-Bit Quantized Auditor for Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantized-auditor-for-agent-evidence-ledger-bbe0d8953a9b`
Run ID: `4-bit-quantized-auditor-for-agent-evidence-ledger-bbe0d8953a9b-20260525T020642241067+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8993b96b9aa6

## What looked useful

The corrected task is auditable by a deterministic checker at 100% accuracy. A raw FP32 text auditor failed near chance and accepted 87.35% of invalid standard ledgers; its 4-bit version preserved that unsafe behavior rather than fixing it. A hybrid invariant-feature FP32/8-bit auditor reached 100% standard accuracy, but naive 4-bit post-training quantization fell to 79.45% accuracy with a 41.94% false-accept rate, making it unsafe without calibration or QAT.

## Boundaries and scale limits

Synthetic ledgers only; no real agent traces, no long-context production ledgers, no human/LLM adjudication baseline, no quantization-aware training, and no deployment latency study. The 4-bit implementation is transparent weight-only dequantized PyTorch rather than a specialized packed inference kernel.

## Claim scope

Bounded synthetic evidence-ledger classification on generated ledgers with exact hash, signature, dependency, timestamp, duplicate-evidence, and verdict invariants. Raw text GRU auditors and naive post-training 4-bit weight-only quantization were tested against FP32, 8-bit, symbolic, and invariant-feature controls.

## Why it stopped

Bounded local evidence does not support a paper-positive 4-bit auditor claim: the raw neural auditor is unsafe, and naive 4-bit post-training quantization creates unacceptable false accepts in the otherwise solvable feature-auditor control.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded test is quantization-aware or calibrated 4-bit training for the hybrid invariant-feature auditor with a false-accept threshold below 1%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated 4-bit hybrid auditor for exact evidence-ledger invariants
- Success threshold: Calibrated/QAT 4-bit hybrid auditor achieves at least 99% standard accuracy, less than 1% standard false-accept rate, and no more than 2 percentage points absolute accuracy drop from FP32 on the same features.
- Stop condition: Stop if calibrated/QAT 4-bit still exceeds 5% false-accept rate on standard invalid ledgers or if hard-split false accepts remain above 20% after feature and threshold calibration.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantized-auditor-for-agent-evidence-ledger-bbe0d8953a9b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
