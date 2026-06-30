# N-Gram Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-on-cpu-a576665bcae3`
Run ID: `n-gram-draft-speculative-decoding-on-cpu-a576665bcae3-20260527T072346496222+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/42851e3fbff3

## What looked useful

Max-draft-8 distilgpt2 run had 0 greedy mismatches, 37.11% fewer target decode calls, 1.24x overall speedup, 1.86x mean speedup on repeated-span prompts, and 0.99x mean speedup on controls.

## Boundaries and scale limits

Only 8 synthetic prompts x 32 generated tokens plus a tiny-model smoke were tested. No larger models, sampling mode, production traces, broad natural prompt suite, server batching, or optimized partial-cache slicing were validated.

## Claim scope

On a CPU worker with cached HuggingFace distilgpt2, exact greedy n-gram speculative decoding preserved token identity and improved latency on small synthetic prompts with repeated local spans; controls showed no material speedup.

## Why it stopped

Useful local mechanism evidence, but no paper-positive closure because the benchmark is small and synthetic and controls show negligible benefit.

## Recommended next action

Run a bounded natural-prompt benchmark with at least 100 snippets stratified by local repetition and add exact cache slicing before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Prompt Validation of Lossless N-Gram Speculative Decoding on CPU
- Success threshold: High-repetition stratum achieves at least 1.20x median wall-clock speedup with zero token mismatches, while low-repetition stratum is identified as neutral or harmful with a clear routing rule.
- Stop condition: Stop if high-repetition natural prompts do not reach 1.10x median speedup or if exact cache slicing cannot preserve greedy token identity.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-cpu-a576665bcae3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
