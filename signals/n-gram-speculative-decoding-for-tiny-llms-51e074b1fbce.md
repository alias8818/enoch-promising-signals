# N-gram Speculative Decoding for Tiny LLMs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-speculative-decoding-for-tiny-llms-51e074b1fbce`
Run ID: `n-gram-speculative-decoding-for-tiny-llms-51e074b1fbce-20260604T180932806140+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/051f75e5febd

## What looked useful

A simple n-gram suffix drafter from calibration text had low accepted/proposed rates around 6% and weak median call-reduction ceilings. The bounded direct implementation also exposed a cached block-verification correctness issue in this stack, so future work should validate exact greedy equivalence before optimizing latency.

## Boundaries and scale limits

Single tiny/small GPT-2-class model, WikiText-2 only, 48-prompt trace confirmation, 4-prompt direct smoke. Trace results are idealized and do not replace a correct optimized speculative decoder. No large-model, multi-domain, batching, or serving-system validation was run.

## Claim scope

On distilgpt2 with WikiText-2 prompts and a calibration-corpus n-gram drafter, max draft length 4, the method did not validate as a practical speedup. The direct cached smoke was slower than greedy and had one exact-output mismatch; ideal trace ceilings showed only 8.72% overall target-call reduction for n=2..5 and 12.63% with unigram backoff.

## Why it stopped

Bounded local evidence is an early negative/proxy falsification of the practical-speedup hypothesis, not a full validation: the direct smoke failed exact-output equivalence on 1/4 prompts and was slower than greedy, while the trace ceiling showed low median target-call savings.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test a prompt-local or domain-matched n-gram cache with a verified exact cached decoder.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-local n-gram speculative decoding with exact cache validation
- Success threshold: Zero correctness mismatches, median target-call reduction >= 20%, and measured speedup > 1.05x on the same bounded prompt/model setup.
- Stop condition: Stop if exact-output equivalence fails after cache verification fixes, or if median target-call reduction remains below 20% on the 48-prompt trace.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-tiny-llms-51e074b1fbce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
