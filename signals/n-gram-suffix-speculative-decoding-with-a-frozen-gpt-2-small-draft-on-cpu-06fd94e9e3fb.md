# N-gram suffix speculative decoding with a frozen GPT-2-small draft on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-speculative-decoding-with-a-frozen-gpt-2-small-draft-on-cpu-06fd94e9e3fb`
Run ID: `n-gram-suffix-speculative-decoding-with-a-frozen-gpt-2-small-draft-on-cpu-06fd94e9e3fb-20260621T183936638840+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41859764a854

## What looked useful

Plain GPT-2-small speculative decoding reached 1.05-1.10x baseline speedup with exact output matching. Adding suffix proposals reached 1.09-1.13x speedup, but suffix proposals were only 7.7-15.8% of proposals and had lower acceptance than plain GPT-2 draft proposals.

## Boundaries and scale limits

Three short repeated-structure prompts, 48-72 generated tokens per aggregate run, CPU-only PyTorch without KV-cache optimization, target limited to GPT-2-medium, no large corpus, no sampling-mode validation, and no long-context stress benchmark.

## Claim scope

On a bounded CPU benchmark using gpt2-medium as target and frozen gpt2 as draft, exact greedy speculative decoding reduced target forwards per generated token and produced identical output, but n-gram suffix augmentation added only small, fragile throughput gains over plain GPT-2-small draft speculative decoding.

## Why it stopped

Bounded CPU evidence supports the general speculative decoding mechanism but not a robust positive claim for n-gram suffix augmentation; the result is a proxy-scale early falsification of the suffix-specific benefit, not a full validation.

## Recommended next action

Stop this run as no-paper useful evidence; only revisit with a KV-cache implementation and a repetition-heavy prompt corpus that can isolate suffix proposal acceptance and draft-forward savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram suffix speculative decoding on repetition-heavy prompts
- Success threshold: Suffix-augmented speculative decoding must beat plain GPT-2-small speculative decoding by at least 10% end-to-end tokens/s across the corpus while maintaining exact greedy target outputs and not increasing target forwards per token.
- Stop condition: Stop if suffix proposal acceptance stays below plain draft acceptance or if end-to-end speedup over plain GPT-2-small speculative decoding is under 5% after the KV-cache implementation and repetition-heavy corpus are in place.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculative-decoding-with-a-frozen-gpt-2-small-draft-on-cpu-06fd94e9e3fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
