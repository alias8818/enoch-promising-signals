# Model-generated copy suffix localization with controlled exposure

Status: `useful_signal`
Project ID: `model-generated-copy-suffix-localization-with-controlled-e-b7a81ba63a`
Run ID: `model-generated-copy-suffix-localization-with-controlled-e-b7a81ba63a-20260516T163742943761+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Model-generated copy suffix localization with controlled exposure: internal_generated:model-generated-copy-suffix-localization-with-controlled-e-b7a81ba63a

## What looked useful

Across 960 generations, exposed copy5 rate was 0.402 versus 0.035 in withheld controls. Qwen/Qwen3-0.6B showed 0.9875 exposed copy5 versus 0.06875 control; SmolLM2-135M-Instruct showed 0.15 versus 0.03125; Pythia-410m showed 0.06875 versus 0.00625. Copy5-gated suffix localization was 0.85 to 0.92 across models, while shuffled wrong-item localization stayed near chance.

## Boundaries and scale limits

Validated on 160 items, three cached local models, four candidate sources per item, Qwen-generated suffixes with deterministic unique tails, and one operations-update prompt family. It does not test spontaneous copying, training-data leakage, large production models, real documents, or long-context deployment traces.

## Claim scope

In a synthetic controlled-exposure inference task with explicit quote-style instructions, small local causal language models copy visible model-generated target suffixes more often than withheld controls, and copied suffixes can usually be localized to the correct exposed source by contiguous-overlap matching.

## Why it stopped

Bounded validation supports the controlled-exposure mechanism but remains synthetic and copy-directed, so it is not publication-grade evidence for naturalistic model-generated suffix localization.

## Recommended next action

Run one capped depth-4 deepen test with naturalistic prompts that do not explicitly ask for copying; otherwise stop as no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturalistic copy suffix localization without explicit quote instructions
- Success threshold: Exposed-control copy5 lift >= 0.10 and copy-gated localization accuracy >= 0.70 across at least two model families, with shuffled-source localization near chance.
- Stop condition: Stop as unsupported if copy5 lift is below 0.10 or copy-gated localization is below 0.70 in both model families, or if control copying is high enough that exposure cannot be isolated.

## Evidence references

- Artifact root: `<local-path>/projects/model-generated-copy-suffix-localization-with-controlled-e-b7a81ba63a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
