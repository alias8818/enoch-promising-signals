# Zero-Draft SpecDec via N-gram Cache Recycling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `zero-draft-specdec-via-n-gram-cache-recycling-a4228e7a5f5c`
Run ID: `zero-draft-specdec-via-n-gram-cache-recycling-a4228e7a5f5c-20260610T002532572835+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/89779ce81038

## What looked useful

Synthetic controls behaved correctly. Wikitext continuation proxy showed at most 1.59% target-step reduction with median per-sample reduction 0. DistilGPT-2 greedy smoke showed 29.5-35.8% fewer verification steps across nearby n-gram/gamma settings with 71-90% proposed-token acceptance.

## Boundaries and scale limits

No end-to-end speculative decoding kernel or KV-cache relocation was implemented; tests used 24 DistilGPT-2 greedy prompts and 256 Wikitext proxy samples, not larger models, learned-draft baselines, sampling, code/log workloads, or production serving.

## Claim scope

Exact n-gram copied continuations from already decoded history can reduce verification steps for small DistilGPT-2 greedy generations on Wikitext prompts, but the same mechanism is weak on ordinary held-out Wikitext continuations.

## Why it stopped

The result is mixed and proxy-level: promising for small greedy model repetitions but too weak on ordinary corpus continuations and lacks end-to-end KV/speculative-decoding timing.

## Recommended next action

Stop as no-paper useful-signal evidence; run one bounded follow-up implementing real target-model verification timing on repetitive/code-like prompts before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end zero-draft verification timing on repetitive/code-like generation
- Success threshold: At least 15% end-to-end tokens/sec improvement over greedy no-spec decoding on repetitive/code-like prompts with exact output equality, and no claimed broad prose benefit unless ordinary-prose speed also improves by at least 10%.
- Stop condition: Stop if accepted-token yield does not translate into at least 5% wall-clock improvement after batching verification, or if positional/KV handling prevents exact output preservation.

## Evidence references

- Artifact root: `<local-path>/projects/zero-draft-specdec-via-n-gram-cache-recycling-a4228e7a5f5c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
