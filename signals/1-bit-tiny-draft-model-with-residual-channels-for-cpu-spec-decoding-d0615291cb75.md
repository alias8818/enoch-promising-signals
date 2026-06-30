# 1-bit tiny draft model with residual channels for CPU spec-decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-tiny-draft-model-with-residual-channels-for-cpu-spec-decoding-d0615291cb75`
Run ID: `1-bit-tiny-draft-model-with-residual-channels-for-cpu-spec-decoding-d0615291cb75-20260608T211344208338+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a8aaff34ff66

## What looked useful

Across 7 seeds, binary-only acceptance proxy was 0.3644; binary plus 16 supervised residual channels reached 0.6902 and plus 32 reached 0.7023. Dense low-rank parameter-matched control at k=32 reached 0.5662. Activation-norm channel selection was weak, reaching only 0.3907 at k=32 with 0.10 outlier recall.

## Boundaries and scale limits

No real language-model training or activation traces, no end-to-end speculative decoding, no multi-token acceptance measurement, and no packed 1-bit CPU kernel benchmark. NumPy timing used fp32 sign weights and cannot support a throughput claim.

## Claim scope

Synthetic teacher-student linear-logit proxy with sparse high-magnitude input channels: supervised residual-channel selection can recover binary-head logit error and improve one-token speculative acceptance proxy versus binary-only and dense low-rank parameter-matched controls.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only and practical CPU speculative decoding speed was not directly validated.

## Recommended next action

Run a bounded real-activation distillation follow-up: collect hidden states and target logits from a small open LM, train binary-plus-residual and dense/quantized parameter-matched draft heads, and measure real one-token and multi-token speculative acceptance before any packed-kernel work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation distillation test for binary draft heads with supervised residual channels
- Success threshold: At matched parameter budget, binary plus residual channels should improve held-out speculative acceptance by at least 15 percent relative over binary-only and at least 5 percent relative over the strongest dense/quantized control, with no regression in KL/top-k agreement.
- Stop condition: Stop if residual channels fail to beat binary-only by 5 percent relative acceptance on held-out real activations or if gains disappear against a parameter-matched dense/quantized control.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-tiny-draft-model-with-residual-channels-for-cpu-spec-decoding-d0615291cb75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
