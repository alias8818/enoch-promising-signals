# Tiered KV Cache with Exact Anchors and Low-Rank Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-cache-with-exact-anchors-and-low-rank-compression-386899697817`
Run ID: `tiered-kv-cache-with-exact-anchors-and-low-rank-compression-386899697817-20260602T174643567827+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6178637ba9c2

## What looked useful

Exact anchors plus low-rank middle compression strongly reduced attention-output error when non-anchor tokens were truly low-rank and anchors carried high attention mass, but the advantage mostly disappeared against memory-matched uniform low-rank compression in moderately compressible cases and remained high-error on full-rank noisy controls.

## Boundaries and scale limits

No real transformer decoding, perplexity, downstream task, online causal anchor selection, quantized storage, or fused serving-kernel benchmark was run. Sequence lengths were 2048 and 4096 with head dimension 128 and synthetic K/V distributions.

## Claim scope

Synthetic attention-output benchmark for KV-cache reconstruction with exact sink/recent anchors plus low-rank non-anchor compression, compared against same-rank and memory-matched uniform low-rank baselines.

## Why it stopped

Closed as no-paper useful signal: the current evidence is synthetic and mixed, supporting the mechanism only under favorable low-rank-middle assumptions rather than validating a general KV-cache compression method.

## Recommended next action

Run a bounded real-model GPT-2-small-class decode benchmark with causal anchor selection and memory-matched baselines before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Decode Test for Tiered Exact-Anchor KV Compression
- Success threshold: Tiered KV must reduce next-token KL or perplexity degradation by at least 25% versus memory-matched uniform low-rank KV at equal estimated cache memory, without more than 10% decode throughput loss on the measured setup.
- Stop condition: Stop if tiered KV does not beat memory-matched uniform low-rank KV on next-token KL/perplexity in two tested cache budgets or if decode overhead exceeds 25% before quality improves.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-cache-with-exact-anchors-and-low-rank-compression-386899697817`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
