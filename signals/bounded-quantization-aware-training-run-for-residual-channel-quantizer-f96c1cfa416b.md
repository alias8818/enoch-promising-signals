# Bounded Quantization-Aware Training Run for Residual Channel Quantizer

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-quantization-aware-training-run-for-residual-channel-quantizer-f96c1cfa416b`
Run ID: `bounded-quantization-aware-training-run-for-residual-channel-quantizer-f96c1cfa416b-20260609T095315235216+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b4f39773704c

## What looked useful

Bounded residual-channel QAT consistently reduced quantization RMSE and improved synthetic validation accuracy relative to PTQ, especially under the harsher 1-bit residual setting. It nearly matched full precision in the 2-bit setting but remained below full precision in the 1-bit setting.

## Boundaries and scale limits

No real language-model, vision-model, GPT-2-small-class, dataset-scale, kernel-efficiency, or production compressed-weight validation was run. The bounded-vs-unbounded QAT accuracy gain was small, so the result is mechanism evidence only.

## Claim scope

Synthetic teacher-student MLP classification benchmark with residual per-output-channel scalar weight quantization. Bounded QAT improved validation accuracy over PTQ by 1.595 percentage points at 2 bits x 2 stages and 5.586 percentage points at 1 bit x 2 stages, with lower quantization RMSE than unbounded QAT.

## Why it stopped

No-paper closure: this was a synthetic bounded mechanism test, not a direct/full validation of model-training performance.

## Recommended next action

Run a bounded direct-evidence follow-up on a compact transformer or GPT-2-small-class language-model baseline with the same four controls and repeated seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct compact-transformer validation of bounded residual-channel QAT
- Success threshold: Bounded residual QAT improves validation loss or perplexity over PTQ and unbounded residual QAT in the majority of seeds while staying within 5% of full-precision validation loss at one tested bit budget.
- Stop condition: Stop if bounded residual QAT fails to beat PTQ in validation loss/perplexity in at least two of three seeds or requires materially more compute than the bounded local budget.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-quantization-aware-training-run-for-residual-channel-quantizer-f96c1cfa416b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
