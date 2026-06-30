# Self-speculative decoding with early exit draft heads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-with-early-exit-draft-heads-bdfd0dc921f5`
Run ID: `self-speculative-decoding-with-early-exit-draft-heads-bdfd0dc921f5-20260611T180730572189+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ecacc591180f

## What looked useful

Layer-2 and layer-4 trained draft heads improved verifier agreement over untrained tied projections, showing intermediate states contain trainable draft signal. However, observed greedy accept rates were 0.323, 0.364, and 0.400 for layers 2, 4, and 5, while break-even accept rates under measured prefix costs were 0.837, 0.913, and 0.936. Estimated gamma=4 speedups were only 0.407x, 0.371x, and 0.375x.

## Boundaries and scale limits

Small-model/small-corpus probe only; speedup is analytically estimated for greedy gamma=4 rather than measured in a full autoregressive speculative serving loop with KV-cache reuse. No larger-model, larger-corpus, stochastic decoding, or production kernel validation was run.

## Claim scope

On a frozen DistilGPT-2 verifier with Tiny Shakespeare windows, trainable LayerNorm-plus-linear early-exit draft heads at layers 2, 4, and 5 learn measurable top-1 agreement with the final verifier, but their greedy self-speculative acceptance and measured early-prefix cost do not support speedup.

## Why it stopped

Proxy/early falsification for the straightforward linear early-exit draft-head design: the heads learn, but acceptance is far below the break-even threshold implied by measured early-prefix cost, so this scoped implementation is not speedup-viable.

## Recommended next action

Stop this run as a no-paper useful signal; a follow-up should test a cheaper shared-unembedding or adapter-style draft head in a real KV-cache speculative decoding loop and require measured throughput above baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware cheap early-exit adapter heads for self-speculative decoding
- Success threshold: At least 1.15x measured wall-clock tokens/second over baseline greedy decoding with identical outputs on the prompt suite and no more than 5% extra peak memory.
- Stop condition: Stop if measured speedup remains below 1.0x after testing a cache-aware loop and at least one cheaper draft-head design, or if acceptance remains below the measured break-even threshold by more than 20 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-with-early-exit-draft-heads-bdfd0dc921f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
