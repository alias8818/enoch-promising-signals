# N-Gram Draft Speculative Decoding for GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-for-gpt-2-ac9129a4de6c`
Run ID: `n-gram-draft-speculative-decoding-for-gpt-2-ac9129a4de6c-20260604T064804495168+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/368bec57e31c

## What looked useful

Across all runs, speculative n-gram decoding matched baseline greedy outputs exactly. Repetitive prompts showed strong gains with n=3, draft=8: 97.3% mean draft acceptance, 86.3% verifier call reduction, and 2.68x mean wall speedup. Natural prompts were mixed: n=3 reached 1.29x mean wall speedup, n=2 was break-even, and n=4 slowed to 0.94x despite nonzero acceptance.

## Boundaries and scale limits

Small hand-authored prompt sets only; 64 generated tokens per case; no KV-cache-optimized baseline, batching, sampling, long-context serving, larger models, or corpus-scale prompt distribution.

## Claim scope

For GPT-2 small greedy decoding in a simple full-context verifier harness, prefix-derived n-gram drafts preserve exact greedy outputs and can reduce verifier calls and wall-clock latency when generated text has strong local repetition; natural-prompt gains are smaller and configuration-sensitive.

## Why it stopped

Bounded local evidence supports the mechanism under repetition but is not publication-grade because it uses a simple full-context verifier harness and small prompt sets; natural-prompt speedups are mixed rather than robust.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement a KV-cache-aware n-gram speculative decoder and compare against KV-cached greedy GPT-2 on a held-out corpus prompt set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware n-gram speculative decoding for GPT-2 on corpus prompts
- Success threshold: 100% exact greedy-output match and at least 1.15x median wall-clock speedup with p10 speedup above 1.0x versus KV-cached greedy GPT-2 on held-out corpus prompts.
- Stop condition: Stop if exactness fails, median speedup is below 1.05x, or p10 speedup remains below 1.0x after n-gram order and draft-length tuning.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-gpt-2-ac9129a4de6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
