# Persistent Suffix-Trie Spec Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `persistent-suffix-trie-spec-decoding-5436ff940e0c`
Run ID: `persistent-suffix-trie-spec-decoding-5436ff940e0c-20260628T044018427218+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e49079f54af2

## What looked useful

The trie did not show a stable advantage over n-gram controls. Five-seed mean trie-minus-best-control was -0.001945 tokens/call on low-noise templates and -0.001718 under shifted noise, while Markov/random controls showed no advantage and the trie used much more persisted state.

## Boundaries and scale limits

No real LLM logits, no GPU decoding runtime, no natural-language benchmark, and no memory-bounded production cache implementation. Main run used 120k train tokens and 40k test tokens; replication used five 60k/20k seeds.

## Claim scope

Bounded synthetic-token proxy for a simple persistent suffix-context-to-continuation trie used as a speculative decoding drafter, compared with unigram, 4-gram, and 8-gram controls.

## Why it stopped

Early proxy falsification: the directly tested suffix-trie drafter was unstable or worse than n-gram controls on synthetic repeated streams and offered no gain on control streams; this is not a full LLM validation.

## Recommended next action

Stop this exact simple suffix-trie variant; only pursue a follow-up if it replaces the unbounded table with a memory-bounded retrieval/cache policy and validates on a real small LLM decoding loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-bounded suffix retrieval for real small-model speculative decoding
- Success threshold: At least 5% wall-clock tokens/sec improvement over the best n-gram/cache baseline on two natural repetitive workloads, no regression greater than 2% on shifted-domain workload, and cache memory bounded by a predeclared limit.
- Stop condition: Stop if the bounded cache fails to beat the best baseline by 2% accepted tokens per target call in a smoke real-model run, or if memory required for parity exceeds the predeclared cache budget.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-suffix-trie-spec-decoding-5436ff940e0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
