# GPT-2-medium INT2 residual channel preservation robustness and storage-normalized baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-medium-int2-residual-channel-preservation-robustness-ca06202b8f`
Run ID: `gpt-2-medium-int2-residual-channel-preservation-robustness-ca06202b8f-20260611T123000477825+0000`

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

- Parent run decision: Residual Channel Preservation in INT2 Quantization: enoch://control-plane/projects/residual-channel-preservation-in-int2-quantization-b5e66ee85e13/runs/residual-channel-preservation-in-int2-quantization-b5e66ee85e13-20260611T115328298341+0000
- Parent run decision: Medium GPT-2 INT2 Residual Channel Preservation With Realistic Quantization Baselines: enoch://control-plane/projects/medium-gpt-2-int2-residual-channel-preservation-with-reali-672c66cd3f/runs/medium-gpt-2-int2-residual-channel-preservation-with-reali-672c66cd3f-20260611T121052902930+0000

## What looked useful

Activation-selected residual channel preservation reduced loss from 13.1404 for uniform INT2 to 9.9105 at 2.4375 average target bits. Same-storage random masks averaged 12.4138 loss, low-activation masks 13.0027, and a top weight-norm baseline was close at 10.1498, indicating a real channel-importance effect but not activation salience exclusivity.

## Boundaries and scale limits

Single model, single validation dataset, 64 evaluation windows, fake quantization rather than packed INT2 kernels, no latency or deployed memory-bandwidth measurements, and no GPTQ/AWQ/OmniQuant-style optimized INT2 baseline.

## Claim scope

On GPT-2-medium with fake-quantized INT2 target weights and 64 fixed WikiText-2 validation windows, preserving 32 high-activation residual dimensions in fp16 improved causal language-model loss versus uniform INT2 and same-storage random/low-activation controls.

## Why it stopped

Tier-2 local evidence supports the mechanism, but publication readiness is blocked by scope and baseline limits rather than by execution failure.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded deepen test should compare activation RCP against GPTQ/AWQ-style INT2 baselines across multiple preserve fractions and at least two validation corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-medium INT2 RCP versus optimized PTQ baselines across preserve fractions
- Success threshold: RCP must beat the strongest same-storage optimized INT2 baseline by at least 0.10 mean loss on one corpus without losing by more than 0.05 mean loss on another, and must retain clear advantage over random/low-salience controls.
- Stop condition: Stop if optimized PTQ baselines match or beat activation RCP within 0.05 mean loss at matched storage across tested fractions, or if the effect only appears on one narrow corpus/window selection.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-medium-int2-residual-channel-preservation-robustness-ca06202b8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
