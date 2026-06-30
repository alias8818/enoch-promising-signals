# N-Gram Speculative Decoding on CPU with Exact Fallback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-on-cpu-with-exact-fallback-1be2472caebc`
Run ID: `n-gram-speculative-decoding-on-cpu-with-exact-fallback-1be2472caebc-20260531T181640998104+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1f7c49f7f4e2

## What looked useful

Best speedups were 2.36x at zero mismatch, 2.16x at low mismatch, 3.03x at moderate mismatch, 1.75x at medium mismatch, and 1.24x at high mismatch. At high mismatch, block sizes 2 and 16 were slower than baseline. The 3,000-sample parity check showed mean total variation 0.103 and max 0.162 versus a rough finite-sample noise scale of 0.292, supporting exact-fallback distribution preservation in this proxy.

## Boundaries and scale limits

No PyTorch/Transformers runtime was available in the worker, so this did not test a real transformer, KV cache, tokenizer, production CPU serving stack, or natural-language corpus. Timing is for a synthetic 256-token conditional distribution with 4,000-token rows and a 29-second bounded run.

## Claim scope

In a self-contained NumPy CPU proxy with an exact speculative sampler, n-gram draft proposals reduce target invocations and improve throughput when draft-target mismatch is low to moderate; high mismatch and oversized blocks can erase or reverse the speedup.

## Why it stopped

Bounded proxy evidence supports the mechanism but is not a full validation on a real transformer CPU runtime.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should port the harness to a real small CPU causal LM with KV cache and a prompt/corpus n-gram draft.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LM n-gram speculative decoding with exact fallback
- Success threshold: At least 1.25x median tokens/sec speedup over baseline on one realistic repeated-context regime without distribution/parity failure, plus a documented mismatch regime where the method is neutral or negative.
- Stop condition: Stop if acceptance stays below 0.6 across realistic prompts or if verified throughput is not at least 1.1x baseline after block-size tuning.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-with-exact-fallback-1be2472caebc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
