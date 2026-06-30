# Prompt-Suffix Draft CPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-suffix-draft-cpu-speculative-decoding-2f4e1def1049`
Run ID: `prompt-suffix-draft-cpu-speculative-decoding-2f4e1def1049-20260527T070813258219+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ff40aea468c3

## What looked useful

Prompt-only suffix drafting achieved 0.780 acceptance and 88.5% target-step reduction on exact copy, 0.644 acceptance and 76.3% reduction on edited copy, but only 2.1% reduction on nonlocal continuations. Prompt-plus-output lookup can look much stronger by exploiting generated self-repetition, so evaluations must report match scope.

## Boundaries and scale limits

No real LLM logits, tokenizer, KV cache, batching, or wall-clock serving latency were tested. Speedups are verifier-step upper bounds from exact-token acceptance, not production latency measurements.

## Claim scope

Model-free CPU proxy over 288 synthetic continuation cases: prompt-suffix lookup supports speculative decoding verifier-step reductions on exact or lightly edited prompt-local copying, but not on reordered or unrelated prompt-only continuations.

## Why it stopped

Proxy mechanism test supports a narrow copy-heavy use case but early-falsifies a broad prompt-only benefit claim for reordered or unrelated continuations; it is not full LLM validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test a real small CPU language model on extraction/copy-heavy prompts with prompt-only and prompt-plus-output match attribution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM prompt-suffix speculative decoding on copy-heavy tasks
- Success threshold: At least 1.2x median wall-clock speedup on copy-heavy tasks with exact greedy-output preservation, plus less than 1.05x speedup on non-copy controls or a clear explanation for any broader effect.
- Stop condition: Stop if prompt-only acceptance is below 0.35 or median wall-clock speedup is below 1.1x on copy-heavy tasks after suffix-search overhead is optimized enough to be below 10% of target verification time.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-suffix-draft-cpu-speculative-decoding-2f4e1def1049`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
