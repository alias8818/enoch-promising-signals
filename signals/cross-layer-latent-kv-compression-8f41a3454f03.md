# Cross-Layer Latent KV Compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cross-layer-latent-kv-compression-8f41a3454f03`
Run ID: `cross-layer-latent-kv-compression-8f41a3454f03-20260609T015859102793+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48099f486882

## What looked useful

At 50% effective cache storage, cross-layer latent compression produced mean attention-output relative MSE 0.859 on both DistilGPT2 and GPT-2, versus 0.372 and 0.341 for matched per-layer PCA controls. The simplest cross-layer latent mechanism is therefore a poor candidate without a more structured or learned decoder.

## Boundaries and scale limits

This was a bounded activation-level probe, not a full generation/perplexity or serving benchmark. It used fixed local text samples, sequence length 128, DistilGPT2 and GPT-2 only, and an unsupervised linear decoder rather than a learned or finetuned compression architecture.

## Claim scope

A global shared layer-axis PCA/SVD latent basis for GPT-style K/V caches was tested on pretrained DistilGPT2 and GPT-2 activations at sequence length 128; at useful compression ratios it failed to preserve attention-output behavior and underperformed a matched per-layer PCA control.

## Why it stopped

Proxy/activation-level early falsification: direct Q/K/V attention-output diagnostics showed high error at useful compression ratios, but full compressed-cache generation was not tested.

## Recommended next action

Stop this run as a no-paper early falsification of the global shared layer-basis mechanism; the only worthwhile next local test is a bounded learned or grouped-layer decoder with full perplexity evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Grouped or learned cross-layer KV decoder with perplexity validation
- Success threshold: <=50% cache storage, mean attention-output relative MSE <0.10, max-layer relative MSE <0.25, perplexity degradation <5%, and better than matched per-layer PCA.
- Stop condition: Stop if the learned/grouped decoder remains above 0.25 mean attention-output relative MSE or loses to matched per-layer PCA at the same storage after one bounded training/evaluation pass.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-latent-kv-compression-8f41a3454f03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
