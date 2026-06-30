# 2-bit KV Cache with Channel-Wise Residual Scale Factors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-kv-cache-with-channel-wise-residual-scale-factors-51d100d45729`
Run ID: `2-bit-kv-cache-with-channel-wise-residual-scale-factors-51d100d45729-20260621T024922030928+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc4ce748255b

## What looked useful

Across 45 held-out synthetic cases, token residual scaling reduced attention-output relative MSE to a mean 0.1891x of the token baseline, and channel residual scaling reduced it to 0.3133x of the channel baseline; both improved reconstruction and attention MSE in 45/45 cases. Worst-case max-absolute error worsened for the per-channel corrected baseline.

## Boundaries and scale limits

No real LLM activations, perplexity, task accuracy, packed-cache serving implementation, latency, or long-context generation stability were tested. The result is synthetic and mechanism-level only.

## Claim scope

On held-out synthetic KV tensors with Gaussian, heavy-tailed channel-variance, and outlier-channel profiles, per-head/channel residual post-dequant scale factors reduced 2-bit KV reconstruction MSE and attention-output MSE versus matching 2-bit per-token and per-channel baselines.

## Why it stopped

Finalized as no-paper useful signal because the evidence is synthetic/proxy-only despite consistent held-out MSE improvements.

## Recommended next action

Run a bounded direct-evidence follow-up on real small-transformer KV activations with held-out perplexity or next-token KL plus packed-cache overhead accounting; do not write a paper from this synthetic probe alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Activation 2-bit KV Residual Scale Validation
- Success threshold: Residual-scale 2-bit KV should recover at least 25% of the perplexity or KL gap between the best plain 2-bit baseline and fp16 while adding less than 5% cache storage overhead and no more than 10% decode latency in a simple implementation.
- Stop condition: Stop if residual-scale variants fail to improve held-out perplexity/KL over both matching 2-bit baselines or if overhead removes the expected 2-bit cache-memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-channel-wise-residual-scale-factors-51d100d45729`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
