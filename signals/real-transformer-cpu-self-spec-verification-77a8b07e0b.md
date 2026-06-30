# Real Transformer CPU Self-Spec Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-transformer-cpu-self-spec-verification-77a8b07e0b`
Run ID: `real-transformer-cpu-self-spec-verification-77a8b07e0b-20260531T103004063615+0000`

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

- Parent run decision: Self-Speculative Layer-Skip Decoding on CPU: enoch://control-plane/projects/self-speculative-layer-skip-decoding-on-cpu-fe323590d23c/runs/self-speculative-layer-skip-decoding-on-cpu-fe323590d23c-20260530T053301099076+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c14bdb765dcf

## What looked useful

Self-verification exactness was achieved for all tested depths, and acceptance increased with draft depth, but the best depth reached only 0.684x speed versus uncached greedy and 0.316x versus cached greedy. Naive early-layer CPU self-spec is not practically faster in this setup.

## Boundaries and scale limits

Five short prompts, 32 generated tokens per prompt, distilgpt2 only, greedy decoding only, unbatched CPU execution, block size 4, draft depths 1-5, no cache-aware speculative verifier, no stochastic sampling, no larger model validation.

## Claim scope

In a Tier 1 CPU-only direct test on distilgpt2, a self-speculative greedy decoder using truncated copied early layers preserved exact greedy output but did not accelerate decoding versus uncached or cached greedy baselines.

## Why it stopped

Controlled small direct test falsified the practical acceleration threshold for the tested naive CPU self-spec implementation; this is not a full validation of all self-spec variants.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement cache-aware speculative verification before considering any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware CPU self-spec verification on distilgpt2
- Success threshold: All outputs exactly match cached greedy and at least one draft depth/block-size setting achieves mean speedup > 1.0 versus cached greedy across the five-prompt distilgpt2 test.
- Stop condition: Stop if exactness fails, if all tested settings remain <= 1.0x versus cached greedy, or if the CPU-only run would exceed 15 minutes without checkpointed partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-cpu-self-spec-verification-77a8b07e0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
