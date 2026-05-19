# Storage-matched residual-channel binary transformer ablation

Status: `useful_signal`
Project ID: `storage-matched-residual-channel-binary-transformer-ablati-65f8861a0b`
Run ID: `storage-matched-residual-channel-binary-transformer-ablati-65f8861a0b-20260516T152632406050+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3b8b513aeb52

## What looked useful

Residual dense channels were active but consistently worse than spending the same MLP bit budget on more binary channels; best residual setting was still +0.0329 median validation NLL worse than the all-binary control, while residual-channel models remained better than a same-storage dense-tiny MLP.

## Boundaries and scale limits

Small synthetic corpus, small transformer, MLP-only binarization, three residual widths, three seeds, and inference-storage accounting only; not evidence about large natural-language models or fully binarized transformer stacks.

## Claim scope

In a 2-layer d_model=64 causal transformer trained for 900 steps on a structured synthetic next-token task, adding 4, 8, or 16 dense fp16 residual MLP channels at the same MLP inference storage budget did not improve validation NLL over a storage-matched all-binary wide MLP.

## Why it stopped

Controlled small direct test did not meet the mechanism threshold: residual-channel variants failed to beat the storage-matched all-binary baseline across tested residual widths.

## Recommended next action

Stop this run as a bounded Tier 1 early falsification; if deepening, rerun the same storage-matched residual-width sweep on a small real text corpus before considering larger scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text storage-matched residual-channel binary MLP sweep
- Success threshold: A residual-channel variant beats the storage-matched all-binary baseline by at least 0.03 median validation NLL across three seeds without exceeding the MLP bit budget.
- Stop condition: Stop if all residual-channel variants are at least 0.02 median validation NLL worse than the all-binary baseline or if the effect changes sign across seeds without a median improvement.

## Evidence references

- Artifact root: `<local-path>/projects/storage-matched-residual-channel-binary-transformer-ablati-65f8861a0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
