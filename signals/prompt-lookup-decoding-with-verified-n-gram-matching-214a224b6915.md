# Prompt Lookup Decoding with Verified N-gram Matching

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-decoding-with-verified-n-gram-matching-214a224b6915`
Run ID: `prompt-lookup-decoding-with-verified-n-gram-matching-214a224b6915-20260603T233143747911+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9b0f2019f36a

## What looked useful

Verified n-gram matching is a correct way to exploit prompt-local repetition when the generated continuation re-enters prompt substrings; the verifier rejected mismatched drafts and maintained greedy equivalence. The useful practical boundary is also clear: low-repeat prompts and degenerate models yield no accepted drafts, so this should be treated as an opportunistic decoding acceleration rather than a universal speedup.

## Boundaries and scale limits

Evidence is limited to tiny-gpt2 and distilgpt2, synthetic repeated prompts, greedy decoding, batch size 1, short 64-token generations, and a non-optimized verification implementation. It does not establish production latency, long-context robustness, sampling behavior, or performance on 7B+ models and real serving traces.

## Claim scope

On three bounded 64-token decoding cases with distilgpt2 and a direct verified prompt n-gram draft implementation, verified prompt lookup preserved exact greedy output. It reduced model forward calls by 78.1% on a repeated checklist prompt and 90.6% on a repeated code prompt, and produced 0% reduction on a low-repeat control.

## Why it stopped

Bounded local evidence supports the mechanism but is proxy-scale and synthetic; it is not direct publication-grade validation of broad prompt lookup decoding speedups.

## Recommended next action

Stop this worker run as no-paper useful evidence; next run should evaluate the same verifier on realistic long-context prompt traces with an optimized KV-cache implementation and a GPT-2-small-class or larger baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Trace Evaluation for Verified Prompt Lookup Decoding
- Success threshold: All outputs must match greedy exactly; repeated-prompt subset must show at least 25% median latency or forward-call reduction, and low-repeat controls must show less than 5% overhead.
- Stop condition: Stop as negative if exact greedy equivalence fails, if repeated realistic prompts accept drafts in fewer than 10% of cases, or if optimized verification overhead removes the call-count advantage.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-decoding-with-verified-n-gram-matching-214a224b6915`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
