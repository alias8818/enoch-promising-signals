# Anchor-Based KV Compression for Long-Context Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-based-kv-compression-for-long-context-memory-59b2e22005a4`
Run ID: `anchor-based-kv-compression-for-long-context-memory-59b2e22005a4-20260619T042847581467+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/02d6a3a11c2b

## What looked useful

At 8192 tokens with budget 128, anchors_recent reached 0.612 anchor-target accuracy and 1.000 target retention, while recent, strided, and random_recent were about 0.009 to 0.012 accuracy. On uniform-target lookup, anchors_recent stayed near chance, e.g. 0.006 accuracy at budget 128. Anchor-density ablations showed performance depends on fitting the anchor set in the cache.

## Boundaries and scale limits

Proxy-only evidence: random normalized keys, explicit anchor labels, one-query retrieval, and exact argmax accuracy. No learned transformer, semantic anchor discovery, multi-layer KV behavior, generation quality, perplexity, or real long-context benchmark was tested.

## Claim scope

On a synthetic CUDA attention-retrieval task with known anchor metadata, anchor+recent KV retention preserves anchored long-context lookup much better than recent, strided, or random retention at 16x to 64x compression, but it does not preserve unanchored uniform lookup.

## Why it stopped

The run produced a useful synthetic mechanism signal and a clear limitation, but it is proxy-only evidence and not publication-grade validation of anchor-based KV compression in real long-context language models.

## Recommended next action

Run a bounded direct-evidence follow-up in a small transformer using real KV tensors and a passkey/needle retrieval task with controlled anchor markers and imperfect-anchor ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV anchor retention in a small transformer retrieval task
- Success threshold: At equal KV budget, anchor+recent improves anchored retrieval accuracy by at least 20 percentage points over recent-only and strided baselines without more than a 5 percent relative perplexity regression on non-retrieval text.
- Stop condition: Stop if anchor+recent fails to beat both recent-only and strided baselines by at least 10 percentage points on anchored retrieval, or if imperfect-anchor ablations erase the gain.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-based-kv-compression-for-long-context-memory-59b2e22005a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
