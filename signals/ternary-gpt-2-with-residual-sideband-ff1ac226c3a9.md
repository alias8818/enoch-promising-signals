# Ternary GPT-2 with Residual Sideband

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ternary-gpt-2-with-residual-sideband-ff1ac226c3a9`
Run ID: `ternary-gpt-2-with-residual-sideband-ff1ac226c3a9-20260608T035844627728+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4244dd767c13

## What looked useful

Residual sideband size produced monotonic loss repair across two seeds: mean validation-loss delta versus dense improved from +0.2086 for ternary-only to +0.0803 at 5% sideband and +0.0581 at 10% sideband.

## Boundaries and scale limits

Toy model only: 112k parameters, character-level data, 300 training steps, two seeds, linear weights only, no pretrained GPT-2, no tokenizer-level benchmark, no quantization-aware training, no inference kernel or throughput measurement.

## Claim scope

In a tiny GPT-style character-level causal LM trained on Tiny Shakespeare, post-training ternarization of linear weights is consistently repaired by adding a sparse residual sideband; a 5% sideband recovered about 61% of ternary-only validation-loss damage while preserving a 7.27x fp32 linear-weight storage proxy.

## Why it stopped

No-paper closure: this run provides a toy/proxy mechanism signal, not direct GPT-2-small or publication-grade evidence.

## Recommended next action

Run one bounded deepen follow-up on pretrained GPT-2-small or an equivalently standard token-level LM validation slice, comparing ternary-only, 2%, 5%, and 10% residual sideband perplexity plus a realistic sideband storage/lookup estimate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small residual sideband PTQ validation
- Success threshold: 5% sideband recovers at least 50% of ternary-only perplexity degradation versus dense and stays below 5 effective bits per linear weight under the stated storage model.
- Stop condition: Stop as negative if 5% sideband recovers less than 25% of ternary-only degradation or if storage/lookup accounting exceeds 8 effective bits per linear weight for the smallest useful sideband.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-gpt-2-with-residual-sideband-ff1ac226c3a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
