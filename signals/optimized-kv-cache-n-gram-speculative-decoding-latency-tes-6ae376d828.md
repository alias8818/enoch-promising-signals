# Optimized KV-cache n-gram speculative decoding latency test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `optimized-kv-cache-n-gram-speculative-decoding-latency-tes-6ae376d828`
Run ID: `optimized-kv-cache-n-gram-speculative-decoding-latency-tes-6ae376d828-20260522T032104481187+0000`

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

- Parent run decision: N-gram speculative decoding for tiny LLMs with exact draft verification: enoch://control-plane/projects/n-gram-speculative-decoding-for-tiny-llms-with-exact-draft-verification-e1ba28b240f2/runs/n-gram-speculative-decoding-for-tiny-llms-with-exact-draft-verification-e1ba28b240f2-20260521T221318485798+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1d33469bb5d9

## What looked useful

After fixing draft selection to choose a prior n-gram occurrence with the longest continuation, the speculative path reduced median repeat-prompt model calls from 97 to about 20 on tiny-gpt2 and from 65 to 16-21 on distilgpt2, with exact greedy-token matches and 2.6x-3.4x per-prompt speedups.

## Boundaries and scale limits

Small models only; few prompts; greedy decoding only; no batched serving, long-context pressure, sampling, production inference engine, or 7B+ validation.

## Claim scope

On GB10 CUDA with greedy decoding for sshleifer/tiny-gpt2 and distilgpt2, an optimized n-gram KV-cache verifier preserved exact greedy outputs and reduced latency on short repeated-output prompts.

## Why it stopped

Tier 1 direct test produced useful mechanism support but remains no-paper evidence because the models and prompts are too small and repetitive for a publication-grade latency claim.

## Recommended next action

Run a medium direct follow-up on a stronger causal LM with a fixed corpus split of repeated code/text prompts and non-repetitive controls, reporting exact-match rate, acceptance, latency, and call-count reductions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium corpus validation of KV-cache n-gram speculative decoding on repeated code and text
- Success threshold: Exact greedy match rate 100%; median repeated-subset speedup >= 1.25x; non-repetitive control median speedup >= 0.95x; acceptance rate >= 0.25 on repeated subsets.
- Stop condition: Stop if exact greedy matching fails, if repeated-subset speedup is below 1.10x after n-gram/draft ablation, or if controls show more than 10% median slowdown.

## Evidence references

- Artifact root: `<local-path>/projects/optimized-kv-cache-n-gram-speculative-decoding-latency-tes-6ae376d828`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
