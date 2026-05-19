# ResidualFP channels in a tiny transformer language model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residualfp-channels-in-a-tiny-transformer-language-model-deadf0804b`
Run ID: `residualfp-channels-in-a-tiny-transformer-language-model-deadf0804b-20260517T144904130348+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a6cce9232f27

## What looked useful

Zeroing the 4 persistent ResidualFP channels after each block increased validation loss by 0.0247 +/- 0.0080 nats, showing the model uses them. Final validation loss was slightly worse than both standard d64 (+0.0101 loss) and standard d60 active-width (+0.0052 loss) controls.

## Boundaries and scale limits

Tiny char-level LM only: 65-token vocabulary, 1.1M-character corpus, 800 training steps, 3 seeds, <=164k parameters. No GPT-2-small-class, tokenizer-scale, long-training, or corpus-robustness validation was run.

## Claim scope

In a 3-layer char-level Tiny Shakespeare transformer trained for 800 steps across 3 seeds, explicit 4-channel ResidualFP bypass channels are measurably used by the model but do not improve validation loss over standard d64 or d60 active-width controls.

## Why it stopped

Tier 1 direct test found mechanism support but no validation-loss advantage, so this is no-paper evidence rather than a paper-positive positive result.

## Recommended next action

Run one bounded deepen test with longer training, 5+ seeds, parameter-matched standard baselines, random frozen bypass controls, and learned-gated bypass controls; stop if ResidualFP still fails to beat controls by more than seed variance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Controlled ResidualFP channel ablations in a longer tiny LM run
- Success threshold: ResidualFP mean validation loss at least 0.02 nats better than every control with non-overlapping or clearly separated seed intervals, and FP-channel zero-ablation delta >=0.02 nats.
- Stop condition: Stop as negative if ResidualFP does not beat all controls by at least 0.02 nats or if FP ablation delta falls below 0.02 nats after the longer run.

## Evidence references

- Artifact root: `<local-path>/projects/residualfp-channels-in-a-tiny-transformer-language-model-deadf0804b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
