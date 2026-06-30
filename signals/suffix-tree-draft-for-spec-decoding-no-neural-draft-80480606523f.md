# Suffix-tree draft for spec decoding, no neural draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-draft-for-spec-decoding-no-neural-draft-80480606523f`
Run ID: `suffix-tree-draft-for-spec-decoding-no-neural-draft-80480606523f-20260619T151232641007+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/32d194b9714d

## What looked useful

Suffix-copy drafting is a narrow repetition/copy mechanism: corpus proxy accepted 1.3828 of 7.864 proposed bytes on average versus 1.1852 of 7.9872 for a capped n-gram baseline; neural greedy traces accepted drafted tokens when repeated spans appeared, with 2.4 tokens/iteration on a small distilgpt2 trace.

## Boundaries and scale limits

Tested on a 1.1 MB Shakespeare corpus at byte level, plus small greedy verifier traces with sshleifer/tiny-gpt2 and distilgpt2. No fused speculative decoding kernel, no wall-clock serving comparison, no sampling, no instruction-tuned model, and no large model validation.

## Claim scope

A prompt-local exact suffix-copy draft can provide accepted speculative tokens in repeated/copyable spans and slightly outperformed a cheap train n-gram byte baseline on Tiny Shakespeare, but the evidence does not support broad LLM serving speedup.

## Why it stopped

Evidence supports a narrow mechanism but not a publication-grade or broad positive claim; neural evidence is a small greedy acceptance trace and corpus evidence is a proxy with low accepted/proposed rate.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement batched verifier speculative decoding on GPT-2-small-class prompts and compare actual tokens/sec against ordinary greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched verifier latency test for suffix-copy speculative decoding
- Success threshold: At least 1.15x end-to-end tokens/sec on repeated-span prompts with no more than 5% slowdown on non-repetitive controls, measured over at least 2,000 generated tokens.
- Stop condition: Stop if batched verification gives less than 1.05x speedup on repeated-span prompts or causes more than 5% slowdown on controls after suffix lookup overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-for-spec-decoding-no-neural-draft-80480606523f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
