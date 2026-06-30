# CPU N-gram Suffix Draft for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-suffix-draft-for-speculative-decoding-741a12e4ee11`
Run ID: `cpu-n-gram-suffix-draft-for-speculative-decoding-741a12e4ee11-20260604T185133988789+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/34c67bd6c0ac

## What looked useful

CPU suffix lookup is fast and memory-light at this scale, and online history improves over controls, but naive most-common suffix continuation mostly helps one-token drafts and has weak multi-token acceptance.

## Boundaries and scale limits

Proxy trace replay only: no real LLM tokenizer, no target model verification, no KV-cache or CPU/GPU synchronization costs, one small public text corpus, and no end-to-end serving latency measurement.

## Claim scope

On a 262,927-token Tiny Shakespeare regex-token trace, a CPU online n-gram suffix table gives a small exact-match draft signal above static-prefix and shuffled-token controls, with best upper-bound 1.145 tokens per target call for one-token drafts.

## Why it stopped

Proxy evidence is mixed: ordered online suffix drafting beats shuffled/static controls, but the absolute effect is small and not a full validation of speculative decoding speedup.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded follow-up on real LLM-token traces with verifier-cost accounting before considering the idea further.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token CPU suffix drafting replay with verifier-cost accounting
- Success threshold: At least two corpora must show >=0.25 accepted draft tokens per target call or >=1.20x modeled/measured end-to-end speedup with CPU overhead included.
- Stop condition: Stop if best real-token result remains below 0.15 accepted draft tokens per target call or modeled speedup is below 1.10x after overhead.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-suffix-draft-for-speculative-decoding-741a12e4ee11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
