# End-to-end block-parallel n-gram speculative decoding with a small real LM

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `end-to-end-block-parallel-n-gram-speculative-decoding-with-e583ddd092`
Run ID: `end-to-end-block-parallel-n-gram-speculative-decoding-with-e583ddd092-20260523T114246080538+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Corpus-backed cached verifier ablation for n-gram speculative decoding: enoch://control-plane/projects/corpus-backed-cached-verifier-ablation-for-n-gram-speculat-661ab1f77b/runs/corpus-backed-cached-verifier-ablation-for-n-gram-speculat-661ab1f77b-20260523T094635668479+0000
- Parent run decision: Block-parallel corpus verifier for n-gram speculative decoding: enoch://control-plane/projects/block-parallel-corpus-verifier-for-n-gram-speculative-deco-aa39626f96/runs/block-parallel-corpus-verifier-for-n-gram-speculative-deco-aa39626f96-20260523T102354696676+0000

## What looked useful

Strict exact n-gram speculation with order 2 and draft length 8 achieved 1.31x GPT-2 throughput and 2.02x distilgpt2 throughput versus KV-cache greedy while exact-matching all strict validation rows. Random-draft controls were about 0.45x greedy, and the faster block-correction path reached about 2.06x on GPT-2 but exact-matched only 87.5% of prompts.

## Boundaries and scale limits

Only two GPT-2-class small LMs, one dataset slice, one host/runtime, one seed, greedy decoding only, batch size 1, and 32 prompts per model. No larger models, production serving kernels, sampling distribution checks, larger prompt corpus, or multi-run variance estimates.

## Claim scope

Bounded local evidence on NVIDIA GB10 for batch-1 greedy decoding with GPT-2 and distilgpt2 on 32 WikiText-2 validation prompts per model, 96 prompt tokens and 96 generated tokens. Strict n-gram speculative decoding exactly matched greedy output and improved mean throughput; faster block-correction decoding did not preserve exactness.

## Why it stopped

Evidence supports a useful mechanism but not Tier-4 publication readiness; block-correction exactness is mixed and the strict exact positive result is still bounded to a small local validation.

## Recommended next action

Stop this follow-up chain at depth 4 and do not write a paper from this run; retain the strict exact benchmark and metrics as useful bounded evidence for any future independent broader validation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-block-parallel-n-gram-speculative-decoding-with-e583ddd092`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
