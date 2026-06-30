# Prompt-Lookup Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-speculative-decoding-on-cpu-032201ac6b33`
Run ID: `prompt-lookup-speculative-decoding-on-cpu-032201ac6b33-20260619T162342331215+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1bcea6a10f29

## What looked useful

Across 200 case/config rows, median verifier-call reduction was 0.353571 and best reduction was 0.895833. Extractive copy and boilerplate scenarios showed large reductions; low-repeat random and local project-doc suffix scenarios showed zero or negligible reduction.

## Boundaries and scale limits

No neural target model, no tokenizer-specific benchmark, no KV-cache or batched verification measurement, and no end-to-end CPU tokens/sec comparison. Results are verifier-call reduction upper bounds, not observed LM throughput.

## Claim scope

Exact prompt-lookup draft acceptance on deterministic CPU-local token traces. PLD can greatly reduce ideal verifier calls for repeat-heavy extractive and boilerplate traces, but gives negligible benefit on low-repeat/local-doc traces.

## Why it stopped

This run produced useful proxy/trace evidence but not direct real-model CPU throughput evidence, so it is not paper-positive.

## Recommended next action

Run a bounded direct CPU LM follow-up that integrates PLD into an actual decode loop and reports autoregressive vs PLD wall-clock tokens/sec on repeat-heavy and low-repeat prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LM wall-clock validation of prompt-lookup speculative decoding
- Success threshold: At least 1.15x end-to-end tokens/sec on repeat-heavy prompt sets with no more than 5% slowdown on low-repeat controls.
- Stop condition: Stop if PLD produces less than 1.05x speedup on repeat-heavy prompts or more than 5% slowdown on low-repeat controls under a valid direct CPU LM implementation.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-speculative-decoding-on-cpu-032201ac6b33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
