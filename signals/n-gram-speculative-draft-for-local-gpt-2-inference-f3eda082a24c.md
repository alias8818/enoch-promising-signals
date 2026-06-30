# N-gram speculative draft for local GPT-2 inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-for-local-gpt-2-inference-f3eda082a24c`
Run ID: `n-gram-speculative-draft-for-local-gpt-2-inference-f3eda082a24c-20260602T195822719118+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b6e6e6737050

## What looked useful

The n-gram speculative draft mechanism reduced GPT-2 forward calls and improved exact greedy decoding throughput when prompt/generated context contained repeated spans; all measured rows matched baseline greedy output exactly.

## Boundaries and scale limits

Small hand-built prompt suite; no sampling, batching, long-context serving, larger GPT-2 variants, 7B+ models, real traffic, adversarial non-repetitive suite, or optimized serving implementation.

## Claim scope

On one NVIDIA GB10 running GPT-2 small with greedy decoding, a simple dynamic n-gram draft proposal verified by the target model produced exact outputs and improved throughput by 1.21x to 3.04x across six bounded prompt/run settings.

## Why it stopped

Bounded local evidence supports the mechanism but is too narrow and hand-built for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should compare dynamic generated-context n-gram drafting against prompt-only lookup and no-draft controls on a larger pre-registered prompt suite with adversarial non-repetitive cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Controlled prompt-suite comparison for GPT-2 n-gram draft sources
- Success threshold: Dynamic-context n-gram drafting achieves at least 1.25x mean throughput improvement over no-draft on repetitive/natural cases while staying within 5% slowdown on adversarial non-repetitive cases, with exact-match outputs.
- Stop condition: Stop if exact-match divergence occurs or if dynamic n-gram drafting has less than 1.10x mean speedup on repetitive cases after overhead accounting.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-local-gpt-2-inference-f3eda082a24c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
