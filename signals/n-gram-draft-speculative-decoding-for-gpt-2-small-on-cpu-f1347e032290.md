# N-Gram Draft Speculative Decoding for GPT-2-Small on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-draft-speculative-decoding-for-gpt-2-small-on-cpu-f1347e032290`
Run ID: `n-gram-draft-speculative-decoding-for-gpt-2-small-on-cpu-f1347e032290-20260608T112943656416+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c21b4dafbe61

## What looked useful

Corrected exact-match runs show the mechanism works: repetition n3 d8 accepted 172/213 draft tokens, reduced target-advance forwards from 200 to 28 plus 29 verifier forwards, and reached 2.916x median speedup. Mixed prompts also matched exactly and showed 1.575x to 1.772x median speedup, but with one d8 slowdown and outlier-sensitive means.

## Boundaries and scale limits

Only 2 smoke prompts plus two 8-prompt hand-written suites were tested, with 24 generated tokens per confirmation prompt. No real corpus, production workload, batch-serving scenario, p90 latency analysis, or optimized cache-isolation implementation was tested.

## Claim scope

On a small hand-written prompt suite, an exact greedy n-gram draft verifier for GPT-2-small on CPU preserves token outputs and speeds decoding when repeated n-gram continuations are available, with strongest corrected result at 2.916x median speedup on 8 repetition-heavy prompts for n=3, max_draft=8, 24 new tokens.

## Why it stopped

No-paper useful signal: direct GPT-2-small CPU evidence supports the mechanism on small hand-written prompts, but the run is not broad or robust enough for publication-grade claims.

## Recommended next action

Run a corpus-level CPU benchmark on at least 100 real prompts with p50/p90 latency, acceptance-rate stratification, and an optimized cache-isolation strategy before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus benchmark for exact n-gram speculative decoding on GPT-2-small CPU
- Success threshold: Exact token match on all prompts, corpus median speedup >= 1.25x, no p90 latency regression greater than 5%, and a documented positive relationship between acceptance rate and speedup.
- Stop condition: Stop if exactness fails after cache-isolation fixes, or if median speedup is <= 1.0x on the real corpus while p90 latency regresses.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-gpt-2-small-on-cpu-f1347e032290`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
