# Ternary Weights + Learned Residual Scale Channels for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-learned-residual-scale-channels-for-gpt-2-small-180e87e7c562`
Run ID: `ternary-weights-learned-residual-scale-channels-for-gpt-2-small-180e87e7c562-20260531T155351276788+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/290050cb2943

## What looked useful

Ternary-forward Transformer layers were trainable with about 42% zero weights, but validation loss trailed dense by 0.021 at 220 steps and 0.100 at 1000 steps. Residual channel scales moved from 1.0 but changed ternary validation loss by only -0.00013 at 220 steps and -0.00479 at 1000 steps.

## Boundaries and scale limits

This run did not train GPT-2-small, did not use BPE/tokenized web corpora, did not test inference kernels or deployed ternary speedups, and used only two seeds for the 220-step comparison plus one seed for the 1000-step check.

## Claim scope

On a 112k-parameter, 2-layer, 64-hidden character-level GPT-style Transformer trained on Tiny Shakespeare with STE ternary-forward linear layers, learned per-channel residual scales are used by optimization but provide only marginal validation-loss improvement over unscaled ternary weights and do not close the gap to a dense baseline.

## Why it stopped

Proxy early falsification: the mechanism was directly tested in a small GPT-style LM and residual scales produced only a marginal benefit while ternary+scale remained materially behind dense; this is not a full GPT-2-small validation.

## Recommended next action

Do not write a paper from this run; if continuing, run a bounded deeper-transformer ablation where residual scaling has more residual paths to act on before considering GPT-2-small scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Depth sensitivity of residual channel scales for ternary Transformers
- Success threshold: ternary_res_scale improves mean validation loss over ternary by at least 0.03 and at least one pooled standard deviation while retaining at least half of the dense-to-ternary gap recovery across three or more seeds.
- Stop condition: Stop if the deeper run shows less than 0.01 mean validation-loss improvement over unscaled ternary or if the improvement is smaller than seed-to-seed noise.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-learned-residual-scale-channels-for-gpt-2-small-180e87e7c562`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
