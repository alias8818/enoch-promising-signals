# Suffix-Tree Speculative Decoding Without Extra Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-without-extra-weights-3c6a78cd2993`
Run ID: `suffix-tree-speculative-decoding-without-extra-weights-3c6a78cd2993-20260610T190939690317+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58369bbbc25c

## What looked useful

Variable suffix drafting strongly helps when the target repeats prompt/context spans, fails on no-overlap random traces, and drops to modest gains on GPT-2 continuations. The mechanism is workload-dependent and should be compared against existing n-gram/suffix speculative decoding systems before any novelty or paper claim.

## Boundaries and scale limits

This was a replay/proxy study, not an end-to-end serving benchmark. It did not measure wall-clock LLM latency, KV-cache behavior, batched serving throughput, large models, or real RAG/code/agentic benchmark distributions.

## Claim scope

A prompt/recent-context suffix index without extra weights can produce accepted speculative draft runs on high-overlap copy and structured-output traces, and showed a modest 1.25x optimistic verification-step upper bound on eight overlap-biased GPT-2 greedy continuations.

## Why it stopped

Proxy replay evidence supports a narrow mechanism but is insufficient for publication-grade or broad speedup claims, and closely related retrieval/n-gram/suffix speculative decoding work already exists.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is an inference-engine integration comparing suffix-variable drafting against fixed n-gram speculation on code edit/RAG prompts with wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end suffix-variable speculation versus n-gram speculation on overlap-heavy prompts
- Success threshold: At least 1.15x end-to-end wall-clock latency speedup over the best fixed n-gram control on overlap-heavy prompts, no output divergence under greedy verification, and no regression below 0.98x on no-overlap controls.
- Stop condition: Stop if suffix lookup/update overhead erases the replay advantage or if accepted tokens per verification step is not higher than fixed n-gram controls on the target workloads.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-without-extra-weights-3c6a78cd2993`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
