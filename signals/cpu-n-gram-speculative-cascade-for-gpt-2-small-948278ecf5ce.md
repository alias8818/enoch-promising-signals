# CPU n-gram speculative cascade for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-cascade-for-gpt-2-small-948278ecf5ce`
Run ID: `cpu-n-gram-speculative-cascade-for-gpt-2-small-948278ecf5ce-20260604T171331087063+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7e3d08743ebf

## What looked useful

The cascade achieved 1.59x mean speedup over an unoptimized full-prefix greedy baseline across 20 prompts with exact token matches, but averaged only 0.67x versus cached greedy across 10 prompts and won on 1/10 prompts. Acceptance rate gated usefulness; repetitive prompts helped, low-acceptance prompts regressed.

## Boundaries and scale limits

Tested only 20 prompts for full-prefix comparison and 10 prompts for cached-baseline comparison, 32 generated tokens per prompt, greedy decoding only, one CPU host, no batching, no production cache-aware speculative verifier.

## Claim scope

On cached local GPT-2-small CPU greedy decoding, a prompt-local n-gram speculative cascade with max_n=4 and gamma=4 preserves exact greedy output and can reduce full-prefix target calls, but in this implementation it does not beat a standard KV-cache greedy baseline on a small hand-written prompt sweep.

## Why it stopped

Bounded local evidence shows the mechanism is exact and sometimes useful, but the current implementation loses to the relevant cached GPT-2-small CPU baseline on average, so it is not a paper-positive result.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test is a cache-aware verifier plus adaptive draft gate against cached greedy on a fixed small corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware adaptive n-gram speculative decoding for GPT-2-small CPU
- Success threshold: Exact greedy match on 100% of prompts, mean throughput at least 1.1x cached greedy, p50 at least 1.0x, and fewer than 10% of prompts slower than cached greedy by more than 10%.
- Stop condition: Stop if cache-aware verification cannot preserve exact greedy output, or if after adaptive gating the mean throughput remains below 1.0x cached greedy on the fixed prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-cascade-for-gpt-2-small-948278ecf5ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
