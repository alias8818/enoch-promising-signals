# Principled Residuals for 4-Bit Activations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `principled-residuals-for-4-bit-activations-6f6c21c2d840`
Run ID: `principled-residuals-for-4-bit-activations-6f6c21c2d840-20260528T011103144472+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/125b33f851bb

## What looked useful

Top-error residuals with k=16/128 hidden channels recovered a mean 59.9% of q4 classifier accuracy drop and reduced matmul relative output MSE by 17.6%-21.3% versus q4, beating same-budget random residuals by 12.2%-16.1% MSE reduction across distributions. q5 still had much lower matmul error, limiting the practical claim.

## Boundaries and scale limits

Three synthetic seeds, synthetic teacher/student classifier, synthetic activation distributions, exact selected-channel residual restoration, no real transformer activations, no perplexity, no latency/kernel implementation, and no residual index/value overhead accounting.

## Claim scope

In NumPy-only bounded proxy tests, selecting a small residual side channel by largest per-activation q4 quantization error consistently reduced matmul output error and recovered part of q4-induced classifier accuracy loss versus plain q4 and same-budget random residual controls.

## Why it stopped

Proxy evidence supports the mechanism but not a deployable or publication-grade 4-bit activation method; exact residual restoration and synthetic traces are insufficient for full validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded transformer-trace follow-up that includes residual overhead accounting and perplexity/accuracy before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-trace residual overhead test for q4 activations
- Success threshold: At equal effective bit budget, top-error residualized q4 must recover at least 50% of the q4 perplexity or accuracy degradation and beat same-budget random and top-activation residual controls on at least two seeds or datasets.
- Stop condition: Stop if residualized q4 fails to beat same-budget controls after overhead accounting, or if q5 dominates quality at comparable effective cost and complexity.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residuals-for-4-bit-activations-6f6c21c2d840`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
