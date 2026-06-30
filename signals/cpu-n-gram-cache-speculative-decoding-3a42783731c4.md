# CPU N-gram cache speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-cache-speculative-decoding-3a42783731c4`
Run ID: `cpu-n-gram-cache-speculative-decoding-3a42783731c4-20260524T042712943688+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9b19fa4a73f3

## What looked useful

CPU n-gram cache speculation is mechanically viable and cheap, but acceptance quality is weak for general prose and only moderately useful for repetitive code. Best gamma=8 full-draft acceptance was below 0.05% on prose and at most 1.215% on Python code, so this is not paper-positive as a general speculative decoder.

## Boundaries and scale limits

Proxy trace replay only; no target LLM, sampler, GPU verifier, KV-cache scheduler, multi-request cache sharing, or wall-clock serving benchmark. Corpora are small to medium, with only one 250k-token corpus and two small code files.

## Claim scope

Online replay over four public cl100k_base-tokenized text/code traces shows that a simple CPU n-gram cache has tiny lookup overhead and can reduce optimistic target verification calls by 28-35% on small Python code files, but only 11-15% on prose, before real LLM serving overheads.

## Why it stopped

Bounded proxy evidence supports the mechanism only for repetitive code-like traces and does not validate net LLM serving speedup; broader paper claims would require direct target-model wall-clock evidence.

## Recommended next action

Stop this run as no-paper useful signal; next concrete test is a bounded real serving benchmark on code-completion traces comparing CPU n-gram speculation with no speculation and a tiny neural draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real serving benchmark for CPU n-gram speculation on code completion
- Success threshold: At least 10% net wall-clock throughput improvement over no speculation on code-completion traces, with no quality regression and a clear domain where CPU n-gram speculation matches or beats the tiny neural draft baseline.
- Stop condition: Stop if integrated serving speedup is below 5% after overheads or if accepted tokens per verifier call stays below 1.2 on code traces.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-cache-speculative-decoding-3a42783731c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
