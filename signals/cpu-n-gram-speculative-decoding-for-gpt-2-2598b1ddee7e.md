# CPU N-gram Speculative Decoding for GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-gpt-2-2598b1ddee7e`
Run ID: `cpu-n-gram-speculative-decoding-for-gpt-2-2598b1ddee7e-20260528T173113387121+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8fda443b78db

## What looked useful

A simple context n-gram drafter can reduce target model forwards and accelerate greedy GPT-2-family CPU decoding when continuations are locally repetitive. The mechanism is real under exact greedy-equivalence checks, but GPT-2 small results are mixed across prompts and not paper-ready.

## Boundaries and scale limits

No KV-cache optimized verifier, no sampling, no long-form benchmark corpus, no batched serving workload, no GPT-2 medium/large, and no modern LLM validation. Results are short-run CPU measurements on a single worker with full-context PyTorch forwards.

## Claim scope

CPU-only Python benchmark of n-gram speculative greedy decoding on sshleifer/tiny-gpt2, distilgpt2, and gpt2 for 2-6 short prompts and 16-48 generated tokens. Speculative outputs exactly matched greedy outputs. GPT-2 small reached 1.72x-1.97x mean tokens/s speedup in this bounded setup, but gains were prompt-dependent and one prompt had zero draft acceptance.

## Why it stopped

Bounded local evidence supports the mechanism but is prompt-dependent and lacks optimized serving-style validation, so it is not sufficient for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded deepen study with a KV-cache verifier and fixed text benchmark, requiring median GPT-2 speedup and no tail regressions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram speculative decoding benchmark for GPT-2 CPU
- Success threshold: At least 1.25x median tokens/s speedup on GPT-2 small CPU greedy decoding, exact output match for every prompt, and no more than 10% of prompts slower than greedy by more than 5%.
- Stop condition: Stop as negative if KV-cache verification does not preserve exact greedy output, median speedup is below 1.10x, or more than 25% of prompts regress versus greedy.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-gpt-2-2598b1ddee7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
