# KV-Cache Attention Pattern Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-attention-pattern-drafting-27bf354319f8`
Run ID: `kv-cache-attention-pattern-drafting-27bf354319f8-20260527T221613315510+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d4f50291ad3

## What looked useful

Simple previous-attention drafting is only useful in synthetic regimes with peaky persistent attention. At about 25% candidate fraction it reached 0.924 top-k recall but only 0.673 mass recall in the easiest peaky regime, and mass recall was 0.293-0.424 elsewhere. Reaching 0.809 mass recall required about 41% candidate fraction.

## Boundaries and scale limits

No trained transformer, no language-model loss/perplexity, no kernel implementation, no real serving traces, and no datacenter-scale model validation. Main evidence used sequence length 512, 8 heads, 5 seeds; budget sweep used 3 seeds.

## Claim scope

Bounded NumPy proxy over generated causal attention traces: previous-token top-k plus a local window can recover high top-k overlap in deliberately peaky persistent regimes, but does not preserve enough attention mass at small candidate fractions to support a practical sparse-attention drafting claim.

## Why it stopped

Proxy evidence is mixed and insufficient for a paper: the mechanism appears under peaky persistence, but small-budget candidate sets do not preserve enough attention mass and output error remains high.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should audit trained-model attention traces with entropy-gated drafting before any kernel or serving work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained-model entropy-gated attention drafting audit
- Success threshold: At candidate fraction <= 0.25, entropy-gated drafting should cover at least 30% of evaluated head-token cases with attention mass recall >= 0.85 and next-token loss delta <= 1% relative to dense attention.
- Stop condition: Stop if trained-model traces show mass recall below 0.75 at candidate fraction <= 0.25 for low-entropy heads, or if loss delta exceeds 1% in the gated subset.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-attention-pattern-drafting-27bf354319f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
