# Speculative Decoding With Exact No-Spec and N-Gram Baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-exact-no-spec-and-n-gram-baselines-4186429d9c1e`
Run ID: `speculative-decoding-with-exact-no-spec-and-n-gram-baselines-4186429d9c1e-20260629T090015319777+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58869bd8e939

## What looked useful

N-gram prompt-lookup is a worthwhile exact baseline for copyable contexts, but acceptance rate alone is insufficient: distilgpt2 natural prompts slowed down despite 77.5% draft acceptance because target-call reduction was negligible. Cache mutation during rejected draft verification can silently break exactness unless rollback is handled.

## Boundaries and scale limits

Small prompt set, 64 generated tokens per prompt, greedy decoding only, no production serving stack, no large corpus, no confidence intervals, and low-precision exactness failed for gpt2 fp16 on one prompt.

## Claim scope

On two GPT-2-family models and 12 local prompts under greedy decoding, exact n-gram prompt-lookup speculative decoding preserved greedy output and improved aggregate wall-clock time, with strong gains on repeated synthetic prompts and mixed natural-prompt behavior.

## Why it stopped

The evidence is direct but too small and greedy-only for publication-grade validation; it supports baseline guidance and implementation cautions rather than a paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a larger corpus, repeated timing trials, and an optimized rollback cache before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-Scale Exact N-Gram Speculative Decoding With Rollback Cache
- Success threshold: Exact equality on all prompts and at least 1.10x natural-prompt wall-clock speedup on two target models with confidence intervals excluding parity.
- Stop condition: Stop if exactness fails, if natural-prompt speedup is below 1.05x on both models after optimized rollback, or if repair overhead erases target-call reductions.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-exact-no-spec-and-n-gram-baselines-4186429d9c1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
