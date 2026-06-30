# N-Gram Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-on-cpu-f360008a74cc`
Run ID: `n-gram-draft-speculative-decoding-on-cpu-f360008a74cc-20260602T183710774052+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b67010670af1

## What looked useful

Indexed n-gram drafting reduced target calls by 81.05% and improved repeated-span proxy decoding by 1.36x mean speedup, but mixed data was roughly break-even at 0.98x and random data was strongly negative at 0.27x. Naive n-gram lookup was slower even when target-call reduction was high.

## Boundaries and scale limits

This was not a real transformer LM or production serving runtime. Target verification was proxied by NumPy matrix work, with 512 generated tokens per scenario repetition and 5 repetitions per scenario.

## Claim scope

In a bounded CPU NumPy deterministic-continuation proxy, indexed prompt/history n-gram drafting produced a wall-clock win on repeated-span continuations but not on mixed or random continuations.

## Why it stopped

Proxy evidence supports only a conditional mechanism, not a publication-grade or broad CPU speculative decoding claim.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is a real small-CPU-LM validation with the indexed drafter and prompt-regime gating.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate indexed n-gram drafting on a real small CPU language model
- Success threshold: At least 1.15x end-to-end tokens/s on repeated-span/code-log prompts with no more than 5% slowdown on prose after gating, over at least 20 prompts.
- Stop condition: Stop if repeated-span/code-log prompts fail to exceed 1.05x end-to-end speedup or if prose/high-entropy prompts cannot be gated to within 5% of baseline.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-cpu-f360008a74cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
