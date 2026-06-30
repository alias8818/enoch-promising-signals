# Anchored N-gram Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchored-n-gram-speculative-decoding-for-cpu-inference-86e04a4c2d9f`
Run ID: `anchored-n-gram-speculative-decoding-for-cpu-inference-86e04a4c2d9f-20260605T025643994014+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ce76442746ef

## What looked useful

For max_n=4, draft_len=8, full-context n-gram drafting reduced oracle target verification cycles by 13.11% on Sherlock Holmes, 8.97% on Frankenstein, and 38.29% on local Python stdlib code; deterministic shuffled controls averaged only 1.45% reduction.

## Boundaries and scale limits

No real CPU LLM integration, no BPE tokenizer, no logits/KV-cache measurement, no end-to-end tokens/s benchmark, and only three ordered corpora after fallback corpora were excluded.

## Claim scope

Offline exact-match oracle benchmark over 60k regex-token public prose/code streams shows anchored n-gram drafting can reduce target verification cycles when ordered continuations repeat, especially for code-like text.

## Why it stopped

Bounded oracle proxy supports a mechanism but is not direct publication-grade CPU inference evidence.

## Recommended next action

Integrate max_n=4, draft_len=8 anchored n-gram drafting into a CPU LLM greedy decoder and measure end-to-end tokens/s on repeated-context prose and code prompts against greedy and no-draft controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM benchmark for anchored n-gram speculative decoding
- Success threshold: At least 10% end-to-end tokens/s improvement on code-like repeated-context prompts and non-negative throughput on prose prompts, with shuffled or non-repeated controls showing no comparable gain.
- Stop condition: Stop if draft overhead plus verification removes wall-clock throughput gains, or if accepted tokens per target call stays below 0.15 on both prose and code prompts.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-n-gram-speculative-decoding-for-cpu-inference-86e04a4c2d9f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
