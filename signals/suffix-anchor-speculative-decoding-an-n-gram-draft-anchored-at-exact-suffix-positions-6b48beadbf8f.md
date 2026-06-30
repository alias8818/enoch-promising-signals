# Suffix-anchor speculative decoding: an n-gram draft anchored at exact suffix positions

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-anchor-speculative-decoding-an-n-gram-draft-anchored-at-exact-suffix-positions-6b48beadbf8f`
Run ID: `suffix-anchor-speculative-decoding-an-n-gram-draft-anchored-at-exact-suffix-positions-6b48beadbf8f-20260629T035021972181+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a06f4725978c

## What looked useful

Exact suffix-anchor drafting showed 20.7x to 79.5x higher accepted tokens per position on natural streams than shuffled controls across tested corpus/tokenization pairs, with particularly strong code-domain results.

## Boundaries and scale limits

No live neural target model, no production tokenizer, no wall-clock decoding speedup, no KV-cache or batching measurement, and no quality-invariance check. Corpora were Tiny Shakespeare, Alice in Wonderland, and local Python stdlib text capped at 350k tokens and 120k evaluated positions.

## Claim scope

Offline causal exact-suffix lookup on public text/code streams can produce non-trivial accepted draft tokens versus shuffled controls; strongest observed setting was Python stdlib word/punctuation tokens with 1.1626 accepted tokens per position and 2.0080 accepted tokens per covered proposal.

## Why it stopped

Offline oracle acceptance supports the mechanism but is only a proxy; full validation requires live target-model verification and latency/throughput measurements.

## Recommended next action

Stop this run as a no-paper useful signal; next run should implement a bounded live-model speculative decoder using the same suffix-anchor rule and compare wall-clock throughput against greedy decoding and prompt-lookup baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-model suffix-anchor speculative decoding latency test
- Success threshold: At least 10% wall-clock tokens/s improvement over greedy decoding on a bounded prompt set, with exact greedy-output equivalence and acceptance rates materially above prompt-lookup or shuffled-anchor controls.
- Stop condition: Stop if accepted tokens per target call remain below 0.2 or wall-clock throughput is not improved after controlling for lookup/index overhead.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-anchor-speculative-decoding-an-n-gram-draft-anchored-at-exact-suffix-positions-6b48beadbf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
