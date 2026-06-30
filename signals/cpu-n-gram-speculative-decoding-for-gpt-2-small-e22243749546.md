# CPU N-gram Speculative Decoding for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-gpt-2-small-e22243749546`
Run ID: `cpu-n-gram-speculative-decoding-for-gpt-2-small-e22243749546-20260604T050953827921+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d98aa62de3c8

## What looked useful

Exact-match CPU n-gram speculation is feasible for GPT-2-small and can reduce forward calls and improve median throughput on repeated contexts; always-on speculation is not robust because low-acceptance prompts and overhead can erase or reverse gains.

## Boundaries and scale limits

Six hand-written prompts, 16/32/64-token generations, CPU-only PyTorch implementation, greedy decoding only, no corpus-level serving benchmark, no sampling, no optimized inference runtime, and no larger-model validation.

## Claim scope

On a CPU worker using real GPT-2-small greedy decoding, prompt n-gram speculative decoding with n=3 and max draft length 4 reproduced greedy outputs exactly and improved throughput on repeated/templated prompts, but regressed on some prompt families.

## Why it stopped

Bounded local benchmark produced mixed evidence: mechanism supported, general always-on speedup not robust enough for a paper.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test adaptive speculation gating on a small natural repeated-context corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive CPU n-gram speculation gate for GPT-2-small
- Success threshold: Adaptive gating beats greedy baseline by at least 15% median tokens/s across the corpus and has no prompt-family median slowdown below 0.95x, while preserving exact greedy outputs.
- Stop condition: Stop if adaptive gating cannot eliminate the observed slowdown prompts or if confidence intervals overlap baseline by less than 5% median improvement.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-gpt-2-small-e22243749546`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
