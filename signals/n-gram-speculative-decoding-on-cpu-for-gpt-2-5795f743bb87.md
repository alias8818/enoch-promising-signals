# N-gram Speculative Decoding on CPU for GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-on-cpu-for-gpt-2-5795f743bb87`
Run ID: `n-gram-speculative-decoding-on-cpu-for-gpt-2-5795f743bb87-20260525T133721037732+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ee1b9b06ebf8

## What looked useful

Exact n-gram speculative decoding reached 1.82x median speedup on intentionally repetitive prompts with 100% median acceptance and 73% fewer target forwards, but slowed to 0.48x on natural prompts and 0.73x on mixed prompts. Gamma sweep reproduced the split: natural 0.42-0.47x, mixed 0.62-0.67x, repetitive 1.27-2.40x.

## Boundaries and scale limits

Tested GPT-2 small only, CPU only, greedy decoding only, 4 handcrafted prompt sets per regime, 24-32 generated tokens, no production serving stack, no external corpus n-gram table, no sampling/temperature evaluation, and conservative cache recomputation after partial mismatch.

## Claim scope

On GPT-2 small CPU greedy decoding with exact verification, a simple prompt/context n-gram draft model accelerates highly repetitive prompts but slows natural and moderately repetitive prompts in this bounded benchmark.

## Why it stopped

Bounded direct GPT-2 CPU evidence is mixed and not paper-ready: the mechanism works on highly repetitive contexts but fails to improve natural or moderately repetitive prompts.

## Recommended next action

Do not write a paper from this run; use the result as a scoped negative/practical signal and only deepen if targeting repeated-template/code/log workloads with a rigorously exact KV rollback implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact KV-rollback n-gram speculation for repeated-template CPU workloads
- Success threshold: Median speedup at least 1.25x on repeated-template/code/log prompts, no median slowdown below 0.95x on mixed prompts, and 100% exact token equality.
- Stop condition: Stop if exact KV rollback cannot be made reliable or if median speedup remains below 1.1x outside intentionally repetitive prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-for-gpt-2-5795f743bb87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
