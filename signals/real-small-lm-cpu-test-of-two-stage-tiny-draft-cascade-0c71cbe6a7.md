# Real Small-LM CPU Test of Two-Stage Tiny Draft Cascade

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-small-lm-cpu-test-of-two-stage-tiny-draft-cascade-0c71cbe6a7`
Run ID: `real-small-lm-cpu-test-of-two-stage-tiny-draft-cascade-0c71cbe6a7-20260527T093043283696+0000`

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

- Parent run decision: CPU-bounded Speculative Decoding with Tiny Draft Model Cascade: enoch://control-plane/projects/cpu-bounded-speculative-decoding-with-tiny-draft-model-cascade-de104d674078/runs/cpu-bounded-speculative-decoding-with-tiny-draft-model-cascade-de104d674078-20260526T014830968302+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/09eea6a20198

## What looked useful

Two-stage decoding was exact but slower than direct decoding in every gamma sweep point; best two-stage speedup was 0.958x direct at gamma_mid=2, gamma_tiny=8. The one-stage 31m -> 70m control sometimes exceeded direct speed, reaching 1.205x at gamma_mid=2, indicating the extra tiny->mid stage was the likely overhead source.

## Boundaries and scale limits

Small controlled CPU test only: 4 PyTorch CPU threads, naive PyTorch implementation, no KV-cache optimization, no quantization, 6 fixed prompts, 144 generated tokens per mode per run, gamma sweep over 2/4/8. Does not rule out optimized runtimes, different model ladders, larger models, sampling, or broader corpora.

## Claim scope

On this CPU worker, exact greedy two-stage speculative decoding with EleutherAI/pythia-14m -> EleutherAI/pythia-31m-deduped -> EleutherAI/pythia-70m-deduped did not exceed direct pythia-70m-deduped greedy throughput over 6 prompts and 24 generated tokens per prompt.

## Why it stopped

Direct Tier-1 small-LM CPU validation falsified the operational threshold: exact two-stage cascade never beat direct target greedy throughput in the gamma sweep, so this is an early bounded negative rather than full-scale validation.

## Recommended next action

Stop the two-stage cascade claim for this ladder; if continuing, run a bounded robustness test of the one-stage 31m -> 70m CPU speculative path with KV-cache support and a broader prompt set.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: KV-cache CPU robustness test for one-stage 31M-to-70M speculative decoding
- Success threshold: One-stage speculative decoding must preserve exact target greedy outputs and achieve at least 1.15x direct target tokens/sec with the lower bound of a simple bootstrap confidence interval above 1.0x.
- Stop condition: Stop if exactness fails, if best tuned one-stage speedup is below 1.05x, or if KV-cache overhead makes the run exceed the 15-minute CPU-only budget without partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-lm-cpu-test-of-two-stage-tiny-draft-cascade-0c71cbe6a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
