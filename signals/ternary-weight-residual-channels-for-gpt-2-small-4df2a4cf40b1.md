# Ternary-Weight Residual Channels for GPT-2-Small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ternary-weight-residual-channels-for-gpt-2-small-4df2a4cf40b1`
Run ID: `ternary-weight-residual-channels-for-gpt-2-small-4df2a4cf40b1-20260527T164127117767+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fe6b5049c075

## What looked useful

Ternary residual channels did not cause optimization collapse in the local GPT-like probe: mean ternary-minus-dense validation loss was -0.0109 over three seeds, with two ternary wins and one practical tie, at matched parameter count.

## Boundaries and scale limits

This run did not train GPT-2-small, did not use a tokenized large corpus, did not test multiple ternary fractions beyond 50%, and did not implement packed ternary kernels; therefore it does not support claims about GPT-2-small quality, compression, throughput, or deployment efficiency.

## Claim scope

In a 1.83M-parameter GPT-like character language model on Tiny Shakespeare, replacing 50% of residual MLP output channels with straight-through ternary projections remained trainable and matched or slightly improved validation loss versus a parameter-matched dense residual MLP across three 300-step seeds.

## Why it stopped

The result is a bounded local useful signal, not full validation: it uses a tiny character-level proxy model and standard dense PyTorch operations rather than GPT-2-small-scale training or packed ternary kernels.

## Recommended next action

Run a bounded GPT-2-small-class follow-up using a real tokenizer/corpus, multiple ternary fractions, and a dense baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-Small-Class Ternary Residual Channel Ablation
- Success threshold: Ternary residual variants at one or more fractions reach validation perplexity within 1% of the dense baseline across at least three seeds without unstable loss spikes, and show stable nonzero ternary sparsity.
- Stop condition: Stop if every tested ternary fraction is more than 3% worse in validation perplexity than dense after matched training budget, or if training becomes unstable in two or more seeds.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weight-residual-channels-for-gpt-2-small-4df2a4cf40b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
