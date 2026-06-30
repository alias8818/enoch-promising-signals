# N-gram Suffix Speculative Decoding for CPU Workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-speculative-decoding-for-cpu-workers-0e37be26785a`
Run ID: `n-gram-suffix-speculative-decoding-for-cpu-workers-0e37be26785a-20260621T060222098915+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/7933f37160e7

## What looked useful

Best local project-text run reduced target calls by 43.1% with a 1.724x cost-model speedup; repetitive trace control reduced target calls by 80.9% with a 5.135x cost-model speedup; shuffled and low-reuse controls were slightly below 1.0x after lookup cost.

## Boundaries and scale limits

Only bounded token traces were evaluated. No real LLM verifier, tokenizer-specific serving path, KV-cache behavior, batching, sampling quality, or wall-clock decoder integration was measured.

## Claim scope

Trace-level online n-gram suffix speculative decoding can reduce verifier target-call count on repeated local token streams and local project prose, but controls show no benefit on shuffled or low-reuse streams.

## Why it stopped

Proxy trace evidence is useful but insufficient for a paper or full validation; no real model verifier wall-clock result was produced.

## Recommended next action

Run a bounded direct CPU-decoder integration on a small local model with repeated prompt traces and shuffled/non-repetitive controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU decoder test for n-gram suffix speculative drafting
- Success threshold: At least 25% wall-clock decode throughput improvement on repeated prompt traces with no quality regression and less than 5% overhead on non-repetitive controls.
- Stop condition: Stop if direct decoder integration shows less than 10% throughput improvement on repeated traces or more than 5% slowdown on controls after lookup overhead.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculative-decoding-for-cpu-workers-0e37be26785a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
