# Ternary Backbone with Low-Rank Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-backbone-with-low-rank-residual-channel-b4dc2be5c3ee`
Run ID: `ternary-backbone-with-low-rank-residual-channel-b4dc2be5c3ee-20260525T230611481892+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3eeacff15f2e

## What looked useful

Matrix approximation showed monotonic error reductions from rank 4 to 32, with rank 32 reducing ternary-only relative error from 0.4384 to 0.3183. In the trainability probe, the best ternary+low-rank model reduced validation MSE by 3.5% versus ternary-only, but dense remained about 34% lower MSE than the best ternary+low-rank variant.

## Boundaries and scale limits

No transformer, real language corpus, GPT-2-small-class baseline, custom ternary kernel, inference throughput, or long training run was tested. The trainability probe used small synthetic teacher-student MLPs over 3 seeds and 320 optimizer steps.

## Claim scope

On a bounded GB10 PyTorch probe, ternary-plus-low-rank residuals reduce random dense matrix approximation error versus ternary-only, and give a small teacher-student MLP validation-MSE improvement over ternary-only.

## Why it stopped

Closed as no-paper useful signal: the local proxy supports the residual-channel mechanism, but the trainability gain is small and not direct transformer/language-model evidence.

## Recommended next action

Run a bounded deepen experiment with a small transformer or GPT-2-small-class block on a real text corpus, comparing dense, ternary-only, and ternary+low-rank at matched parameter budgets and reporting perplexity plus throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer Validation of Ternary Plus Low-Rank Residuals
- Success threshold: Ternary-plus-low-rank closes at least 25% of the validation-perplexity gap between dense and ternary-only at comparable training budget, without erasing the storage or inference rationale for ternary weights.
- Stop condition: Stop if ternary-plus-low-rank closes less than 10% of the dense-versus-ternary perplexity gap after matched training budget, or if throughput/storage accounting shows no plausible efficiency advantage over dense.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-backbone-with-low-rank-residual-channel-b4dc2be5c3ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
