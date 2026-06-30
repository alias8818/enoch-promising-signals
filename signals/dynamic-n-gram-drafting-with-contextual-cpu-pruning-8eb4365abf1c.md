# Dynamic N-gram Drafting with Contextual CPU Pruning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-n-gram-drafting-with-contextual-cpu-pruning-8eb4365abf1c`
Run ID: `dynamic-n-gram-drafting-with-contextual-cpu-pruning-8eb4365abf1c-20260629T064242140473+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/520493da9a0d

## What looked useful

Dynamic n-gram drafting beat static 4-gram on the proxy. Contextual pruning is useful only if metadata gating is cheap: high-retention pruning cut continuation lookups by 86.7% but ran 1.29x slower; cheap gating cut lookups by 73.4%, ran at 0.55x exhaustive wall time, and retained 85.4% accepted-token yield.

## Boundaries and scale limits

No transformer verifier, tokenizer-level LM evaluation, CPU/GPU overlap, KV-cache behavior, batching, or production serving scheduler was tested. Corpus scope is one small public text corpus.

## Claim scope

On a Tiny Shakespeare held-out n-gram drafting proxy with 112000 train tokens, 28000 held-out tokens, 8000 sampled positions, max n=8, and draft length 6, contextual pruning can substantially reduce continuation-table probes. A high-retention gate preserved accepted-token yield but was slower due metadata overhead; a cheap gate improved Python wall time while retaining 85.4% of exhaustive dynamic accepted-token yield.

## Why it stopped

Proxy evidence supports a mechanism and tradeoff but does not directly validate real LM serving speedups.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, implement the cheap contextual gate inside a small real speculative decoder and require end-to-end tokens/sec improvement versus exhaustive n-gram and no-draft baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LM speculative decoding test for cheap contextual n-gram gating
- Success threshold: Cheap contextual gating improves end-to-end tokens/sec by at least 10% over exhaustive n-gram drafting while retaining at least 80% of accepted-token yield on the same target and prompts.
- Stop condition: Stop if cheap gating fails to beat exhaustive n-gram wall-clock throughput or falls below 80% accepted-token yield after bounded threshold tuning.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-n-gram-drafting-with-contextual-cpu-pruning-8eb4365abf1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
