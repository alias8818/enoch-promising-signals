# 2-bit KV cache with per-head residual channels for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-per-head-residual-channels-for-long-context-ecc55b027239`
Run ID: `2-bit-kv-cache-with-per-head-residual-channels-for-long-context-ecc55b027239-20260620T121537170359+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4a28c0fcbf95

## What looked useful

On synthetic outlier-channel KV at sequence lengths 4096 and 16384, targeted residual channels reduced attention-output relative L2 by about 43-55% versus plain 2-bit KV, while random residual channels reduced only about 3-9%. Gaussian KV saw only about 6-12% relative L2 reduction, showing the method depends on persistent outlier channels.

## Boundaries and scale limits

No real LLM KV activations, perplexity, benchmark accuracy, packed-kernel throughput, metadata overhead accounting, or production serving validation were tested. Compression estimates are data-bit-only.

## Claim scope

Synthetic attention/KV-cache reconstruction tests show that retaining 8-16 full-precision per-head residual channels selected by key absolute max can substantially reduce 2-bit KV attention-output error when persistent per-head outlier channels are present.

## Why it stopped

Synthetic mechanism evidence is useful but insufficient for a paper; the result lacks direct real-model quality and serving evidence.

## Recommended next action

Run a bounded real-activation follow-up on a small open model: capture KV tensors, compare per-head residual channels against KIVI-style 2-bit KV and recent-token residual baselines on perplexity plus passkey/RULER-style retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM KV activation validation for per-head residual 2-bit cache
- Success threshold: At matched effective bit budget, targeted per-head residual channels reduce perplexity or task accuracy degradation by at least 25% versus plain 2-bit KV and outperform random residual channels across at least two seeds/context sets.
- Stop condition: Stop if targeted residual channels fail to beat random residual channels or KIVI-style baseline on real activations at matched effective bit budgets.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-per-head-residual-channels-for-long-context-ecc55b027239`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
