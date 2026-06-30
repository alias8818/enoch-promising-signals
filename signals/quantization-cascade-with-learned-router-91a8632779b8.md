# Quantization Cascade with Learned Router

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantization-cascade-with-learned-router-91a8632779b8`
Run ID: `quantization-cascade-with-learned-router-91a8632779b8-20260628T185815387004+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/325fe8d4803e

## What looked useful

Full learned router AUC for fixable low-bit errors was 0.8969 vs 0.6744 for confidence. At 20% escalation it improved cascade accuracy by 5.31 percentage points and captured 58.7% of fixable errors vs 35.3% for confidence. Uncertainty-only learned routing produced only tiny gains, implicating input-conditioned quantization-error regions as the useful mechanism.

## Boundaries and scale limits

Synthetic data only; MLP only; weight-only quantization; no token-level language modeling; no activation quantization; no measured kernel latency, energy, batching, or serving effects; short local run on GB10.

## Claim scope

In a synthetic nonlinear classification proxy with a 3-layer MLP and post-training symmetric weight-only quantization, an input-conditioned learned router improved a 2-bit-to-8-bit cascade over confidence-threshold routing at matched escalation rates across 5 seeds.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy and cannot support a publication-grade claim about real language-model quantization cascades.

## Recommended next action

Run a bounded GPT-2-small-class token-level follow-up comparing input-conditioned learned routing against confidence routing using validation loss/perplexity and measured inference cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level learned router for GPT-2-small quantization cascade
- Success threshold: At 10-30% escalation, learned routing improves validation loss/perplexity over confidence routing by at least 10% of the low-bit-to-high-bit gap at matched measured cost across at least 3 seeds or corpus shards.
- Stop condition: Stop if learned routing fails to beat confidence routing at matched escalation/cost in two independent token-level configurations, or if router overhead erases the cascade cost advantage.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-cascade-with-learned-router-91a8632779b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
