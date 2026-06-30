# Suffix-Array Speculative Decoding from Prompt Token Cache

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `suffix-array-speculative-decoding-from-prompt-token-cache-c5deafe547d1`
Run ID: `suffix-array-speculative-decoding-from-prompt-token-cache-c5deafe547d1-20260529T165133786908+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/35d2c96c8efa

## What looked useful

Prompt-cache suffix-array drafting mechanically works but most matches back off to 1-2 token contexts. It accepted only 0.116 tokens per decode step in the 12k prompt run and 0.117 in the 64k prompt check, while a simpler hash backoff n-gram cache accepted slightly more tokens with roughly 15-18x lower query latency.

## Boundaries and scale limits

Does not test BPE tokenization, model-generated decoding traces, neural verifier latency, GPU KV-cache integration, batching, or end-to-end serving throughput.

## Claim scope

Offline prompt-cache retrieval benchmark on Project Gutenberg continuations with word/punctuation tokens, 12k-token prompts across four books plus a 64k-token two-book scale check.

## Why it stopped

Proxy early falsification: on real-text continuations the suffix-array prompt-cache drafter had low acceptance and did not beat a simpler hash backoff baseline on the online query path.

## Recommended next action

Stop this project as a no-paper useful negative signal; only reopen for a bounded BPE/model-trace validation against hash backoff if real decode traces are available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE Model-Trace Prompt-Cache Drafter Validation
- Success threshold: Support the suffix-array idea only if it improves accepted tokens per verifier step by at least 20% over hash backoff while keeping p95 query latency below 5% of verifier step time.
- Stop condition: Stop if suffix-array acceptance is within 20% of hash backoff or p95 query latency exceeds 5% of verifier step time.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-from-prompt-token-cache-c5deafe547d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
