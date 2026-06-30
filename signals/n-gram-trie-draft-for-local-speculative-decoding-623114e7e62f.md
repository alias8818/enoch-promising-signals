# N-gram Trie Draft for Local Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-trie-draft-for-local-speculative-decoding-623114e7e62f`
Run ID: `n-gram-trie-draft-for-local-speculative-decoding-623114e7e62f-20260607T211010775289+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b929845421d7

## What looked useful

The n-gram trie accepted 65.7% of proposed tokens on natural prose and 73.0% on repetition-heavy prompts, yielding idealized 3.43x and 4.36x verification-pass reductions versus 1.50x-2.26x for trivial baselines. CPU trie overhead was tens of milliseconds versus roughly two seconds of target inference across the run.

## Boundaries and scale limits

Six hand-written prompts, distilgpt2 only, greedy decoding only, no production speculative decoder, no batched verifier timing, no broad corpus, and no larger-model validation.

## Claim scope

In a bounded local proxy using distilgpt2 greedy continuations over six fixed prompts, a prompt-local n-gram trie drafter produced higher accepted-token rates and larger idealized target verification-pass reductions than unigram and last-token baselines.

## Why it stopped

This run is a useful proxy/mechanism test, not full validation of local speculative decoding speed or robustness.

## Recommended next action

Run a bounded deepen experiment that plugs the trie drafter into a real speculative decoder and measures wall-clock tokens/sec against greedy decoding and simple drafter baselines on small code, log, and prose corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end local n-gram trie speculative decoding benchmark
- Success threshold: At least 1.3x end-to-end tokens/sec improvement over greedy decoding on repetition-rich code/log workloads and at least parity on prose, with no quality regression under the chosen decoding policy.
- Stop condition: Stop if batched verification overhead removes the idealized pass-reduction gain or if acceptance drops below trivial baselines on two workload classes.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-trie-draft-for-local-speculative-decoding-623114e7e62f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
