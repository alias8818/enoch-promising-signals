# Compressed KV Fingerprints with Exact Anchor Hashes for Agent Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-kv-fingerprints-with-exact-anchor-hashes-for-agent-memory-9d9277b4ba58`
Run ID: `compressed-kv-fingerprints-with-exact-anchor-hashes-for-agent-memory-9d9277b4ba58-20260602T230800578041+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/93566c73e35a

## What looked useful

Exact anchor hashes are a low-cost supplement for named memory lookup, but the tested compressed fingerprint mechanism is not viable as a dense semantic retrieval replacement: 2048-bit fingerprints reached recall@10 0.7873 versus 0.9653 for full dense retrieval, and 512-bit fingerprints reached only 0.3013 recall@10.

## Boundaries and scale limits

Synthetic vectors and generated anchor IDs only; no real agent traces, conversation embeddings, learned fingerprints, production hash tables, adversarial anchors, or end-to-end agent tasks were tested.

## Claim scope

On a deterministic synthetic 100k-memory benchmark with 384-dimensional clustered vectors, exact 64-bit anchor hashes recovered named memories with zero observed collisions, but random-projection binary fingerprints did not preserve dense semantic retrieval quality at 6x to 192x bitpacked compression.

## Why it stopped

Bounded synthetic evidence was sufficient to reject the tested random-projection compressed fingerprint design as a semantic retrieval replacement, while preserving the exact-anchor component as a useful supplement.

## Recommended next action

Stop this run as no-paper useful signal; next test should replace random-projection fingerprints with a learned or product-quantized compressed-key method on real embedding traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned or Quantized Compressed Keys with Exact Anchor Hashes on Real Memory Embeddings
- Success threshold: At least 0.90 semantic recall@10 at 12x or better bitpacked compression on 100k+ real embeddings, with exact-anchor recall@1 of 1.0 for unique anchors and zero observed 64-bit hash collisions.
- Stop condition: Stop if the best compressed-key method below 12x compression fails to reach 0.85 recall@10 or if exact-anchor lookup shows non-negligible collision or alias ambiguity under realistic anchors.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-kv-fingerprints-with-exact-anchor-hashes-for-agent-memory-9d9277b4ba58`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
