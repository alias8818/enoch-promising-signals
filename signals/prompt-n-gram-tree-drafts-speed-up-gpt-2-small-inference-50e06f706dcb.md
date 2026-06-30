# Prompt n-gram tree drafts speed up GPT-2-small inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-n-gram-tree-drafts-speed-up-gpt-2-small-inference-50e06f706dcb`
Run ID: `prompt-n-gram-tree-drafts-speed-up-gpt-2-small-inference-50e06f706dcb-20260529T025533497678+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0856d70663e7

## What looked useful

Prompt n-gram drafts are useful when acceptance is high: accepted draft rates of 0.52 to 0.84 cut target forwards from 96 to 47, 25, or 16 and improved wall-clock latency. Low acceptance is a clear failure mode: 0.073 acceptance left 89/96 target forwards and made speculative decoding slower than standard KV greedy decoding.

## Boundaries and scale limits

Single GPT-2-small model, greedy decoding only, four synthetic/local prompt types, 96 generated tokens, one NVIDIA GB10, full-prefix speculative verifier rather than production KV-aware tree verification, no batched serving or real traffic distribution.

## Claim scope

On four bounded GPT-2-small greedy-decoding prompts, exact prompt n-gram draft verification speeds up highly repetitive prompt/output cases by 1.45x to 4.36x at max_draft=8, but slows down a low-overlap prompt to 0.845x versus a KV-cache greedy baseline.

## Why it stopped

Bounded direct GPT-2-small evidence is mixed: the mechanism works on repetitive prompts but the broad speedup claim fails on low-overlap prompts, so this is useful signal rather than a paper-ready result.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should implement KV-aware verification plus an online acceptance/fallback gate and require net speedup on a mixed prompt suite.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-aware prompt n-gram drafting with acceptance-gated fallback
- Success threshold: At least 1.2x median speedup versus optimized KV greedy decoding on the mixed prompt suite, no more than 5% p95 latency regression on low-overlap prompts, and exact greedy output equivalence.
- Stop condition: Stop if the gate cannot reliably detect low-acceptance cases or if KV-aware verification plus gating fails to beat the KV baseline by 1.2x median on the mixed prompt suite.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-n-gram-tree-drafts-speed-up-gpt-2-small-inference-50e06f706dcb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
