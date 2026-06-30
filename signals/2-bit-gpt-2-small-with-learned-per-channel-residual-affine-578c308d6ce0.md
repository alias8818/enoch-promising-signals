# 2-bit GPT-2-small with learned per-channel residual affine

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-gpt-2-small-with-learned-per-channel-residual-affine-578c308d6ce0`
Run ID: `2-bit-gpt-2-small-with-learned-per-channel-residual-affine-578c308d6ce0-20260630T100603698948+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b208dfad9bd4

## What looked useful

Plain 2-bit GPT-2-small Conv1D quantization produced validation loss 36.8919 versus dense loss 4.0471. Learned per-channel affine calibration improved validation loss to 5.6328, recovering 95.17% of the dense-to-plain loss gap but still leaving a 1.5858 nats/token gap and 279.44 perplexity versus dense 57.23.

## Boundaries and scale limits

Single seed, subset validation of 32768 tokens, affine-only calibration for 2048 steps, dequantized float weights rather than packed 2-bit kernels, no full WikiText-2 validation, no downstream tasks, no full-model QAT, and no speed or memory efficiency claim.

## Claim scope

Bounded post-training GPT-2-small probe on WikiText-2 subsets: learned per-output-channel affine corrections on frozen 2-bit per-channel Conv1D weights can recover most of the cross-entropy gap versus catastrophic plain 2-bit quantization, but not dense quality.

## Why it stopped

Bounded direct evidence supports the stabilizing mechanism but not a publication-grade positive: quality remains materially worse than dense and robustness/full-validation baselines are missing.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded multi-seed full-WikiText-2 affine-ablation follow-up before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed full-WikiText-2 ablation of learned affine for 2-bit GPT-2-small
- Success threshold: Across three seeds, affine-all-layers must recover at least 90% of the dense-to-plain loss gap on full WikiText-2 validation and leave less than 0.75 nats/token loss gap to dense, while at least one ablation explains most of the mechanism.
- Stop condition: Stop as negative if full-validation affine-all-layers leaves at least 1.0 nats/token gap to dense or recovery falls below 80% in two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-gpt-2-small-with-learned-per-channel-residual-affine-578c308d6ce0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
