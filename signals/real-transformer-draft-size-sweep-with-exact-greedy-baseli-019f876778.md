# Real Transformer Draft-Size Sweep with Exact Greedy Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-transformer-draft-size-sweep-with-exact-greedy-baseli-019f876778`
Run ID: `real-transformer-draft-size-sweep-with-exact-greedy-baseli-019f876778-20260628T133915103124+0000`

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

- Parent run decision: Draft-Size Sweep for Speculative Decoding with Exact No-Spec Baseline: enoch://control-plane/projects/draft-size-sweep-for-speculative-decoding-with-exact-no-spec-baseline-92c671203a75/runs/draft-size-sweep-for-speculative-decoding-with-exact-no-spec-baseline-92c671203a75-20260628T130233354164+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3761ac6f7de5

## What looked useful

Target forwards per output token fell from 1.000 at draft size 1 to 0.136 at draft size 16, but throughput peaked at draft size 4 with only 0.965x the greedy baseline. A float16 run also exposed an exactness pitfall: batched verifier logits can flip a close argmax relative to sequential greedy logits.

## Boundaries and scale limits

Small GPT-2-class models, 8 hand-written prompts, 1024 generated tokens per mode, straightforward Python/Transformers implementation with full-sequence target verification and sequential drafter calls. Not a KV-cache-optimized serving runtime and not a 7B+/datacenter-scale benchmark.

## Claim scope

On GB10 with GPT-2 as target and DistilGPT-2 as drafter, an exact float32 speculative greedy decoder over 8 prompts and 128 generated tokens per prompt reproduced the greedy baseline for draft sizes 1, 2, 4, 8, and 16. Larger draft sizes reduced target forward calls but did not improve wall-clock throughput over the exact greedy baseline in the bounded implementation.

## Why it stopped

Bounded direct evidence did not show a speedup over exact greedy decoding, and the implementation limits prevent a publication-grade positive claim.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a KV-cache-aware exact speculative decoder on the same model pair with the same equality assertions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware exact speculative draft-size sweep
- Success threshold: At least 1.15x greedy-baseline throughput at one draft size with exact token equality across at least 32 prompts and 128 generated tokens per prompt.
- Stop condition: Stop if exactness fails under the chosen precision policy or if no draft size reaches at least 1.05x baseline after KV-cache optimization.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-draft-size-sweep-with-exact-greedy-baseli-019f876778`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
