# Hierarchical Local Attention for 8K CPU Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-local-attention-for-8k-cpu-context-2463f793e2f4`
Run ID: `hierarchical-local-attention-for-8k-cpu-context-2463f793e2f4-20260529T125543334494+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6788e13f97b2

## What looked useful

At 8192 tokens, HLA was 4.74x faster than dense on iid inputs and 5.79x faster on clustered inputs. On clustered inputs, HLA reduced relative MSE versus dense from local-only 3.146 to 0.000420 and improved mean cosine from 0.9125 to 0.9998. On iid inputs, HLA improved over local-only but remained a weak approximation, with mean cosine 0.518.

## Boundaries and scale limits

No model training, no real text corpus, no causal language-model perplexity, no retrieval benchmark, no learned summaries, and no optimized kernel were tested. Dense, local, and HLA timings are single-process NumPy CPU measurements on one 8-core worker.

## Claim scope

Synthetic CPU forward-pass probe only: a NumPy hierarchical local attention operator with 128-token local windows and 64-token block summaries was faster than dense attention at 8192 tokens and approximated dense outputs much better than local-only attention on block-structured synthetic Q/K/V inputs.

## Why it stopped

Current evidence is a useful synthetic forward-pass signal but not direct model-quality validation, so this run should close as no-paper rather than continue or claim publication readiness.

## Recommended next action

Run a bounded small-transformer follow-up comparing dense, local, and HLA at matched parameter count on a real 8K retrieval or language-modeling task, with perplexity or retrieval accuracy plus CPU throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer HLA vs Dense and Local at 8K CPU Context
- Success threshold: HLA should recover at least half of the quality gap between local-only and dense while retaining at least 2x CPU forward-pass speedup or memory reduction versus dense at 8K.
- Stop condition: Stop if HLA does not improve real-task quality over local-only by a measurable margin, or if its CPU overhead erases the expected advantage versus dense at 8K.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-local-attention-for-8k-cpu-context-2463f793e2f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
