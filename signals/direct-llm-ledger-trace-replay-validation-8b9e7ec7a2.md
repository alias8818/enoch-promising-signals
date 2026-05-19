# Direct LLM Ledger Trace-Replay Validation

Status: `useful_signal`
Project ID: `direct-llm-ledger-trace-replay-validation-8b9e7ec7a2`
Run ID: `direct-llm-ledger-trace-replay-validation-8b9e7ec7a2-20260515T183823217677+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Direct LLM Ledger Trace-Replay Validation: internal_generated:direct-llm-ledger-trace-replay-validation-8b9e7ec7a2

## What looked useful

Across 256 completed direct LLM generations, exact replay occurred once. Qwen2.5-1.5B-Instruct zero-shot reached 1/64 exact overall and 0/48 exact for 8+ operation traces; its few-shot ablation reached 0/64 exact despite 100% parse rate. The deterministic oracle was 64/64 exact and a transfer-ignorant shortcut baseline outperformed every LLM configuration on exact rate.

## Boundaries and scale limits

No production ledgers, external API/frontier models, 7B+ open models, tool-augmented replay, constrained decoding, or real audit workflows were tested. Two cached local checkpoints were incomplete and could not be evaluated. The result is a direct local falsification for prompt-only small LLM replay, not a universal impossibility proof for larger or tool-assisted systems.

## Claim scope

Direct prompt-only local LLM ledger trace replay was tested on seeded synthetic ledgers with 3-5 accounts, 4-32 operations, ordered and shuffled transaction streams, deterministic replay baseline, shortcut controls, and zero-shot/few-shot prompt variants. Local models up to Qwen2.5-1.5B-Instruct did not achieve reliable exact final-balance replay.

## Why it stopped

Direct seeded validation falsified the paper-readiness threshold for prompt-only local LLM ledger replay: exact replay was effectively absent beyond the easiest traces and the best LLM underperformed a simple shortcut baseline.

## Recommended next action

Stop this depth-4 follow-up as a no-paper useful negative; archive the harness and metrics rather than launching another chained follow-up from this campaign.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/direct-llm-ledger-trace-replay-validation-8b9e7ec7a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
