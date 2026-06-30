# CPU-draft speculative decoding for home llama.cpp

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-draft-speculative-decoding-for-home-llama-cpp-bafcc3c87130`
Run ID: `cpu-draft-speculative-decoding-for-home-llama-cpp-bafcc3c87130-20260629T073011802209+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9aa549c948d0

## What looked useful

Target-only 8-thread decoding averaged 10.53 tok/s. Speculative target6+draft2 averaged 3.38 tok/s (0.32x baseline), and target4+draft4 averaged 4.57 tok/s (0.43x baseline). A target-only 4-thread control averaged 9.13 tok/s, so the slowdown was not just from giving the target fewer threads.

## Boundaries and scale limits

Bounded to one CPU host, one target/draft model pair, llama.cpp build b1-ac4cdde, short 48-token generations, and llama-cli throughput output without draft acceptance counters.

## Claim scope

On an 8-logical-CPU Xeon Silver 4114 worker, llama.cpp draft-model speculative decoding with Qwen2.5-1.5B-Instruct-Q4_K_M as target and Qwen2.5-0.5B-Instruct-Q8_0 as CPU draft was slower than target-only decoding for short fixed prompts.

## Why it stopped

Direct bounded local benchmark falsified the practical speedup hypothesis for the tested home-CPU configuration; this is not a full universal validation.

## Recommended next action

Stop this run as a bounded negative result; only run a follow-up if using llama-server acceptance counters to diagnose why the CPU draft path lost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: llama.cpp CPU speculative acceptance-rate diagnostics
- Success threshold: Show a speculative configuration with at least 1.10x target-only 8-thread throughput and draft acceptance high enough to explain the gain, or produce acceptance-counter evidence explaining the slowdown.
- Stop condition: Stop after three prompts x two repeats for baseline/spec/control if speculative throughput remains below 0.9x target-only or draft acceptance is below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-draft-speculative-decoding-for-home-llama-cpp-bafcc3c87130`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
