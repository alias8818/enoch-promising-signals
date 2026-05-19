# Curriculum Length-Progressive Data Selection

Status: `useful_signal`
Project ID: `curriculum-length-progressive-data-selection-81ef6a727b81`
Run ID: `curriculum-length-progressive-data-selection-81ef6a727b81-20260516T235457581126+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8a610f7413d8

## What looked useful

Ascending length curriculum beat mixed sampling on all validation loss by -0.004905 nats mean paired delta across 10 seeds and improved 7/10 seeds, but long validation improved only 4/10 seeds; descending control showed no benefit.

## Boundaries and scale limits

Synthetic data only; small model; maximum sequence length 128; no real-text corpus, GPT-2-small-class baseline, downstream evaluation, or exact FLOP-matched training. Throughput differences are confounded with schedule-dependent sequence lengths.

## Claim scope

In a synthetic variable-length causal LM benchmark with a 357k-parameter transformer and 10 seeds at 5M training tokens per schedule, ascending length-progressive sampling produced a small all/short/medium validation-loss improvement versus mixed sampling, while long-length validation was not consistently improved.

## Why it stopped

This run produced a bounded synthetic useful signal but not direct publication-grade evidence; broad LM curriculum claims require real-corpus and larger-model validation.

## Recommended next action

Run a bounded real-text GPT-2-small-class follow-up at equal token and FLOP budgets before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text FLOP-matched length curriculum for GPT-2-small-class training
- Success threshold: Ascending schedule improves overall held-out loss by at least 0.01 nats versus mixed and improves long-bucket loss in at least 2 of 3 seeds at equal FLOP budget.
- Stop condition: Stop as no-paper if ascending fails to beat mixed on overall or long-bucket held-out loss under equal FLOP budget.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-length-progressive-data-selection-81ef6a727b81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
