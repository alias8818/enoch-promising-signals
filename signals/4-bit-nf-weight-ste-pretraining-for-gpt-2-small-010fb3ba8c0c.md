# 4-bit NF weight STE pretraining for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-nf-weight-ste-pretraining-for-gpt-2-small-010fb3ba8c0c`
Run ID: `4-bit-nf-weight-ste-pretraining-for-gpt-2-small-010fb3ba8c0c-20260604T205230754888+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/210199ea0250

## What looked useful

NF4 weight STE trained stably and closely tracked dense validation loss in both paired probes. Final NF4-minus-dense validation-loss gaps were +0.0222 for the 10.7M model and +0.0147 for the 85.3M GPT-2-small-shape model. The naive implementation was slower than dense by 2.74x and 4.24x respectively.

## Boundaries and scale limits

Not full GPT-2-small pretraining: no GPT-2 BPE vocabulary, no full 124M parameter embedding/head, no standard web/text corpus, no long schedule, no multi-seed robustness, and no packed 4-bit training kernels.

## Claim scope

Short-run character-level GPT-style pretraining with FP master weights, NF4 forward weight quantization, and STE gradients. Evidence covers a 10.7M-parameter compact model for 200 updates and an 85.3M-parameter GPT-2-small-depth/width/head-geometry model for 100 updates on Tiny Shakespeare.

## Why it stopped

Closed as no-paper useful signal: short-run proxy evidence supports the mechanism but does not validate full GPT-2-small pretraining, and the naive quantize-on-forward path is substantially slower than dense.

## Recommended next action

Run a bounded deepen follow-up using GPT-2 BPE tokenization, full GPT-2-small vocabulary/head, a standard corpus slice, at least 1000-5000 updates, and two or more seeds before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-vocabulary GPT-2-small NF4-STE early pretraining confirmation
- Success threshold: NF4-STE completes without divergence and final validation loss is within 0.05 of dense in both seeds, with no widening loss gap after the first 1000 updates.
- Stop condition: Stop early if NF4-STE diverges, produces NaN/Inf, or remains more than 0.15 validation loss above dense for three consecutive evaluations after warmup.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-nf-weight-ste-pretraining-for-gpt-2-small-010fb3ba8c0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
