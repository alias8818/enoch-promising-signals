# 1-Bit Draft with Residual Correction Speculative Decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-draft-with-residual-correction-speculative-decode-15f1a61ca7fe`
Run ID: `1-bit-draft-with-residual-correction-speculative-decode-15f1a61ca7fe-20260604T154210864966+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/52d33b61574f

## What looked useful

In a deterministic proxy with 4096 distribution contexts and 2500 speculative windows per lookahead, uncorrected 1-bit draft achieved 3.3896 output tokens per target call at lookahead 8. Rank-64 residual correction improved this to 4.5104, a 33.1% relative gain, while using 31.47% of dense fp16 storage.

## Boundaries and scale limits

No real transformer, tokenizer, training, serving latency, KV-cache behavior, or hardware 1-bit kernel was tested. Metrics are mechanism-level acceptance and storage proxies, not end-to-end LLM throughput.

## Claim scope

Synthetic linear-logit proxy evidence shows that low-rank residual correction can improve exact speculative decoding acceptance for a 1-bit draft distribution compared with uncorrected 1-bit quantization.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/logit-level and cannot validate real LLM serving speed or quality.

## Recommended next action

Run a bounded real-transformer deepen test with exact speculative sampling, wall-clock throughput, and dense versus 1-bit-plus-residual draft baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer 1-Bit Residual Draft Speculative Decode Benchmark
- Success threshold: At least 15% wall-clock throughput improvement over uncorrected 1-bit draft and at least 80% of dense-draft acceptance while using no more than 35% of dense fp16 draft storage.
- Stop condition: Stop if residual correction fails to improve wall-clock throughput by 5% over uncorrected 1-bit draft or if residual storage exceeds 50% of dense fp16 without approaching dense-draft acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-draft-with-residual-correction-speculative-decode-15f1a61ca7fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
