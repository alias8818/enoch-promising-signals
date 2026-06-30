# Adaptive N-Gram Speculative Decoding for Local LLMs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `adaptive-n-gram-speculative-decoding-for-local-llms-44003c04405d`
Run ID: `adaptive-n-gram-speculative-decoding-for-local-llms-44003c04405d-20260524T042143015944+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e3b3d8e8ad10

## What looked useful

Fixed n-gram speculation had only small ceilings on ordinary prose (1.02x-1.06x) but a large ceiling on a repeated code-like trace (5.82x). Two adaptive policies underperformed the best fixed policy on every confirmation trace, suggesting workload-class detection plus tuned fixed settings is a stronger first baseline than adaptive n/gamma control.

## Boundaries and scale limits

No real LLM verifier, GPU batch verification, KV-cache rollback, sampling, or production runtime latency was measured. Results are a mechanism-level proxy and should not be read as full local LLM serving validation.

## Claim scope

Trace-level prompt-lookup speculative decoding on 10k-token local evaluation windows from public-domain prose and a synthetic repeated code-like trace. The tested adaptive n/gamma policies did not beat the best tuned fixed n/gamma policy on target-call reduction ceiling.

## Why it stopped

Proxy confirmation falsified the adaptive-policy advantage at the trace level; this is not a full serving validation, but it is enough to reject paper writing from the current evidence.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test direct local LLM serving latency and require adaptive control to beat the best tuned fixed n/gamma baseline by at least 5%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local LLM Latency Test for Adaptive N-Gram Prompt Lookup
- Success threshold: Adaptive policy achieves at least 5% higher end-to-end tokens/s or 5% lower p50 latency than the best fixed n/gamma policy on repeated-template/code or RAG-copy prompts without regressing prose by more than 2%.
- Stop condition: Stop if adaptive policy fails to beat the tuned fixed baseline by 5% on two prompt classes or if proposer overhead exceeds the verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-n-gram-speculative-decoding-for-local-llms-44003c04405d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
