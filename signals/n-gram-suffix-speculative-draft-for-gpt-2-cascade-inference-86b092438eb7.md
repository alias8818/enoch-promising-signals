# N-gram suffix speculative draft for GPT-2 cascade inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-suffix-speculative-draft-for-gpt-2-cascade-inference-86b092438eb7`
Run ID: `n-gram-suffix-speculative-draft-for-gpt-2-cascade-inference-86b092438eb7-20260529T062001008731+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ce92ee43bde

## What looked useful

N-gram suffix copying produced a reproducible target-call reduction under exact GPT-2 greedy verification: 1.60x in smoke, 1.886x in the 32-prompt main run, and 1.7-2.2x across a small draft-length/suffix-length ablation. Controls almost never matched the target. A separate 8-prompt exactness check matched ordinary greedy GPT-2 generation on all prompts.

## Boundaries and scale limits

Small prompt sample, GPT-2-small only, greedy decoding only, full-prefix verifier rather than production KV-cache assisted generation, and no larger cascade or batched serving latency validation.

## Claim scope

Bounded local evidence: for GPT-2-small greedy decoding on 32 WikiText-2 prompts, an in-context n-gram suffix drafter with exact target verification reduced target forward calls from 2048 one-token greedy calls to 1086 verifier calls, a 1.886x call reduction, while simple controls remained near 1.04x.

## Why it stopped

The run supports a mechanism-level target-call reduction but does not provide production KV-cache latency, larger-model, stochastic decoding, or broad-corpus evidence required for a paper.

## Recommended next action

Stop this run as no-paper useful signal; next implement a KV-cached verifier and compare exact greedy-output equality plus end-to-end latency on a larger prompt set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cached n-gram suffix speculative decoding for GPT-2 greedy generation
- Success threshold: At least 1.3x median end-to-end latency speedup with exact output equality and no worse than 1.5x target-call reduction on the full prompt set.
- Stop condition: Stop if exact output equality fails, if median latency speedup is below 1.1x despite target-call reduction, or if controls match the n-gram drafter within 10% on both latency and call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculative-draft-for-gpt-2-cascade-inference-86b092438eb7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
