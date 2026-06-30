# N-gram Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-on-cpu-3ee0e8eda858`
Run ID: `n-gram-draft-speculative-decoding-on-cpu-3ee0e8eda858-20260607T140212043873+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a62e72f4c9fb

## What looked useful

N-gram draft speculative decoding can reduce calls when generated text repeats prior context almost exactly, but the naive CPU implementation is not practically viable on GPT-2 small without an adaptive gate and stronger exactness handling.

## Boundaries and scale limits

Tested Hugging Face CPU decoding only, with sshleifer/tiny-gpt2 over three short prompts and gpt2 over two short prompts. No 7B+ model, no production serving trace, no sampling-mode validation, and no optimized C++ inference runtime.

## Claim scope

On this CPU worker, a naive suffix n-gram drafter for exact greedy decoding speeds up a tiny repetitive GPT-2 checkpoint but does not transfer to a GPT-2-small-class probe; the GPT-2 probe slows down because full-block acceptance is too rare and verification overhead dominates.

## Why it stopped

Bounded local evidence is mixed-to-negative: toy tiny-GPT-2 showed speedup, but the more relevant GPT-2-small-class probe slowed decoding and a shorter-draft ablation exposed exact-output fragility.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should add an adaptive attempt gate and token-id exactness checks on GPT-2-small-class prompts before considering larger CPU serving validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive gate for exact n-gram speculative decoding on CPU
- Success threshold: No output mismatches and at least 1.1x mean end-to-end speedup over cached greedy decoding on GPT-2-small-class CPU prompts, with no prompt slower than 0.95x.
- Stop condition: Stop if the adaptive gate cannot keep target forward calls at or below greedy on GPT-2-small-class prompts or if any token-id mismatch appears under exact greedy comparison.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-cpu-3ee0e8eda858`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
