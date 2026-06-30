# INT8 Agent Ledger Parsing Fidelity Test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-agent-ledger-parsing-fidelity-test-6cd623f5b4f2`
Run ID: `int8-agent-ledger-parsing-fidelity-test-6cd623f5b4f2-20260527T010413114434+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ca553ab2b4b6

## What looked useful

INT8 quantization was not the bottleneck in this proxy: FP32 and INT8 behaved nearly identically, while both failed on unseen ledger templates. Future work should prioritize layout robustness and real trace evaluation before treating INT8 as a parsing-fidelity risk.

## Boundaries and scale limits

Synthetic ledger records only; small MLP parser only; CPU NumPy implementation only; no real agent traces, no OCR/noisy ledgers, no LLM extraction model, and no production INT8 kernel or hardware-specific quantization backend.

## Claim scope

On a self-contained synthetic character-level ledger parsing benchmark, weight-only INT8 inference preserved FP32 extraction behavior for a small NumPy MLP tagger, with four-seed mean character prediction agreement of 0.999657 and no observed in-distribution record-exact degradation.

## Why it stopped

Proxy-only evidence supports INT8 fidelity for the toy tagger but also shows the broader ledger parser is not robust to unseen formats, so this is not a paper-ready validation.

## Recommended next action

Stop this run as a proxy useful-signal result; next run should evaluate a stronger parser on real or realistic agent ledger traces with explicit FP32/BF16 versus INT8 exact JSON recovery thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Agent Ledger INT8 Extraction Benchmark
- Success threshold: INT8 record-exact accuracy is no more than 0.5 percentage points below FP32/BF16 on in-distribution and near-distribution splits, with at least 95% FP32/BF16 baseline record-exact accuracy.
- Stop condition: Stop if the FP32/BF16 parser cannot reach 95% record-exact accuracy on the benchmark or if INT8 loses more than 0.5 percentage points after controlling prompts and decoding.

## Evidence references

- Artifact root: `<local-path>/projects/int8-agent-ledger-parsing-fidelity-test-6cd623f5b4f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
