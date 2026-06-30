# N-gram speculative draft for local GPT-2-small serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-local-gpt-2-small-serving-de49accbd52e`
Run ID: `n-gram-speculative-draft-for-local-gpt-2-small-serving-de49accbd52e-20260607T100109969952+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3381bf24a3dd

## What looked useful

Prompt/history n-gram speculation reduced estimated target passes by about 48% and improved strict-fp32 aggregate throughput from 302.6 to 394.5 tokens/s while preserving requested-prefix correctness after truncation. The same mechanism was not safely correct in fp16/auto, despite a 1.23x aggregate speedup, because some outputs diverged inside the requested generation window.

## Boundaries and scale limits

Only 24 prompts x 64 new tokens were tested, with GPT-2-small, greedy decoding, single-request generation, and one n-gram/draft configuration. The run did not test batch serving, concurrent traffic, sampling, longer contexts, other model sizes, production servers, or broad prompt distributions. Default fp16/auto generated in-window mismatches and is not validated as a drop-in greedy replacement.

## Claim scope

On this GB10 worker with GPT-2-small greedy generation, Hugging Face prompt-lookup n-gram speculation using prompt_lookup_num_tokens=8 and max_matching_ngram_size=4 produced a bounded useful signal: strict fp32 with TF32 disabled preserved the requested 64-token greedy prefix after truncating extra returned tokens and improved aggregate throughput by 1.30x over baseline on 24 WikiText-style prompts.

## Why it stopped

No-paper closure: bounded direct benchmark produced a useful mechanism signal, but default fp16 correctness failures and raw extra-token returns prevent a positive serving claim.

## Recommended next action

Run a bounded deepen follow-up that implements an explicit output-length guard and investigates fp16/bfloat16-safe verification before any production or paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Correctness-preserving n-gram prompt lookup for fp16 GPT-2-small serving
- Success threshold: At least 1.10x aggregate throughput improvement with zero requested-prefix mismatches and no unguarded max_new_tokens overruns on the bounded prompt set.
- Stop condition: Stop if any in-window mismatch remains after length guarding and deterministic precision controls, or if correctness-preserving throughput is below 1.05x baseline.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-local-gpt-2-small-serving-de49accbd52e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
