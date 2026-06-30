# Low-Rank Residual Channels for 2-bit KV Cache on CPU Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-residual-channels-for-2-bit-kv-cache-on-cpu-long-context-39ed926f575c`
Run ID: `low-rank-residual-channels-for-2-bit-kv-cache-on-cpu-long-context-39ed926f575c-20260610T150859248791+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5a7e9b2e7706

## What looked useful

Residual information materially improves 2-bit KV attention fidelity versus q2-only, reducing attention-output relative MSE by about 39.49% on average. Low-rank residuals were only effectively tied with a simpler same-budget residual-channel baseline, with a 0.32% mean output-MSE edge, 15/24 output-MSE wins, 12/24 attention-KL wins, and only 4/24 top-1 agreement wins.

## Boundaries and scale limits

No real pretrained-model KV traces, perplexity, generation-quality, cache-paging, grouped-query, or fused-kernel decode measurements were run. Low-rank factors were fit by oracle SVD, so the run does not validate an online CPU update algorithm.

## Claim scope

Bounded NumPy operator-level test of 2-bit per-channel affine KV quantization with oracle low-rank residual factors versus a same residual-byte-budget exact-channel baseline on synthetic long-context K/V tensors up to 8192 tokens and d=128 on CPU.

## Why it stopped

Proxy/operator-level evidence supports residual correction versus q2-only but early-falsifies the stronger low-rank advantage claim because the method is only tied with a simpler matched residual-channel baseline and used oracle SVD factors.

## Recommended next action

Do not write a paper from this run; run a bounded follow-up on real small-model KV traces with an incremental or blockwise low-rank update path and require a meaningful same-budget win over residual channels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV Trace Test for 2-bit Low-Rank Residuals versus Matched Residual Channels
- Success threshold: Low-rank residuals must improve attention-output relative MSE or perplexity delta by at least 5% over matched residual channels at equal storage and keep CPU decode latency within 10% of the channel baseline.
- Stop condition: Stop if real-trace low-rank gains are below 2% over matched channels at two storage budgets or if the update path adds more than 25% decode latency.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-residual-channels-for-2-bit-kv-cache-on-cpu-long-context-39ed926f575c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
