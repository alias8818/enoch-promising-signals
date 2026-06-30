# 2-Bit KV Cache with Principled Residual Channels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-kv-cache-with-principled-residual-channels-b47f7c5b75fd`
Run ID: `2-bit-kv-cache-with-principled-residual-channels-b47f7c5b75fd-20260619T082212053623+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/d1eab8914979

## What looked useful

Sensitivity-selected fp16 residual channels produced mean relative-RMSE reductions versus full 2-bit quantization of 6.1%, 10.3%, and 19.3% at 6.25%, 12.5%, and 25% channel budgets on GPT-2 attention outputs, winning 71/72 to 72/72 paired layer/prompt cases. Gains versus random residual channels were smaller but positive on average; gains versus magnitude-selected channels were only 0.7% to 1.9%.

## Boundaries and scale limits

Single GPT-2 model, 12 short prompts, attention-output reconstruction only, no end-to-end perplexity/generation/retrieval metrics, no long-context tests, no packed 2-bit kernel throughput measurement, and no comparison to full KIVI/KVQuant implementations.

## Claim scope

On GPT-2 small activation traces with prompts up to 96 tokens, fp16 residual KV channels selected by a calibration-time quantization-error/activity score reduce attention-output reconstruction error versus full 2-bit KV quantization and usually beat random residual channels at equal residual budgets. The advantage over magnitude-selected channels is small.

## Why it stopped

No-paper closure: the local evidence supports the residual-channel mechanism as a useful signal, but it is proxy-only and the improvement over a simple magnitude heuristic is too small for a paper-ready claim.

## Recommended next action

Run a bounded deepen test that replaces reconstruction error with end-to-end perplexity and a small passkey/retrieval probe using the same channel-selection budgets before considering any larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end quality test for sensitivity-selected 2-bit KV residual channels
- Success threshold: At 12.5% residual channels, sensitivity selection should reduce perplexity degradation by at least 10% relative to magnitude selection and improve passkey/retrieval accuracy by at least 5 percentage points relative to random residual channels at equal effective bytes per element.
- Stop condition: Stop if sensitivity selection does not beat magnitude selection on perplexity at the 12.5% residual budget or if passkey/retrieval accuracy is indistinguishable from random residual channels.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-principled-residual-channels-b47f7c5b75fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
