# Multi-model corpus validation of context-suffix speculative decoding on structured text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-model-corpus-validation-of-context-suffix-speculativ-effb296cbe`
Run ID: `multi-model-corpus-validation-of-context-suffix-speculativ-effb296cbe-20260523T180604389810+0000`

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

- Parent run decision: Real-model trace validation for context-suffix speculative decoding on structured text: enoch://control-plane/projects/real-model-trace-validation-for-context-suffix-speculative-b7fbae9f1c/runs/real-model-trace-validation-for-context-suffix-speculative-b7fbae9f1c-20260523T174434462587+0000
- Parent run decision: Context-Suffix Matching Speculative Decoding for Structured Text: enoch://control-plane/projects/context-suffix-matching-speculative-decoding-for-structured-text-c0e4c0ba9a39/runs/context-suffix-matching-speculative-decoding-for-structured-text-c0e4c0ba9a39-20260523T171226663359+0000

## What looked useful

suffix_k4_L8 averaged 1.708 tokens/target-call and 38.0% target-call reduction on both distilgpt2 and gpt2 tokenizations, with paired +0.705 tokens/call versus shuffled context. However random_hit_k4_L8 averaged 1.776 tokens/call and unigram_k1_L8 averaged 1.969 tokens/call, indicating the gain mainly comes from repetition and formatting rather than the proposed recency-based suffix mechanism.

## Boundaries and scale limits

Synthetic/generated corpora only; no actual serving latency kernel; no target-model sampling loop; only distilgpt2 and gpt2 diagnostics; max 900 tokens per document; 5 corpora x 5 fixed seeds.

## Claim scope

On deterministic generated structured/repetitive corpora with GPT-2-family tokenizers and distilgpt2/gpt2 diagnostics, context-copy draft proposals reduce teacher-forced target validation calls versus no speculation and shuffled-context controls, but the specific most-recent 4-token context-suffix strategy is not better than simpler repetition baselines.

## Why it stopped

Tier 2 fixed-seed validation found real acceptance over controls but failed the specificity test: simpler repetition controls matched or exceeded the nominal context-suffix strategy, so the mechanism is mixed rather than paper-ready.

## Recommended next action

Stop this branch as no-paper useful signal; if continuing, run an actual prompt-lookup speculative decoding implementation on real JSON/SQL/Markdown corpora against a no-spec and unigram/repetition baseline with wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual prompt-lookup decoding latency on real structured corpora with repetition baselines
- Success threshold: Context-copy decoding must improve wall-clock tokens/sec by at least 20% over no-spec and at least 10% over unigram/repetition baseline on at least 3 of 4 real structured corpus families, without regressions above 5% on the remainder.
- Stop condition: Stop if context-copy does not beat unigram/repetition on target-call reduction in the first real-corpus calibration, or if validation overhead erases wall-clock gains despite acceptance improvements.

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-corpus-validation-of-context-suffix-speculativ-effb296cbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
