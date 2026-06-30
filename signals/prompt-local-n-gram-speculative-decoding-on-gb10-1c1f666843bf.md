# Prompt-Local N-Gram Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-local-n-gram-speculative-decoding-on-gb10-1c1f666843bf`
Run ID: `prompt-local-n-gram-speculative-decoding-on-gb10-1c1f666843bf-20260528T185023291962+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/afdbd41a7a28

## What looked useful

Repeated prompts with n=3 and K=8 matched greedy output across 20 runs, reached 92.57% mean draft acceptance, 80.77% mean target-call reduction, and 2.68x mean/1.79x median speedup. Control prompts matched greedy but had 0% acceptance and slowed to 0.69x mean/0.57x median speed.

## Boundaries and scale limits

Small synthetic prompt set, one small model, batch size 1, greedy decoding only, no production serving stack, no real prompt-trace corpus, no larger model family validation, and no adaptive gating policy.

## Claim scope

On GB10 with distilgpt2 BF16 batch-1 greedy decoding, prompt-local 3-gram draft verification can preserve exact greedy output and improve latency on intentionally repetitive prompts where draft acceptance is high; it slows down control prompts with no useful local n-gram drafts.

## Why it stopped

No-paper useful signal: the mechanism works in a narrow repetitive-prompt case but is mixed and synthetic; control prompts show overhead without gating, so this is not a publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on real chat/code prompt traces with an adaptive gate that disables prompt-local speculation when suffix-hit rate or recent acceptance is low.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Prompt-Local N-Gram Speculation on Real Prompt Traces
- Success threshold: Across at least 100 real prompts on a local GPU model, exact greedy outputs in all cases, median speedup at least 1.15x overall, at least 1.5x on high-repetition prompts, and less than 5% median slowdown on low-repetition prompts.
- Stop condition: Stop if the adaptive gate cannot keep low-repetition prompt slowdown under 5% median or if exact greedy equivalence fails.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-local-n-gram-speculative-decoding-on-gb10-1c1f666843bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
