# N-gram CPU Speculative Decode

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-cpu-speculative-decode-241538880383`
Run ID: `n-gram-cpu-speculative-decode-241538880383-20260525T054001064067+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fa784b59fdfb

## What looked useful

Distilgpt2 repeated-context probe accepted 71/101 proposed tokens, had zero greedy-output mismatches, reduced target calls from 192 to 126, and measured 1.57x wall speedup. Mixed prompts still had zero mismatches and 1.33x wall speedup, but no-match controls fell back near baseline.

## Boundaries and scale limits

Small models only; short hand-written prompts; CPU full-context PyTorch validation rather than production KV-cache serving; no sampling, batching, GPU scheduling, 7B+ model, or natural large prompt-suite validation.

## Claim scope

In a small CPU-only greedy decoding harness, a prompt-lookup n-gram drafter can preserve exact target-model output while reducing target forward calls and wall time for repeated-context prompts on tiny-gpt2 and distilgpt2.

## Why it stopped

Evidence supports the local mechanism but is proxy-scale and not a full validation of production LLM speculative decoding.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded KV-cache compatible benchmark on a natural repeated-context code/document prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache prompt-lookup n-gram speculative decoding on natural repeated-context prompts
- Success threshold: Zero greedy-output mismatches, at least 1.20x wall speedup on repetition-heavy prompts, and no more than 5% wall-time regression on no-repeat controls.
- Stop condition: Stop if acceptance is below 25% or end-to-end wall speedup is below 1.05x on the repetition-heavy slice after proposal-length tuning.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-speculative-decode-241538880383`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
