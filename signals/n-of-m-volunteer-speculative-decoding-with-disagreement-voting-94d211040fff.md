# N-of-M Volunteer Speculative Decoding with Disagreement Voting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-of-m-volunteer-speculative-decoding-with-disagreement-voting-94d211040fff`
Run ID: `n-of-m-volunteer-speculative-decoding-with-disagreement-voting-94d211040fff-20260621T211622049090+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f18329caecc8

## What looked useful

Across all bounded tests, disagreement voting did not beat the single-draft baseline on target-call efficiency. The stronger GPT-2/distilgpt2 baseline achieved 2.553 output tokens per target call; 5-volunteer voting ranged from 1.277 to 2.553, with the best settings only tying while adding about 3.2x local wall-clock and 5x draft-call overhead. Higher-temperature voting degraded target-call efficiency to 0.50-0.64x of baseline. Exact greedy-target output was preserved in all runs.

## Boundaries and scale limits

This was not a datacenter-scale serving benchmark and did not test independently hosted human/volunteer machines, 7B+ targets, network latency, learned routing, or truly heterogeneous fine-tuned volunteer drafts. The N-of-M volunteers in the model-backed sweep were independent samples from one draft model rather than separately trained models.

## Claim scope

Bounded local probe of N-of-M disagreement-voted speculative decoding using a synthetic Markov target/draft and small GPT-2-family target/draft pairs. The tested implementation requires exact greedy-target output and compares output tokens per target verification call against a single-draft baseline.

## Why it stopped

Proxy plus small-model direct evidence early-falsified the operational hypothesis that naive N-of-M disagreement voting improves speculative decoding efficiency; this is not full-scale validation, but it is enough to reject the tested mechanism as paper-positive.

## Recommended next action

Stop this run as a bounded negative/useful-signal result; only revisit with a heterogeneous-volunteer selector test that must show more than 10% target-call efficiency gain over single-draft speculation before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous volunteer selector for speculative decoding
- Success threshold: A selector must preserve exact greedy-target output and exceed the single-best-draft baseline by at least 10% output tokens per target verification call on held-out prompts without more than 2x local end-to-end slowdown when drafts are run locally.
- Stop condition: Stop if heterogeneous volunteers have correlated errors or no selector exceeds the single-best-draft target-call efficiency by 10% in a <= 12 prompt, <= 64 token bounded probe.

## Evidence references

- Artifact root: `<local-path>/projects/n-of-m-volunteer-speculative-decoding-with-disagreement-voting-94d211040fff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
