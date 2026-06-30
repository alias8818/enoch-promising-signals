# N-gram Speculative Draft on CPU for GPU Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-on-cpu-for-gpu-decoding-3ca68df668e0`
Run ID: `n-gram-speculative-draft-on-cpu-for-gpu-decoding-3ca68df668e0-20260607T173141091804+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/95be05aca633

## What looked useful

CPU lookup cost is not the blocker; generic-corpus n-gram acceptance is the blocker. The standalone idea should not advance to paper or production integration without a better draft source.

## Boundaries and scale limits

Bounded local proxy only: distilgpt2, WikiText-2, greedy target tokens, 2048 single-token samples, 256 four-token rollout samples, isolated verifier calls rather than an end-to-end speculative decoding implementation.

## Claim scope

On distilgpt2 with WikiText-2 prefixes, a CPU n-gram draft table built from generic train text is much faster than GPU next-token verification but has low accepted-token yield: 21.63% single-token exact match for 1-5 backoff and 0.332 average accepted tokens per 4-token draft.

## Why it stopped

Bounded proxy falsification for the standalone idea: CPU drafting was fast, but four-token rollout accepted zero tokens on 74.22% of prefixes and accepted all four tokens on only 0.39%, so the measured yield is too low for a useful speculative decoder.

## Recommended next action

Stop this standalone generic-corpus n-gram path; a bounded follow-up should test whether prompt-local or target-generated n-gram caches raise average accepted tokens enough to matter.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-local n-gram cache draft for GPU speculative decoding
- Success threshold: At least 1.05x end-to-end generated tokens/sec over greedy decoding and at least 1.0 average accepted tokens per 4-token draft on two of three prompt domains, without more than 5% slowdown on the non-repetitive control.
- Stop condition: Stop if average accepted tokens remains below 0.75 per 4-token draft or end-to-end speedup is below 1.0x on two prompt domains after prompt-local cache tuning.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-on-cpu-for-gpu-decoding-3ca68df668e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
