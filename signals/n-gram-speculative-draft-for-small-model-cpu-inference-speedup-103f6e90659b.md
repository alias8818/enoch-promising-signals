# N-gram speculative draft for small-model CPU inference speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-small-model-cpu-inference-speedup-103f6e90659b`
Run ID: `n-gram-speculative-draft-for-small-model-cpu-inference-speedup-103f6e90659b-20260604T034813889721+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/91e01e9fca96

## What looked useful

Prompt n-gram drafting reduced target calls and improved mean CPU throughput for distilgpt2: draft length 8 mean speedup 2.029x, median 2.061x, range 0.943x-3.583x, with exact token equality. Repetitive/code/list prompts sped up 2.061x-3.583x, while natural prose with 0.282 acceptance slowed slightly to 0.943x.

## Boundaries and scale limits

Single small unquantized model, five hand-written prompts, greedy decoding only, no production runtime, no quantized kernels, no batching, no long-context serving distribution, and no larger modern small-LM family coverage.

## Claim scope

On one CPU worker using Hugging Face eager cached greedy decoding with distilgpt2, prompt n-gram speculative drafting preserved exact greedy outputs and improved mean throughput on five fixed 48-token prompts, mainly when the target continuation copied repeated prompt structure.

## Why it stopped

Bounded local evidence supports the mechanism but also shows prompt-dependent downside; this is useful no-paper evidence rather than broad validation.

## Recommended next action

Do not write a paper from this run; run a bounded follow-up in a production CPU runtime with quantized 0.5B-3B models and an adaptive acceptance gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive prompt n-gram drafting in a production CPU runtime
- Success threshold: At least 1.25x median throughput or latency improvement on high-repetition strata with no more than 2% p90 latency regression on low-repetition strata, all with exact greedy-output equivalence.
- Stop condition: Stop if the adaptive gate cannot prevent more than 2% p90 regression on low-repetition prompts or if high-repetition speedup is below 1.15x across both tested model sizes.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-small-model-cpu-inference-speedup-103f6e90659b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
