# Zero-VRAM N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `zero-vram-n-gram-speculative-decoding-ea5574ff6960`
Run ID: `zero-vram-n-gram-speculative-decoding-ea5574ff6960-20260628T050533995500+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/bd7acb8f5843

## What looked useful

The zero-VRAM draft mechanism is practically plausible: CPU n-gram proposals were verified by the target model with KV cache, produced exact greedy-equivalent output in the clean gpt2 fp32 matrix, and lowered target forwards substantially. The result is a bounded mechanism signal, not a paper-ready validation.

## Boundaries and scale limits

Tested only tiny-gpt2, distilgpt2, and gpt2 on 24-96 new tokens with synthetic/small prompts and a Python suffix lookup. Not validated on 1B-8B+ instruction models, batched serving, sampling, long contexts, production kernels, or broad prompt corpora. One gpt2 fp16 prompt diverged from greedy while fp32 matched, so low-precision exactness needs safeguards.

## Claim scope

On GPT-2-class causal language models with short greedy generations, a CPU-only token n-gram draft can reduce target-model CUDA forward calls without draft-model VRAM when generated text has local repetition; exact fp32 gpt2 tests showed 35.4% to 86.2% target-call reduction and 1.42x to 4.24x speedup across four prompts.

## Why it stopped

No-paper closure: this run produced bounded GPT-2-class evidence but not broad publication-grade validation; remaining work is a direct medium-scale confirmation rather than more smoke testing.

## Recommended next action

Run a medium confirmation on a 1B-8B local instruction/code model with realistic prompts, exactness or argmax-margin safeguards for low precision, and ablations over draft length and n-gram size.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium-scale exactness and throughput test for zero-VRAM n-gram speculative decoding
- Success threshold: Exact greedy match on at least 99% of prompts or documented margin-safe fallback, at least 25% median target-call reduction and at least 1.2x median wall-clock speedup on repetition-rich prompts, and no more than 10% slowdown on low-repetition prompts.
- Stop condition: Stop if exactness fails without a practical margin/fallback fix, if median target-call reduction is below 15% on repetition-rich prompts, or if low-repetition prompts show more than 20% slowdown after draft_len/max_n tuning.

## Evidence references

- Artifact root: `<local-path>/projects/zero-vram-n-gram-speculative-decoding-ea5574ff6960`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
