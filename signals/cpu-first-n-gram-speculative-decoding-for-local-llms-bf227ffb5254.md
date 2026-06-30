# CPU-First N-gram Speculative Decoding for Local LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-first-n-gram-speculative-decoding-for-local-llms-bf227ffb5254`
Run ID: `cpu-first-n-gram-speculative-decoding-for-local-llms-bf227ffb5254-20260602T211454196249+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/613211601a03

## What looked useful

CPU n-gram drafting produced a reproducible call-count signal: best order 5, max_spec 16 achieved 2.013x mean ideal verifier-call speedup and 49.7% mean call reduction, while short max_spec 2 had higher proposal acceptance at 37.1% with 1.735x speedup. This suggests the mechanism is worth a direct local-LM timing benchmark but is not paper-ready.

## Boundaries and scale limits

No direct neural local LLM timing was completed. The target was held-out byte text rather than model greedy outputs; verifier cost was counted ideally rather than measured through KV-cache block verification; corpus scope was one small repetitive text source with 32 held-out windows.

## Claim scope

A dependency-light trace probe on 200,000 bytes of Tiny Shakespeare shows that a CPU n-gram draft table can reduce ideal verifier-call counts by about 1.7x to 2.0x on held-out repetitive byte continuations, but this is not direct local-LLM serving evidence.

## Why it stopped

Stopped at a bounded proxy/useful-signal result because the available Python 3.14 Torch path pulled an incomplete multi-GB CUDA install and no direct local-LM timing was completed; the trace result should not be treated as full validation.

## Recommended next action

Run a direct local CPU LLM benchmark using llama.cpp or a complete CPU inference stack, comparing baseline greedy decoding to n-gram speculative verification on code, markdown/chat, and prose prompts with exact output equivalence and wall-clock tokens/s.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU Local-LLM Timing for N-gram Speculative Verification
- Success threshold: At least 1.2x wall-clock tokens/s improvement on two repeated/prompt-copy-heavy prompt categories with exact output equivalence, and no more than 5% slowdown on prose prompts.
- Stop condition: Stop as negative if direct local-LM wall-clock speedup is below 1.1x on repeated/prompt-copy-heavy prompts or output equivalence fails under deterministic greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-first-n-gram-speculative-decoding-for-local-llms-bf227ffb5254`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
