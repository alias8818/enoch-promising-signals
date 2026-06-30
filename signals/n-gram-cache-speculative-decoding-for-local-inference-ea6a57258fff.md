# N-gram cache speculative decoding for local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cache-speculative-decoding-for-local-inference-ea6a57258fff`
Run ID: `n-gram-cache-speculative-decoding-for-local-inference-ea6a57258fff-20260527T152803174805+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d359c38564ef

## What looked useful

On 768 distilgpt2 greedy tokens, n=2 draft_len=8 reduced replay target calls from 768 to 404 (1.90 tokens/call, 47.4% ideal call reduction) with exact-output preservation, but traces were highly repetitive (mean repeat fraction 0.862).

## Boundaries and scale limits

Tested only 12 builtin prompts x 64 generated tokens with distilgpt2 plus a tiny-gpt2 smoke. No dataset-backed natural corpus, no larger local model, no sampling, and no production KV-cache wall-clock decoder were validated.

## Claim scope

A prompt/history n-gram cache can reduce ideal target verification calls for exact greedy speculative replay on small, repetitive distilgpt2 continuations.

## Why it stopped

No-paper closure: direct replay supports the mechanism only on small repetitive outputs, while broad/local-inference viability remains unvalidated and the Wikitext dataset probe timed out.

## Recommended next action

Stop this run as a bounded useful signal; the next concrete step is a KV-cache wall-clock implementation on a dataset-backed code or natural-text completion benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram speculative decoding benchmark for local code completion
- Success threshold: At least 15% p50 wall-clock latency reduction and exact output equality on 100+ prompts, with no more than 5% p95 latency regression.
- Stop condition: Stop if target-call reduction does not translate to at least 5% p50 wall-clock improvement in the first 30 benchmark prompts or if output equality fails.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cache-speculative-decoding-for-local-inference-ea6a57258fff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
