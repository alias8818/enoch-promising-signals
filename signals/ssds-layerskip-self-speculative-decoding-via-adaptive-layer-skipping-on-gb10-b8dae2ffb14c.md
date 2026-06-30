# SSDS-LayerSkip: Self-Speculative Decoding via Adaptive Layer Skipping on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `ssds-layerskip-self-speculative-decoding-via-adaptive-layer-skipping-on-gb10-b8dae2ffb14c`
Run ID: `ssds-layerskip-self-speculative-decoding-via-adaptive-layer-skipping-on-gb10-b8dae2ffb14c-20260621T205607905551+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c880ed71591

## What looked useful

Dense decoding beat every fixed and adaptive early-exit mode on both accessible model scales. Qwen2.5-0.5B adaptive throughput was 50.59 tok/s versus 112.15 tok/s dense (0.451x) with 0.625 exact match; Qwen2.5-1.5B adaptive throughput was 27.84 tok/s versus 49.08 tok/s dense (0.567x) with 0.75 exact match.

## Boundaries and scale limits

The official documented LayerSkip checkpoint facebook/layerskip-llama3.2-1B was gated and inaccessible, so this is a plug-in/proxy negative rather than a full falsification of trained LayerSkip self-speculative decoding. The largest direct run was Qwen2.5-1.5B-Instruct on 4 prompts with 24 generated tokens.

## Claim scope

On GB10, using accessible unmodified Qwen2.5 0.5B and 1.5B checkpoints with Hugging Face Transformers assistant_early_exit, prompt-level adaptive layer skipping did not improve decoding speed over dense greedy generation and sometimes changed generated tokens.

## Why it stopped

The direct trained LayerSkip checkpoint was gated, and the accessible GB10 proxy tests showed slower-than-dense throughput plus occasional greedy-output changes rather than a speed/correctness win.

## Recommended next action

Stop this run as an early proxy falsification of plug-in adaptive layer skipping; the next bounded evidence step is to train or obtain an ungated early-exit-trained small model and compare adaptive versus fixed exits under the same GB10 harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a small ungated early-exit model for adaptive LayerSkip on GB10
- Success threshold: Adaptive early-exit decoding reaches at least 1.15x dense tokens/s and at least 1.05x the best fixed exit with at least 0.99 exact greedy-token match on a 100-prompt bounded benchmark.
- Stop condition: Stop if trained early-exit checkpoints still fail to exceed dense throughput, if exact match/acceptance falls below 0.99, or if training cost exceeds a bounded single-worker budget without producing a usable checkpoint.

## Evidence references

- Artifact root: `<local-path>/projects/ssds-layerskip-self-speculative-decoding-via-adaptive-layer-skipping-on-gb10-b8dae2ffb14c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
