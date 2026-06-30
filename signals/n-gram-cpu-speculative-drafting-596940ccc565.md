# N-Gram CPU Speculative Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-speculative-drafting-596940ccc565`
Run ID: `n-gram-cpu-speculative-drafting-596940ccc565-20260523T034753497828+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2783101e236a

## What looked useful

Order-3 n-grams with block size 8 were best on both corpora: 1.268 emitted tokens per verifier call on Alice and 1.159 on Tiny Shakespeare. Median accepted run was 0 and p90 was 1, so gains came from sparse short matches rather than long accepted blocks. If verifying a draft block costs 1.25x a greedy verifier step, estimated speedup is near 1.01x on Alice and below 1.0x on Tiny Shakespeare.

## Boundaries and scale limits

No transformer model, tokenizer, KV cache, GPU/CPU overlap, learned draft baseline, or production serving stack was tested. Corpora were Alice in Wonderland and Tiny Shakespeare only; this is a CPU proxy benchmark, not full LLM validation.

## Claim scope

On two small public text corpora using a held-out exact-match proxy, a prefix-trained CPU n-gram drafter reduced verifier calls by 16-27% at the best settings, but accepted runs were sparse and the estimated latency benefit was fragile.

## Why it stopped

Closed as no-paper useful signal because the evidence is a proxy benchmark with mixed practical value, not a direct LLM serving validation.

## Recommended next action

Run a bounded direct GPT-2-small integration with online prompt n-grams and require at least 1.10x measured wall-clock speedup on repeated-prefix workloads before considering further scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-Small N-Gram Speculative Decoding Test
- Success threshold: At least 1.10x measured wall-clock speedup on repeated-prefix prompts with identical generated tokens and no more than 5% slowdown on ordinary prompts.
- Stop condition: Stop if exact output equality cannot be maintained, if accepted tokens per verifier call stays below 1.10 on repeated-prefix prompts, or if CPU drafting overhead removes measured wall-clock speedup.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-speculative-drafting-596940ccc565`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
