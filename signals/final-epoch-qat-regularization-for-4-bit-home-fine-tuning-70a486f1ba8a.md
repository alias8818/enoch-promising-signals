# Final-Epoch QAT Regularization for 4-Bit Home Fine-Tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `final-epoch-qat-regularization-for-4-bit-home-fine-tuning-70a486f1ba8a`
Run ID: `final-epoch-qat-regularization-for-4-bit-home-fine-tuning-70a486f1ba8a-20260605T025101065855+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47a251bb1026

## What looked useful

Final fake-QAT appears useful as a last-mile adaptation when the deployed artifact is definitely 4-bit: confirmation run improved int4 validation loss in 5/5 seeds by mean -0.01978 CE and reduced quantization gap by mean -0.03894. It is not a free regularizer: fp loss worsened in 5/5 seeds by mean +0.01917, and round-grid regularization had mixed signs with mean int4 delta +0.00055.

## Boundaries and scale limits

Synthetic next-token task, small from-scratch Transformer, weight-only symmetric int4 quantization, no pretrained LLM, no LoRA/adapters, no NF4/bitsandbytes deployment path, no real downstream benchmark.

## Claim scope

On a small synthetic causal-Transformer probe, a final-only fake-quantized training phase reduced post-training symmetric int4 Linear-weight validation loss versus an equal-budget ordinary final phase, but explicit round-to-grid regularization did not help and fake-QAT degraded fp validation loss.

## Why it stopped

This run produced useful bounded evidence, but it is synthetic/proxy evidence and does not validate final-epoch QAT regularization for real 4-bit home fine-tuning at paper quality.

## Recommended next action

Run a bounded direct follow-up on a pretrained GPT-2-small-class model with LoRA and a real text/task dataset, comparing ordinary final epoch, final fake-QAT, and no final epoch under an actual 4-bit deployment path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Final Fake-QAT on GPT-2-Small LoRA 4-Bit Fine-Tuning
- Success threshold: Final fake-QAT improves deployed 4-bit validation or task metric in at least 3/3 matched seeds with mean relative loss reduction of at least 2% or task-metric gain of at least 1 absolute point, while fp regression remains below 1% relative loss increase or is irrelevant to the deployment claim and explicitly scoped out.
- Stop condition: Stop if final fake-QAT fails to improve deployed 4-bit metrics in at least two matched seeds, causes fp regression above the acceptable threshold without deployed gains, or cannot be evaluated in a realistic 4-bit path within the local compute budget.

## Evidence references

- Artifact root: `<local-path>/projects/final-epoch-qat-regularization-for-4-bit-home-fine-tuning-70a486f1ba8a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
