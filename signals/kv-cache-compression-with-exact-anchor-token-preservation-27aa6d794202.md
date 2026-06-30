# KV cache compression with exact anchor-token preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-compression-with-exact-anchor-token-preservation-27aa6d794202`
Run ID: `kv-cache-compression-with-exact-anchor-token-preservation-27aa6d794202-20260613T113500900290+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3e5761862387

## What looked useful

Oracle exact-anchor preservation reduced MSE versus quantize-all by about 99.92%-99.94% in the mixed regime and essentially 100% in anchor-targeted queries; preserve-first-N improved only about 3%-4%, and random preservation was near neutral.

## Boundaries and scale limits

No real LLM cache, perplexity, retrieval, latency, GPU kernel, or serving benchmark was run. Anchor identities were known by construction, so deployable online selection remains unvalidated.

## Claim scope

Synthetic single-step attention probe: preserving a known oracle set of 32 anchor KV tokens exactly while quantizing all other KV entries to 2-4 bits greatly reduces attention-output MSE versus quantizing all tokens, at estimated 6.14x-9.92x cache compression versus fp32.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic oracle-anchor probe, but the result is not a deployable or publication-grade validation and overlaps existing attention-sink/heavy-hitter KV preservation literature.

## Recommended next action

Run a bounded real-cache follow-up using a small pretrained transformer: identify anchors online from attention/key statistics, preserve them exactly under 2-4 bit KV quantization, and compare against preserve-first-N, H2O-style accumulated attention, and quantize-all on perplexity or retrieval plus attention-output perturbation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-cache online anchor selection for exact-preservation KV quantization
- Success threshold: Online anchor preservation achieves at least 50% of the oracle MSE reduction and improves perplexity or retrieval accuracy over preserve-first-N at comparable estimated KV memory in at least two quantization settings.
- Stop condition: Stop if online anchors do not beat preserve-first-N on attention-output MSE or downstream metric in a small real-model run, or if selector overhead exceeds the compression benefit.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-with-exact-anchor-token-preservation-27aa6d794202`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
