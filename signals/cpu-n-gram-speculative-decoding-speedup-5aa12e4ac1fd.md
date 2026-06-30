# CPU N-Gram Speculative Decoding Speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-speedup-5aa12e4ac1fd`
Run ID: `cpu-n-gram-speculative-decoding-speedup-5aa12e4ac1fd-20260526T005751120550+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2b2b33e5d6e9

## What looked useful

Cache-sliced rejection handling fixed the main conservative overhead and improved over full KV rebuild, but acceptance was too sparse and rejection/proposal overhead remained high. Draft-4 sliced mode slowed to 0.761x total speed; draft-2 sliced mode was 1.002x total but 0.922x median; min_count gating slowed to 0.888x.

## Boundaries and scale limits

The benchmark is small and CPU/Python/HF-specific. It does not cover sampling, batch serving, long repeated contexts, optimized C++ lookup, cache-native non-mutating DynamicCache handling, or larger prompt suites.

## Claim scope

On a CPU worker using Hugging Face GPT-2-small greedy decoding for 6 natural-language prompts x 64 new tokens, exact n-gram speculative decoding accepted some repeated-history drafts but did not deliver a robust wall-clock speedup. The best tested fixed setting was effectively neutral in total time and below baseline by median prompt.

## Why it stopped

Bounded direct GPT-2-small CPU evidence did not support a robust speedup: one variant was neutral in total time but worse by median prompt, while other exact variants slowed decoding.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test would need a cache-native adaptive-gated implementation and a 50 prompt x 128 token exact GPT-2-small benchmark before any speedup claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive cache-native n-gram speculative decoding on GPT-2-small CPU
- Success threshold: Exact output equality with total speedup >1.10x and median prompt speedup >1.05x on 50 prompts x 128 new tokens.
- Stop condition: Stop if the adaptive cache-native implementation is below 1.05x total speedup or has median prompt speedup below 1.0x after the 50 prompt benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-speedup-5aa12e4ac1fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
