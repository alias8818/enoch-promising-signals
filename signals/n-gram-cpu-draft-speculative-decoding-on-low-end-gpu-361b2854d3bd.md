# N-gram CPU Draft Speculative Decoding on Low-End GPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `n-gram-cpu-draft-speculative-decoding-on-low-end-gpu-361b2854d3bd`
Run ID: `n-gram-cpu-draft-speculative-decoding-on-low-end-gpu-361b2854d3bd-20260529T000231118646+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e74519f2f76a

## What looked useful

The CPU n-gram drafter was cheap, but acceptance was too low to amortize GPU target verification. The speculative path used roughly 1.74x-1.79x as many target calls as cached greedy baseline and roughly doubled per-prompt latency.

## Boundaries and scale limits

Small model, Wikitext prompt distribution, fp32 target execution, single-process benchmark, no batched serving, no instruction-tuned target, no fp16/bf16 final metrics, and no learned/retrieval-assisted drafter.

## Claim scope

On GB10 with cached distilgpt2 in CUDA fp32, Wikitext-trained CPU n-gram drafting did not speed exact greedy speculative decoding for 16 Wikitext validation prompts of 48 generated tokens; all final outputs matched baseline exactly, but acceptance stayed below 7.4% and latency was about 0.49x-0.51x of baseline throughput.

## Why it stopped

Bounded direct evidence falsified the practical speedup hypothesis for simple CPU n-gram drafting in the tested local setting: exact speculative decoding remained correct but low acceptance increased target calls and roughly doubled latency.

## Recommended next action

Stop this simple CPU n-gram drafting line unless the drafter is replaced with a materially stronger CPU-cheap mechanism; this result is a bounded negative, not full production-scale validation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-draft-speculative-decoding-on-low-end-gpu-361b2854d3bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
