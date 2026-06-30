# Live latency microbenchmark for prompt-local n-gram speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-latency-microbenchmark-for-prompt-local-n-gram-specul-19e439abd1`
Run ID: `live-latency-microbenchmark-for-prompt-local-n-gram-specul-19e439abd1-20260605T070844176000+0000`

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

- Parent run decision: N-gram Draft Speculative Decode: enoch://control-plane/projects/n-gram-draft-speculative-decode-0ce27366b8bf/runs/n-gram-draft-speculative-decode-0ce27366b8bf-20260604T222103992367+0000
- Parent run decision: Optimized n-gram speculative decoding on real prompt corpora: enoch://control-plane/projects/optimized-n-gram-speculative-decoding-on-real-prompt-corpo-f350e211a7/runs/optimized-n-gram-speculative-decoding-on-real-prompt-corpo-f350e211a7-20260605T031814020971+0000

## What looked useful

Mechanism support is positive but fragile: tuned draft length reduced model forwards/token from 1.008 to 0.872 and gave median 1.100x speedup, while shuffled drafts were about 0.516x and no-draft overhead was neutral. Overlong drafts and bf16 exactness issues prevent a paper-ready claim.

## Boundaries and scale limits

Evidence is limited to one 410M causal LM, fp32 precision, batch size 1, 128-token continuations, synthetic prompt-local prompts, and a conservative Python cache-clone/replay implementation. Qwen/Qwen3-0.6B bf16 and Pythia bf16 runs exposed exact-output mismatches for accepted drafts, and max_draft=8 was slower despite real acceptance.

## Claim scope

On EleutherAI/pythia-410m fp32 inference on one GB10, prompt-local n-gram speculative decoding with n=3 and max_draft=4 emitted tokens identical to greedy decoding and improved median live tokens/s by 1.100x across three synthetic prompt-local continuation variants, beating no-draft and shuffled controls.

## Why it stopped

Medium local validation found a scoped positive mechanism signal but also prompt/model/precision fragility and insufficient robustness for publication.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should implement optimized exact cache snapshot/rollback and validate fp16/bf16 exactness on 0.5B-1B models before any paper-scale latency claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact mixed-precision cache rollback for prompt-local n-gram speculation
- Success threshold: Across at least two models and two prompt suites, exact-output intact n-gram decoding achieves >=1.10x median tokens/s versus greedy and beats shuffled/no-draft controls, with zero accepted-draft output mismatches.
- Stop condition: Stop if exact bf16/fp16 output mismatches persist after cache rollback fixes, or if tuned exact implementation fails to exceed 1.05x median speedup on both models.

## Evidence references

- Artifact root: `<local-path>/projects/live-latency-microbenchmark-for-prompt-local-n-gram-specul-19e439abd1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
