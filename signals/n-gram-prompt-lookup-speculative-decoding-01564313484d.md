# N-gram prompt lookup speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-prompt-lookup-speculative-decoding-01564313484d`
Run ID: `n-gram-prompt-lookup-speculative-decoding-01564313484d-20260531T161411429853+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b3cd440f7980

## What looked useful

The mechanism is real for copy-heavy contexts, but it is not a safe drop-in decoding replacement in the tested Transformers path without prompt gating and output-length/equivalence guards.

## Boundaries and scale limits

Synthetic prompts only; GPT-2 and tiny-GPT-2 only; batch size 1; no 7B+ models, no production serving stack, no natural long-context corpus, no sampling validation, and no latency-tail or batching study. Low-repeat controls showed output-equivalence and length hazards.

## Claim scope

On local GPT-2-class greedy decoding with synthetic copy-heavy prompts, Transformers prompt lookup speculative decoding can reduce target forward calls by up to 87.5% at prompt_lookup_num_tokens=8 and produce about 4x median speedups while preserving exact 64-token output for the tested repeated prompts.

## Why it stopped

Bounded local evidence supports the mechanism but revealed practical correctness hazards, so this run should close as no-paper useful signal rather than full validation.

## Recommended next action

Run a bounded deepen follow-up on natural copy-heavy workloads with exact-equivalence gating and enforced max_new_tokens trimming before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-workload prompt lookup decoding with exact-equivalence guards
- Success threshold: For copy-heavy natural prompts, at least 1.5x median latency speedup with exact trimmed token equality in 99.9% or more cases, and no median slowdown greater than 5% on low-repeat prompts after gating.
- Stop condition: Stop if guarded prompt lookup cannot preserve exact trimmed greedy output or if low-repeat gating fails to prevent material latency regressions.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-prompt-lookup-speculative-decoding-01564313484d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
