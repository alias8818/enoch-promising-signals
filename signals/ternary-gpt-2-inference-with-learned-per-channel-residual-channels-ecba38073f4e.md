# Ternary GPT-2 Inference with Learned Per-Channel Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-gpt-2-inference-with-learned-per-channel-residual-channels-ecba38073f4e`
Run ID: `ternary-gpt-2-inference-with-learned-per-channel-residual-channels-ecba38073f4e-20260613T180741672624+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/faf8d73e53c5

## What looked useful

Residual channels monotonically reduced loss damage, but even k=128 residual entries per output channel left perplexity 6062.81 versus dense 288.04 while reducing estimated compression to 2.76x versus fp16. The naive top-k residual side-channel version is not close to dense quality at useful small budgets.

## Boundaries and scale limits

Not a learned residual-channel training run; not evaluated on a standard public benchmark; no optimized ternary kernels or latency/energy measurements; distilgpt2 is smaller than GPT-2-small and the text sample is short.

## Claim scope

Bounded CPU inference probe on distilgpt2 using a 512-token local text sample; all Conv1D/Linear weights including lm_head were replaced by per-output-channel ternary weights plus analytic top-k residual input weights per output channel.

## Why it stopped

Proxy early falsification of the naive ternary plus top-k residual-channel mechanism: direct distilgpt2 inference quality remained far from dense despite increasing residual budgets.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test activation-aware learned residual-channel selection on a public validation corpus before any larger scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware learned residual channels for ternary GPT-2-family inference
- Success threshold: At a minimum 4x estimated fp16 linear-weight compression, activation-aware residual allocation should reduce the dense-vs-quantized NLL gap by at least 75% relative to static top-k residual selection and keep perplexity within 2x dense on held-out validation text.
- Stop condition: Stop if activation-aware residual allocation fails to halve the NLL gap versus static top-k residuals at matched bit budget on a public held-out corpus.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-gpt-2-inference-with-learned-per-channel-residual-channels-ecba38073f4e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
