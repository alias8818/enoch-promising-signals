# N-Gram Suffix Draft for Edge Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-suffix-draft-for-edge-speculative-decoding-4954ed37aa9a`
Run ID: `n-gram-suffix-draft-for-edge-speculative-decoding-4954ed37aa9a-20260524T000132802021+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/84a15477df72

## What looked useful

The method reduced distilgpt2 target calls by 79.7% on repetitive prompts with 76.4% proposal acceptance and by 58.6% on less deliberately repetitive prompts with 45.0% proposal acceptance, while exactly matching baseline greedy tokens.

## Boundaries and scale limits

Small GPT-2-class models only; 10 hand-built prompts per distilgpt2 condition; greedy decoding only; no public trace suite; no sampling-mode verification; no optimized KV-cache verifier; no mobile, NPU, or production edge runtime.

## Claim scope

In a bounded exact-greedy decoding harness with sshleifer/tiny-gpt2 smoke and distilgpt2 confirmation, a zero-parameter n-gram suffix draft over prompt/generated history preserved exact target output and reduced target forward calls on small hand-built repetitive and diverse prompt sets.

## Why it stopped

No-paper useful signal: the bounded local mechanism is supported, but the evidence is too small, hand-built, and non-production to justify a publication-grade positive claim.

## Recommended next action

Build an optimized KV-cache verifier and rerun on a public prompt trace or task corpus; proceed only if exact decoding keeps at least 25% target-call reduction and at least 10% end-to-end latency improvement versus one-token greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram suffix speculative decoding on public prompt traces
- Success threshold: At least 25% target-call reduction and at least 10% median end-to-end latency improvement with exact output preservation on the selected public corpus.
- Stop condition: Stop if exact-output preservation fails, median latency does not improve by 10%, or call reduction falls below 25% after KV-cache implementation and parameter sweep.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-draft-for-edge-speculative-decoding-4954ed37aa9a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
