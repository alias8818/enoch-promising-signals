# Prompt N-Gram Speculative Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-n-gram-speculative-draft-4e6e269be1b0`
Run ID: `prompt-n-gram-speculative-draft-4e6e269be1b0-20260523T045634557409+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bb1f540afb65

## What looked useful

Prompt n-gram drafts are conditionally useful: quote/repeat prompts accepted 294 of 352 drafted tokens and reduced target calls by 75.5%, copy-loop prompts reduced target calls by 43.0%, while natural prompts accepted only 5 of 215 drafted tokens and reduced target calls by 1.3%.

## Boundaries and scale limits

Small GPT-2-class target model, synthetic prompt classes, greedy decoding only, prototype full-prefix verifier timing, no production KV-cache kernel, no sampled decoding, no large instruction/coding model, and no real serving workload.

## Claim scope

On 18 synthetic distilgpt2 greedy-decoding prompts, prompt-only n-gram speculative drafts exactly preserved target outputs and reduced sequential target verification calls for copy/repetition-heavy prompts, with little benefit on ordinary open-ended prompts.

## Why it stopped

Bounded local evidence supports the mechanism only in copy-heavy regimes and is insufficient for a paper or broad speculative-decoding claim.

## Recommended next action

Stop this run as no-paper useful evidence; next run should test real copy-heavy retrieval/code workloads with a KV-cache verifier and compare against no-draft and small-model draft baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt N-Gram Drafting on Real Copy-Heavy Workloads
- Success threshold: At least two real copy-heavy workloads show exact-output preservation and at least 25% target-call reduction with non-regressed latency versus no draft.
- Stop condition: Stop if acceptance on real copy-heavy workloads is below 10% or target-call reduction is below 15% on all tested workloads after verifier correctness is confirmed.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-n-gram-speculative-draft-4e6e269be1b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
