# Prompt-Suffix N-gram Speculative Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-suffix-n-gram-speculative-decoding-without-draft-model-60e30849be7f`
Run ID: `prompt-suffix-n-gram-speculative-decoding-without-draft-model-60e30849be7f-20260604T012313671441+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4c5e4892e116

## What looked useful

Prompt-order suffix matches carry practical multi-token continuation signal in repetitive code/log contexts; the same mechanism is too weak on ordinary prose under the tested configuration.

## Boundaries and scale limits

No real target-model decoding loop, GPU serving stack, KV-cache implementation, sampling distribution, or 7B-class benchmark was tested. Speedup values are verifier-cycle upper bounds, not measured end-to-end latency.

## Claim scope

In a corpus-continuation simulator with 512-token prompts, prompt-suffix n-gram copying without a draft model produced negligible verifier-cycle benefit on prose/drama but an optimistic 1.57x-1.65x verifier-cycle speedup bound on Python stdlib code and templated logs, beating shuffled-order and unigram controls.

## Why it stopped

Closed as useful no-paper evidence because this run directly tested corpus continuation acceptance but only proxied model verification latency; it is not a full serving validation.

## Recommended next action

Run a bounded real-target-model benchmark with a small GPT-2-class or similar model, measuring wall-clock greedy equivalence and tokens/s for code/log/prose prompt sets before considering larger serving validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real target-model benchmark for prompt-suffix n-gram speculative decoding
- Success threshold: At least 10% wall-clock tokens/s improvement on code or log prompts with exact greedy output equivalence and no more than 2% slowdown on prose prompts.
- Stop condition: Stop if verifier/KV overhead yields less than 5% throughput gain on both code and log prompts or causes consistent prose slowdown above 5%.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-suffix-n-gram-speculative-decoding-without-draft-model-60e30849be7f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
