# Ternary attention Q/K/V with per-head FP16 residual scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-attention-q-k-v-with-per-head-fp16-residual-scaling-ac2fc3b1c3b9`
Run ID: `ternary-attention-q-k-v-with-per-head-fp16-residual-scaling-ac2fc3b1c3b9-20260613T023448085684+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9001c3f006c4

## What looked useful

On a CUDA GB10 associative-recall probe, dense reached 0.2861 accuracy and 1.4855 loss; plain ternary Q/K/V reached 0.2909 accuracy and 1.4962 loss at 2 estimated Q/K/V bits/weight; ternary Q/K/V with per-head FP16 residual scales reached 0.2899 accuracy and 1.4841 loss at 2.0069 estimated Q/K/V bits/weight. The residual scales were used, with mean learned scale 0.5278, but did not clearly beat plain ternary on accuracy.

## Boundaries and scale limits

Not validated on natural-language modeling, GPT-2-small-class scale, long-context settings, real packed ternary kernels, actual memory savings, or wall-clock deployment speedups.

## Claim scope

Small synthetic associative-recall transformer probe: ternary Q/K/V with one FP16 residual scale per Q/K/V head preserved dense-like task accuracy and matched/slightly improved dense eval loss across 3 seeds while using approximately 2.007 estimated Q/K/V bits per weight.

## Why it stopped

The result is bounded synthetic evidence only, not full language-model validation or compressed-kernel evidence.

## Recommended next action

Stop this worker run as a no-paper useful signal; the concrete next bounded action is a GPT-2-small-class language-model follow-up comparing dense, ternary, and ternary-residual Q/K/V on validation perplexity and attention diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class validation of ternary Q/K/V residual scaling
- Success threshold: Ternary-residual Q/K/V finishes within 3% validation perplexity of dense and improves perplexity by at least 2% relative to plain ternary Q/K/V at the same training budget.
- Stop condition: Stop if ternary-residual Q/K/V is more than 8% worse than dense validation perplexity after an initial calibrated budget or if residual scales saturate without improving over plain ternary.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-attention-q-k-v-with-per-head-fp16-residual-scaling-ac2fc3b1c3b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
