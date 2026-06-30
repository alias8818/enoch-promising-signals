# N-gram suffix tree speculative decoding for GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-for-gb10-0201da713d07`
Run ID: `n-gram-suffix-tree-speculative-decoding-for-gb10-0201da713d07-20260605T081114220651+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c8778d209414

## What looked useful

Suffix-copy produced useful exact draft prefixes only on highly repetitive synthetic traces. On tiny Shakespeare, exact future acceptance was very low at 0.1256 accepted tokens/query and 0.0170 accepted/drafted. Against a 70M teacher's greedy continuations, suffix-copy averaged 0.3021 accepted tokens/query with 0.0858 accepted/drafted, which is too weak for a GB10 serving-speedup claim but useful for bounding future tests.

## Boundaries and scale limits

No end-to-end speculative decoder was integrated; no teacher-logit acceptance test, batched tree verification, inference-server latency measurement, large target model, code/assistant serving trace, or long-run robustness study was performed.

## Claim scope

Bounded local evidence for an n-gram/suffix-copy speculative drafter on a synthetic repetitive trace, tiny-Shakespeare trace continuation, and a 96-prompt greedy-continuation probe with cached EleutherAI/pythia-70m-deduped on GB10.

## Why it stopped

Proxy and small-teacher evidence does not support a paper or GB10 speedup claim: natural-language exact acceptance is low, teacher-greedy accepted/drafted is low, and a simple Markov baseline is competitive on the synthetic repetition control.

## Recommended next action

Stop this run as a proxy and small-teacher useful signal; the next bounded test should integrate teacher-logit speculative verification on a realistic repeated assistant/code trace and require measured latency benefit after verifier overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Teacher-verified suffix-copy speculative decoding on repeated assistant/code traces
- Success threshold: At least 1.0 accepted teacher-verified token per query and at least 10% wall-clock latency reduction versus greedy decoding on the same GB10 host after verifier overhead.
- Stop condition: Stop if accepted teacher-verified tokens stay below 0.5 per query or measured latency is not better than greedy decoding after verifier overhead on the repeated trace.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-for-gb10-0201da713d07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
