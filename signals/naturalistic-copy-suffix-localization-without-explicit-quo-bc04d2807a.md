# Naturalistic copy suffix localization without explicit quote instructions

Status: `useful_signal`
Project ID: `naturalistic-copy-suffix-localization-without-explicit-quo-bc04d2807a`
Run ID: `naturalistic-copy-suffix-localization-without-explicit-quo-bc04d2807a-20260516T164752982514+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Naturalistic copy suffix localization without explicit quote instructions: internal_generated:naturalistic-copy-suffix-localization-without-explicit-quo-bc04d2807a

## What looked useful

Naturalistic forced-choice accuracy was 1.0 for all tested models in both exact-phrase and paraphrased-target conditions; corrupt-source controls were 0.0, redacted controls were near chance with zero exact generation, and source-suffix occlusion was the top-impact span in every model. Greedy exact copying degraded under paraphrase, especially Pythia-70M at 0.016.

## Boundaries and scale limits

Synthetic templated prompts only; small pretrained decoder-only models only; no organic corpus extraction, no instruction-tuned large models, no long-context setting, and no internal activation/attention causal tracing.

## Claim scope

Across 128 fixed-seed synthetic handoff/checklist prompts per condition, four small decoder-only pretrained models strongly preferred the true earlier suffix over a paired corrupt suffix without explicit quote instructions, and input occlusion localized the effect to the source suffix span.

## Why it stopped

No-paper closure: direct local evidence supports a mechanism-level useful signal, but exact free generation is mixed under paraphrased cues and the validation remains synthetic/proxy rather than paper-ready.

## Recommended next action

Stop this follow-up chain: depth is already 4, and the current evidence is a useful synthetic/input-occlusion signal but not paper-positive naturalistic localization.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/naturalistic-copy-suffix-localization-without-explicit-quo-bc04d2807a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
