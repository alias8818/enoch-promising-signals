# Anchor-Preserving KV Compression (APKVC) for Long-Context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserving-kv-compression-apkvc-for-long-context-on-gb10-790ab4757b18`
Run ID: `anchor-preserving-kv-compression-apkvc-for-long-context-on-gb10-790ab4757b18-20260610T030813634439+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a7be01676626

## What looked useful

Corrected sweep over 135 rows showed APKVC top-1 preservation of 0.724-0.726 mean versus 0.448 for the best non-APKVC baseline, and 1.000 anchor top-1 preservation versus 0.216 for the best non-APKVC baseline. APKVC did not improve mean attention-output relative L2, so the signal is a targeted anchor retrieval safeguard rather than a general KV compression quality win.

## Boundaries and scale limits

Proxy-only evidence: no trained long-context model, no perplexity or retrieval QA benchmark, no real inference-engine KV cache integration, and no production latency measurement. Sequence lengths were 4096-16384 with 8 heads, head dim 64, 384 synthetic queries, and budgets 512-2048.

## Claim scope

In a synthetic PyTorch attention-level probe on GB10 with explicit known anchors, preserving anchor KV positions plus a recent window substantially improved full-cache top-1 target preservation for anchor/local retrieval queries versus recent, uniform, and uniform+recent baselines.

## Why it stopped

Stopped after a corrected bounded GPU proxy sweep because the mechanism signal is useful but synthetic and mixed; presenting it as paper-positive would overclaim beyond the evidence.

## Recommended next action

Run a bounded real-model deepen test by implementing static APKVC in a small transformer inference path and comparing retrieval QA/perplexity and decode latency against recent and uniform+recent eviction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model APKVC validation on small long-context retrieval tasks
- Success threshold: At matched KV budget, APKVC improves retrieval accuracy by at least 10 absolute percentage points over the best non-APKVC eviction baseline while keeping perplexity/logit-drift and decode latency within 5% of that baseline.
- Stop condition: Stop if APKVC fails to beat the best baseline on retrieval accuracy, causes more than 5% perplexity/logit-drift degradation, or selection overhead erases any memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-kv-compression-apkvc-for-long-context-on-gb10-790ab4757b18`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
