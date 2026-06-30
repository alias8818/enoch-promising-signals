# N-gram speculative drafting for tiny CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-drafting-for-tiny-cpu-inference-6c7087db0611`
Run ID: `n-gram-speculative-drafting-for-tiny-cpu-inference-6c7087db0611-20260526T021901002344+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/77620b22bbc3

## What looked useful

On distilgpt2 repeated-context prompts, n-gram drafting exactly matched greedy outputs, reduced target forwards by 75.0%, and improved mean throughput from 23.39 to 50.63 tok/s (2.17x). On natural prompts it exactly matched greedy outputs but achieved only 1.30x mean speedup with one near-break-even prompt.

## Boundaries and scale limits

Tested only distilgpt2 plus a tiny smoke model, greedy decoding only, 4 repeated-context prompts and 4 natural prompts, 32 generated tokens each, Python/Transformers runtime rather than an optimized quantized serving engine.

## Claim scope

A Python/PyTorch exact-greedy benchmark on CPU showed that prompt/context n-gram speculative drafting can accelerate distilgpt2 decoding on repeated-context prompts, with smaller and workload-dependent gains on natural prompts.

## Why it stopped

Bounded local evidence supports the mechanism but is too small and runtime-specific for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement the same n-gram verifier in a quantized CPU runtime and test a repetition-stratified workload suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantized CPU runtime validation for n-gram speculative drafting
- Success threshold: Median speedup >=1.25x on repetition-rich prompts, p25 speedup >1.0x in that bucket, and median speed >=0.95x baseline on low-repetition prompts.
- Stop condition: Stop if exactness fails, if repetition-rich median speedup is <1.10x, or if low-repetition prompts regress by more than 10% median throughput.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-drafting-for-tiny-cpu-inference-6c7087db0611`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
