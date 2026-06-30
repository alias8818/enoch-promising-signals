# CPU N-gram Draft for GPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-for-gpu-speculative-decoding-e049dbc5da19`
Run ID: `cpu-n-gram-draft-for-gpu-speculative-decoding-e049dbc5da19-20260608T191142451676+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/90c415cb3930

## What looked useful

CPU n-gram drafting is cheap and can reduce target forward calls when generated text becomes repetitive. The signal weakens on GPT-2 prompts with less degenerate repetition, so the idea is useful but not paper-ready.

## Boundaries and scale limits

Small prompt set; distilgpt2 and gpt2 only; recompute-based verifier rather than production KV-cache serving; no p50/p95 serving latency or broad workload coverage.

## Claim scope

In short greedy-decoding tests on GB10, a CPU n-gram proposer produced accepted draft tokens and reduced GPU target-model forward calls, with the strongest effect on repetitive continuations.

## Why it stopped

No-paper useful signal: direct acceptance and forward-call evidence exists, but the current run is a bounded proxy and not full serving validation.

## Recommended next action

Run a bounded KV-cache implementation on representative prompts and compare p50/p95 latency against target-only decoding plus repeat/unigram controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache latency test for CPU n-gram speculative decoding
- Success threshold: At least 15% p50 latency improvement and no p95 regression over target-only decoding on a declared repetitive/code-like subset, with exact greedy-output match.
- Stop condition: Stop if acceptance stays below 25% or p50 latency improvement is under 5% after controlling for repeat/unigram baselines.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-for-gpu-speculative-decoding-e049dbc5da19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
