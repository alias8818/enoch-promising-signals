# N-gram draft speculative decoding on hybrid CPU-GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-on-hybrid-cpu-gpu-677de2e94d80`
Run ID: `n-gram-draft-speculative-decoding-on-hybrid-cpu-gpu-677de2e94d80-20260525T115551415739+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/625d0a40f048

## What looked useful

Static corpus n-grams accepted only 3.0% of proposed tokens on distilgpt2 and estimated 1.004x speedup, effectively flat. Prompt lookup accepted 81.1% on distilgpt2 and 61.1% on gpt2, with estimated speedups of 1.90x and 1.68x under measured GB10 GPU chunk timings.

## Boundaries and scale limits

Small/medium local probe only: greedy decoding, Wikitext prompts, GPT-2/distilgpt2, estimated end-to-end speed from measured GPU verifier chunks rather than a full cache-slicing speculative decoder; no stochastic decoding, no 7B+ model, no production serving stack.

## Claim scope

Bounded GB10 probe on Wikitext prompts with GPT-2-class models: static external n-gram drafting did not produce useful speedup, while CPU prompt-lookup n-gram drafting showed high exact greedy-token agreement and calibrated speedup potential for distilgpt2 and gpt2.

## Why it stopped

This run produced a useful bounded mechanism signal but not direct production-decoder or publication-grade evidence; static external n-gram drafting was an early negative in the tested setting.

## Recommended next action

Implement prompt-lookup n-gram drafting in a real cache-preserving speculative decoder and require at least 1.3x measured median wall-clock speedup with exact output equivalence before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end prompt-lookup speculative decoding with real KV-cache rejection handling
- Success threshold: Median end-to-end speedup >= 1.3x on copy/repetition-heavy prompts, no output drift versus greedy decoding, and no more than 10% slowdown on the open-ended control workload.
- Stop condition: Stop if real cache-preserving implementation cannot exceed 1.1x median speedup on the copy-heavy workload or if rejection/cache handling causes any greedy output mismatch.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-hybrid-cpu-gpu-677de2e94d80`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
