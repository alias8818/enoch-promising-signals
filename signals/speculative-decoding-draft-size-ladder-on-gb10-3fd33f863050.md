# Speculative Decoding Draft-Size Ladder on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-draft-size-ladder-on-gb10-3fd33f863050`
Run ID: `speculative-decoding-draft-size-ladder-on-gb10-3fd33f863050-20260612T004214743745+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f44ce5341be3

## What looked useful

Target verification calls fell from 2048 greedy calls to 858 for static K2 and 658 for confidence-gated max16, but aggregate speedup was only 1.135x for static K2 and 1.184x for confidence-gated max16. Static K8/K16 were slower than greedy at 0.843x/0.607x, and heuristic_ladder_start4 reached only 1.051x. Assisted configs repeatedly failed exact greedy token equality, so correctness needs diagnosis before scaling.

## Boundaries and scale limits

Single GB10 host, one target/draft pair, 64-token generations, 32 prompt-repeat cases per config, unbatched Transformers generate path, no production serving trace, no custom verifier with explicit accepted-token counters.

## Claim scope

On GB10 with cached Qwen/Qwen2.5-1.5B as target and Qwen/Qwen2.5-0.5B as draft, short greedy assisted decoding over 16 prompts x 2 repeats showed target-call reduction but only modest throughput gains for small/static or confidence-gated draft lookahead; large fixed draft sizes and the heuristic ladder were not beneficial.

## Why it stopped

Bounded local evidence is mixed and not paper-positive: the ladder proxy did not beat the best fixed small K, large draft sizes were negative, and recurring greedy-output divergence prevents a clean speed/correctness claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should diagnose assisted-decoding exactness and add explicit accepted/rejected token counters before testing a custom ladder policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exactness and acceptance-counter diagnosis for GB10 speculative decoding ladders
- Success threshold: A custom ladder achieves at least 1.19x greedy throughput and at least 5% higher aggregate throughput than static K2 with 100% greedy-token equality on the bounded benchmark.
- Stop condition: Stop if exactness cannot be achieved or explained within the bounded benchmark, or if acceptance-counter results show the custom ladder does not beat static K2 by 5%.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-draft-size-ladder-on-gb10-3fd33f863050`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
