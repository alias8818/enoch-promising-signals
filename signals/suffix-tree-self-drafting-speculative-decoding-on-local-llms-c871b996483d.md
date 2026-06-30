# Suffix-Tree Self-Drafting Speculative Decoding on Local LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-self-drafting-speculative-decoding-on-local-llms-c871b996483d`
Run ID: `suffix-tree-self-drafting-speculative-decoding-on-local-llms-c871b996483d-20260619T125932090188+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2902e151206

## What looked useful

Conservative suffix-context drafting achieved 4.576x ideal step reduction on a repeated agent trace and 3.416x on templated code, outperforming a fixed 4-token n-gram proposer in those traces. It only achieved 1.069x on low-repetition prose and 1.000x on random-token control, while long-context tables created substantially more context entries than n-gram lookup.

## Boundaries and scale limits

Single-process CPU Python benchmark, up to 24k tokens per corpus, synthetic/generated local traces, GPT-2 tokenization only, no target-model verifier, no GPU inference, no vLLM or llama.cpp integration.

## Claim scope

Trace-level online suffix self-drafting over local deterministic token streams supports high exact-match acceptance on repetitive agent/code-like traces, but not on low-repetition prose or random-token controls. No end-to-end LLM serving speedup was measured.

## Why it stopped

Proxy trace evidence supports the mechanism only for repetitive workloads and prior public work already covers suffix-tree speculative decoding; this is not full validation or a novel paper-ready result.

## Recommended next action

Stop as no-paper useful signal; if continuing, run a bounded direct verifier integration on one local small model with workload detection and compare measured TPOT/tokens-per-second against no speculation and n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded local verifier test for suffix self-drafting on repetitive agent traces
- Success threshold: At least 1.15x measured tokens/sec or TPOT improvement over both no speculation and n-gram baseline on repetitive traces, less than 5% regression on low-repetition control with gating enabled, and bounded CPU memory under 1 GiB for the tested workload.
- Stop condition: Stop if measured throughput fails to beat n-gram by 5% on repetitive traces, if CPU proposer overhead erases verifier savings, or if memory exceeds the configured local-serving budget.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-self-drafting-speculative-decoding-on-local-llms-c871b996483d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
