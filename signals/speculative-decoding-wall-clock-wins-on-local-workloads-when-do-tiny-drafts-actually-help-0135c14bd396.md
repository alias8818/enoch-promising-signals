# Speculative Decoding Wall-Clock Wins on Local Workloads: When Do Tiny Drafts Actually Help?

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-wall-clock-wins-on-local-workloads-when-do-tiny-drafts-actually-help-0135c14bd396`
Run ID: `speculative-decoding-wall-clock-wins-on-local-workloads-when-do-tiny-drafts-actually-help-0135c14bd396-20260619T182532068389+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b52d97c3c692

## What looked useful

Tiny drafts can help local wall-clock generation, but only after prompt formatting and output length are controlled. In the calibrated chat-template sweep, 135M/360M drafts produced 1.02x-1.12x speedups while reducing target forward calls by 42.9%-60.6%. Raw/malformed instruct prompts and overly costly drafts can erase or reverse the win even when target forwards drop.

## Boundaries and scale limits

Single GPU, single model family, small hand-written prompt suite, greedy decoding only, no serving framework, no batching/concurrency, one assistant candidate budget, no broad quality evaluation, and no production traffic traces.

## Claim scope

On one NVIDIA GB10 host using Transformers 4.57.6 greedy generation with SmolLM2-1.7B-Instruct as target and SmolLM2-135M/360M as assistants, chat-formatted local prompts showed modest assisted-decoding wall-clock wins across 16-128 token caps when target forward calls fell by roughly 40-60% and draft cost stayed below saved target cost.

## Why it stopped

Evidence is direct for one local Transformers/SmolLM2 setup but too narrow for a paper; broader model-family and serving-stack validation is required before publication claims.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should repeat the same harness on a second cached model family such as Qwen2.5/Qwen3 and sweep assistant candidate budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-family speculative decoding threshold on local GB10
- Success threshold: At least one non-SmolLM2 pair shows a consistent assisted-decoding speedup above 1.10x on two or more token caps, or a clear negative where draft cost explains failure despite target-forward reduction.
- Stop condition: Stop after one additional model family and candidate-budget sweep if speedups stay within +/-5% of baseline or if assistant overhead dominates despite at least 40% target-forward reduction.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-wall-clock-wins-on-local-workloads-when-do-tiny-drafts-actually-help-0135c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
