# CPU-Only N-Gram Suffix Tree Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-only-n-gram-suffix-tree-speculative-decoding-a45c9699f4b7`
Run ID: `cpu-only-n-gram-suffix-tree-speculative-decoding-a45c9699f4b7-20260621T000937871806+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/27c1aaf47045

## What looked useful

Mechanism is promising only for repeated/code-like contexts: best code-boilerplate proxy reached 4.740x idealized target-call speedup and 0.789 target-call reduction, while random tokens stayed at 1.000x and project scaffold text reached only 1.076x.

## Boundaries and scale limits

No real LLM target model, no tokenizer-ID integration, no KV-cache or batched verification timing, no external corpus, and no end-to-end tokens-per-second serving benchmark. The largest local grid was 160 synthetic/project-text proxy rows in 157.355 seconds.

## Claim scope

Bounded CPU-only proxy: an exact-match n-gram/suffix-style draft index can reduce idealized verifier call counts on deterministic repetitive and code-boilerplate token streams, but shows weak gain on the real scaffold text and no gain on random tokens.

## Why it stopped

Proxy evidence supports the mechanism in repetitive/code-like streams but does not directly validate real LLM speculative decoding throughput.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded direct GPT-2-small-class CPU serving test with tokenizer-level n-gram drafting and measured tokens/second versus greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-level CPU n-gram drafting with a small real target model
- Success threshold: At least 10% end-to-end tokens/second improvement over greedy decoding on code-like/repetitive prompts without more than 5% slowdown on the negative control.
- Stop condition: Stop if tokenizer-level acceptance is below 0.15 or measured speculative decoding is slower than greedy after overhead on both code-like and natural-language prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-only-n-gram-suffix-tree-speculative-decoding-a45c9699f4b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
