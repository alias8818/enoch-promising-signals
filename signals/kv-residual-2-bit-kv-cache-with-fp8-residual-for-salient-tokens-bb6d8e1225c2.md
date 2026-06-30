# KV Residual: 2-bit KV cache with FP8 residual for salient tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-residual-2-bit-kv-cache-with-fp8-residual-for-salient-tokens-bb6d8e1225c2`
Run ID: `kv-residual-2-bit-kv-cache-with-fp8-residual-for-salient-tokens-bb6d8e1225c2-20260614T033642028199+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8afe4dd041f4

## What looked useful

2-bit KV alone increased distilgpt2 mean NLL from 1.9890 to 3.3444. Norm-salient FP8 residuals at 20% coverage still had mean NLL 3.0987, while 100% residual coverage restored mean NLL to 1.9956. Oracle quantization-error salience improved sparse recovery but still left a 0.5851 NLL gap at 20% coverage.

## Boundaries and scale limits

Single small causal LM, deterministic synthetic local text, simulated packed storage, no fused serving kernel, no standard validation corpus, no 7B+ model, and no learned or attention-based salience predictor.

## Claim scope

In a bounded distilgpt2 CUDA teacher-forced decoding probe with per-token/head 2-bit KV quantization, FP8 residuals for 5-20% norm-salient cache token positions did not recover enough next-token quality to support the sparse salient-token proposal; dense residuals over all tokens nearly restored full precision at an estimated 0.625x BF16 KV storage.

## Why it stopped

Proxy/early falsification of the simple sparse norm-salient formulation, not full validation or full rejection of all residual KV-cache designs.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test attention/quantization-error-predictive salience on GPT-2-small-class validation data before any kernel or large-model work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Attention-predictive salience for 2-bit KV plus FP8 residuals
- Success threshold: At 20% FP8 residual coverage and <=0.25x BF16 KV logical storage, a deployable salience selector recovers at least 50% of the NLL degradation caused by 2-bit KV on a standard validation corpus.
- Stop condition: Stop if attention/predictive salience recovers less than 30% of the 2-bit NLL degradation at 20% coverage or if results are not better than the norm-salience baseline.

## Evidence references

- Artifact root: `<local-path>/projects/kv-residual-2-bit-kv-cache-with-fp8-residual-for-salient-tokens-bb6d8e1225c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
