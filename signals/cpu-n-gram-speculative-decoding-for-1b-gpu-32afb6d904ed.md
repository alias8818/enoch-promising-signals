# CPU n-gram speculative decoding for 1B GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-1b-gpu-32afb6d904ed`
Run ID: `cpu-n-gram-speculative-decoding-for-1b-gpu-32afb6d904ed-20260602T212513438044+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4174e93ed6b9

## What looked useful

Corrected exact-match runs show general prompts at 0.80-0.82x greedy baseline with 0.04-0.11 draft acceptance, while repetition-heavy prompts improve from 1.44x at max_draft=2 to 4.11x at max_draft=8 with 0.60-0.70 draft acceptance. The mechanism is useful only for repeated-span workloads in this bounded test.

## Boundaries and scale limits

One 1.5B model, greedy decoding only, 4 general and 4 synthetic repetition-heavy prompts, 64 generated tokens per prompt, Python/Transformers prototype with conservative cache copying on rejected drafts. No production batching, sampling, optimized KV branching, long-context traffic, or multi-model validation.

## Claim scope

On a GB10 GPU with Qwen/Qwen2.5-Coder-1.5B-Instruct under exact greedy decoding, a CPU longest-suffix n-gram drafter is slower than baseline on ordinary instruction prompts but can accelerate short repetition-heavy prompts when draft acceptance is high.

## Why it stopped

Bounded local evidence is mixed: the mechanism works on synthetic repetition-heavy prompts but is slower than greedy baseline on ordinary prompts, so it does not support a broad paper claim.

## Recommended next action

Stop this run as no-paper useful signal; next, implement optimized KV-cache branching and evaluate on a bounded retrieval/repetition-heavy prompt suite rather than broad ordinary prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized cache-branching CPU n-gram drafting for repeated-span workloads
- Success threshold: At least 1.5x mean throughput over greedy baseline on repeated-span prompts with exact token match and no more than 5% slowdown on ordinary control prompts.
- Stop condition: Stop if optimized cache handling still gives less than 1.2x speedup on repeated-span prompts or more than 10% slowdown on ordinary controls.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-1b-gpu-32afb6d904ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
